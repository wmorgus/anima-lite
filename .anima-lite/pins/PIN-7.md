### PIN-7 — Deployment-config generator (Cursor/Windsurf/Copilot sync)
captured: 2026-07-06
stub: 1
status: open
home: anima-lite
goes-stale: superseded once the generator ships and all three configs are regenerated with a generated-banner, or once explicitly deferred with new reasoning
relates-to: spine-anima-lite/formal.md §5, FINDING-5, HARNESS.md §3 (doc-drift check row), HARNESS.md §4, PIN-18

Deployment targets (Cursor `.cursor/rules/*.mdc`, Windsurf `.windsurf/rules/*`, Copilot `.github/copilot-instructions.md`) restate skill/doc content for other coding tools and have drifted badly (doc audit 2026-07-06 found single-file spine descriptions, old flat layout, no backlog/gates — worse than README's drift). Design decided (docs-strategy proposal, approved 2026-07-06): **generate, don't hand-sync.** Hand-sync is exactly the mechanism that already failed here. A generator converts this from HARNESS §3's "judgment" column to "mechanical."

Design: build `scripts/gen-deployment-configs.py` that stitches one shared markdown fragment (the facts meant to be identical across all four surfaces per HARNESS §4 — four-causes lens, skill roster, commitments) into each target's own template wrapper (Cursor `.mdc` frontmatter, Windsurf `trigger: always_on` frontmatter, Copilot plain markdown). Mark every generated file with `<!-- GENERATED — do not edit by hand; source: scripts/gen-deployment-configs.py -->`. Honest boundary: only kills drift for facts meant to be identical; genuinely tool-specific content (e.g. Copilot's extra claim-trap examples) stays hand-authored and can still drift — that's the right boundary, not full automation.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the generator script, a shared fact-fragment source, regenerating all three configs with generated-banners. Out — the mechanical drift *check* that diffs committed-vs-regenerated (that's PIN-18, ari-backlog sweep step 8); and any tool-specific hand-authored content, which the generator deliberately leaves alone.
**Batch:** docs-strategy
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**

**Spike-first (blocker before stub:2):** unverified whether `.cursor/*.mdc` frontmatter and Windsurf `trigger: always_on` have quirks (length limits, required per-file ordering) that make a shared-fragment generator harder than it looks. Short spike on the two frontmatter formats before committing to the generator's exact interface. This is why the pin sits at stub:1, not stub:2 — scope is named but the interface isn't nailed.
