# Formal: plus-uno (proto)
(Reference depth — see telos.md for entry point and commit hash)

## Module boundaries
- `design-system/src/` — shared component/token library; consumed by all playgrounds via `@` alias; barrel-exported through `design-system/src/index.js`
- `playground/<name>/` — isolated prototype; owns its own `vite.config.js`, `src/`, SCSS; reaches into `design-system/` only through the alias
- `src/` — root SPA shell (App.jsx, main.jsx); routes across playgrounds via react-router

## Dominant pattern: playground isolation with shared DS
Each playground is a self-contained Vite root (`playground/<name>/vite.config.js`) that re-resolves `@` to `design-system/src`. Playgrounds share no state and import no code from each other — the cross-playground asset import in weekly-report-demo (`../../home-redesign/src/assets/...`) is a named inconsistency (see below).

## Typical change shape
1. Add `playground/<name>/` directory with its own `vite.config.js` and `src/`
2. Import PLUS components via `@/components/<Name>/<Name>` (never by path into DS internals)
3. Import composite specs via `@/specs/<Domain>/<Group>` (re-exported from DS)
4. Write playground-local SCSS that uses token variables and avoids hardcoded values
5. Register a dev script in root `package.json` (`dev:<name>`)

## Animation pattern (weekly-report-demo)
- Entry animation: CSS class toggle (`has-entered`) on mount via `requestAnimationFrame`
- Numeric count-up: `easeOutCubic` RAF loop with staggered `setTimeout` offsets (0ms / 120ms / 220ms / 320ms)
- `prefers-reduced-motion` respected: motion skipped, final values set immediately
- Inline `<style>` tag injected into component for animation keyframes — not in external SCSS

## Icon convention
- Font Awesome Free only: `fa-solid`, `fa-regular`, `fa-brands` class prefixes
- Icons are `<i>` elements with `aria-hidden="true"` where decorative
- `lucide-react` and `react-bootstrap-icons` present as package deps but weekly-report-demo uses FA exclusively

## Design-token consumption
- CSS custom properties: `var(--color-success)`, `var(--color-warning)`, `var(--color-surface-container)`, `var(--size-element-gap-sm)` etc.
- SCSS token imports available via `loadPaths` (no `@use` path required — just `@use 'colors'`)

## Named inconsistencies (findings)
- **Cross-playground asset import**: `WeeklyReportContent.jsx` imports images from `../../home-redesign/src/assets/`. This violates the playground isolation boundary. The images are not in a shared assets location — they live inside another playground's src.
- **Inline keyframe injection**: Animation CSS is injected via `<style>` inside the component render rather than the playground's SCSS file. This is inconsistent with the rest of the file's SCSS-based styling approach.
- **`tailwind-merge` + `clsx` + CVA present but unused in playgrounds**: These are design-system-level utilities not wired into weekly-report-demo's component pattern.
- **`manualChunks` deprecated note**: Root `vite.config.js` documents that `manualChunks` is deprecated in Vite 8 but defers migration — an acknowledged drift point.
