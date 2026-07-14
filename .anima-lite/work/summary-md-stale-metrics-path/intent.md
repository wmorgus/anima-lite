# Intent: fix metrics/summary.md's stale pre-rename spec path
Slug: summary-md-stale-metrics-path
Work-type: debt-work
Generated: 2026-07-14
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 522e44b (current)

## Telos statement
Correct `summary.md`'s schema pointer so a live, standing document names the spec file's current path instead of a dead pre-rename one. Checked against RESOLUTION.md: clean — this is the custodian's normal work, directly: catching and fixing a promise/artifact divergence (the doc promises a path; the artifact isn't there) is exactly what the resolution names as anima-lite's job. Checked against spine-anima-lite/telos.md §1/§2: clean — no rule in §2's Don't-contradict list touched; §1's purpose (custody of promise/artifact alignment) is directly served, not just left unconflicted.

## Sources
- `work/summary-md-stale-metrics-path/diagnosis.md` — the diagnosis this intent is built from (primitive: spec, evidence cited)
- `.anima-lite/pins/PIN-38.md` — prior capture of this same divergence (2026-07-09), already scoped as mechanical with no argument to preserve

## Claims
- Claim 1 — `.anima-lite/metrics/summary.md` line 3's schema pointer names `.claude/skills/ari-code-rhetoric/metrics-spec.md` (current path), not `.claude/skills/ari-port/metrics-spec.md` (dead, pre-PIN-26-rename path).
  argued-by: language <work/summary-md-stale-metrics-path/diagnosis.md>

## Notes
Single mechanical claim, no substrate/claim ambiguity — a path string either matches the live file location or doesn't. First debt-work item to run end to end through `/ari-diagnose` → `/ari-intake`, satisfying PIN-39's goes-stale condition once `/ari-argue-rhetoric` and the fix itself land.
