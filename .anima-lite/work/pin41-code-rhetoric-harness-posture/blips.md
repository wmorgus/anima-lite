## Blip: Step 4 header contradicted the new posture note
Severity: review-suggested
Location: `ari-code-rhetoric/SKILL.md` Step 4 opening line — "This step runs in the prod repo, not the anima-lite repo"
What happened: posture note (Claim 3) says harness-change reconcile treats anima-lite as its own prod; Step 4's own unedited header said the opposite in the same file.
Why: Claim 3, gap in propagation — the note existed but didn't override the pre-existing line it contradicted.
Resolution: fixed — Step 4 header and 4a now carry an explicit harness-change exception.

## Blip: Step 2 execution-subagent inputs required both spine files unconditionally
Severity: review-suggested
Location: `ari-code-rhetoric/SKILL.md` Step 2, execution subagent input list
What happened: still mandated `spine-proto/telos.md` + `spine-prod/telos.md` both, no harness-change exception, contradicting Claim 1's "no proto/prod split."
Why: Claim 1, propagation gap.
Resolution: fixed — input list now names the harness-change single-spine exception per line.

## Blip: top-level Inputs section unchanged for harness-change
Severity: info
Location: `ari-code-rhetoric/SKILL.md` Inputs section
What happened: same two-repo assumption baked into the file's opening Inputs list.
Why: not covered by a specific claim; residual propagation gap, cheap to close.
Resolution: fixed — each spine-dependent input row now carries a harness-change parenthetical.

## Blip: 4a's remote PR-target check not exempted for direct-commit deviation
Severity: info
Location: `ari-code-rhetoric/SKILL.md` 4a
What happened: no exception for harness-change direct-commit deviation licensed by Claim 3/4d-4f.
Resolution: fixed — 4a now names the exception explicitly.

## Blip: enumerated harness-change file types not literally in contract wording
Severity: info
Location: `ari-code-rhetoric/SKILL.md` posture note opener
What happened: SKILL.md names specific file types (skill file, HARNESS.md, CLAUDE.md, spec support file); contract speaks generically of "harness-change."
Resolution: no change — reasonable elaboration consistent with how `ari-argue-rhetoric`'s own harness-change section and PIN-26/32/36 precedent name concrete examples; not scope creep.

## Validation
Independent clean-context validation agent, 2026-07-14: all 4 claims present and correctly matching the contract; consistent with ari-argue-rhetoric's existing harness-change posture (no contradiction between the two skills). Initial verdict PASS (pending review) on two review-suggested propagation gaps (Step 4 header, Step 2 inputs) — both fixed. Three info-level notes, two fixed as cheap closes, one (enumerated file types) judged not actionable. Final status: **PASS**.
