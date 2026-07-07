# Efficient: plus-uno (proto)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Build tooling
Root `vite.config.js` deliberately try/catches its own Tailwind and Storybook-vitest plugin `require()`s so the same config file is safely reusable by both the app dev server and Storybook's own config loader — a "config file wearing two hats" pattern. Aliases: `@`/`@plus-ds` → `design-system/src`, `~` → `node_modules`. SCSS uses `api: 'modern-compiler'` with `loadPaths` into `design-system/src/{tokens,styles,forms}`. Vendor chunk splitting (`vendor-motion`/`vendor-charts`/`vendor-bootstrap`/`vendor-core`) is done via `manualChunks`, which the config's own comment flags as deprecated in Vite 8 ("migrate to codeSplitting when stable") with no fallback in place — a live landmine for a future Vite bump.

## §2 Key targets
- `npm run dev` — Vite (4100) + Storybook (4200) concurrently
- `npm run dev:vite` / `npm run storybook` — either alone (`storybook` script requires a `NODE_OPTIONS=--require ./scripts/storybook-networkinterfaces-fix.cjs` preload that monkey-patches `os.networkInterfaces()` to swallow a sandboxed-environment error from Storybook's `detect-port`/`address` dependency chain)
- `npm run dev:<playground>` — only exists for playgrounds with a named root script (`home-redesign`, `monthly-report`, `toolkit-ia-revision`); otherwise run `vite --config playground/<name>/vite.config.js` directly if that playground has its own config (formal.md §2)
- `npm run build` (→ `build:react`, Vite only) / `npm run build-storybook` / `npm run build:all` (build + `build:demo` + build-storybook) — `build:all` is the Netlify build command
- `npm run generate:tokens` / `npm run sync:tokens` — token pipeline (§5)

## §3 CI/CD
No lint/test/build merge gate exists. `.github/workflows/` holds only Figma-integration and Marketplace-automation workflows (`figma-implement-design.yml`, `figma-implement.yml`, `figma-library-poll.yml`, `marketplace-add.yml`, `marketplace-edit.yml`) — none run tests or block a merge. The only safety net is Netlify's own `build:all` failing; that step does not run `npm test`, so a broken `design-system` test suite can merge to `main` freely.

## §4 Branching model
Informal: personal branches (`ashley-main`, `bryan-main`, …), topical feature branches (`chore/uno-*`, `feat/uno-bot-v2-sandbox`, `refactor/*`), and auto-generated branches from a design-system-review bot (`ds-review/*`) and Cursor (`cursor/fix-*`). `main`'s recent history is dominated by bot commits (`chore: update Figma component snapshot [skip ci]`). README's stated flow (feature branch → PR → Netlify Deploy Preview → merge to `main` → auto-deploy) is plausible but not enforced by any branch-protection or CI config visible in-repo.

## §5 Deploy path
Netlify: `build.command = "npm run build:all"`, `publish = "dist"`, env `VITE_STORYBOOK_URL`. Two ordered redirects in `netlify.toml`: `/storybook/*` → `/storybook/:splat` (200, static passthrough) must precede the SPA catch-all `/*` → `/index.html` (200) — order matters, Storybook must resolve first. Deploy previews are automatic per-PR (`deploy-preview-{PR#}--plus-uno.netlify.app`); no separate branch-deploy config found.

## Testing
`design-system/package.json`'s `test` script is plain `vitest run` (Vitest ^4.0.15, jsdom, testing-library). Root `vite.config.js` additionally, conditionally wires a `test.projects` block using `@storybook/addon-vitest`'s `storybookTest()` + `@vitest/browser-playwright` (Playwright ^1.58.2 as the Vitest **browser-mode driver only**, chromium, headless) — this really executes Storybook stories in a live browser via Vitest, not a mock. No standalone `playwright.config.*` or `e2e/` directory exists anywhere — Playwright has no separate end-to-end role. Root `npm test` delegates to `npm --prefix design-system test`; nothing in CI runs either suite (§3).

## Token generation
`scripts/sync-figma-tokens.js` fetches live from the Figma API (`FIGMA_FILE_KEY`/`FIGMA_ACCESS_TOKEN`) into intermediate token JSON; `scripts/generate-all-tokens.js` / `scripts/generate-token-scss.js` map Figma variable names into Material-Design-3-style CSS variable names and emit the SCSS/JS consumed under `design-system/src/tokens/`. No "do not edit" header was found on the generated token files themselves at this HEAD — AGENTS.md's "never edit generated token files" rule (#12) is a convention, not a runtime-enforced one; treat generated output as off-limits by policy, not by tooling.

## Verification checklist for a change to any playground
1. If the playground has a `vite.config.js`, run `vite --config playground/<name>/vite.config.js`; otherwise it's SPA-embedded only — verify through `npm run dev` + `/market` or the direct route in `src/App.jsx`.
2. Confirm no hardcoded color/spacing/typography/radius/elevation values were introduced (material.md §7).
3. Confirm any new DS import goes through `@`/`@plus-ds` as a deep component path (formal.md §4) and doesn't duplicate an existing component (material.md §7).
4. If the playground should appear in the Marketplace, confirm both `prototypes-data.js` and `App.jsx`'s route/lazy-import maps were updated (formal.md §4).
5. Run `npm run build` to check for chunk-size regressions; run `npm --prefix design-system test` if a DS component changed — remember neither is CI-enforced (§3), so this step is manual discipline, not a gate.
