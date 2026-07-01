# Efficient: plus-uno (proto)
(Reference depth — see telos.md for entry point and commit hash)

## Development
- `npm run dev` — starts Vite (port 4100) + Storybook (port 4200) concurrently via `concurrently`
- `npm run dev:vite` — Vite only, no Storybook
- `npm run dev:<playground>` — individual playground dev server (e.g., `dev:monthly-report` runs `vite --config playground/monthly-report/vite.config.js`)
- Weekly-report-demo has no named dev script in root package.json; run directly: `vite --config playground/weekly-report-demo/vite.config.js` (port 3009)

## Build
- `npm run build` — React SPA only → `dist/`
- `npm run build-storybook` — Storybook static site → `dist/storybook/`
- `npm run build:all` — both above, in sequence; this is the Netlify build command
- Vendor chunk splitting: `framer-motion` → `vendor-motion`, `highcharts` → `vendor-charts`, `react-bootstrap` → `vendor-bootstrap`, remaining node_modules → `vendor-core`

## Deploy
- Netlify: build command `npm run build:all`, publish dir `dist`
- Deployed URL: `https://plus-uno.netlify.app`
- Storybook accessible at `/storybook/` (served as static files before SPA catch-all redirect)
- SPA catch-all: all unmatched routes → `/index.html` (status 200)
- No branch deploys or preview environments documented in netlify.toml

## Testing
- Vitest 4 + Storybook vitest addon + Playwright (chromium, headless)
- `npm test` delegates to `npm --prefix design-system test` — tests live in `design-system/`, not root
- Storybook stories double as test units via `storybookTest` vitest plugin
- No CI config file present at repo root (no `.github/workflows/`, no `netlify.ci.yml` observed)

## Token generation
- `npm run generate:tokens` — regenerates SCSS/JS from token source; do not edit generated files directly
- `npm run sync:tokens` — syncs from Figma via API

## Verification checklist for a change to weekly-report-demo
1. Run `vite --config playground/weekly-report-demo/vite.config.js` and confirm port 3009 opens
2. Check animation plays on load and respects `prefers-reduced-motion`
3. Step through dimension review flow (unlock → feedback → training reveal)
4. Confirm no hardcoded color/spacing values introduced
5. Run `npm run build` to verify no chunk-size regressions
