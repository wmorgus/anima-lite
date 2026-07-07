### PIN-17 — Commit-shape discipline hook (first discipline hook)
captured: 2026-07-06
stub: 0
status: open
home: anima-lite
goes-stale: if run4 shows the prompt-level stub discipline (PIN-10) holds on its own, urgency drops; if commit-shape fails again, this escalates; DOWNGRADED 2026-07-07 — run4 showed prompt-level commit discipline holds, mechanical hook no longer urgent
relates-to: HARNESS.md §3 (first hook candidate), PIN-1, PIN-10

HARNESS.md Section 3 tags commit-shape discipline as mechanical and names it the first hook candidate, with run3's empty-claim-commit failure as evidence that prompt-only enforcement was insufficient. Build the actual check: a script (pre-commit hook in the prod repo, or a validation-agent step) that verifies the substrate commit contains no behavior belonging to a confirmed claim and that no claim commit is empty. Distinct from the session-cost hook (metrics); this is the first *discipline* hook — it blocks rather than records. Wait for run4 evidence before building: if PIN-10's stub discipline holds, this may be unnecessary ceremony.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:** not traced (not closing). run4 (2026-07-07): commit-shape discipline HELD under prompt-level enforcement (PIN-10) on a hard port, so the mechanical commit-shape hook is DE-PRIORITIZED — no longer the urgent "first hook candidate." A mechanical commit-shape check could still be built later, but run4 showed the more valuable enforcement gap is elsewhere: judgment-type gates (e.g. GATE-BREAK) that cannot be mechanized and were bypassed by subagent judgment — see PIN-20. Reassess only if a future run shows commit-shape regressing.
