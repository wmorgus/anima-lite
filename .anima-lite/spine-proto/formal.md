# Formal: plus-uno (proto)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Layered architecture
Three strata, frontend-only (no servlet/service/dao/DB tier — do not force one): **design-system → playground → SPA shell**. `design-system/src/` is the shared component/token library (barrel `design-system/src/index.js`). `playground/<name>/` (22 dirs) are individually-scaffolded prototypes, each intended to be a standalone Vite root. `src/` is the root SPA shell (`App.jsx`/`main.jsx`) that both hosts the Prototype Marketplace and, in the shipped build, compiles playground source directly into its own bundle via `React.lazy(import(...))`.

## §2 Module boundaries
Root `vite.config.js` and every standalone playground `vite.config.js` independently define `@`/`@plus-ds` → `design-system/src` (two cosmetically different but equivalent forms: 7 configs use a literal `path.resolve(__dirname, '../../design-system/src')`, 9 use a `root = path.resolve(__dirname, '../..')` indirection). 7 of 22 playgrounds (`group-performance-v2`, `prototyping`, `research-assistant-chat`, `storybook-ai-agent-llm-api`, `training-onboarding`, `tutor-risk-interventions`, plus one more) have **no** `vite.config.js` — they are SPA-embedded page components only, not independently runnable, despite the README's "22 isolated prototype projects" framing.

## §3 Dominant patterns — per stratum

### Design-system layer
Function components throughout (`Button.jsx`, `Card.jsx` read in full — no class components). PropTypes present in 41/79 `.jsx` files under `components/` — used, not universal; no TypeScript inside `components/` proper (TS lives only in `storybook-docs/`, an unrelated helper kit). Token consumption is via component-scoped `.scss` files plus CSS custom properties referenced in className strings, not inline style objects.
`Seams:` className composition is three uninified idioms — one file imports `classnames`, most use manual `.filter(Boolean).join(' ')` or template-literal concatenation — despite `clsx`/`cva` sitting in `package.json` unused (material.md §3, §8). PropTypes coverage is also inconsistent (38/79 files skip it entirely).

### Playground layer
Each of the 16 standalone playgrounds re-resolves `@`/`@plus-ds` to `design-system/src` and is meant to import no code from any other playground. `playground/starter/` (the documented intern template) is clean — no cross-playground imports. All DS imports across playgrounds go through the alias as a **deep component path** (`@/components/Button/Button`, `@plus-ds/components/Table`) — 96/96 sampled `@`/`@plus-ds` import lines are deep paths; zero bare `from '@'` barrel imports were found anywhere.
`Seams:` isolation is real for DS access but broken for a ~5-playground cluster (`home-redesign`, `monthly-report`, `weekly-report-demo`, `research-assistant-chat`, `in-session-ux`) that import each other's `ShellContext` and image assets directly (`../../home-redesign/src/context/ShellContext`, `../../home-redesign/src/assets/...`) — an undocumented shared-shell sub-layer the one-playground-per-sandbox model doesn't account for. One broken import was also found (`home-redesign/src/components/AssistantWrappers.jsx` → `../../../sessions/ReflectionAssistant/...`, a nonexistent playground path).

### SPA shell
`src/main.jsx` mounts `<BrowserRouter><App/></BrowserRouter>`; `src/App.jsx` defines `<Routes>`: `/` and `/market` both render `PrototypeMarket`, `/storybook` iframes the Storybook dev server, and per-prototype routes either `React.lazy`-import a playground's page directly into the shell bundle or redirect into a shared `HomeRedesignApp` shell. The Marketplace catalog (`src/pages/PrototypeMarket/prototypes-data.js`, 427 lines) is plain exported JS objects/arrays — not an external manifest file.
`Seams:` the Marketplace is fully in-process — all routable playgrounds get compiled into one SPA bundle regardless of whether they have their own `vite.config.js`. The catalog (`prototypes-data.js`) and the route/lazy-import maps in `App.jsx` are two independently hand-maintained registries with no enforced sync (material.md §8).

## §4 Seam protocols (CROSS-layer — distinct from the per-layer `Seams:` lines above)
- **Design-system → playground**: (code-derived) every DS import is a deep path through the `@`/`@plus-ds` alias — `@/components/<Name>/<Name>`, `@/specs/<Domain>/<Group>`. AGENTS.md #10 states this should go through the barrel index instead; 0/96 sampled imports do (README-stated, code-contradicted — telos.md §2 already reflects the actual convention, not the stated one).
- **Playground → SPA shell / Marketplace**: (code-derived) a playground becomes visible in the Marketplace only if added to both `prototypes-data.js` and `App.jsx`'s route maps by hand; no build-time check confirms the two agree. A port adding a new playground must update both or it silently won't appear.
- **Playground → playground (should not exist)**: (code-derived) the `home-redesign` shell-family cluster is the one confirmed exception to playground isolation — a new playground should not add a new cross-playground import; if state must be shared, that itself is a finding worth surfacing, not silently replicating the pattern.

## §5 Named findings
1. (README/AGENTS.md-stated, code-contradicted) "Never deep-import — use barrel exports" (AGENTS.md #10): 0/96 sampled playground imports use the barrel; all are deep component paths. Not a regression to fix reflexively — it is the actual, working convention.
2. (code-derived) 7 of 22 playground directories have no `vite.config.js` and are not independently runnable, contradicting the README's "22 isolated prototype projects."
3. (code-derived) Playground isolation holds for DS access, breaks for the home-redesign/monthly-report/weekly-report-demo/research-assistant-chat/in-session-ux cluster sharing `ShellContext` and assets across playground boundaries.
4. (code-derived) One dead/broken cross-playground import in `home-redesign/src/components/AssistantWrappers.jsx` pointing at a nonexistent `../../../sessions/...` path.
5. (skeptical, code-derived) `SidebarTab.mdx` (a Storybook doc file inside `design-system/src`) uses a Tailwind-only `md:` responsive-prefix class — a literal violation of AGENTS.md #9's Tailwind ban, isolated to a doc file, not a rendered component. No MUI/AntD imports found anywhere (that ban holds cleanly).
6. (code-derived) className composition inside `design-system/src/components/` is three inconsistent idioms with no shared helper, despite `clsx`/`cva`/`tailwind-merge` being installed dependencies (material.md §3).

## Concrete example — playground scaffolding traced (`playground/starter/`, cap-exempt reference)
`playground/starter/` is the documented intern template (README "For Interns" section) and the cleanest confirmed instance of the intended pattern:
1. `playground/starter/vite.config.js` — its own Vite root; re-resolves `@`/`@plus-ds` to `../../design-system/src`.
2. `playground/starter/src/` — owns its own entry/App component and SCSS; imports DS components only via deep `@/components/<Name>/<Name>` paths (§4).
3. No cross-playground imports present — the isolation contract holds here where it fails elsewhere (§3 Playground layer seam).
4. To make a new playground independently runnable, add a root `package.json` script `dev:<name>` pointing at `vite --config playground/<name>/vite.config.js` (efficient.md §2) — this step is what the 7 config-less playgrounds skipped.
5. To surface it in the Marketplace, add an entry to `src/pages/PrototypeMarket/prototypes-data.js` AND a route/lazy-import in `src/App.jsx` — both, by hand (§4).
