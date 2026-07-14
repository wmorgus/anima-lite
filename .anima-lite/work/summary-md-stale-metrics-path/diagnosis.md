# Diagnosis: metrics/summary.md's stale pre-rename spec path
Slug: summary-md-stale-metrics-path
Entry mode: operator-nominated (pointer: `.anima-lite/metrics/summary.md`, per PIN-38)
Generated: 2026-07-14
Spine checked: spine-anima-lite/, Commit: 522e44b (current)
Primitive(s): spec

## Divergence
`.anima-lite/metrics/summary.md` line 3 reads: "Schema for every artifact under `.anima-lite/metrics/`: `.claude/skills/ari-port/metrics-spec.md`." That path is dead. The file it names now lives at `.claude/skills/ari-code-rhetoric/metrics-spec.md` — confirmed present on disk at that path, absent at the old one.

## Scan
- **Epistemic** — checked first, cleared immediately. The *because* is fully recoverable: PIN-26 (ripple work-type build, ratified 2026-07-07) renamed `ari-port` → `ari-code-rhetoric` and specified "full forward-facing reference sweep across CLAUDE.md/HARNESS.md/README.md/PHILOSOPHY.md/.windsurf/.github" as part of that build's scope. Nobody has to guess why this line exists or what it used to point at — it's a known, dated, documented rename. Not epistemic: proceed to spec.
- **Spec** — matches. At the time `summary.md` was written, the pointer was correct — faithful to the then-current skill name. PIN-26's rename changed the intent (the skill's name and canonical path) without this file's pointer being updated to track it. This is exactly spec's definition: code (the pointer) faithfully implements an intent that has since changed. Scan stops here — evidence cleanly settles on one primitive, no ambiguity between primitives to note.
- World-drift and craft not reached (per Process step 3's stopping rule — a single primitive confirmed with citable evidence, no signal of a second primitive also applying).

## Evidence
Per spec's evidence bar (Process step 4): the recovered *because* is PIN-26's rename commit and its explicitly-scoped reference sweep (`.anima-lite/pins/PIN-26.md`, Resolution field: "full forward-facing reference sweep... historical/archive/done-pin text left untouched on purpose"). The delta: the because asks for every *live, forward-facing* reference to use `ari-code-rhetoric`; `summary.md` line 3 is a live, standing document (not an archived/dated snapshot — PIN-38 already distinguishes it explicitly from the 2026-07-06 backlog-health row, which correctly keeps the old name as a historically accurate dated record) still carrying the pre-rename name. The sweep's own stated scope (CLAUDE.md/HARNESS.md/README.md/PHILOSOPHY.md/.windsurf/.github) never named `.anima-lite/metrics/summary.md` — this file was out of the sweep's checked set, not an edge case the sweep considered and got wrong.

## Open questions
None. Single primitive, cleanly cited, no ambiguity. Fix is mechanical (one-line path correction) — matches PIN-38's own Contract field ("n/a — mechanical, no argument to preserve").
