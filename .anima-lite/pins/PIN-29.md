### PIN-29 — workstream vocabulary + suspension procedure (pause/resume as first-class)
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: superseded once ari-backlog/SKILL.md carries the workstream definition + suspension procedure AND run5 has been suspended through it (first dogfood)
relates-to: .anima-lite/_run5_isolated/RESTORE.md (the ad-hoc precedent), PIN-25 (reorient parent), .claude/skills/ari-backlog/SKILL.md (pin format + lifecycle — owning spec), vocab.md (workstream joins the settled vocabulary)

Vocabulary gap found while pausing run5: nothing names a work item IN FLIGHT with live state (staged git, partial artifacts, mid-lifecycle) that can be suspended and resumed. Pins capture future work; runs name attempts; work-types name kinds. Definition ratified 2026-07-07: **workstream = the live span of a work item from intake to harvest; suspension = its pause verb; a pin points at the suspension record, doesn't contain it.** Evidence the concept is real: run5 got ad-hoc suspension by hand (_run5_isolated/ + RESTORE.md) before the word existed. Formalization: ari-backlog gains a `paused` pin status + a workstream-suspension procedure (state manifest, mandatory suspension commit — no dirty-tree pauses, State: field). Run5 is the first dogfood.

---
Shaping fields.

**Scope:** In — workstream definition + suspension/resume procedure in ari-backlog/SKILL.md (owning spec for pin lifecycle); `paused` added to pin status enum; suspend run5 through the new procedure (separate pin records the paused workstream itself). Out — automation/hooks for suspension checks; any generalization to multi-workstream scheduling.
**Batch:** reorient
**Contract:** claim-shaped — the harness newly promises its operator that pausing a workstream is durable and reversible: all live state committed at suspension (no dirty-tree pauses), a manifest names exactly what exists and how to resume, and the backlog carries the paused status visibly until resumed or superseded.
**Resolution:** procedure landed in ari-backlog/SKILL.md; run5 suspended through it as first dogfood (PIN-30, commits 7b19d56/9dc2e86); three dogfood findings recorded — (a) procedure ambiguous on concurrent-workstream dirt: "commit-everything" needs scoping to the suspended workstream's own files, (b) pin-of-record edits can collide file-locally with another in-flight pin's uncommitted edit in backlog.md (needed manual hunk split), (c) State: field format unspecified — first-instance convention is "manifest <path>; suspension commit <hash>".
