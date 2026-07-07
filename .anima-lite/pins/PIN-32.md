### PIN-32 — intent.md work-type enum has no value for harness self-changes
captured: 2026-07-07
stub: 0
status: open
home: anima-lite
goes-stale: superseded once ari-intake/SKILL.md's intent template carries a work-type value (or open-enum rule) covering harness self-changes
relates-to: .claude/skills/ari-intake/SKILL.md (Output template), work/suspension-hardening/intent.md (first instance), PIN-27

Surfaced by ari-intake's very first work item (PIN-31, a harness self-change): the intent template's work-type enum is `port | ripple | debt-work` — none fit. First instance recorded `harness-change` ad hoc rather than fabricating a fit. Decide: add `harness-change` to the enum, or make the enum open with the listed values as the specified work-types. Also worth noting at shaping: PIN-31 resembled debt-work but the diagnosis was already human-made — the honesty gate's boundary (refuse undiagnosed debt-work vs. accept human-diagnosed divergence with language provenance) could be stated explicitly.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:**
