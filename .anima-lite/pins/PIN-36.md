### PIN-36 — harness self-changes skip contract machinery
captured: 2026-07-07
stub: 0
status: open
home: anima-lite
goes-stale: a ratified decision on how harness-change work-types run the argue/contract stage (or an explicit ruling that pin-level Contract fields suffice)
relates-to: PIN-32 (work-type enum gap), PIN-27 (ari-intake), work/pin33-ratification/judgment.md (surfaced it)

Operator observation during PIN-34 dogfood GATE-QUERY: "we should be running contracts on build changes to anima-lite system. oops." Harness self-changes (PIN-33 resolution build, PIN-34 ari-read build) ran intake (intent.md with argued-by claims) but never the argue stage — no contract.md, no formal claim-by-claim confirmation artifact; ratification lived in design-round Q&A plus pin Contract fields instead. Either harness-change work-types should run ari-argue to a real contract, or the pin-level Contract field should be ratified as the equivalent for this work-type. Ties into PIN-32: the enum gap and the pipeline gap are the same underlying fact — harness self-changes are a work-type the pipeline doesn't formally know yet.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:** <filled only at done/superseded>
