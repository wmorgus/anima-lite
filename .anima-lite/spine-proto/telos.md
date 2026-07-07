# Telos: plus-uno (proto)
Commit: 9c02f5e8
Confidence: high
Refresh trigger: Any change to root `vite.config.js` alias/chunking config, `package.json` dependency surface, `design-system/src/index.js` barrel exports, `AGENTS.md` forbidden-patterns list, or `src/pages/PrototypeMarket/prototypes-data.js` registry shape.

## §1 Purpose
plus-uno is a Vite + React + Storybook prototyping environment for the PLUS design system. It exists to produce high-fidelity UI prototypes that demonstrate design intent using real PLUS design-system components and tokens, surfaced through an in-app Prototype Marketplace — not to ship production features. New playground work either validates a design hypothesis using the established component/token system, or it does not belong here. Code is disposable; the design-system conventions it exercises, and the Marketplace's ability to surface the result, are not.

## §2 Don't contradict
- Do not hardcode colors, spacing, typography, radius, or elevation — every visual value must resolve through a design token (CSS custom property `var(--color-*)`/`var(--size-*)`, or an SCSS token import). See material.md §7.
- Import design-system components through the `@` / `@plus-ds` alias (resolves to `design-system/src`). The actual, universal convention is deep component-path imports (`@/components/Button/Button`) — AGENTS.md's stricter "always use the barrel (`design-system/src/index.js`)" rule is aspirational and followed nowhere in sampled code (0/96 imports); don't invent a barrel-only migration unless asked. See formal.md §3–§4.
- Do not create a component that duplicates one already in `design-system/src/components/` (39 components) or `design-system/src/forms/` (20 form components) — check both directories first.
- Do not install new packages without explicit user approval — the dependency surface is intentionally locked.
- Do not use Font Awesome Pro icon classes (`fa-light`, `fa-thin`, `fa-sharp`, `fa-duotone`, Pro-only names) — FA Free 7.2.0 only, loaded via CDN `<link>`, not an npm dependency.
- Do not invent a backend, persistence layer, or auth for a playground — every displayed field is a design promise, not a backing. The one sanctioned exception (a live third-party API call) is named in material.md §8; do not treat it as precedent without asking.

## §3 Cause files (reference depth)
- [material.md](material.md) — tech stack, design-system component/token contract (§7), capabilities this proto does NOT have (§8), domain vocabulary (§9)
- [formal.md](formal.md) — design-system / playground / SPA-shell layering, per-stratum patterns + seams, cross-layer registration protocol
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## §4 Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
