# Material: plus-uno (proto)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Languages
- JavaScript/JSX — majority of `design-system/src/` and `playground/*/src`
- TypeScript/TSX — real, not vestigial: `playground/research-assistant-chat/` is a full TS/TSX playground (App.tsx, types.ts, ~13 .tsx files); `design-system/src/storybook-docs/` has a small shadcn-style TS UI kit (button/card/alert/badge/tabs/separator + `lib/utils.ts`); root `tsconfig.json` present.
- SCSS — component styles + token source (`design-system/src/tokens/*.scss`, `design-system/src/styles/`)

## §2 Backend frameworks
None — plus-uno has no server tier. See §8 for the confirmed no-backend/no-persistence boundary and its one named exception.

## §3 Frontend libraries (versions confirmed in `package.json` / `design-system/package.json`)
- React 19.2.1 + react-dom — function components/hooks only
- react-router-dom 7.13.1 — SPA routing (real `<BrowserRouter>`, not static links; formal.md §3)
- Vite 8.0.1 (root and `design-system`) — dev server + build
- Storybook 10.2.7
- Bootstrap 5.3.3 + react-bootstrap 2.10.10 — layout/grid primitives PLUS components wrap
- Highcharts 12.4.0 (root) vs 12.5.0 (design-system devDep) — version skew between the two package.json files, unresolved (named finding)
- Framer Motion 12.38.0 — vendor-split chunk (`vendor-motion`)
- lucide-react, react-bootstrap-icons, radix-ui 1.4.3 (headless primitives)
- class-variance-authority + clsx + tailwind-merge — present as dependencies but **zero actual usage** inside `design-system/src/components/` (grep confirmed); className composition is instead three ad-hoc idioms (a `classnames` import in one file, manual `.filter(Boolean).join(' ')`, or template-literal concatenation) — see formal.md §3 seam
- tailwindcss 4.2.2 + `@tailwindcss/vite` — devDep only, conditionally loaded in root `vite.config.js` for Storybook docs; forbidden in components per AGENTS.md #9 (one violation found: `SidebarTab.mdx` uses Tailwind's `md:` responsive prefix — a doc file, not a rendered component)
- Font Awesome Free 7.2.0 — **not an npm package**, loaded via CDN `<link>` in `index.html` / `.storybook/*-head.html`; a live external pin outside lockfile control

## §4 Key dependencies
- `design-system/src/` is the one load-bearing shared dependency every playground pulls from (see §7).
- `uno-bot/` is a separate Cloudflare Workers Slack bot subsystem (own TS codebase, real Anthropic/Slack/Notion/GitHub/Figma API calls) — out of scope for the frontend prototype; do not fold its patterns into playground work.

## §5 Data structures / schemas
No shared schema of any kind. Every playground's "data" is a hand-written module-level JS/JSON constant shaped to look plausible for that one prototype — not derived from, or checked against, any real API or database contract. See §8.

## §6 State shape
Component-local React state (`useState`/hooks) is the norm; no repo-wide global state manager (no Redux/Zustand/general Context-as-store pattern) is confirmed. One exception: a cluster of ~5 playgrounds around `home-redesign` share a `ShellContext` by importing it across playground boundaries (`../../home-redesign/src/context/ShellContext`) rather than through any shared module — a de facto, undocumented shared-state layer. See formal.md §3–§4.

---
(Sections below are lookup APPENDICES — exempt from the ~50-line narrative cap per ari-map SKILL.md.)

## §7 Design-system component + token contract

One row per load-bearing DS component actually read (main `.jsx` + `.stories.jsx` where present). `design-system/src/components/` has 39 named component dirs (+ `layout/`, `training/` subdirs, `constants.js`, `index.js`); `design-system/src/forms/` has 20 form components; not every entry was opened — see gaps below.

