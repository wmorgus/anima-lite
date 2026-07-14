# Intent: PIN-39 diagnosis-layer contract — /ari-diagnose scope
Slug: pin39-diagnose-contract
Work-type: harness-change
Generated: 2026-07-14
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 522e44b (current, matches HEAD per PIN-23 re-probe — no staleness note needed)

## Telos statement
Give the diagnosis layer (PIN-39) a written contract before build starts, following the same intake→argue path harness self-changes now use (PIN-36) rather than a pin-field stand-in. Checked against RESOLUTION.md: clean — this is machinery that lets debt-work (already named in RESOLUTION.md's own custody claim) become buildable; it extends the custodian's reach rather than changing what it's custodian of. Checked against spine-anima-lite/telos.md §1: clean — §1 names debt-work explicitly as "ratified direction, built partway"; this item is the next increment of that, not a new purpose. Checked against §2's Don't-contradict list: clean — no rule touched (this item, if anything, extends "nothing enters through an undeclared default" to debt-work's missing intake path).

## Sources
- Operator design round, this session, 2026-07-14 — five shaping questions answered directly by the operator, one clarified via structured choice (scan order)
- `.anima-lite/reorient/diagnosis-layer.md` — the five ratified rulings this contract formalizes
- `.anima-lite/pins/PIN-39.md` — captured scope, stub:1 at start of this pass
- `.anima-lite/reorient/identity.md` — four-primitive taxonomy (spec/epistemic/world-drift/craft), provenance anima-corps `logic.md` §8.6/§8.11 (read directly this session to confirm non-mapping against Aristotle's four causes)

## Claims
- Claim 1 — `/ari-diagnose` is a new skill, upstream of `/ari-intake`, invoked only for debt-work; port/ripple/harness-change are unaffected and do not route through it. Bare name, no `-rhetoric` suffix (diagnosis surfaces fact, doesn't argue).
  argued-by: language <operator, this session, 2026-07-14: "1. separate skill i'd say">
- Claim 2 — `/ari-diagnose` writes a new committed artifact type, `work/<slug>/diagnosis.md` (divergence located, primitive(s) assigned, evidence cited), which `/ari-intake` then reads as debt-work's source — the same structural role prototype plays for port.
  argued-by: language <operator, this session, 2026-07-14: "3. should get its own committed artifact for sure">
- Claim 3 — the four primitives are scanned in a fixed order, not treated as an independent checklist: epistemic → spec → world-drift → craft. This closes anima-corps `logic.md` §8.12's explicitly-open orthogonal-vs-ordered question, for anima-lite's diagnosis layer specifically.
  argued-by: language <operator, this session, 2026-07-14: "4. they relate to each other - there's a correct order to do the scan. causes aren't independent of each other." — order confirmed via structured choice: "epistemic → spec → world-drift → craft">
- Claim 4 — `/ari-diagnose` accepts exactly two entry modes: (a) operator-nominated pointer ("diagnose this"), (b) `/ari-read` honoring-failure handoff (an honoring-question failure already routed to "pin → debt-work intent" per `read-register.md`). Self-triggered/unprompted spine scanning is explicitly out of this contract's scope — different commitment shape (trigger cadence, cost model, false-positive tolerance), left to spin to its own future pin if picked up.
  argued-by: language <operator, this session, 2026-07-14, on entry point: "a and b are good" (confirming both in scope, self-triggered scan left out per the prior design-round framing)>
- Claim 5 — evidence bar is per-primitive, not uniform: each primitive's citation standard is specified on its own terms when the skill is built. World-drift's bar is external-record-strong (CVE/EOL/deprecation notice); spec's and epistemic's bars are not fixed by this contract and remain build-time decisions.
  argued-by: language <operator, this session, 2026-07-14: "5. bar per primitive">

## Notes
This is PIN-39's contract pass, second instance of PIN-36's fix (first was PIN-26/work/pin26-ripple-contract). All five claims are scope/shape rulings about a skill not yet built — no code exists yet to check claims against, same posture as PIN-26's claims 1-2 (ripple's own unbuilt machinery). Claim 1's invocation-surface change (a new skill name entering the harness) is the higher-blast-radius item, same pattern PIN-26's claim 3 flagged for renames — here it's an addition, not a rename, so the blast radius is smaller (no existing references to sweep) but the same discipline applies: the name must be right before anything references it.
