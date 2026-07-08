# Intent: PIN-26 ripple contract — rulings + skill renames
Slug: pin26-ripple-contract
Work-type: harness-change
Generated: 2026-07-07
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 28d8464 (self-spine known stale — PIN-23 re-probe pending, held until after this build lands; staleness noted per honesty discipline, not treated as blocking for a harness-change whose telos check is narrow)

## Telos statement
Give the ripple work-type (PIN-26) a written contract before build starts, and in doing so give harness self-changes a real intake→argue path instead of a pin-field stand-in (PIN-36). Checked against RESOLUTION.md: clean — this change is machinery that lets the harness argue for its own changes, directly reinforcing "software that admits change only as argument," not in tension with it. Checked against spine-anima-lite/telos.md §1/§2: clean — no rule in §2's Don't-contradict list is touched; §1's "argument survives substrate translation" purpose is about the port pipeline specifically, and this item is upstream harness structure, not a port run, so no conflict to adjudicate.

## Sources
- Operator design round, this session, 2026-07-07 — live gate discussion working through `reorient/ripple.md`'s two unratified proposals, plus an operator-initiated third item (skill renames)
- `.anima-lite/reorient/ripple.md` — prior spec, rulings 1-3, proposed-not-ratified section (source of the two proposals being resolved)
- `.anima-lite/pins/PIN-26.md` — captured scope, stub:1 at start of this round

## Claims
- Claim 1 — CONTRACT-BREAK in any ripple leg reopens ari-argue-rhetoric *consideration* for every other leg; execution (ari-code-rhetoric re-run) only reopens where that consideration concludes the leg's telos is better honored by the amendment; otherwise logged closed, not silently skipped.
  argued-by: language <operator ratification, this session, 2026-07-07: "break all legs for consideration (not necessarily execution) of rework... a lil judgement can save a lot of downstream telos">
- Claim 2 — Ripple legs execute in parallel by default; no privileged first leg. Sequential ordering (any leg first) is available only as an explicit judgment-based deviation, not a fixed default.
  argued-by: language <operator ratification, this session, 2026-07-07: "porting to N legs at once seems like a reasonable default (contract guarantees they'll all speak the same language)... unless the user has a specific reason not to">
- Claim 3 — `ari-argue` is renamed to `ari-argue-rhetoric`; `ari-port` is renamed to `ari-code-rhetoric`. `ari-intake` and `ari-map` are not renamed.
  argued-by: language <operator proposal + ratification, this session, 2026-07-07: "ari-argue is ari-argue-rhetoric (formal) and ari-code-rhetoric (efficient). those names?" — confirmed>

## Notes
This item is itself the first instance of PIN-36's fix: a harness self-change running a real intake→argue pass instead of stopping at a pin's Contract field. Claims 1-2 alter gate/execution behavior for a work-type not yet built (ripple's own machinery, PIN-26 scope); claim 3 is a rename affecting the invocation surface of two already-built, already-in-use skills — flagged to argue as the higher-blast-radius item (full-repo reference sweep) versus claims 1-2 (spec text not yet built against).
