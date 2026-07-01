# Material: plus-uno (proto)
(Reference depth — see telos.md for entry point and commit hash)

## Runtime
- React 19.2 + react-dom — function components, hooks only (no class components observed)
- React Router DOM 7.13 — SPA routing for multi-playground navigation
- Vite 8 — dev server (port 4100) and production build

## Design system layer (load-bearing)
- `design-system/src/` — component library consumed via `@` / `@plus-ds` alias
  - `components/` — ~38 named components (Button, Badge, Alert, Progress, PageLayout, etc.)
  - `tokens/` — SCSS token files: `_colors.scss`, `_spacing_semantics.scss`, `_elevation.scss`, `_fonts.scss`, `_layout.scss`, `_primitives.scss`
  - `specs/` — higher-order composite specs (Home/Cards, Home/Sections, etc.) re-exported via `design-system/src/index.js`
  - `styles/main.scss` — global stylesheet entry; load paths wired in vite config

## UI dependencies
- Bootstrap 5.3 + react-bootstrap 2.10 — foundational layout/grid primitives; PLUS components layer on top
- Highcharts 12 + highcharts-react-official — charting (used in other playgrounds; not in weekly-report-demo)
- Framer Motion 12 — animation primitives (vendor-split chunk; present in main bundle)
- Lucide React + react-bootstrap-icons + Font Awesome Free (CDN) — icon sets; FA Free only per forbidden-patterns
- Radix UI 1.4 — accessible primitives (headless)
- class-variance-authority + clsx + tailwind-merge — className composition utilities

## State shape (weekly-report-demo)
- All mock data is module-level constants (`REPORT_DATA`, `FILTERED_TRAINING`) — no external data fetching
- Component-local state only: `reviewedCount`, `activeKey`, `feedbackSelections`, `hasEntered`, animation counters
- No global state manager (no Redux, Zustand, Context API for data)

## Styling
- SCSS modules per-playground (`WeeklyReportPage.scss`) — not CSS Modules, plain SCSS
- Design tokens consumed as CSS custom properties (`var(--color-*)`) and SCSS variables
- Tailwind CSS 4 present but conditional in vite config (Storybook docs only; NOT used in playground components)

## Build artifacts
- `dist/` — React SPA build
- `dist/storybook/` — Storybook static site
- Vendor chunks: `vendor-motion`, `vendor-charts`, `vendor-bootstrap`, `vendor-core`
