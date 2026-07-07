# Intent: the resolution — one-sentence sovereign description (PIN-33)
Slug: resolution
Work-type: harness-change *(enum gap — second instance, PIN-32 tracks; see Notes)*
Generated: 2026-07-07
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 28d8464 *(stale vs. HEAD — known, tracked as PIN-23; see Notes)*

## Telos statement

Institute the resolution: a one-sentence sovereign description of the repo, above the telos doc in authority — the sentence is ground truth, the code is fallible embodiment, the telos doc is fallible commentary. Wire it into intake's existing telos check and define how divergence is adjudicated (drift vs. growth). Checked against spine-anima-lite telos §1 Purpose and §2 Don't-contradict: clean — this extends promise-custody upward to the repo's own top-level promise and strengthens §2 "never change an argument without the user noticing" (the resolution is the apex argument); no conflict raised, GATE-TELOS did not fire.

## Sources

- `.anima-lite/backlog.md` PIN-33 body (captured 2026-07-07, operator proposal)
- Design ratification round 2026-07-07 (operator answers, four questions: home / text / mechanism / adjudication — all recommended options confirmed)
- `.anima-lite/reorient/identity.md` (custodian identity the resolution caps)
- `.anima-lite/reorient/four-causes.md` (final-cause frame; resolution is the final cause's final cause)

## Claims

- The resolution lives in its own artifact at repo root: `RESOLUTION.md` — the sentence plus a ratification line (date + operator), nothing else. Smallest file, highest authority; telos.md, README, and skills cite it rather than restating it. anima-lite only for now; target repos getting one (ari-map emits?) is future work, not this claim.
  argued-by: language PIN-33 body + ratification round Q1 (home)
- anima-lite's own resolution text is: "agentic harness using aristotelean decomposition to build software that admits change only as argument." The closing clause replaces the flagged-soft "manage its changes through language"; post-intake it states an enforced property (nothing enters the pipeline unargued), not an aspiration.
  argued-by: language PIN-33 body (draft + soft flag) + ratification round Q2 (text)
- The per-intake terminal check — "does the repo this change produces still answer to the resolution?" — folds into GATE-TELOS as its apex layer: intake reads `RESOLUTION.md` first, then telos.md. One gate, two authority layers; no new gate ID. Bootstrap posture: if the target repo has no RESOLUTION.md, the apex layer is noted absent, not fabricated (anima-lite is the only repo with one today).
  argued-by: language PIN-33 mechanism-fit paragraph + ratification round Q3 (mechanism)
- Divergence adjudication is constitutional: a GATE-TELOS resolution-layer failure is named either drift (the change/code is wrong — fix it, custodian's normal work) or growth (the resolution itself must change). Growth is never bundled: a resolution edit is its own workstream — separate intake, separate commit, explicit operator ratification recorded in RESOLUTION.md's ratification line — and the change that provoked the divergence stays blocked until the resolution question resolves. Guard target: quietly editing the resolution to match drifted code.
  argued-by: language PIN-33 adjudication paragraph (founder-exemption trap shape) + ratification round Q4 (adjudication)

## Notes

- **Work-type enum gap, second instance.** `harness-change` again; PIN-32 already tracks the enum fix. Recording the recurrence, not re-pinning.
- **Generalization / paper-shaped claim: capture only.** The resolution generalizes beyond anima-lite (every repo could carry one; teleological-software claim). Ratified as capture-only this round — record in the design record and PHILOSOPHY.md, build nothing for other repos.
- **Target spine is stale** (28d8464; PIN-23). Its §1/§2 remain accurate for the check performed here. The telos refresh trigger ("gate structure changes") fires again with this work item — third firing on 2026-07-07. Noted for PIN-23, not blocking intake.
- **Authority-inversion wrinkle for the checker.** GATE-TELOS's two layers have opposite fallibility postures: telos.md is commentary that can be stale (hash-checked), RESOLUTION.md is sovereign and presumed correct — a mismatch with it indicts the change (drift) or triggers constitutional growth, never a silent RESOLUTION.md edit. The spec text must state this asymmetry.
