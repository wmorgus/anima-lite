# Intent: spine connective tissue — `lives-in:` tags + self-correction procedure
Slug: pin37-spine-connective-tissue
Work-type: harness-change
Generated: 2026-07-08
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 522e44b (current, freshly re-probed by PIN-23 this week)

## Telos statement
Give the spine a mechanical way to know which of its own promises a code change implicates, and name the standing procedure by which the spine corrects itself — closing the gap PIN-25 item (c) left open ("incremental spine maintenance design") and replacing an earlier, weaker proposal (a `Pending triggers:` field) discussed but not yet ratified this session. Checked against RESOLUTION.md: clean — traceable promise-to-file pointers directly serve "software that admits change only as argument," the same direction as the resolution itself. Checked against spine-anima-lite/telos.md §1/§2: clean — reinforces §1's custodial purpose (alignment between promise and artifact) and touches no §2 don't-contradict rule.

## Sources
- `.anima-lite/reorient/spine-self-correction.md` — agent-authored audit (operator: "i had an agent write it"), operator-ratified 2026-07-08 with one correction (PIN-26 "stuck" overclaim, noted in that file)
- Operator design round, this session, 2026-07-08 — live discussion folding the audit into PIN-25c, replacing the `Pending triggers:` proposal

## Claims
- Claim 1 — `ari-map`'s output spec gains a `lives-in: <path[s]>` tag on every §2 Don't-contradict rule and every named finding, pointing at the file(s) that embody the promise (connective tissue, not cached code — the file/symbol pointer only).
  argued-by: language <reorient/spine-self-correction.md, "Prospective useful features" item 1>
- Claim 2 — multi-path `lives-in:` is allowed (a promise enforced at N call sites), but `ari-map` flags 3+ paths on one rule during authoring as a smell — a signal the rule may be too coarse and should split, not silently accepted.
  argued-by: language <reorient/spine-self-correction.md, item 3>
- Claim 3 — the spine self-correction procedure is named explicitly (PHILOSOPHY.md, alongside the five-field tiling): detection is a diff against `lives-in:`-tagged paths since the spine's `Commit:` hash (mechanical, once claim 1 ships); judgment on whether a flagged rule is actually stale stays a human/agent call, never an auto-rewrite; execution is today's full re-probe (incremental re-probe of only the affected section is named as future direction, not built); correction narrative stays out of the spine artifact and lives in the commit message instead — the same belief/record split the five-field tiling already states, cited rather than restated as a new rule.
  argued-by: language <operator design round, this session, 2026-07-08 + reorient/spine-self-correction.md's recommendation section>
- Claim 4 — a staleness-check script (diffing `git log` against `lives-in:`-tagged paths to flag due-for-audit rules) and a promise→promise graph (for PIN-26's deeper ripple needs) are explicitly deferred, not built now: the staleness script waits until claim 1 has shipped and at least one spine has been hand-re-audited against it; the graph waits until a real N-leg ripple exists to design against.
  argued-by: language <reorient/spine-self-correction.md, items 2 and 4, "Recommendation">

## Notes
This is the second harness-change to run the real intake→argue path (first was PIN-26/PIN-37's sibling, work/pin26-ripple-contract/). Claims 1-2 are a spec-only change to ari-map/SKILL.md's Output section (no behavior change to any other skill). Claim 3 is a doc addition to PHILOSOPHY.md, no code/spec mechanism beyond claim 1. Claim 4 authorizes nothing being built — it's the explicit deferral itself that's the claim, so a future reader doesn't mistake silence for an oversight.
