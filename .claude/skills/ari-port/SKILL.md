---
name: ari-port
description: Performs the code translation from prototype to prod repo, using spine.md and the current branch's contract as binding context. Called by ari-lite only after ari-map and ari-argue have produced current, hash-matched, branch-scoped artifacts. Logs every meaningful translation decision as a blip and halts back to ari-argue if the contract proves unsatisfiable against the real code, rather than guessing.
---

# ari-port

Four steps: plan → execute → validate → reconcile. The hard epistemic work happened upstream in ari-argue. If execution feels ambiguous, that's a sign the contract was incomplete, not a cue to use judgment alone.

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

**Conservative default.** When the contract does not cover a decision, preserve current behavior and log a blip. Do not guess which bucket an uncovered case belongs in. Do not resolve ambiguity by choosing the option that makes the port simpler or faster. The conservative default is a mechanism: it makes gaps visible rather than hiding them behind a plausible-looking implementation. A blip saying "preserved by default, contract gap" is a correct artifact; a silently-resolved gap is a failure mode.

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

> **⛔ REQUIRED GATE — plan blockers**
> If `## Blockers` in the plan is non-empty, surface each blocker to the user. Do not spawn the execution subagent until all blockers are explicitly cleared.
> The pipeline halts here. Do not proceed until explicitly cleared.

> **◎ OPTIONAL GATE — plan review**
> After blockers are cleared (or if none exist), offer plan review. "Plan written — review before execution? (skip to proceed)."

### Step 2 — Execute

**Feature branch first.** Before touching any code, check the current branch in the prod repo. If you are on a long-lived branch (`main`, `master`, `dev`, `develop`, `staging`, or any branch that appears to be an integration target), create and switch to a feature branch named after the contract slug:

```
git checkout -b <branch-slug>
```

If a branch with that name already exists, check it out and verify it's at the same base as the current integration branch (no stale commits). If the branch is ahead of the integration target in unexpected ways, halt and ask the user.

Do not make any commits on a long-lived branch. All port commits must land on the feature branch. The commit discipline below is meaningless if the commits end up on `dev` — there is no clean PR surface to review against.

**Execution subagent.** Spawn a single execution subagent with clean context. The clean-context isolation is the point: an agent that cannot fall back on upstream argumentation to fill gaps must blip anything the contract doesn't cover. This enforces contract-as-filter discipline — gaps that a context-carrying agent would silently paper over become visible blips.

The execution subagent receives:
- The contract (`.anima-lite/contracts/<branch-slug>.md`)
- Both spine telos files (`spine-proto/telos.md` and `spine-prod/telos.md`) — for don't-contradict rules
- The plan (`.anima-lite/plans/<branch-slug>.md`)
- The prototype source files being translated
- The prod repo path and current branch name

The subagent's job: implement the plan, follow commit discipline below, write blips to `.anima-lite/blips/<branch-slug>.md`. Work through the plan using the contract as the filter for every decision:

- **Substrate changes** — translate freely, using the prod spine's `formal.md` as the guide for idiom and structure. Every substrate translation decision must cite the spine section that grounds it (e.g. "Translating jQuery collapse to Bootstrap 4.1.3 data-toggle/data-target per spine-prod/material.md §2 (Bootstrap 4.1.3 confirmed)"). If no spine section covers the decision, say so explicitly in the blip or log line. This is the same discipline the blip format's `Why:` field enforces below — one citation rule, not two: every reasoning trail in this skill either names the spine section it rests on or says explicitly that none applies.
- **Claim changes** — implement exactly per the contract's confirmed decision, in that claim's own commit — never inside the substrate commit. See commit discipline below: substrate files touched by a future claim get a stub, not the claim's real behavior. Do not relitigate mid-execution.
- **Anything not covered by the contract** — log as a blip immediately, make the conservative choice (preserve current behavior).
- **Contract-clarity watch** — while implementing, flag anything in the contract that looks under-specified or potentially wrong in light of what the prototype source actually does. This is softer than CONTRACT-BREAK (which fires only when the contract is actively contradicted). Log these as `Severity: info`, `Type: contract-clarity` blips. They don't halt execution but give the main agent and reviewer a signal that the contract may need sharpening for future ports of similar features.

If the contract is actively wrong — not incomplete, but contradicted by what the prototype code does — **halt**. Write the contradiction to blips as `CONTRACT-BREAK` and report execution paused pending a re-run of ari-argue.

