### PIN-32 — intent.md work-type enum has no value for harness self-changes
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: superseded once ari-intake/SKILL.md's intent template carries a work-type value (or open-enum rule) covering harness self-changes
relates-to: .claude/skills/ari-intake/SKILL.md (Output template), work/suspension-hardening/intent.md (first instance), PIN-27

Surfaced by ari-intake's very first work item (PIN-31, a harness self-change): the intent template's work-type enum is `port | ripple | debt-work` — none fit. First instance recorded `harness-change` ad hoc rather than fabricating a fit. Decide: add `harness-change` to the enum, or make the enum open with the listed values as the specified work-types. Also worth noting at shaping: PIN-31 resembled debt-work but the diagnosis was already human-made — the honesty gate's boundary (refuse undiagnosed debt-work vs. accept human-diagnosed divergence with language provenance) could be stated explicitly.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — add `harness-change` as a named work-type value; write per-work-type posture for it (source = live design round, single-spine comparison). Out — building an open-enum mechanism; decided as a closed addition, not a generalization.
**Batch:** unbatched
**Contract:** decided directly (mechanical addition, no separate argue pass needed): `harness-change` added to `.claude/skills/ari-intake/SKILL.md`'s Work-type enum and Output template, plus a per-work-type posture paragraph.
**Resolution:** done 2026-07-07. `harness-change` added to the enum (`ari-intake/SKILL.md`), with posture note (argued-by: language, source names the design round; single-spine, self-repo comparison). `ari-argue/SKILL.md` preconditions updated to accept harness-change's single-spine shape, plus a classification note (renames/gate-rule changes = claim, doc wording/layout = substrate). First live instance run through the fixed path: `work/pin26-ripple-contract/{intent,contract}.md` (PIN-26's own rulings). Same fix closes PIN-36.
