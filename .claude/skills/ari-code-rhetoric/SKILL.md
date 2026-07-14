---
name: ari-code-rhetoric
description: Performs the code translation from prototype to prod repo, using spine.md and the current branch's contract as binding context. Called by ari-lite only after ari-map and ari-argue-rhetoric have produced current, hash-matched, branch-scoped artifacts. Logs every meaningful translation decision as a blip and halts back to ari-argue-rhetoric if the contract proves unsatisfiable against the real code, rather than guessing.
---

# ari-code-rhetoric

Four steps: plan → execute → validate → reconcile. The hard epistemic work happened upstream in ari-argue-rhetoric. If execution feels ambiguous, that's a sign the contract was incomplete, not a cue to use judgment alone.

## Inputs

- `.anima-lite/spine-proto/telos.md` — commit hash for precondition check. (Harness-change: this repo's own `spine-<label>/telos.md` — no separate proto spine exists.)
- `.anima-lite/spine-prod/formal.md` — primary reference for substrate translation. This is the guide for idiom and structure: new code must follow the prod repo's architectural patterns, not copy the proto's. (Harness-change: this repo's own `formal.md` — there is no substrate to translate between repos, only this repo's own dominant patterns to follow.)
- `.anima-lite/spine-prod/telos.md` — for the don't-contradict rules; substrate translations must not violate them. (Harness-change: same file as the proto-spine row above — single spine, read once.)
- Pull `material.md` or `efficient.md` from either spine directory if a specific translation decision requires it.
- `.anima-lite/work/<branch-slug>/contract.md` for the current branch and feature.
- The prototype code being translated. (Harness-change: the harness files themselves, changed in place — no separate prototype.)
- `.claude/skills/ari-code-rhetoric/metrics-spec.md` — canonical spec for the run row written at Step 5.5.

## Preconditions

1. The spine(s) relevant to this work item's comparison exist and `telos.md` in each is current — two spines for a port, one for single-repo debt work or harness-change (the repo's own spine — no `spine-proto`/`spine-prod` split), zero additional spines for a pure world-drift check. Port and harness-change are the only work-types fully specified today (harness-change per the posture note below, PIN-41). Single-repo debt work (beyond a harness self-change) and pure world-drift checks are ratified direction, not yet built — this skill does not yet run them end to end. If a required spine is stale or missing: halt, request ari-map for the affected repo.
2. `work/<branch-slug>/contract.md` exists for the current branch and feature, status is not "DRAFT," and has no unconfirmed items in Open Questions. If any fail: halt, request ari-argue-rhetoric.
3. The contract's `Spine commit:` hash matches `spine-proto/telos.md`'s current `Commit:`. If mismatched — another branch refreshed the spine since this contract was confirmed — don't auto-fail or proceed silently. Summarize what changed and ask the user whether the contract still holds or needs a quick re-pass through ari-argue-rhetoric.

Do not proceed on partial or mismatched context. This is the failure mode the whole pipeline exists to prevent: code moved without its meaning, or moved against terrain that already shifted underneath it.

## Active orientations

**Ari face (self-policing).** Every blip carries a `Contracting failure?` field. This is not optional metadata — it is the self-policing obligation: each uncovered case is an occasion to ask whether the contract was incomplete, not just what to do now. A blip that skips this question exempts the contracting phase from the quality sweep.

**Conservative default.** When the contract does not cover a decision, preserve current behavior and log a blip. Do not guess which bucket an uncovered case belongs in. Do not resolve ambiguity by choosing the option that makes the port simpler or faster. The conservative default is a mechanism: it makes gaps visible rather than hiding them behind a plausible-looking implementation. A blip saying "preserved by default, contract gap" is a correct artifact; a silently-resolved gap is a failure mode.

**Bidirectional audit.** The execution and validation agents read the contract, plan, spines, and ledger as binding context — and are the first readers who check those artifacts against the full prod codebase rather than against each other. Drift found in any direction (spine vs. code, contract vs. proto source, ledger vs. the current chain) is blip material, with the direction named in the `Why:` field, citing the spine § or artifact section that drifted (consistent with the mandatory-citation rule below). The CONTRACT-BREAK and contract-clarity mechanisms already below are instances of this orientation pointed specifically at the contract; this extends the same attention to every artifact these agents read, not only the contract.

## Harness-change posture (PIN-41)