The subagent returns a handoff to the main agent:
- List of commits made (hash + claim mapping)
- Summary of blips logged
- `contract_break: true/false` — if true, execution is paused

Main agent on `contract_break: true`: surface the CONTRACT-BREAK blip to the user and request an ari-argue re-run before proceeding. Do not advance to Step 3.

**Partial commit preservation.** Do not revert commits already made before the CONTRACT-BREAK was discovered. The commits represent completed work that the contract did cover — reverting them loses that work without benefit. Leave the branch as-is. When re-running ari-argue, provide the list of commits already made (from the execution subagent's handoff) so ari-argue can write a contract amendment rather than a full re-contract. The amendment covers only the uncovered case; previously confirmed and implemented claims are settled.

> **⛔ REQUIRED GATE — CONTRACT-BREAK**
> If the execution subagent returns `contract_break: true`, surface the CONTRACT-BREAK blip to the user and halt. Re-run ari-argue with the new information before proceeding to Step 3.
> The pipeline halts here. Do not proceed until explicitly cleared.

**Commit discipline** — commit after each claim is fully implemented, before moving to the next. Do not accumulate all changes into a single working-tree blob. The commit message format:

```
port(<feature>): <claim name> — <one-line summary>

Contract: .anima-lite/contracts/<branch-slug>.md
Claim: <Claim N>
```

Example: `port(monthly-report): isLowData empty state — show limited-data alert when <5 sessions`

Rules:
- Substrate-only changes (no claim) may be batched into a single `port(<feature>): substrate — <description>` commit at the start.
- The substrate commit contains scaffolding only. Where a file will later carry claim behavior, the substrate version stubs it — the claim's behavior is visibly absent (not yet wired) or a no-op at substrate commit time. Do NOT write claim logic into substrate files; stub them, then fill the stub in that claim's own commit.
- Each confirmed claim change gets its own commit, and that commit's diff IS the claim's implementation — it fills the stub left by the substrate commit. An empty claim commit (message with no corresponding behavioral diff) is a discipline failure, never correct; if a claim commit would be empty, the behavior was left in the substrate commit and must be pulled back out.
- If a claim spans multiple files (e.g. Java DTO + JS), they commit together — the claim is the unit, not the file.
- Never commit dev-only config changes (e.g. `hbm2ddl.auto=none`, dummy secret files). These are working-tree scaffolding, not part of the port.
- New files must be explicitly `git add`ed — don't assume they'll be picked up.

**Self-check before the substrate commit:** does this diff contain behavior belonging to any confirmed claim? If yes, pull it out and stub it before committing.

Clean commit history is load-bearing for Step 4 (reconcile): the per-claim diff is the reviewable unit that maps commit → contract claim. A monolithic substrate commit that carries claim behavior destroys that mapping — a reviewer reading the git log should be able to map each commit to a contract claim without opening the code.

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

**E. Visual audit for review-suggested blips with UI implications.** After the static checks in A–C pass, for each `review-suggested` blip that describes a visible UI state (placeholder content, stub section, missing expected content, partially-implemented UI), the validation agent runs a playwright step:

1. Navigate to the feature URL (from the contract's `playwright.feature_url`, or from the prod dev server if the contract does not yet have a playwright block).
2. Screenshot the specific section the blip describes.
3. Describe what renders: text content, element count, any placeholder indicators, button states.
4. Append this description to the blip as a `Visual audit:` field — a single sentence describing the actual rendered state.

This is not a PASS/FAIL gate. It is documentation: the validation agent surfaces the actual rendered state for human review alongside the blip. A blip that says "training recommendations stub" should become "training recommendations stub — Visual audit: section renders one card with text 'Training recommendations coming soon'" so the reviewer knows exactly what they are approving, not just that something is deferred.

If the dev server is not running, note it per blip as `Visual audit: skipped — dev server not reachable` and proceed. Do not block PASS on a missing dev server; the visual audit is documentation, not a verification gate.

The validation agent returns one of:
- **PASS** — all claims implemented; all blip classifications correct; no `review-suggested` blips pending acknowledgment
- **PASS (pending review)** — claims and blip classifications correct, but `review-suggested` blips present; surface to user for acknowledgment, then PASS

> **⛔ REQUIRED GATE — review-suggested blips**
> If the validation agent returns PASS (pending review), surface each review-suggested blip to the user. The user must acknowledge each one before the pipeline proceeds to Step 4.
> The pipeline halts here. Do not proceed until explicitly cleared.
- **FAIL: <specific finding>** — a confirmed claim absent/partial/contradicted, or a blip misclassification caught

On FAIL: loop back to Step 2, fix the specific finding, re-validate. Do not declare completion before the validation agent returns PASS or PASS (pending review) with acknowledged items.

**D. Live browser validation (strongly recommended, optional)** — if the contract specifies a `playwright:` block (see contract format below), the validation agent runs a browser pass using Playwright MCP tools after the static checks pass. The browser pass is a second validation layer: it confirms claims are not only implemented in code but functional in a running browser.

If `playwright:` is present in the contract, the validation agent:
1. Navigates to `playwright.login_url` and performs the login sequence specified in `playwright.login_steps`
2. Navigates to `playwright.feature_url`
3. Takes a full-page screenshot
4. For each claim in `playwright.checks`, performs the specified interaction and verifies the expected outcome
5. Logs any failure as a `CONTRACT-BREAK` blip — a claim that passes static code review but fails live in the browser is a CONTRACT-BREAK

The Playwright pass does not replace the static check — both must pass. If the dev server is not running, skip D and note it as an info blip: `Severity: info — Playwright pass skipped: dev server not reachable at <url>`.

**Contract `playwright:` block format** (add to the contract file):
```markdown
## Playwright verification
login_url: http://localhost:8080/demo?pl2-demo-type=tutor&demo-category=toolkit
feature_url: http://localhost:8080/PLUS/TutorReview
checks:
  - claim: "Claim 4 — feedback text minimum"
    steps: "Click 'Not Helpful' button on the first insight card"
    expect: "Textarea appears with character count label showing '0/10 characters minimum'; Submit button is disabled"
  - claim: "Claim 5 — training accordion"
    steps: "Click 'Recommended Training' accordion header"
    expect: "Training cards expand and are visible"
```

Each check names the claim, the interaction steps (human-readable, Playwright agent will interpret), and the expected outcome. If an expected outcome is not met, that is a CONTRACT-BREAK for the named claim.

### Step 4 — Reconcile

After validation PASS, prepare the working tree for PR. This step runs in the prod repo, not the anima-lite repo.

**4a. Confirm you are on the feature branch.** Run `git branch --show-current` and verify the current branch is the feature branch created in Step 2 (named after the contract slug). If you are still on a long-lived branch (`dev`, `main`, etc.) with uncommitted port changes, stop. Create the feature branch now (`git checkout -b <slug>`), move the commits there (`git cherry-pick` if needed), and reset the long-lived branch to its pre-port state. The PR target is the integration branch (e.g. `dev`) — confirm it exists on the remote before running `gh pr create`.

**4b. Identify and separate unrelated changes.** Run `git diff HEAD` and inspect every modified file. Flag any change not traceable to a contract claim or its required substrate. Common sources:
- Dev-only config (`hbm2ddl.auto=none`, dummy secret files, local build properties)
- Compatibility fixes surfaced during local build (e.g. Java version enum syntax)
- Files accidentally modified during investigation

For each unrelated change: revert it from the working tree (`git checkout HEAD -- <file>`) and note it in the reconcile summary. If the change is a legitimate fix (not just dev scaffolding), note it for a separate PR.

**4b. Stage everything that belongs.** Explicitly `git add` all modified and new files that are part of the port. New files (e.g. `training_section.js`) must be staged manually — confirm they are tracked.

**4c. Verify the final diff.** Run `git diff --staged` and confirm:
- Every staged change maps to a contract claim or required substrate
- No dev-only changes are staged
- No unintended files are staged

**4d. Draft the PR description.** Write `.anima-lite/pr-<branch-slug>.md`:

```markdown
## Summary

Ports [feature name] from plus-uno prototype to prod.

Claim changes (confirmed by user):
- **[Claim 1 name]**: [one-line description]
- **[Claim 2 name]**: [one-line description]
...

Deferred:
- [item]: [reason]

## Files changed
[list key files and what each does — one line each]

## Test plan
- [ ] Load /PLUS/TutorReview as a tutor with AI insights data
- [ ] [per-claim check from playwright: block, one checkbox each]
- [ ] Confirm no regression on existing insight review flow

## Blips
[paste blip log summary — info blips only; CONTRACT-BREAKs would have blocked this PR]
```

**4e. Write the catch-up summary.** Write `.anima-lite/catchup-<branch-slug>.md` — a self-contained briefing document designed to be fed directly to a review agent (or a senior engineer doing an AI-assisted review). It must give the reviewer everything they need to understand not just what changed but why, without requiring access to the conversation or prior context.

Structure:

```markdown
# Catch-Up: <feature-name> port

## What this is
One paragraph: what feature was ported, from which proto source, to which prod target, and what it does for the user. Written for someone who hasn't seen the conversation.

## Repo context
- **Proto** (<repo name>): <telos — one sentence from spine-proto/telos.md>
- **Prod** (<repo name>): <telos — one sentence from spine-prod/telos.md>
- **Key translation constraint**: <the most important formal-cause difference between the repos — e.g. "React/Vite → Java servlet + JSP + jQuery; no client-side state management">
- **Framework versions relevant to this PR**: <any version-specific syntax choices a reviewer might flag as wrong — e.g. "Bootstrap 4: data-toggle/data-target (not data-bs-*); jQuery 3.x">
- **Diff base**: `git diff <base-commit>..HEAD` — the 5 commits on this branch against `<base-commit>` (v11.3.0.4 tag or equivalent)

## What changed and why

### Substrate (translate freely — no argument change)
For each substrate change: one line stating what was translated and what prod convention it follows.

### Claim changes (confirmed by user — argument is preserved)
For each claim, in implementation order:
**<Claim N — name>**
- Argument: <what the user experiences and why it matters — one sentence>
- Why it's a claim: <what would change about the argument if this were done differently>
- Invariant: <the non-negotiable observable behavior — include file:line for the key enforcement point>
- Old behavior: <one line on what the code did before this claim was ported — so the reviewer can confirm the delta without diffing>
- Implementation: <files changed with line numbers — specific enough that a reviewer can jump directly. For config files (XML, properties), include the element name or bean ID, not just the file path.>

## Deferred
<items not ported — one line each, reason only if non-obvious. Omit items that are simply out of scope with no ambiguity.>

## Blips
<review-suggested and CONTRACT-BREAK blips only. Info blips that are dev-diary residue (e.g. "we considered X but dropped it") are noise — omit them. Each blip must answer: what does the reviewer need to check, and why does it matter?>

## What to focus on in review
Based on blip severity and claim complexity, the highest-attention areas are:
- <area 1> (`file:line`): <why — what breaks silently if this is wrong>
- <area 2> (`file:line`): <why>
(Generate from blips and claim invariants. Every item must have a file:line anchor and a concrete failure mode, not just "check this area.")

## How to verify
<Dev server start command, login URL, feature URL. Then per-claim checks from the playwright: block — each check names the interaction and the exact expected outcome. Include what "not verifiable" means for stub-data checks so a reviewer knows it's expected, not skipped.>
```

**Quality bar for the catch-up doc:** A reviewer with zero prior context should be able to open this doc, jump to any invariant via the file:line anchor, confirm the old-vs-new delta, and run the verify steps — without asking a follow-up question. If writing any section requires knowledge that isn't in the doc itself, add it. Each `file:line` anchor in "What to focus on in review" must include a clause that names the concrete failure mode if the line is wrong — not just what's there, but what breaks if it isn't.

**4e(ii). Completeness critic pass.** After writing the catch-up doc, spawn a single completeness-critic subagent with clean context. The subagent receives **only the catch-up doc** — no contract, no spines, no blips. The isolation is the point: if the critic can't answer a reviewer question from the doc alone, a real reviewer can't either.

The critic's job: attempt to answer the questions a reviewer would ask from the doc alone. For each section where a question cannot be answered, return a specific gap:
- What question it couldn't answer
- Which section is missing the information
- What specific content would resolve it

Secondary task: scan the blips log for any `Contracting failure?: n/a` entries and check whether they describe something that a more rigorous ari-argue pass would have caught. If yes, note it — not as a blocking finding, but as a signal that the ari-argue step may have under-classified. This closes the feedback loop from execution back to argumentation.

If the critic finds no gaps, proceed directly to 4f — no patch needed.

If the critic finds gaps, the main agent patches the catch-up doc to close them. The main agent may optionally run one additional critic pass to confirm the patches landed — cap at one re-run, do not loop.

> **◎ OPTIONAL GATE — catch-up doc review**
> After the critic's patches are applied, offer the user a chance to review the catch-up doc before proceeding to 4f. "Catch-up doc written — review before PR creation? (skip to proceed)."

**4f. Present for approval.** Surface the PR description and the staged diff summary to the user. Do NOT run `gh pr create` without explicit user confirmation — PRs are social objects.

> **⛔ REQUIRED GATE — PR creation**
> Surface the PR description and staged diff summary to the user before running `gh pr create`. Do not create the PR without explicit user confirmation.
> The pipeline halts here. Do not proceed until explicitly cleared. Once approved, the user or agent runs `gh pr create --body "$(cat .anima-lite/pr-<branch-slug>.md)"`.

The reconcile step is complete when: working tree is clean of unrelated changes, all port files are staged, and the PR description is written and surfaced.

### Step 5 — Harvest the feature ledger

After reconcile is complete, harvest the durable feature-area knowledge this port produced. This is not a new probe — it distills from artifacts already written (blips, catch-up doc, contract). The target is `.anima-lite/features/<feature-slug>.md`. If it exists (an ari-map stub), enrich it to `stub:3`. If it does not exist, create it at `stub:3` directly using the template in ari-map's Feature Ledger section.

**What goes in the ledger vs. what stays out:**
- **In**: observations that pass a weaker test than the spine — useful to any agent in this subsystem, even one working on a different feature. Seam-specific protocols. Known quirks with traceable sources. State machines. Feature gates.
- **Out**: anything tied to this feature's specific argument (that is the contract's job). Anything true repo-wide (that is the spine's job). If an observation would pass the spine's different-feature test, it belongs there via an ari-map refresh, not here.

Every `Known quirks` entry must name the blip or catch-up section it was distilled from — so a future agent can assess staleness against the source.

If nothing qualifies for the ledger, write no file and note that in the session summary. An empty ledger entry is worse than none: it reads as "this feature has no durable knowledge" when the truth is "nothing qualified for harvest."

Commit the ledger file alongside the spine — it persists across sessions.

## Output

Write `.anima-lite/plans/<branch-slug>.md` before execution (Step 1 output).

Append to `.anima-lite/blips/<branch-slug>.md` (same slug as the contract) throughout the session:

```markdown
## Blip: <short title>
Severity: <info|review-suggested|CONTRACT-BREAK>
Location: <file:line — one clause naming what's at that location and why it's load-bearing for the reviewer>
What happened: <the decision>
Why: <reasoning — cite the spine section this rests on (e.g. "spine-prod/formal.md §3 — the actual pattern diverges from what the spine describes") or state explicitly "no spine section applies; reasoning is by telos inference.">
Downstream consequence: <what this means going forward>
Contracting failure?: <what should have been in the contract to cover this — or "n/a" if genuinely unforeseeable>
```

**Every blip's `Why:` field cites the spine section it rests on.** Bare reasoning ("this seemed right," "kept the existing behavior") is not acceptable, the same discipline ari-argue applies to substrate/claim classifications. If no spine section applies, the blip must say so explicitly rather than omitting the question — a blip that skips the citation is as unverifiable as a bare classification.

A blip is logged whenever: a substrate change has a non-obvious downstream consequence; something uncovered by the contract came up and got a conservative default; a prod-repo convention conflicts with the prototype's approach and one was chosen; or anything a user skimming the PR would likely miss but want to know.

At session end (after reconcile complete):
1. Summarize blips.md conversationally, grouped by severity, leading with `review-suggested` or above.
2. State explicitly which contract items (claim changes) were exercised and validated.
3. Surface the PR description, catch-up summary, and staged diff for user approval.
4. Leave the spine directories, contract, plan, blips, PR draft, and catch-up summary in place — don't delete `.anima-lite/`.
5. If Step 5 produced a ledger file, state its slug and stub level. If it did not, state that no durable feature knowledge qualified for harvest.

## Escalation / Notes

One agent session, one feature. A second feature on the same branch needs its own ari-argue pass and its own contract file, even if the spine is reused.

This skill does not implement locking for two sessions running against the identical branch-slug simultaneously — that's out of scope for a prototyping-stage tool. If that happens, the right answer is "don't," not new infrastructure.
