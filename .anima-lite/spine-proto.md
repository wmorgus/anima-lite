# Spine: plus-uno (proto)
Generated: 2026-07-01
Commit: 9c02f5e8
Confidence: high
Refresh trigger: Any change to vite.config.js, package.json, netlify.toml, or the design-system/src barrel; or addition/removal of a playground directory.

## Material

**Runtime stack:** React 19 + React Router v7 + Vite 8. React-Bootstrap 2 and Bootstrap 5 are the layout and grid primitives. Framer Motion (animation), Highcharts (data visualization), Radix UI and class-variance-authority (component variants), Lucide React and Font Awesome Free (icons).

**Design system (PLUS DS):** First-class internal package at `design-system/src/`, aliased as `@` and `@plus-ds`. Exposed via barrel at `design-system/src/index.js` — components, forms, DataViz. Tokens live in `design-system/src/tokens/` as SCSS partials (`_colors.scss`, `_spacing_semantics.scss`, etc.). All token usage must go through design tokens; no raw hex/px values. Generated token files are not hand-edited.

**Key dependencies not to overlook:** `@assistant-ui/react` (AI chat interface component), TypeScript 5 (in devDeps, used in config but codebase is predominantly `.jsx`/`.js`).

**State:** All application state is component-local (`useState`, `useContext`). Mock data is hardcoded inline in feature components. No external data-fetching layer, no global store.

**CSS:** SCSS with modern-compiler API. Token load paths injected via vite/storybook config — not via `@use`/`@forward` in each file.

## Formal

**Dominant pattern:** Isolated playground workspaces. Each playground (e.g., `playground/monthly-report/`) is a self-contained Vite app with its own `vite.config.js`, `index.html`, and `src/` subtree. Playgrounds share `design-system/src/` through the `@` alias and share `node_modules` from the repo root — but they do not share routing, app shell, or business logic with each other.

**Cross-playground coupling (named inconsistency):** `MonthlyReportContent.jsx` imports `ShellContext` from `../../home-redesign/src/context/ShellContext` and imports image assets from `../../home-redesign/src/assets/`. This is a direct cross-playground import — the monthly-report prototype is not independently runnable without home-redesign's source tree. This seam is not documented and violates the isolation implied by the separate-vite-config pattern.

**Typical change shape:** New feature → new directory under `playground/` with its own `vite.config.js` and `index.html`. A new npm `dev:*` script is added to `package.json`. The feature's main component imports DS components via `@/components/...`. Mock data is hardcoded in the component. No routing wiring to any shared shell is required (unless coupling to home-redesign as above).

**Shell pattern (home-redesign specific):** `home-redesign` implements a `ShellContext` + `ShellLayout` that provides a `TopBar`, breadcrumbs, and `mainClassName` injection. `MonthlyReportContent` uses this shell pattern — its content-only component relies on `ShellContext` to update navigation state. Other playgrounds do not use this shell.

**Storybook:** Present and first-class. Component stories live in `design-system/src/`. The storybook config (`/.storybook/`) builds a static site into `dist/storybook/`. Vitest/Playwright integration is conditionally loaded so Storybook can start without full test tooling.

**Module boundary rule (AGENTS.md):** Agents must not deep-import from `design-system/src/` — barrel exports only. This rule is stated in AGENTS.md; enforcement is agent-convention only, not structurally enforced by tooling.

## Efficient

**Local dev:** `npm run dev` runs Vite (port 4100) and Storybook (port 4200) concurrently via `concurrently`. Per-playground dev via named scripts (e.g., `npm run dev:monthly-report` on port 3008). Each playground's vite.config sets its own root and port.

**Build:** `npm run build:all` = React build (`dist/`) + demo build + Storybook static build (`dist/storybook/`). This is the Netlify build command.

**Deploy:** Netlify. Build output at `dist/`. Storybook served at `/storybook/*` with a static pass-through redirect. SPA catch-all to `index.html` for the React app. Deployed to `plus-uno.netlify.app`.

**Testing:** Storybook-integrated Vitest + Playwright (browser tests against stories). Configuration is conditional — if vitest addon is unavailable, the config degrades gracefully. `npm test` delegates to `design-system/` package's own test suite.

**Figma integration:** Multiple scripts in `scripts/` for Figma token sync, component metadata fetch, write-back, and Code Connect publish. These are manual CLI operations (`npm run sync:tokens`, etc.), not CI-automated.

**Agent workflow:** AGENTS.md defines a six-skill pipeline (uno-research → uno-plan → uno-prototype → uno-review → uno-post → uno-compound). Agents are expected to read component source and stories before implementing, follow a Figma implement-design workflow when a Figma link exists, and document learnings via `uno-compound` after significant work.

**Branching / review:** Not documented in the repo. No CI config (no `.github/workflows/` or similar observed). Netlify likely auto-deploys on push to main.

## Final

**Inferred telos:** This repo is a rapid design exploration environment for the PLUS product — a place where design concepts, new UI features, and design-system components can be prototyped quickly (often agent-driven) and reviewed before any production commitment. Each playground is a throwaway (or promote-to-production-candidate) artifact. The design system is the load-bearing shared asset; the playgrounds are experiments over it.

**Evidence:**
- Package name is literally `plus-vibe-coding-starting-kit`; description says "starter kit for PLUS design prototyping with Cursor agent."
- AGENTS.md encodes a full agent-skill pipeline oriented around rapid build → review → compound cycles.
- All state is mock data hardcoded inline — no API, no persistence, no auth. This is consistent with prototype-only intent.
- Multiple independent playground directories with no shared routing suggest each is a standalone demo, not a feature branch of a single app.
- Netlify deploy makes prototypes shareable with stakeholders without local setup.
- Figma integration scripts (write-back, code-connect publish) suggest a tight design-tool ↔ prototype feedback loop.

**Confidence:** High. The telos is stated in the package metadata, corroborated by structural choices (isolated playgrounds, mock data, agent pipeline), and consistent with the Figma tooling. No conflicting evidence observed.

## Disclaimers
This spine points in a direction. It is not a guarantee. Treat any claim
here that materially affects a port decision as worth a quick verification
pass against the actual code, not as settled fact.
