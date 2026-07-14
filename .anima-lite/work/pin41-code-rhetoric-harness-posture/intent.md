# Intent: PIN-41 — give ari-code-rhetoric a harness-change posture
Slug: pin41-code-rhetoric-harness-posture
Work-type: harness-change
Generated: 2026-07-14
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 522e44b (current)

## Telos statement
Add an explicit harness-change posture to `ari-code-rhetoric/SKILL.md`, parallel to the one `ari-argue-rhetoric/SKILL.md` already carries, so a harness self-change gets the same execute/validate discipline (plan, clean-context execution against the contract, blip logging, independent validation) a port gets — without forcing it through port-specific machinery (spine-proto/prod split, playwright, PR-to-external-repo) that doesn't apply when the repo being changed and the repo running the pipeline are the same repo. Checked against RESOLUTION.md: clean — this closes a gap in the harness's own self-change discipline, directly serving "software that admits change only as argument" by making harness self-changes argue and execute through the same rigor as everything else. Checked against spine-anima-lite/telos.md §1/§2: clean — no Don't-contradict rule touched; extends existing harness-change support (already real in ari-intake and ari-argue-rhetoric) to the one skill that's missing it.

## Sources
- Operator design round, this session, 2026-07-14 — surfaced live when PIN-39's diagnosis-layer build skipped ari-code-rhetoric entirely because nothing in its spec covered a single-repo, no-proto/prod, no-external-PR build; operator confirmed the gap and asked for both a flag pin and a lightweight ad hoc validation pass on PIN-39, then to fix the gap itself
- `.anima-lite/pins/PIN-41.md` — captured scope, stub:0 at start of this pass
- `.claude/skills/ari-argue-rhetoric/SKILL.md` — "Harness-change classification" section, the parallel fix this same gap already received on the argue side (added per PIN-26/32/36 precedent)
- `.anima-lite/work/pin39-diagnose-contract/{plan,blips}.md` — the ad hoc code-rhetoric-shaped pass run manually for PIN-39, proof that the discipline (plan, clean-context validation, blips) translates to single-repo posture without needing spine-proto/prod or playwright

## Claims
- Claim 1 — `ari-code-rhetoric/SKILL.md` Preconditions §1 names `harness-change` explicitly as a posture (currently lists port, single-repo debt-work, world-drift; omits harness-change entirely), with the same single-repo/self-spine comparison debt-work already uses — no `spine-proto`/`spine-prod` split required.
  argued-by: language <operator, this session, 2026-07-14, confirming the flagged gap and asking for it to be fixed>
- Claim 2 — Harness-change execution skips playwright verification (Step 3 D/E) and the cross-leg coherence check (Step 3 F, ripple-only) entirely — neither applies when there's no running feature to browse to and no second leg to compare against.
  argued-by: language <operator, this session — same reasoning ari-argue-rhetoric's existing harness-change carve-out already used for its own playwright/Schema-deps omission>
- Claim 3 — Harness-change reconcile (Step 4) treats the harness repo itself as both the "prod repo" and the target of the PR — no cross-repo PR flow, no `spine-proto/formal.md` translation-guide step (Step 2's "Feature branch first" and commit-discipline rules still apply: a feature branch, commit-per-claim, PR against this repo's own integration branch if one exists, or a direct reviewed commit if the harness has no PR convention of its own for internal changes).
  argued-by: language <operator, this session, confirming the ad hoc PIN-39 pass (direct commit, no PR) as an acceptable precedent for how small harness-change fixes land>
- Claim 4 — The core discipline is preserved regardless of posture: Step 1 (plan before execute), Step 2's clean-context execution subagent working the contract as filter, blip logging on anything uncovered, and Step 3's independent validation agent checking claim implementation against the contract (checks A and B; C's blip-classification-quality check still applies). This is not new — it's the explicit statement that harness-change does NOT get to skip this core loop the way it currently does by omission.
  argued-by: language <operator, this session: "why not do the code-rhetoric execution step tho? ... we miss out on the built-in validation from the code-rhetoric step" — the direct statement this pin exists to answer>

## Notes
Fourth harness-change to run real intake→argue (after PIN-26, PIN-39, and this one) — same posture as those: single-spine, `argued-by: language <source>` throughout, no prototype to read an argument off of. This item is self-referential in one respect worth naming: it is a harness-change about how harness-changes execute. No infinite regress risk — this build itself still runs through the (currently gapped) ari-code-rhetoric informally, the same ad hoc way PIN-39's build did, and closes the gap for every harness-change after it, not for itself retroactively.
