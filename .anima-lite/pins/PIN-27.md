### PIN-27 — ari-intake: new upstream skill (telos-sharpening + everything-argued-for)
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: superseded once an intake skill (or explicitly-ratified argue-phase alternative) exists with a defined argued-intent-artifact format and at least one work-type running through it
relates-to: .anima-lite/reorient/intake.md (spec stub), PIN-26 (ripple — first consumer), PIN-25 (reorient parent), GATE-TELOS (fires earlier under intake), .anima-lite/reorient/identity.md (diagnosis layer — candidate future home)

Ratified 2026-07-07 (Will): intake is currently implicit pre-mapping inside ari-argue; ripple exposes the seam. New skill sharpens the work item's telos and ensures everything being added is argued for — by prototype or by language derived from context. Output: argued intent artifact that ari-argue contracts from. Cross-cutting: upstream of argue for all work-types (port's intake near-trivial; ripple's authored; debt-work's intake = the diagnosis layer itself — noted as diagnosis's natural home, not yet ratified). Open at shaping: skill-vs-phase boundary, artifact format (per-claim argued-by provenance), telos-sharpening gate semantics. Spec stub: reorient/intake.md.

---
Shaping fields.

**Scope:** In — settle the three open questions in intake.md (DONE 2026-07-07, Q1–3 round: separate skill; `work/<slug>/intent.md` w/ per-claim `argued-by:` provenance; GATE-TELOS owned by intake + cheap argue backstop — recorded in reorient/intake.md); write ari-intake/SKILL.md; rewire ari-argue inputs to consume the intent artifact; HARNESS updates (§1 GATE-TELOS ownership + backstop, §2 argued-intent format row, §4 roster 4→5); README/CLAUDE/PHILOSOPHY roster + flow updates. Out — the diagnosis layer build (separate; intake is only its candidate home); ripple execution machinery (PIN-26).
**Batch:** reorient
**Contract:** claim-shaped — the pipeline's entry promise changes: nothing enters the pipeline unargued. Every work item passes intake before contracting; intake mints the workstream slug and emits `work/<slug>/intent.md` where every claim carries an `argued-by: prototype <path>` or `argued-by: language <source>` provenance line; ari-argue contracts only from that artifact and refuses claims without provenance; GATE-TELOS fires at intake (repo-telos meets change-telos) with a conditional re-fire backstop in argue. Ratified 2026-07-07.
**Resolution:** in-progress — skill built 2026-07-07 (sonnet subagent, driver-validated): new `.claude/skills/ari-intake/SKILL.md` (7-step process, GATE-TELOS primary fire, intent.md template, debt-work honesty-gated as "ratified direction, not yet built"); ari-argue rewired (intent.md primary input, argued-by refusal precondition, GATE-TELOS conditional backstop); HARNESS §1 gate row split intake/backstop, §2 intent-format row, §4 roster 4→5; README/CLAUDE/PHILOSOPHY roster + flow updated. DONE 2026-07-07: dogfood complete — PIN-31 ran end-to-end as first language-derived work item (`work/suspension-hardening/intent.md`, GATE-TELOS clean, claim confirmed via argue round, changes landed). goes-stale condition met (skill exists, format defined, one work-type through it). Dogfood yield: PIN-32 (work-type enum gap).