A harness self-change (a skill file, `HARNESS.md`, `CLAUDE.md`, a spec support file) executes through this skill same as a port, minus the parts of the process that assume two different repos. What's degraded, and what isn't:

- **No spine-proto/spine-prod split.** Comparison is against this repo's own spine (`spine-<label>/`), same as debt-work's single-repo posture. Step 1's plan and Step 2's execution subagent read the contract and this repo's own `formal.md`/`telos.md` — there is no second spine to translate substrate against.
- **No playwright verification.** Step 3 D/E (browser pass, screenshot capture) does not apply — there is no running feature to navigate to. Skip both without noting `dev-server-not-reachable`; this is not a degraded-fallback case, it's out of scope for the work-type. Step 3 F (cross-leg coherence) likewise does not apply outside ripple.
- **No cross-repo PR flow.** Step 4's "prod repo" is this repo. Feature-branch-first and commit-per-claim discipline (Step 2) still apply exactly as written. Step 4d-4f's PR flow still applies if the harness's own convention calls for a PR against its integration branch; a harness-change small enough to land as a direct reviewed commit (no PR) is an acceptable deviation — name it plainly in the reconcile summary rather than silently skipping 4d-4f, so a reader can tell "no PR" was a decision, not an omission.
- **What is NOT degraded — the core loop stays intact.** Step 1 (plan before execute), Step 2's clean-context execution subagent working the contract as the filter for every decision (with blip logging on anything uncovered), and Step 3's independent validation agent running checks A (claim implementation) and B (blip classification quality) — all apply to a harness-change exactly as they apply to a port. A harness-change contract is not a shortcut around this loop; skipping it because "it's just a doc/skill file" is exactly the failure mode this posture note exists to close (PIN-41, surfaced when PIN-39's diagnosis-layer build skipped this loop entirely for lack of a written posture).

## Process

### Step 1 — Plan

Before touching any code, write an execution plan and surface it. The plan maps every contract item to specific files and specifies the order of operations. No code moves until the plan is written.

Write `.anima-lite/work/<branch-slug>/plan.md`:

```markdown
# Execution Plan: <feature-name>
Contract: .anima-lite/work/<branch-slug>/contract.md
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

Surface the plan before executing. If a blocker is found in planning, halt here — re-run ari-argue-rhetoric rather than proceeding with partial information.

> **⛔ REQUIRED GATE — GATE-BLOCKERS (plan blockers)**
> If `## Blockers` in the plan is non-empty, surface each blocker to the user. Do not spawn the execution subagent until all blockers are explicitly cleared.
> The pipeline halts here. Do not proceed until explicitly cleared.

> **◎ OPTIONAL GATE — GATE-PLAN-REVIEW (plan review)**
> After blockers are cleared (or if none exist), offer plan review. "Plan written — review before execution? (skip to proceed)."

### Step 2 — Execute

**Ripple: per-leg execution, parallel by default.** For a ripple work item, this step runs once per target leg named in the shared contract's apex — each leg gets its own execution subagent, its own feature branch (in its own repo), and its own commit history, all reading the same frozen contract. Legs execute **in parallel by default** (`reorient/ripple.md` ruling 5): the shared contract is what guarantees cross-leg coherence, so there is no correctness reason to stage one leg ahead of another, and no leg is privileged as "first." Sequential ordering (running one leg to completion before starting the next — e.g. proto-first) is available only as an explicit, judgment-based deviation when the operator has a specific reason to want it, never as the standing default; if you deviate, name the reason in the plan or a blip so a reader doesn't mistake the deviation for a forgotten default. Each leg logs its own blips to its own `.anima-lite/work/<branch-slug>/blips-<leg-label>.md` (or the leg's own repo-local blips file, if the leg's repo maintains one) — never one shared `blips.md` across legs, since a shared file would attribute one leg's decisions to another's commit history and defeat the per-claim traceability commit discipline exists to protect.

**Feature branch first.** Before touching any code, check the current branch in the prod repo. If you are on a long-lived branch (`main`, `master`, `dev`, `develop`, `staging`, or any branch that appears to be an integration target), create and switch to a feature branch named after the contract slug:

```
git checkout -b <branch-slug>
```

If a branch with that name already exists, check it out and verify it's at the same base as the current integration branch (no stale commits). If the branch is ahead of the integration target in unexpected ways, halt and ask the user.

Do not make any commits on a long-lived branch. All port commits must land on the feature branch. The commit discipline below is meaningless if the commits end up on `dev` — there is no clean PR surface to review against.

**Execution subagent.** Spawn a single execution subagent with clean context. The clean-context isolation is the point: an agent that cannot fall back on upstream argumentation to fill gaps must blip anything the contract doesn't cover. This enforces contract-as-filter discipline — gaps that a context-carrying agent would silently paper over become visible blips.

The execution subagent receives:
- The contract (`.anima-lite/work/<branch-slug>/contract.md`)
- Spine telos file(s) for don't-contradict rules — both `spine-proto/telos.md` and `spine-prod/telos.md` for a port; this repo's own `spine-<label>/telos.md` only for a harness-change (no second spine exists to receive)
- The plan (`.anima-lite/work/<branch-slug>/plan.md`)
- The prototype source files being translated (harness-change: the harness files themselves, being changed in place — there is no separate prototype to translate from)
- The prod repo path and current branch name (harness-change: this repo's own path and current branch)

Reading these inputs against the real prod code is also an audit of them — see Bidirectional audit above; flag drift as a blip rather than silently working around it.

The subagent's job: implement the plan, follow commit discipline below, write blips to `.anima-lite/work/<branch-slug>/blips.md`. Work through the plan using the contract as the filter for every decision:

- **Substrate changes** — translate freely, using the prod spine's `formal.md` as the guide for idiom and structure. Every substrate translation decision must cite the spine section that grounds it (e.g. "Translating jQuery collapse to Bootstrap 4.1.3 data-toggle/data-target per spine-prod/material.md §2 (Bootstrap 4.1.3 confirmed)"). If no spine section covers the decision, say so explicitly in the blip or log line. This is the same discipline the blip format's `Why:` field enforces below — one citation rule, not two: every reasoning trail in this skill either names the spine section it rests on or says explicitly that none applies.
- **Claim changes** — implement exactly per the contract's confirmed decision, in that claim's own commit — never inside the substrate commit. See commit discipline below: substrate files touched by a future claim get a stub, not the claim's real behavior. Do not relitigate mid-execution.
- **Anything not covered by the contract** — log as a blip immediately, make the conservative choice (preserve current behavior).
- **Contract-clarity watch** — while implementing, flag anything in the contract that looks under-specified or potentially wrong in light of what the prototype source actually does. This is softer than CONTRACT-BREAK (which fires only when the contract is actively contradicted). Log these as `Severity: info`, `Type: contract-clarity` blips. They don't halt execution but give the main agent and reviewer a signal that the contract may need sharpening for future ports of similar features.
- **Reverse-index check (PIN-40)** — each time this step touches a path (any file written, edited, or stubbed), check that path against the `lives-in:` targets recorded across every spine ingested in this repo's `.anima-lite/` (not just the spine(s) this work item's own contract compares against — a path can implicate a rule recorded in an unrelated spine). This is not a separate pass or script: it folds into the same per-file work already happening in this step, one grep-shaped check per touched file, against the `lives-in:`/`relates-to:` vocabulary `ari-map/SKILL.md`'s Output section owns (HARNESS.md §2). If the touched path matches a `lives-in:` target, log it inline in that step's blip as `Severity: info` with a new field `Spine promise touched:` naming the matched rule/finding and its home spine section (e.g. `Spine promise touched: spine-anima-lite/formal.md §5 — "every blip's Why: field cites the spine section it rests on"`). This is informational, not a halt condition — it makes staleness candidates visible at the moment they're created, per PHILOSOPHY.md's spine self-correction procedure §3, rather than deferred to a future full `/ari-map` re-run.

If the contract is actively wrong — not incomplete, but contradicted by what the prototype code does — **halt**. Write the contradiction to blips as `CONTRACT-BREAK` and report execution paused pending a re-run of ari-argue-rhetoric.

**Halt means halt — do not self-resolve.** On a CONTRACT-BREAK, stop and return the delta to the driver. Do not narrow the claim, drop it, or otherwise work around the contradiction to keep executing — that is the driver's call to make with the user, not yours. Logging the break loudly is necessary but not a substitute for halting; a loudly-logged CONTRACT-BREAK that the subagent then resolved on its own is still a bypassed gate.

This is a different situation from the conservative default above, and the two must not be conflated: the conservative default governs cases the contract did not *cover* (silence — preserve current behavior, log a blip, keep going). CONTRACT-BREAK is reality *contradicting* a claim the contract already confirmed. Narrowing a confirmed claim to route around contradicted-by-reality data is itself a CONTRACT-BREAK — not a conservative narrowing — because it silently substitutes the subagent's judgment for the user's on a claim that was already settled.

The subagent returns a handoff to the main agent:
- List of commits made (hash + claim mapping)
- Summary of blips logged
- `contract_break: true/false` — if true, execution is paused

Main agent on `contract_break: true`: surface the CONTRACT-BREAK blip to the user and request an ari-argue-rhetoric re-run before proceeding. Do not advance to Step 3.

**Partial commit preservation.** Do not revert commits already made before the CONTRACT-BREAK was discovered. The commits represent completed work that the contract did cover — reverting them loses that work without benefit. Leave the branch as-is. When re-running ari-argue-rhetoric, provide the list of commits already made (from the execution subagent's handoff) so ari-argue-rhetoric can write a contract amendment rather than a full re-contract. The amendment covers only the uncovered case; previously confirmed and implemented claims are settled.

**Ripple: two-tier CONTRACT-BREAK reopen (`reorient/ripple.md` ruling 4).** For a ripple work item, a CONTRACT-BREAK discovered in any one leg does not stay scoped to that leg — but it also does not automatically trigger rework everywhere. Two tiers, not one:

1. **Consideration reopens for every other leg, always.** The moment a leg reports `contract_break: true`, ari-argue-rhetoric consideration reopens for every *other* leg named in the contract apex, not just the leg that broke. This is a judgment call, argued explicitly: does the amendment the break requires touch claims this other leg has already honored? The judgment itself — yes or no, and why — is the record, whether or not it leads to rework.
2. **Execution (this skill) only reopens where that judgment concludes the leg's telos is better honored by the amendment.** If ari-argue-rhetoric's per-leg judgment says a leg's already-implemented claims stand unaffected by the amendment, that leg's execution is **not** re-run — the judgment is logged as closed, not silently skipped, and the leg's existing commits stand. Only a leg whose judgment concludes the amendment changes what that leg must honor gets its execution subagent re-spawned against the amended contract.

This replaces both blind full-rework (re-running every leg on any break) and shallow auto-recheck (assuming a break in one leg is scoped to that leg alone) — neither extreme is acceptable, and the judgment call itself is what the harness's discipline requires being on record. Do not let a leg's execution proceed unexamined just because it "probably isn't affected" — the consideration pass in tier 1 is mandatory for every leg, every time, even when the eventual answer is "no rework needed."

> **⛔ REQUIRED GATE — GATE-BREAK (CONTRACT-BREAK)**
> If the execution subagent returns `contract_break: true`, surface the CONTRACT-BREAK blip to the user and halt. Re-run ari-argue-rhetoric with the new information before proceeding to Step 3. For a ripple work item, this includes ari-argue-rhetoric's mandatory per-other-leg consideration pass (tier 1 above) before any leg's execution resumes.
> The pipeline halts here. Do not proceed until explicitly cleared.

**Commit discipline** — commit after each claim is fully implemented, before moving to the next. Do not accumulate all changes into a single working-tree blob. The commit message format:

```
port(<feature>): <claim name> — <one-line summary>

Contract: .anima-lite/work/<branch-slug>/contract.md
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
- The frozen contract (`.anima-lite/work/<branch-slug>/contract.md`)
- The blips log (`.anima-lite/work/<branch-slug>/blips.md`)
- The list of files changed and their content

Reading the contract and blips against the changed files is also an audit of those artifacts — see Bidirectional audit above; a contract or blip that doesn't hold up against the real diff is a finding, not just a validation input.

The validation agent checks three things independently, reading changed files directly — not relying on the execution agent's summary:

**A. Claim implementation** — for each confirmed claim change in the contract: is it implemented correctly? Absent or partial = FAIL.

**B. Blip classification quality** — for each blip with `Contracting failure?: n/a`: does the blip describe something that was actually a claim-level decision (something that should have gone to ari-argue-rhetoric)? If yes, that `n/a` is a misclassification = FAIL. This is the self-audit check the execution agent ran on itself — the validator audits the auditor.

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

> **⛔ REQUIRED GATE — GATE-BLIPS (review-suggested blips)**
> If the validation agent returns PASS (pending review), surface each review-suggested blip to the user. The user must acknowledge each one before the pipeline proceeds to Step 4.
> The pipeline halts here. Do not proceed until explicitly cleared.
- **FAIL: <specific finding>** — a confirmed claim absent/partial/contradicted, or a blip misclassification caught

On FAIL: loop back to Step 2, fix the specific finding, re-validate. Do not declare completion before the validation agent returns PASS or PASS (pending review) with acknowledged items.

**D. Live browser validation (strongly recommended, optional)** — if the contract specifies a `playwright:` block (format: `.claude/skills/ari-argue-rhetoric/playwright-spec.md`), the validation agent runs a browser pass using Playwright MCP tools after the static checks pass. The browser pass is a second validation layer: it confirms claims are not only implemented in code but functional in a running browser.

If `playwright:` is present in the contract, the validation agent:
1. Navigates to `playwright.login_url` and performs the login sequence specified in `playwright.login_steps`
2. Navigates to `playwright.feature_url`
3. Takes a full-page screenshot
4. For each claim in `playwright.checks`, performs the specified interaction and verifies the expected outcome
5. Logs any failure as a `CONTRACT-BREAK` blip — a claim that passes static code review but fails live in the browser is a CONTRACT-BREAK

The Playwright pass does not replace the static check — both must pass. If the dev server is not running, skip D and note it as an info blip: `Severity: info — Playwright pass skipped: dev server not reachable at <url>`.

**F. Cross-leg coherence check (ripple).** For a ripple work item, once every leg's own A–E checks have run, a separate validation pass reads *across* legs against the single shared contract — this is an integration-testing posture, not a per-leg check repeated N times. The named threat is sibling divergence: N repos making almost-the-same promise, nastiest at birth because there is no reference implementation to diff against, only the contract (`reorient/ripple.md` ruling 3). The check:

1. For each claim in the contract's `## Claim changes` section, walk every leg's implementation of that claim (using each leg's per-target substrate-mapping subsection from the contract as the map of where to look) and confirm the *claim itself* — the invariant, not the code shape — is identical across legs. A user-facing promise that holds in leg A but not leg B is a cross-leg CONTRACT-BREAK, logged against whichever leg's implementation diverges from the claim as confirmed.
2. Substrate is explicitly **not** compared leg-to-leg — each leg's substrate is free to follow its own spine's idiom (a React state hook and a JSP conditional include can both honor the same claim correctly). Do not flag a substrate difference as a finding; flag only a claim-level difference.
3. Log the result as a blip regardless of outcome: `Severity: info` if coherent across all legs (a positive finding, not silence — same discipline as ari-argue-rhetoric's lighter-pass rule), `CONTRACT-BREAK` if any leg's rendering of a claim diverges from the others' in what it actually promises the user.

This check cannot run until every leg named in the contract apex has reached its own PASS or PASS (pending review) — a leg still mid-execution has nothing yet to compare.

**Screenshot capture (rides the same D/E browser pass).** While the browser session from D/E is live and `feature_url` is reachable, the validation agent also captures screenshots for human review — one per Playwright `check` and one per `## Proto visual reference` section, saved under `.anima-lite/work/<branch-slug>/screenshots/` with a prose manifest at `.anima-lite/work/<branch-slug>/screenshots.md`. Full capture procedure, save path, naming convention, and manifest format: see `.claude/skills/ari-argue-rhetoric/playwright-spec.md` — canonical, referenced rather than restated here.

This is reachability-gated with the same graceful fallback as D/E and the proto visual reference step: if `feature_url` is not reachable, do not attempt capture — write `screenshots: target-not-reachable — static review only` to `screenshots.md` and proceed. An unreachable target degrades validation to static review; it is never a validation FAIL, and it never blocks PASS or PASS (pending review).

**Surface screenshots in the human-review path.** When screenshots were captured, the end-of-session summary and `catchup.md`'s "How to verify" section must point the reviewer at `.anima-lite/work/<branch-slug>/screenshots/` and `screenshots.md` — so review has a visual, not just PASS/FAIL and prose blips. When capture was skipped (target unreachable), state that plainly in the same places ("screenshots: target-not-reachable — static review only") so the reviewer knows to expect a static-only review rather than assuming the step was forgotten.

Contract `playwright:` block format and the worked example: see `.claude/skills/ari-argue-rhetoric/playwright-spec.md` — the canonical spec, referenced rather than restated here.

### Step 4 — Reconcile

After validation PASS, prepare the working tree for PR. This step runs in the prod repo, not the anima-lite repo — **except for a harness-change, where the prod repo is the anima-lite repo** (posture note above, Claim 3): the rest of this step's mechanics (feature branch, unrelated-change separation, staged diff, PR or direct-commit deviation) apply against anima-lite's own working tree instead of an external one.

**4a. Confirm you are on the feature branch.** Run `git branch --show-current` and verify the current branch is the feature branch created in Step 2 (named after the contract slug). If you are still on a long-lived branch (`dev`, `main`, etc.) with uncommitted port changes, stop. Create the feature branch now (`git checkout -b <slug>`), move the commits there (`git cherry-pick` if needed), and reset the long-lived branch to its pre-port state. The PR target is the integration branch (e.g. `dev`) — confirm it exists on the remote before running `gh pr create`. **Harness-change exception:** if the direct-reviewed-commit deviation (posture note, Claim 3) applies, there is no PR target to confirm — name the deviation in the reconcile summary instead and skip straight to 4b.

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

**4d. Draft the PR description.** Write `.anima-lite/work/<branch-slug>/pr.md`:

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

**4e. Write the catch-up summary.** Write `.anima-lite/work/<branch-slug>/catchup.md` — a self-contained briefing document designed to be fed directly to a review agent (or a senior engineer doing an AI-assisted review). It must give the reviewer everything they need to understand not just what changed but why, without requiring access to the conversation or prior context.

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

Secondary task: scan the blips log for any `Contracting failure?: n/a` entries and check whether they describe something that a more rigorous ari-argue-rhetoric pass would have caught. If yes, note it — not as a blocking finding, but as a signal that the ari-argue-rhetoric step may have under-classified. This closes the feedback loop from execution back to argumentation.

If the critic finds no gaps, proceed directly to 4f — no patch needed.

If the critic finds gaps, the main agent patches the catch-up doc to close them. The main agent may optionally run one additional critic pass to confirm the patches landed — cap at one re-run, do not loop.

> **◎ OPTIONAL GATE — GATE-CATCHUP-REVIEW (catch-up doc review)**
> After the critic's patches are applied, offer the user a chance to review the catch-up doc before proceeding to 4f. "Catch-up doc written — review before PR creation? (skip to proceed)."

**4f. Present for approval.** Surface the PR description and the staged diff summary to the user. Do NOT run `gh pr create` without explicit user confirmation — PRs are social objects.

> **⛔ REQUIRED GATE — GATE-PR (PR creation)**
> Surface the PR description and staged diff summary to the user before running `gh pr create`. Do not create the PR without explicit user confirmation.
> The pipeline halts here. Do not proceed until explicitly cleared. Once approved, the user or agent runs `gh pr create --body "$(cat .anima-lite/work/<branch-slug>/pr.md)"`.

The reconcile step is complete when: working tree is clean of unrelated changes, all port files are staged, and the PR description is written and surfaced.

### Step 5 — Harvest the feature ledger

After reconcile is complete, harvest the durable feature-area knowledge this port produced. This is not a new probe — it distills from artifacts already written (blips, catch-up doc, contract). The target is `.anima-lite/features/<feature-slug>.md`. If it exists (an ari-map stub), enrich it to `stub:3`. If it does not exist, create it at `stub:3` directly.

Format, stub levels, and the template to use: see `.claude/skills/ari-map/ledger-spec.md` — the canonical spec, referenced rather than restated here.

**What goes in the ledger vs. what stays out:**
- **In**: observations that pass a weaker test than the spine — useful to any agent in this subsystem, even one working on a different feature. Seam-specific protocols. Known quirks with traceable sources. State machines. Feature gates.
- **Out**: anything tied to this feature's specific argument (that is the contract's job). Anything true repo-wide (that is the spine's job). If an observation would pass the spine's different-feature test, it belongs there via an ari-map refresh, not here.

Every `Known quirks` entry must name the blip or catch-up section it was distilled from — so a future agent can assess staleness against the source.

If nothing qualifies for the ledger, write no file and note that in the session summary. An empty ledger entry is worse than none: it reads as "this feature has no durable knowledge" when the truth is "nothing qualified for harvest."

Commit the ledger file alongside the spine — it persists across sessions.

### Step 5.5 — Instrument

After the ledger harvest, the main agent writes the run row: `.anima-lite/metrics/run-<date>-<slug>.md`, per `.claude/skills/ari-code-rhetoric/metrics-spec.md` (canonical spec — this step points to it, not restated here).

Two operative instructions:

1. **Track usage as the pipeline runs, not retroactively.** Throughout the pipeline (ari-map, ari-argue-rhetoric, and every ari-code-rhetoric subagent spawn — plan, execute, validate, critic), record each subagent's returned usage (tokens, duration) and the model tier it was spawned at. The run row's phase table is assembled from these running notes at Step 5.5, not reconstructed from memory after the fact. If a subagent's return didn't include usage data, its row gets `not traced` — never a guessed figure.
2. **Fill the gate table exhaustively from the registry.** Every gate ID in `HARNESS.md` Section 1 gets a row in the run row's gate table, whether or not it fired this run. No gate is omitted because it seemed irrelevant to this feature — an omitted row is indistinguishable from an unconsidered gate, which defeats the point of the table.

Also append the run row to `.anima-lite/metrics/summary.md`'s table per metrics-spec.md.

## Output

Write `.anima-lite/work/<branch-slug>/plan.md` before execution (Step 1 output).

Append to `.anima-lite/work/<branch-slug>/blips.md` (same slug as the contract) throughout the session:

```markdown
## Blip: <short title>
Severity: <info|review-suggested|CONTRACT-BREAK>
Location: <file:line — one clause naming what's at that location and why it's load-bearing for the reviewer>
What happened: <the decision>
Why: <reasoning — cite the spine section this rests on (e.g. "spine-prod/formal.md §3 — the actual pattern diverges from what the spine describes") or state explicitly "no spine section applies; reasoning is by telos inference.">
Downstream consequence: <what this means going forward>
Contracting failure?: <what should have been in the contract to cover this — or "n/a" if genuinely unforeseeable>
Spine promise touched: <optional; PIN-40 reverse-index field — only present when this step's touched path matched a lives-in: target in any ingested spine. Names the matched rule/finding and its home spine section. Absent entirely (not "none") when no path touched this step matched anything — an absent field, not a written negative, keeps the common case (no match) from adding noise to every blip.>
```

**Every blip's `Why:` field cites the spine section it rests on.** Bare reasoning ("this seemed right," "kept the existing behavior") is not acceptable, the same discipline ari-argue-rhetoric applies to substrate/claim classifications. If no spine section applies, the blip must say so explicitly rather than omitting the question — a blip that skips the citation is as unverifiable as a bare classification.

A blip is logged whenever: a substrate change has a non-obvious downstream consequence; something uncovered by the contract came up and got a conservative default; a prod-repo convention conflicts with the prototype's approach and one was chosen; or anything a user skimming the PR would likely miss but want to know.

At session end (after reconcile complete):
1. Summarize blips.md conversationally, grouped by severity, leading with `review-suggested` or above.
2. State explicitly which contract items (claim changes) were exercised and validated.
3. Surface the PR description, catch-up summary, and staged diff for user approval.
4. Leave the spine directories, contract, plan, blips, PR draft, and catch-up summary in place — don't delete `.anima-lite/`.
5. If Step 5 produced a ledger file, state its slug and stub level. If it did not, state that no durable feature knowledge qualified for harvest.
6. State that the run row was written (path: `.anima-lite/metrics/run-<date>-<slug>.md`) per Step 5.5.

## Escalation / Notes

**Driver's independent break-scan is not optional.** Before trusting the execution subagent's handoff, the main agent independently scans the committed diff itself for un-surfaced CONTRACT-BREAKs — do not proceed on the subagent's summary that it "handled" everything. GATE-BREAK is a judgment gate (HARNESS.md §3) and cannot be mechanized: no hook can decide whether reality contradicts a claim, so the main-agent review layer is the only reliable enforcement. A self-policing executor is not sufficient on its own.

One agent session, one feature. A second feature on the same branch needs its own ari-argue-rhetoric pass and its own contract file, even if the spine is reused.

This skill does not implement locking for two sessions running against the identical branch-slug simultaneously — that's out of scope for a prototyping-stage tool. If that happens, the right answer is "don't," not new infrastructure.