| component | renders | key props/variants | source |
|---|---|---|---|
| Button | react-bootstrap Button wrapper + leading/trailing visual | `style` (primary/secondary/tertiary/success/warning/danger/info/default + 5 competency variants); `fill` (filled/tonal/outline/ghost/text); `size` (small/medium/large); `block` | `design-system/src/components/Button/Button.jsx` |
| PageLayout | TopBar (from `specs/Universal/Sections`) + Sidebar + content | `sidebarConfig`, `topBarConfig` (normalizes legacy brand/items shape → breadcrumbs/user) | `.../PageLayout/PageLayout.jsx` |
| Card | RB Card wrapper | `paddingSize`/`gapSize`/`radiusSize` (sm/md/lg), `borderSize`, `showBorder`, `image/title/subtitle/body/header/items/footer/links/actionButton` | `.../Card/Card.jsx` |
| Modal | RB Modal dialog | `type` (default/scrollable); `renderAs` (modal/inline); `paddingSize/gapSize/radiusSize`; `width`; `primaryButton/secondaryButton` | `.../Modal/Modal.jsx` |
| Table | plain `<table>` + wrapper | `headers` (string or `{text,width}`), `rows`, `striped`, `hover`, `bordered`, `density` (sm/md/lg) | `.../Table/Table.jsx` |
| Alert | RB Alert, dismissible banner | `style`, `title`, `dismissable`, internal `show` state | `.../Alert/Alert.jsx` |
| Badge | RB Badge pill | `style`, `size`, `leadingVisual/trailingVisual`, `counter`, `dismissible` | `.../Badge/Badge.jsx` |
| Navbar | RB Navbar/Nav/Container | `brand`, `items`, `backgroundColor` | `.../Navbar/Navbar.jsx` |
| Sidebar | fixed nav list, hardcoded Training/Toolkit categories | `user`, `onHomeClick`, `onTabClick`, `activeTabId`, `visible` | `.../Sidebar/Sidebar.jsx` |
| Dropdown | custom (non-RB) dropdown, outside-click close | `size`, `style`, `fill` (outline/ghost), `direction` (up/down/left/right), controlled/uncontrolled `isOpen` | `.../Dropdown/Dropdown.jsx` |
| Progress | custom bar, computed % from min/max/value | `style`, `size`, `striped`, `animated`, `label/showLabel` | `.../Progress/Progress.jsx` |
| Toast | RB Toast/ToastContainer | `style` (icon-mapped danger/success/info/warning/primary/secondary); `delay`, `autohide`, `timestamp` | `.../Toast/Toast.jsx` |
| Section | plain `<section>` container | `padding` (none/sm/md/lg/xl); `background` (transparent/surface/surface-alt); `title` | `.../Section/Section.jsx` |
| CompetencyBadge | icon badge for one of 5 SMART competency areas | `competencyArea` (required, normalized to slug), `size` | `.../CompetencyBadge/CompetencyBadge.jsx` |
| SessionAvailabilitySnackbar | snackbar confirming session availability | `type` (one-time/recurring), `available`, `timestamp`, `onClose` | `.../SessionAvailabilitySnackbar/SessionAvailabilitySnackbar.jsx` |
| DatePicker (forms/) | date input | prop shape not read in detail — gap | `design-system/src/forms/DatePicker/DatePicker.jsx` |
| InputGroup (forms/) | composite input, prefix/suffix slot | prop shape not read in detail — gap | `design-system/src/forms/InputGroup/InputGroup.jsx` |

`design-system/src/specs/` — composite/higher-order specs re-exported via the barrel, one per product pillar (each has a `STRUCTURE.md`): `Admin/` (Group/Session/Student/Tutor composites), `Home/` (Cards/Elements/Modals/Pages/Sections), `Login/`, `Profile/`, `Toolkit/` (pre/in/post-session), `Training/` (Lessons + onboarding), `Universal/` (Cards/Elements/Pages/Sections + `ResponsiveFrame.jsx`, includes the `TopBar` `PageLayout` uses). These map 1:1 to the `PRODUCT_PILLARS` constant (§9).

Gaps (not individually confirmed): Accordion, Breadcrumb, ButtonGroup, Carousel, Collapse, Divider, Footer, Jumbotron, ListGroup, LoadingGif, Logo, MediaObject, NavPills, NavTabs, Pagination, Popover, RichTextEditor, Scrollspy, SidebarTab, Spinner, StaticBadgeSmart, Tooltip, UserAvatar, SessionManagementSnackbar, `layout/`, `training/`, `DataViz/` (9 chart wrappers, barrel-exported), and 18 of 20 form components beyond DatePicker/InputGroup.

### Token categories

