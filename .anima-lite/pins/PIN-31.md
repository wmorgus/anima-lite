### PIN-31 — ari-backlog suspension procedure hardening (three dogfood findings from PIN-29/PIN-30)
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: superseded once ari-backlog/SKILL.md disambiguates suspension-commit scope, addresses same-file pin collision, and specifies State: format
relates-to: PIN-29, PIN-30, .claude/skills/ari-backlog/SKILL.md

First dogfood of the workstream-suspension procedure (run5, PIN-29/PIN-30) surfaced three gaps: (a) procedure ambiguous on concurrent-workstream dirt — "commit-everything" needs scoping to the suspended workstream's own files, not the whole tree; (b) pin-of-record edits can collide file-locally with another in-flight pin's uncommitted edit in backlog.md, needing a manual hunk split; (c) the `State:` shaping field's format is unspecified — first-instance convention used was "manifest <path>; suspension commit <hash>," not yet codified.

---
Shaping fields.

**Scope:** In — the three SKILL.md fixes above. Out — multi-workstream scheduling; suspension automation.
**Batch:** reorient
**Contract:** claim-shaped — suspension-commit scope narrows from "commit everything, no exceptions" to "everything belonging to the suspended workstream; unrelated concurrent-workstream dirt excluded." Confirmed by operator 2026-07-07 (via ari-argue claim round). Findings (b)/(c) substrate.
**Resolution:** done 2026-07-07 — first work item run end-to-end through `/ari-intake` (dogfood of PIN-27): intent artifact `work/suspension-hardening/intent.md`, three claims all `argued-by: language` (PIN-29 findings a/b/c), GATE-TELOS clean against self-spine. Claim 1 operator-confirmed; all three landed in ari-backlog/SKILL.md suspend steps 2–3 (scoped commit + hunk-split maneuver + State: format). Intake surfaced one new gap → PIN-32.
