### PIN-36 — harness self-changes skip contract machinery
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: a ratified decision on how harness-change work-types run the argue/contract stage (or an explicit ruling that pin-level Contract fields suffice)
relates-to: PIN-32 (work-type enum gap), PIN-27 (ari-intake), work/pin33-ratification/judgment.md (surfaced it)

Operator observation during PIN-34 dogfood GATE-QUERY: "we should be running contracts on build changes to anima-lite system. oops." Harness self-changes (PIN-33 resolution build, PIN-34 ari-read build) ran intake (intent.md with argued-by claims) but never the argue stage — no contract.md, no formal claim-by-claim confirmation artifact; ratification lived in design-round Q&A plus pin Contract fields instead. Either harness-change work-types should run ari-argue to a real contract, or the pin-level Contract field should be ratified as the equivalent for this work-type. Ties into PIN-32: the enum gap and the pipeline gap are the same underlying fact — harness self-changes are a work-type the pipeline doesn't formally know yet.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — decide and build the ruling: harness-change runs a real ari-argue-rhetoric pass to a `contract.md`, pin-level Contract fields become a pointer/summary, not a substitute. Out — retroactively re-running PIN-31/PIN-33/PIN-34's already-closed self-changes through the new path; they stand as-is.
**Batch:** unbatched
**Contract:** ratified directly, same session as PIN-32 (they're one fix): harness-change work-types run intake→argue like any other work-type; the pin's Contract field references the resulting contract.md rather than restating it.
**Resolution:** done 2026-07-07. Ruling: harness self-changes run the real argue/contract stage (not the pin-field-as-substitute alternative). Fixed together with PIN-32 (same underlying gap): `ari-intake` and `ari-argue` both updated for the `harness-change` work-type. First instance run live on PIN-26's own three rulings (two-tier break-reopen, parallel-by-default legs, argue/port rhetoric renames) — `work/pin26-ripple-contract/intent.md` + `contract.md`; PIN-26.md's Contract field now points at it instead of duplicating the text. Earlier harness-changes (PIN-31, PIN-33, PIN-34) are not retroactively re-run — this closes the gap going forward, per Scope.
