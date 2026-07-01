---
name: ari-port
description: Performs the code translation from prototype to prod repo, using spine.md and the current branch's contract as binding context. Called by ari-lite only after ari-map and ari-argue have produced current, hash-matched, branch-scoped artifacts. Logs every meaningful translation decision as a blip and halts back to ari-argue if the contract proves unsatisfiable against the real code, rather than guessing.
---

# ari-port

Three steps: plan → execute → validate. The hard epistemic work happened upstream in ari-argue. If execution feels ambiguous, that's a sign the contract was incomplete, not a cue to use judgment alone.

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

### Step 1 — Plan

Before touching any code, write an execution plan and surface it. The plan maps every contract item to specific files and specifies the order of operations. No code moves until the plan is written.

Write `.anima-lite/plans/<branch-slug>.md`:

```markdown
# Execution Plan: <feature-name>
Contract: .anima-lite/contracts/<branch-slug>.md
Generated: <date>

## Claim changes
For each confirmed claim in the contract, in implementation order:
- **<claim name>**: <files to touch> — <what specifically changes and why>

## Substrate translations
- <file>: <what changes> — <prod formal cause pattern being followed>

## Order of operations
1. <step> — <dependency reason if non-obvious>
2. ...

## Blockers
<anything that would halt execution — CONTRACT-BREAK risk, missing infrastructure, ambiguous contract item>
```

Surface the plan before executing. If a blocker is found in planning, halt here — re-run ari-argue rather than proceeding with partial information.

### Step 2 — Execute

Work through the plan using the contract as the filter for every decision:

- **Substrate changes** — translate freely, using the prod spine's `formal.md` as the guide for idiom and structure.
- **Claim changes** — implement exactly per the contract's confirmed decision. Do not relitigate mid-execution.
- **Anything not covered by the contract** — log as a blip immediately, make the conservative choice (preserve current behavior).

If the contract is actively wrong — not incomplete, but contradicted by what the prototype code does — **halt**. Write the contradiction to blips as `CONTRACT-BREAK` and report execution paused pending a re-run of ari-argue.

### Step 3 — Validate

After execution, spawn a **validation agent** with clean context. The validation agent receives:
- The frozen contract (`.anima-lite/contracts/<branch-slug>.md`)
- The blips log (`.anima-lite/blips/<branch-slug>.md`)
- The list of files changed and their content

The validation agent checks three things independently, reading changed files directly — not relying on the execution agent's summary:

**A. Claim implementation** — for each confirmed claim change in the contract: is it implemented correctly? Absent or partial = FAIL.

**B. Blip classification quality** — for each blip with `Contracting failure?: n/a`: does the blip describe something that was actually a claim-level decision (something that should have gone to ari-argue)? If yes, that `n/a` is a misclassification = FAIL. This is the self-audit check the execution agent ran on itself — the validator audits the auditor.

**C. Blip severity routing** — `review-suggested` blips are surfaced to the user and require acknowledgment before PASS. `info` blips are noted but don't block. `CONTRACT-BREAK` blips mean execution should have already halted — if one reaches validation, that is itself a FAIL.

Additional CONTRACT-BREAK trigger: any user-visible broken interaction is a CONTRACT-BREAK regardless of invariant letter. "The feature works" is always an implicit invariant. Specifically: if a user action results in a silent failure or no-op (a control is enabled but the triggered operation fails with no feedback), that is CONTRACT-BREAK — not `review-suggested`. This cannot be waved through to human review. Functional correctness of implemented claims is non-negotiable; the stated invariant text is a floor, not a ceiling.

The validation agent returns one of:
- **PASS** — all claims implemented; all blip classifications correct; no `review-suggested` blips pending acknowledgment
- **PASS (pending review)** — claims and blip classifications correct, but `review-suggested` blips present; surface to user for acknowledgment, then PASS
- **FAIL: <specific finding>** — a confirmed claim absent/partial/contradicted, or a blip misclassification caught

On FAIL: loop back to Step 2, fix the specific finding, re-validate. Do not declare completion before the validation agent returns PASS or PASS (pending review) with acknowledged items.

## Output

Write `.anima-lite/plans/<branch-slug>.md` before execution (Step 1 output).

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

At session end (after validation PASS):
1. Summarize blips.md conversationally, grouped by severity, leading with `review-suggested` or above.
2. State explicitly which contract items (claim changes) were exercised and validated.
3. Leave the spine directories, contract, plan, and blips in place — don't delete `.anima-lite/`.

## Escalation / Notes

One agent session, one feature. A second feature on the same branch needs its own ari-argue pass and its own contract file, even if the spine is reused.

This skill does not implement locking for two sessions running against the identical branch-slug simultaneously — that's out of scope for a prototyping-stage tool. If that happens, the right answer is "don't," not new infrastructure.
