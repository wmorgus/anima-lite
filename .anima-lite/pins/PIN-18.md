### PIN-18 — Doc-drift check as ari-backlog sweep step 8
captured: 2026-07-06
stub: 1
status: open
home: anima-lite
goes-stale: superseded once the check is built and ari-backlog's sweep runs it; or if PIN-7's generator is dropped (then half the check has nothing to diff against)
relates-to: HARNESS.md §3 (doc-drift check row, tagged mechanical/UNBUILT 2026-07-06), HARNESS.md §4, PIN-7

HARNESS.md §3 now tags a doc-drift check as mechanical/unbuilt. Build it, homed in ari-backlog's **slow-lane sweep as step 8** (periodic housekeeping cadence — NOT a per-session hook like session-cost.py; doc drift is sweep-cadence, not session-cadence). The check: (a) grep README.md/CLAUDE.md for layout-path strings and confirm they match the real `ports/<slug>/` pattern on disk rather than a hardcoded stale pattern; (b) diff committed deployment configs against fresh generator output (depends on PIN-7's generator existing — until then, part (b) is a no-op stub). Distinct from session-cost (metrics hook) and from the commit-shape discipline hook (PIN-17): this guards documentation legibility, the inward-facing version of the legibility the harness demands outward.

This is the drift-prevention half of the docs-strategy proposal (approved 2026-07-06); the doc-layer content fixes already landed, this makes re-drift mechanically catchable instead of relying on the next reader noticing.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the check script (or inline sweep logic) + adding step 8 to ari-backlog/SKILL.md's slow-lane sweep. Out — the generator itself (PIN-7); building doc-drift checks for docs beyond README/CLAUDE/configs (start with the ones in HARNESS §4's ownership map).
**Batch:** docs-strategy
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**
