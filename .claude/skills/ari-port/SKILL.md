---
name: ari-port
description: Performs the code translation from prototype to prod repo, using spine.md and the current branch's contract as binding context. Called by ari-lite only after ari-map and ari-argue have produced current, hash-matched, branch-scoped artifacts. Logs every meaningful translation decision as a blip and halts back to ari-argue if the contract proves unsatisfiable against the real code, rather than guessing.
---

# ari-port

Execution: "let it fly, human watches for issues." The hard epistemic work happened upstream — this skill should feel mechanical. If it feels ambiguous, that's a sign the contract was incomplete, not a cue to use judgment alone.

## Inputs

- `.anima-lite/spine-proto/telos.md` — commit hash for precondition check.
- `.anima-lite/spine-prod/formal.md` — primary reference for substrate translation. This is the guide for idiom and structure: new code must follow the prod repo's architectural patterns, not copy the proto's.
- `.anima-lite/spine-prod/telos.md` — for the don't-contradict rules; substrate translations must not violate them.
- Pull `material.md` or `efficient.md` from either spine directory if a specific translation decision requires it.
- `.anima-lite/contracts/<branch-slug>.md` for the current branch and feature.
- The prototype code being translated.

## Preconditions

1. Both `spine-proto/` and `spine-prod/` exist and `telos.md` in each is current. If either is stale or missing: halt, request ari-map for the affected repo.
2. `contracts/<branch-slug>.md` exists for the current branch and feature, status is not "DRAFT," and has no unconfirmed items in Open Questions. If any fail: halt, request ari-argue.
3. The contract's `Spine commit:` hash matches `spine-proto/telos.md`'s current `Commit:`. If mismatched — another branch refreshed the spine since this contract was confirmed — don't auto-fail or proceed silently. Summarize what changed and ask the user whether the contract still holds or needs a quick re-pass through ari-argue.

Do not proceed on partial or mismatched context. This is the failure mode the whole pipeline exists to prevent: code moved without its meaning, or moved against terrain that already shifted underneath it.

## Active orientations

**Ari face (self-policing).** Every blip carries a `Contracting failure?` field. This is not optional metadata — it is the self-policing obligation: each uncovered case is an occasion to ask whether the contract was incomplete, not just what to do now. A blip that skips this question exempts the contracting phase from the quality sweep.

## Process

Work through the port using the contract as the filter for every decision:

- **Substrate changes** — translate freely, using judgment on idiom and structure appropriate to the prod repo's formal cause (from the spine).
- **Claim changes** — implement exactly per the contract's confirmed decision. Do not relitigate mid-execution.
- **Anything not covered by the contract** — new information the contract didn't anticipate. Don't guess which bucket it belongs in. Log it as a blip immediately and make the conservative choice (preserve current behavior) unless the user has pre-authorized judgment calls on uncovered cases.

If the contract is actively wrong — not incomplete, but contradicted by what the prototype code does — **halt**. Write the contradiction to blips as `CONTRACT-BREAK` and report that execution is paused pending a re-run of ari-argue with this new information.

## Output

Append to `.anima-lite/blips/<branch-slug>.md` (same slug as the contract) throughout the session:

```markdown
## Blip: <short title>
Severity: <info|review-suggested|CONTRACT-BREAK>
Location: <file:line>
What happened: <the decision>
Why: <reasoning>
Downstream consequence: <what this means going forward>
Contracting failure?: <what should have been in the contract to cover this — or "n/a" if genuinely unforeseeable>
```

A blip is logged whenever: a substrate change has a non-obvious downstream consequence; something uncovered by the contract came up and got a conservative default; a prod-repo convention conflicts with the prototype's approach and one was chosen; or anything a user skimming the PR would likely miss but want to know.

At session end:
1. Summarize blips.md conversationally, grouped by severity, leading with `review-suggested` or above.
2. State explicitly which contract items (claim changes) were actually exercised, as a record separate from the mechanical diff.
3. Leave `spine.md` and this branch's contract in place — don't delete `.anima-lite/`.

## Escalation / Notes

One agent session, one feature. A second feature on the same branch needs its own ari-argue pass and its own contract file, even if the spine is reused.

This skill does not implement locking for two sessions running against the identical branch-slug simultaneously — that's out of scope for a prototyping-stage tool. If that happens, the right answer is "don't," not new infrastructure.
