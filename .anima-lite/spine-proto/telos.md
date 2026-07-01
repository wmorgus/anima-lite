# Telos: plus-uno (proto)
Commit: 9c02f5e8
Confidence: high
Refresh trigger: Any change to vite.config.js, package.json, design-system/src/ barrel exports, or AGENTS.md forbidden-patterns list

## Purpose
plus-uno is a Vite + React prototyping environment for the PLUS design system — it exists to produce high-fidelity UI prototypes that demonstrate design intent using real PLUS components and design tokens, not to ship production features. New playground work either validates a design hypothesis using the established component/token system, or it does not belong here. Code is disposable; the design system conventions it exercises are not.

## Don't contradict
- Do not hardcode colors, spacing, typography, radius, or elevation — every visual value must resolve through a design token (`var(--color-*)`, `var(--size-*)`, or SCSS token import).
- Do not import design-system internals directly by path — always go through the `@` / `@plus-ds` alias resolving to `design-system/src/`.
- Do not create a component that duplicates one already in `design-system/src/components/` — check the components index first.
- Do not install new packages without explicit user approval — the dependency surface is intentionally locked.
- Do not use Font Awesome Pro icon classes (`fa-light`, `fa-thin`, `fa-sharp`, `fa-duotone`, Pro-only names) — FA Free only.

## Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
