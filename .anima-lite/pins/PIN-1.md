### PIN-1 — Post-run-review: why did the execution plan fall short?
captured: 2026-07-05
stub: 0
status: done
home: anima-lite
goes-stale: superseded once PIN-10 (commit discipline hygiene fix) lands and a subsequent run shows the enforcement actually holding
relates-to: self-spine FINDING-2 (conservative default not always operationalized at skill level), PIN-10, PIN-17

The weekly-report stress-test execution subagent returned empty claim commits — all claim logic landed in the substrate commit rather than being held out per-claim per the commit discipline spec. The plan was correct; the subagent didn't follow it. Open questions: was the plan underspecified about when to separate claim logic from substrate scaffolding? Did the subagent misread the plan or override it with a judgment call? Does the substrate/claim commit boundary need to be enforced more explicitly (e.g. "do NOT write claim logic in substrate files — stub them, then fill in a separate commit")? PIN-10 landed the prompt-level fix; run4 is its live test. Address alongside run4 review.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:** run4 (2026-07-07) confirmed PIN-10's commit-discipline fix HOLDS. The execution subagent kept the substrate commit claim-free on a harder port than run3 (969 insertions, full 7-part Java/Hibernate entity stack): 1 substrate commit (stubs only, driver-verified in isolation) + 4 real per-claim commits, 0 empty claim commits. The run3 shortfall was subagent judgment overriding a correct prompt-level protocol, NOT plan underspecification. The deeper generalization — that the same override pattern recurs on judgment-type gates, not just commit shape — is spun out to PIN-20. Closing.