| category | file | consumption convention |
|---|---|---|
| Color (M3 roles) | `tokens/_colors.scss` | CSS custom property `--color-*` in `:root` |
| Primitives | `tokens/_primitives.scss` | `:root` custom properties |
| Spacing (semantic) | `tokens/_spacing_semantics.scss` | `--size-*`, referencing primitive `--size-spacing-*` |
| Layout | `tokens/_layout.scss` | `:root` custom properties |
| Typography | `tokens/_fonts.scss` | `:root` custom properties |
| Elevation | `tokens/_elevation.scss` | `--elevation-light-N` box-shadow values |
| Source-of-truth JSON | `tokens/source/*.json` (colors_accent, colors_neutral, size_semantics, size_layout, size_primitive) | raw Figma export; not consumed directly by components |

`design-system/src/styles/main.scss` pulls every token partial in with `@use "../tokens/colors" as *;` (Sass namespace import, to preserve `:root` emission); components then consume tokens as plain **runtime CSS custom properties** (`var(--size-element-radius-md)`, `var(--color-on-primary)`), not compile-time Sass value imports.

## §8 Capabilities this proto does NOT have
- **No backend / persistence / auth — every displayed field is a design promise, not a backing.** `fetch(` across `playground/**`+`src/**`: 3 hits total, all inside one playground (`storybook-ai-agent-llm-api`) — one fetches a local `stories.json`, one calls `https://api.openai.com/v1/chat/completions` directly from the browser. `axios`: 0 hits repo-wide. `localStorage`: 0 hits outside that same playground. Every other playground's data is a module-level JS/JSON constant.
- **`storybook-ai-agent-llm-api` is the one sanctioned exception** to "no live external calls" — a real client-exposed call to `api.openai.com`. Treat it as a named exception, not a precedent for adding real API calls elsewhere.
- **DS components do NOT have a uniform className/token-composition contract**, despite `class-variance-authority`/`clsx`/`tailwind-merge` sitting in `package.json` — zero usage of any of them inside `design-system/src/components/`; a port assuming a `cva()`-based variant system would be inventing one.
- **The Prototype Marketplace has no single source of truth.** A playground must be registered in two places by hand — `src/pages/PrototypeMarket/prototypes-data.js` (the catalog) and `src/App.jsx`'s route/lazy-import maps — with nothing enforcing the two stay in sync.
- **`uno-bot/` capabilities (real LLM/Slack/Notion/GitHub/Figma integration) are not available to playgrounds** — it is a wholly separate Cloudflare Worker subsystem, not a service playgrounds can call into.

## §9 Domain vocabulary
- **playground** = one directory under `playground/<name>/` (22 real prototypes; `playground/README.md` and `playground/templates/` are not playgrounds). 16 of 22 have their own `vite.config.js` and are independently runnable; the other 7 are page components only reachable through the SPA shell.
- **design-system** = `design-system/src/`, barrel-exported via `design-system/src/index.js`; the one shared dependency every playground draws from.
- **token** = a design value (color/spacing/typography/radius/elevation) resolved through a CSS custom property or SCSS token file — never a hardcoded literal (§7).
- **spec** = a composite, higher-order component under `design-system/src/specs/<Pillar>/`, one per product pillar, re-exported through the barrel.
- **playground-isolation** = the intended pattern where each playground's `vite.config.js` independently re-resolves `@`/`@plus-ds` to `design-system/src` and imports no code from other playgrounds. Holds for DS access; violated for a ~5-playground cluster around `home-redesign` that shares `ShellContext` and image assets across playground boundaries (formal.md §3).
- **`@` / `@plus-ds` alias** = defined per-`vite.config.js` (root and each standalone playground), resolving to `design-system/src`; the required indirection for any DS import (telos.md §2).
- **Prototype Marketplace** = the `/` and `/market` routes, rendered by `src/pages/PrototypeMarket/PrototypeMarket.jsx`, data-driven by `src/pages/PrototypeMarket/prototypes-data.js`.
- **fidelity stage** = one of `STAGES = ['low','mid','high']`, a real code constant (`prototypes-data.js`), not just README color.
- **product pillar** = one of `PRODUCT_PILLARS = ['admin','home','login','profile','toolkit','training','universal']`, lining up 1:1 with `design-system/src/specs/*` directory names.
- **`ShellContext`** = a React Context defined inside `playground/home-redesign/src/context/`, imported by ~5 other playgrounds across playground boundaries — a de facto shared-state layer the isolation model doesn't formally account for.
- **barrel** = `design-system/src/index.js`; exists and re-exports everything correctly but is not actually consumed by any sampled playground import (formal.md §3–§4).
