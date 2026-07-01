# Spine: plus-uno (proto)
Generated: 2026-06-30
Commit: 9c02f5e8
Confidence: high
Refresh trigger: any change to `design-system/src/` component APIs, `playground/weekly-report-demo/src/`, or the `@` alias resolution in `vite.config.js`

## Material

- **Runtime**: React 19.2, TypeScript 5.9, Vite 8.0
- **PLUS Design System**: internal library at `design-system/src/`, aliased as `@` and `@plus-ds`. Components (Button, Badge, Alert, Progress, PageLayout, etc.), SCSS tokens, DataViz, specs. This is the load-bearing material — all prototypes import from it exclusively.
- **Animation**: Framer Motion 12.38 (runtime dep, vendor-chunked separately)
- **Charts**: Highcharts 12 + highcharts-react-official (vendor-chunked)
- **Bootstrap layer**: React Bootstrap 2 + Bootstrap 5.3 (runtime) — fallback when no PLUS DS equivalent exists per AGENTS.md
- **Tailwind CSS 4**: dev dep only, used by Storybook docs. Forbidden in prototype code per AGENTS.md.
- **AI chat**: @assistant-ui/react (present but not used in weekly-report-demo)
- **State**: client-side only — useState/useRef/useEffect. No Redux/Zustand/external store.
- **Data**: all hardcoded mock data per prototype. No backend API calls.
- **Design tokens**: SCSS variables + JS generated from Figma via `scripts/sync-figma-tokens.js` → `design-system/src/tokens/`. Forbidden to edit generated files directly.
- **Icons**: Font Awesome Free only (fa-solid, fa-regular, fa-brands). FA Pro forbidden.

## Formal

**Primary pattern**: Playground-as-workspace. 22+ independent prototypes in `playground/<name>/`, each with its own `index.html`, `src/`, and `vite.config.js`. Each prototype is a self-contained Vite entry point that aliases into the shared PLUS DS via `@`. The main `src/` app is a secondary structure (React Router, PageLayout shell) — it hosts demos but is not the primary vehicle for feature prototyping.

**Typical shape of a prototype**: standalone Vite app → imports PLUS DS components → mock data hardcoded → single feature flow from entry to end state → no persistence.

**Inconsistencies (named findings):**

1. **Dual WeeklyReport components** — both `WeeklyReportPage.jsx` and `WeeklyReportContent.jsx` exist in the same prototype. `App.jsx` routes to `WeeklyReportContent`; `WeeklyReportPage.jsx` is an older implementation not deleted. They are structurally similar but diverge: `WeeklyReportContent.jsx` is the current version (full animation system, Framer Motion, richer mock data); `WeeklyReportPage.jsx` is stale. ari-argue should use `WeeklyReportContent.jsx` as the canonical source.

2. **Cross-prototype asset imports** — `WeeklyReportContent.jsx` and `WeeklyReportPage.jsx` both import training card images from `../../home-redesign/src/assets/`. Playground sub-projects are not fully self-contained; `weekly-report-demo` has a hard dependency on `home-redesign`'s assets.

3. **Import path variance** — some components imported as `@/components/Button/Button` (explicit file), others as `@/components/Button` (barrel). Inconsistency within the same feature across the two WeeklyReport files.

4. **Package identity mismatch** — `package.json` name is `"plus-vibe-coding-starting-kit"` but the repo is a full multi-year prototype workspace, not a starter kit. The description aligns with early-repo intent, not current function.

5. **Tailwind present despite being forbidden** — `tailwindcss` is a dev dep and appears in `vite.config.js` (conditionally loaded). AGENTS.md rule #9 forbids non-Bootstrap UI frameworks. The conditional guard suggests it was added for Storybook docs and siloed, but the prohibition isn't scoped in the rule.

## Efficient

- **Dev**: `npm run dev` — concurrent Vite (port 4100) + Storybook (port 4200). Playground prototypes run on port 3009 (weekly-report-demo) via their own `vite.config.js`.
- **Build**: `npm run build:all` — main React app → `dist/`, Storybook static → `dist/storybook/`. Triggered by Netlify.
- **Deploy**: Netlify. `netlify.toml` routes SPA catch-all, preserves `/storybook/*` static path.
- **CI**: Present but routinely suppressed — recent commits show `[skip ci]` on Figma snapshot chores. No visible test suite in playground (Storybook vitest for design-system components only).
- **Figma pipeline**: `scripts/poll-figma-library.js` (polling), `scripts/sync-figma-tokens.js` (token sync), `scripts/generate-all-tokens.js`. Design-system source of truth is Figma; tokens flow downward.
- **Prototype graduation**: no explicit mechanism documented. `uno-post` skill is referenced in AGENTS.md but describes submission/publish, not handoff to production engineering.
- **Agent tooling**: Claude Code and Cursor are first-class contributors. `.claude/settings.json`, `AGENTS.md`, and `CLAUDE.md` define agent context. Six named skills: uno-research, uno-plan, uno-prototype, uno-review, uno-post, uno-compound.

## Final

**Inferred telos**: A rapid prototyping workspace where the design team builds interactive, animated demonstrations of feature arguments — grounded in the PLUS Design System — to validate UX intent before handing off to production engineering.

The workspace's product is *arguments*, not production code. Each playground prototype demonstrates what a feature should promise to users (progressive disclosure, metric reveals, locked-until-earned training). The Storybook and design-token pipeline ensure these demonstrations are built from real PLUS components, not approximations — so the argument shown is the argument the production team should implement.

**Evidence:**
- 22+ playground prototypes, each a named feature or UX experiment
- All data is mock — the focus is on the interaction model, not data wiring
- Framer Motion entrance animations (WeeklyReportContent) are persuasion artifacts — they exist to demonstrate the "earned reveal" promise, not as production-ready animation code
- Figma polling integration: design tokens flow from Figma → repo → components. Design-first workflow.
- `package.json` keywords: `["plus", "design-system", "prototyping", "cursor"]`
- Agent skills named for design workflow: uno-plan, uno-prototype, uno-post — lifecycle of a prototype pitch, not a production feature

**Confidence:** high. The telos is stated in multiple places (package.json description, AGENTS.md, README) and confirmed by structural evidence. The only ambiguity is whether some playground items are considered "done" prototypes vs. production-bound candidates — no formal status tracking exists.

## Disclaimers
This spine points in a direction. It is not a guarantee. Treat any claim
here that materially affects a port decision as worth a quick verification
pass against the actual code, not as settled fact.
