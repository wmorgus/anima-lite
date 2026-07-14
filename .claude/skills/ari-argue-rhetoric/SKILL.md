---
name: ari-argue-rhetoric
description: Reads .anima-lite/work/<slug>/intent.md (from ari-intake), the spine.md, and a target feature — or, for ripple work items, the intent artifact directly — classifies every implementation detail as a substrate change (medium, free to translate) or a claim change (argument-altering, requires confirmation), and writes a branch-scoped contract. Called by ari-lite after ari-intake has produced an argued intent artifact and ari-map has produced a current spine, before ari-code-rhetoric touches any code. Never silently drops or alters what a feature argues for.
---

# ari-argue-rhetoric

**This skill runs as a subagent spawned by the main pipeline agent — not as the main agent itself.** By the time ari-argue-rhetoric runs, the main agent carries ari-map probe context (spine reasoning, cause analysis). The classification loop and user back-and-forth are isolated here so the main agent's context stays clean.

The spawning agent passes to this subagent: `work/<slug>/intent.md` from ari-intake, both spine directories (`spine-proto/` and `spine-prod/`, full contents), the proto feature source files being ported, and the current git branch name. On completion, this subagent returns a handoff summary to the main agent: contract path written, number of claim changes confirmed, and whether a telos conflict was found and how it was resolved.

Argumentation: determine what a feature is claiming to the user, separate from how it happens to be implemented, and get the human to confirm anything that would change if the claim itself moved.

## Inputs

- `.anima-lite/work/<slug>/intent.md` — the primary input, produced by `/ari-intake`. Carries the work item's telos statement, sources, and claims, each with an `argued-by:` provenance line.
- `.anima-lite/spine-proto/telos.md` and `.anima-lite/spine-prod/telos.md` — read for the conditional telos backstop (see step 1) and for substrate/claim classification context.
- `.anima-lite/spine-proto/formal.md` and `.anima-lite/spine-prod/formal.md` — read for substrate classification (what patterns the prod spine uses informs what's a free translation vs. a structural claim).
- Pull `material.md` or `efficient.md` from either spine directory if a specific detail requires it.
- The feature/diff/branch being ported — except for **ripple** work items, where there is no proto/prod feature diff to read at all. See "Intent-artifact input mode (ripple)" below.
- Current git branch name (for output naming).

## Intent-artifact input mode (ripple)

When `work/<slug>/intent.md` carries `Work-type: ripple`, this skill's primary input changes shape: the input is the intent artifact itself, directly — not a feature/diff/branch in any one repo. There is no source code to read the argument off of, because a ripple institutes a promise in N repos at once rather than translating one that already exists somewhere (`reorient/ripple.md` ruling 1). Consequences for process:

- Every claim classified here is born from one of `intent.md`'s `Claims` entries and its `argued-by:` provenance line — never inferred by reading a single leg's implementation, and never backfilled from whichever leg happens to be easiest to read. A ripple claim's source is the intent artifact, full stop; a leg's eventual code is downstream of the contract, not upstream of it.
- Step 1a (source-of-truth check, below) does not apply — there is no candidate-component ambiguity to resolve, because there is no existing implementation to disambiguate. Skip it and proceed from the intent artifact's claim list.
- Step 2 (identify the argument) is answered directly from `intent.md`'s Telos statement and Claims section rather than inferred from mechanics.
- Substrate/claim classification (step 3) still applies per target: what's substrate in one leg's spine may not translate identically to another's, but the *claims themselves* are one promise shared across every leg — see the per-target substrate-mapping template in Output, below.

## Preconditions

- `work/<slug>/intent.md` exists for this work item. If it does not, halt and request `/ari-intake` — argue does not construct an argued intent from scratch; it contracts from one.
- Every claim this skill contracts on carries an `argued-by:` line in `intent.md`. A claim without one is refused: send it back to intake rather than classifying or contracting it here. This is not a formatting nitpick — an unsourced claim is exactly the "invented behavior" intake exists to keep out of the pipeline.
- The spine(s) relevant to this work item's comparison exist and `telos.md` in each is current (Commit: hash matches HEAD) — two spines for a port, one for single-repo debt work or a harness-change (the repo's own spine), N target spines for a ripple (one per leg named in the contract apex — the comparison-count generalizes past the fixed two of a port; see `reorient/vocab.md` decision 3b), zero additional spines for a pure world-drift check (the comparison is against the world, not another spine). Port is the only work-type fully specified today: both `spine-proto/` and `spine-prod/` directories must exist. Single-repo debt work and pure world-drift checks are ratified direction, not yet built — this skill does not yet run them end to end. Harness-change is single-spine (this repo's own) and IS built, per PIN-36. If a required spine is missing or stale, halt and request ari-map for the affected repo.
- A specific feature/diff is identified to argue about — except for ripple work items, where the intent artifact itself (with a current spine per named target) stands in; see "Intent-artifact input mode" above.

## Active orientations

**Ari face.** Telos authority sits primarily upstream now, in `/ari-intake` — the feature's argument was already checked against the target telos before this skill ran. What's senior here is vigilance for contradiction surfacing mid-contract: if classification turns up a claim that doesn't square with `intent.md`'s telos statement, that's a routing question — scope creep or telos error — not a classification question. Route it via the conditional GATE-TELOS backstop before proceeding to step 3.

**Builder face.** Classification is argument-work. The substrate vs. claim distinction is determined by whether the user's understanding of what the feature promises would change — not "does this look different" but "does this promise different."

**Bidirectional audit.** Both spines are read here as classification authority — but reading them against the actual proto feature source is a live check of the spines themselves, not just an application of them. If the feature source contradicts a spine claim (a pattern the spine asserts that doesn't hold in the code being classified), that is not only a classification problem to route around — flag it explicitly, either as an Open Question in the contract or as a note back to the caller recommending an ari-map refresh, and state the direction: spine stale (code moved since the probe) or spine wrong at write time (the probe misread the code). Do not classify against a spine claim you have just watched fail; a classification built on a claim known to be false is worse than one built on no claim at all.

## Process

**1. Read both telos files.** GATE-TELOS already fired once, in `/ari-intake`, against `intent.md`'s telos statement — that is the primary check, done before any contracting existed to protect. This step is a backstop, not a repeat of that work: read both telos files for classification context, and only re-raise the gate if contracting itself surfaces a claim that contradicts `intent.md`'s recorded telos statement (a claim the intake pass didn't anticipate, or one whose real shape only becomes clear once classification is underway). Do not re-run the full telos check unconditionally — that is exactly the gate-fatigue failure mode intake's early placement exists to avoid. Note the proto telos's `Commit:` hash; the contract will pin to it.

> **⛔ REQUIRED GATE — GATE-TELOS (telos conflict, conditional backstop)**
> Fires only if contracting surfaces a claim that contradicts the telos statement recorded in `work/<slug>/intent.md`, OR contradicts the target repo's `RESOLUTION.md` (the apex layer checked in intake) — not unconditionally on every run. When it fires: present the conflict to the user, name whether it reads as a telos error (the spine's or intent's purpose is wrong) or scope creep (the claim is beyond what this repo is for) — or, for a resolution-layer conflict, name it drift or growth per `.claude/skills/ari-intake/SKILL.md`'s GATE-TELOS apex layer — and wait for explicit confirmation before continuing. Do not write the contract until the user has acknowledged the conflict.
> The pipeline halts here when triggered. Do not proceed until explicitly cleared.

**1a. Source-of-truth check.** Before identifying the argument, check whether the proto feature has multiple candidate components, variants, or demo wrappers that could each be "the feature" (e.g. two components that both partially implement overlapping behavior, or a demo page wrapping a component that also exists standalone). If more than one candidate exists: identify them, determine which is canonical — most complete, most recently evolved, or referenced by the demo entry point — and confirm the choice with the user before classification begins. Do not classify against an arbitrarily-picked candidate; a contract built on the wrong one silently misrepresents the feature. If only one candidate exists, note "single source" and proceed.

**2. Identify the argument.** What relationship or promise is this feature establishing with the user — not what it does mechanically. A confirmation dialog before a destructive action argues "you should not lose data by accident." A specific widget choice is usually just medium, unless the choice itself was load-bearing (a dropdown chosen specifically to hide a sensitive setting behind a click is making a claim, not just rendering one).

**3. Classify every implementation detail.**

*Substrate change* — free to translate, argument survives: widget library swap, renaming, file restructuring, styling system, colors, fonts, animation library. Wording is substrate only when the semantic register is unchanged — two phrasings of the same promise.

*Claim change* — requires explicit confirmation: removing a UI element the prototype had, dropping a confirmation step, relaxing validation, changing who gets notified, changing reversible vs. permanent. Three categories that consistently look like substrate but are not:

**Every classification cites the spine section it rests on.** Bare assertions ("this is substrate") are not acceptable. Format:
- "Substrate — prod formal.md §3 (Dominant patterns) establishes this as the standard transport mechanism."
- "Claim — no spine section covers this; classification is by telos inference."

If no spine section applies, say so explicitly. The contract must be verifiable: a reviewer should be able to check any classification against the cited spine fact rather than trusting the agent's memory.

**Skeptical read on every substrate classification.** The substrate call is the highest-risk classification — it's the one that lets work proceed without user confirmation. For every detail classified as substrate, verify it does not touch: state management, reversibility, validation, confirmations, who-sees-what, or data persistence. If it touches any of these, escalate to claim review even if the surface appearance is substrate. The cost of a missed claim is higher than the cost of a false-positive escalation. This skeptical read is free — the subagent is already reading the material, so adversarial attention costs nothing.

**Interaction model.** How the user physically moves through the feature — collapse/expand, auto-advance, one-at-a-time focus, toggle behavior, keyboard flow. A user who understood the feature's promise would notice if sequential discovery became everything-at-once. Classify interaction patterns as claims by default; only call them substrate if you can articulate why the specific pattern doesn't affect the promise.

When writing a contract for an interaction model claim, name the invariant the interaction enforces — not just the implementation sub-tasks. "One card expanded at a time" is an invariant; "auto-expand UNDER_REVIEW, toggle on click" are the sub-tasks. A contract that names only the sub-tasks passes to ari-code-rhetoric without stating what the sub-tasks exist to enforce. ari-code-rhetoric will implement the sub-tasks and miss the invariant. Name both.

**Semantic register of labels and attribution.** Wording is substrate when it's two phrasings of the same thing. Register shift is a claim: endorsement → disclaimer, celebration → warning, brand confidence → liability caveat. "Powered by PLUS AI Coach" and "generated by AI, which may make mistakes!" are not two phrasings of the same promise — they are different promises. Surface the shift, confirm it.

**Structural visual hierarchy.** Colors and fonts are substrate. Whether the primary metrics live in a prominent hero block versus a flat card grid is not — it reflects the feature's argument about what the user should feel is important. When the proto's layout visually weights one section differently from how prod would naturally render it, that weighting is a claim about significance. Confirm before flattening.

**Harness-change classification.** The argument (step 2) is what the harness promises — a gate's behavior, a skill's contract, a work-type's guarantees — not what a feature promises a UI user. *Substrate*: doc wording, file layout, internal variable/section naming that doesn't change what's promised. *Claim*: a skill or file rename that changes the invocation surface (`/ari-port` → `/ari-code-rhetoric` is a claim — it changes what the operator types and what every doc must reference correctly), a new or altered gate rule, a change to what a work-type is allowed to do or must check. No `Schema deps:`/playwright block applies — omit those sections rather than fabricating entries; GATE-SCHEMA and the visual-reference step are port-specific and do not fire for harness-change.

When ambiguous, don't guess — escalate to step 4.

**Arete posture.** For an arete work item, this skill's primary input is `/ari-arete-pan`'s ratified `cut.md`, not a proto/prod feature diff and not `intent.md`'s claim list — arete has no `/ari-intake` pass of its own; the cut *is* the argued source. Consequences for process:

- Every claim classified here is born from one `cut.md` nugget or ore entry — never inferred by reading the target repo directly. A nugget's claim is "keep this exactly as it stands" (still stated and confirmed, per `ari-arete-pan`'s own Escalation/Notes, even though no code changes); an ore claim's source is its pressure-note, and the claim to confirm is the *rewrite* the pressure-note motivates, not the ore's current form.
- Slag never reaches this skill — it was dropped at the pan stage and has no claim to classify.
- Step 1a (source-of-truth check) does not apply — `ari-arete-pan` already resolved which units exist and what they're worth; there's no candidate-component ambiguity left to disambiguate here.
- Step 2 (identify the argument) is answered from the arete statement itself (`.anima-lite/work/<arete-slug>/arete-statement.md`), not inferred from mechanics — the statement *is* what every claim in this pass is checked against.
- Substrate/claim classification (step 3) still runs per the target — the **new, empty repo** this claim will land in (ruling 8; see `ari-code-rhetoric`'s own arete posture) — but every nugget and every ore item is claim-shaped by definition: a nugget is "this promise is confirmed worth keeping," an ore item is "this promise is confirmed worth keeping in rewritten form." Neither is substrate; do not attempt a lighter pass here — the whole cut was already filtered by `ari-arete-pan`'s own judgment, and everything that survived that filter is exactly the kind of decision this skill's per-claim confirm exists to protect.
- No `Schema deps:`/playwright block applies — the new repo doesn't exist yet at classification time; omit those fields rather than fabricating entries, same as the harness-change classification rule above.
- **Cutover stays out of scope.** Nothing classified under this posture may include deploy config, DNS/service pointers, downstream-consumer migration, secrets, or CI — that exclusion is permanent for the whole arete work-type, not a per-claim judgment call to make here.

**4. Confirm every claim change with the user.** One at a time, never bundled. Frame concretely: state what the prototype does, what the prod pattern would do instead, and that this is an argument-level decision, not a style choice. If the user is unreachable synchronously, default to preserving the claim and mark it "preserved by default, pending confirmation" — never silently resolve ambiguity by guessing it away.

**Third path — route, don't violate.** If the subagent believes a claim in the prototype looks wrong — not just different in the prod context, but misguided as a design decision — that claim is neither preserved-by-default nor silently dropped. It is surfaced as an Open Question in the contract, with the reasoning stated plainly. The user resolves it before the contract is frozen. Silently satisfying a claim you believe is wrong is worse than either confirming or challenging it: the corpus calls this "route, don't violate" — principled challenge goes through the cycle, not around it. The Open Questions section exists as the halt surface for exactly this case.

**Calibration note — lighter pass.** The full classification pass is the default. A lighter pass is available only when all of the following hold:
1. Both spines are current and have been fully read.
2. The proto feature source has been fully read and no candidate claim changes are visible in any of: state management, reversibility, validation, confirmations, who-sees-what, data persistence.
3. The feature type is well-understood — pure styling, naming, or file restructure with no behavioral change.

This is a signal-clarity condition, not an efficiency shortcut. A full pass on 40 obvious substrate changes before reaching 0 claims generates noise that dulls attention to actual claims. The lighter pass exists to protect focus, not to save time.

Even on a lighter pass, the subagent must produce a positive claim: not "no claims found" but "I looked for claim candidates in [state management, reversibility, validation, confirmations, who-sees-what, data persistence] and found none." The absence of claims is a documented finding, not a silence. This is epistemic hygiene: the skeptical attention is on record even when it finds nothing.

If any of the three conditions is not met, run the full pass.

**4c. Schema-dependency check (pre-freeze).** For every claim's declared `Schema deps:`, verify each named entity/field/enum actually exists in prod before the contract is written. Check the prod spine's entity/field inventory first, if present (`spine-prod/material.md`, per PIN-21's spine-completeness work) — a current, complete spine often settles this by inspection alone. When the spine doesn't cover the dependency, or is silent rather than confirming absence, grep the prod repo directly (path from this project's `CLAUDE.md`, Target repos table) under its schema-bearing directories — `item/`, `dto/`, `enums/` — for the named entity/field/enum. A declared dependency that resolves to zero prod classes or fields is a contract-time break, not a wording detail to smooth over: HALT, surface it to the user for resolution — drop the claim, amend it, or confirm the field exists under a different name — before freezing the contract. This is a backstop, not the primary defense: the spine's entity/field inventory and negative-space list are meant to catch this by the time ari-argue-rhetoric reads them; this check exists for when the spine is still incomplete — a fresh probe, an unusual noun, or drift since the last map. Declaring a `Schema deps:` value is not the same as confirming it resolves — do not skip this step by trusting the claim author's own list.

**Ripple: run this check against every leg, not just prod.** For a ripple work item, "prod" above generalizes to every target repo named in the ripple's contract apex — the check is not satisfied by resolving a `Schema deps:` entry against one leg's spine while the others go unchecked. Since one claim renders differently per leg's substrate (see the per-target substrate-mapping template in Output, below), each leg's own schema-bearing directories must independently confirm the entity/field/enum that leg's rendering of the claim relies on. A dependency that resolves in leg A but not leg B is exactly the sibling-divergence risk `reorient/ripple.md` ruling 3 names — surface it as a per-leg GATE-SCHEMA finding, not a single pass/fail for the whole ripple.

> **⛔ REQUIRED GATE — GATE-SCHEMA (schema dependency)**
> If a claim's declared `Schema deps:` entry resolves to zero classes or fields **in any target repo this claim applies to** — prod for a port, every leg named in the contract apex for a ripple — halt and surface it to the user for resolution — drop the claim, amend it, or confirm the field exists under another name in the affected repo(s). Do not freeze the contract until the user resolves it for every checked target.
> The pipeline halts here. Do not proceed until explicitly cleared.

## Proto visual reference (if server reachable)

Before writing the contract, attempt to capture visual ground truth from the running prototype. This step runs after all claim changes are confirmed but before the contract is written — the screenshots inform the `expect` clauses in the playwright verification block.

1. **Find the dev server URL.** Check `vite.config.js` (or equivalent) in the proto repo for the dev server port. If unclear, ask the user for the URL before attempting to reach it.

2. **Attempt connection.** Try to navigate to the feature in the proto. If the server is not reachable, note `playwright: proto-server-not-reached` in the contract and fall back to source-only reading — do not block the pipeline.

3. **If reachable: take screenshots per section.** Navigate to the feature. For each major section (header, each content block, any gated or locked UI state), take a screenshot and describe what renders in prose — element count, text content, button labels, badge text, image presence. These are prose descriptions, not binary data; the contract remains a markdown file.

4. **Add a `## Proto visual reference` block to the contract** listing each section and what it renders. Example:
   - "Training cards: 4 cards, each shows title, category badge, duration, Start button with image"
   - "Locked gate state: section renders with lock icon and 'Complete your review to unlock' label"

5. **Use these descriptions to write specific `expect` clauses** in the playwright verification block (see Output below). An expect clause derived from a screenshot must name the specific elements observed, not just "the section is visible."

## Output

Write `.anima-lite/work/<branch-slug>/contract.md`, where `<branch-slug>` is the current git branch (sanitized: lowercase, slashes to dashes) or a feature-name slug if not in git:

```markdown
# Contract: <feature-name>
Branch: <branch-slug>
Generated: <date>
Spine commit: <the Commit: hash from spine-proto/telos.md at time of writing>
Source of truth: <component/file confirmed canonical in step 1a — required whenever multiple candidates existed; "n/a — single source" otherwise; "n/a — ripple, no prior implementation" for ripple work items>
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
<one or two sentences: what is this work item claiming to the user>

## Substrate changes (free to translate)
- <detail> — <why this is medium, not claim>

## Claim changes (confirmed with user)
- <detail> — Decision: <preserve|change-to-X> — Confirmed: <yes/default-preserve, with date>
  Schema deps: <prod entities/fields/enums this claim's rule logic relies on, e.g. "SessionItem.sessionStart, StudentSessionItem, InstitutionItem" — or "none" if the claim relies on no prod schema (pure UI/interaction)>

For a **ripple** work item, this section stays single — one promise, N renderings, never N separate claim lists — but each claim gains a per-target substrate-mapping subsection immediately under it, naming how the one claim renders against each target's own substrate:

- <claim name> — Decision: <change-to-X> — Confirmed: <yes, with date>
  Schema deps: <as above, or "none">
  **Per-target substrate mapping:**
  - <target-a label>: <how this claim's invariant renders in target-a's idiom — e.g. "React state hook toggling a `locked` boolean, per spine-target-a/formal.md §3">
  - <target-b label>: <how the same claim's invariant renders in target-b's idiom — e.g. "Java servlet session attribute + JSP conditional include, per spine-target-b/formal.md §3">
  - <target-n label>: <...>

  The claim (what's promised) is identical across every row; the mapping is where substrate is free to differ per leg's own spine (`reorient/ripple.md` ruling 3 — cross-leg coherence is a claims-identical, substrate-free-per-leg check, not a uniform-implementation check).

## Open questions
<anything not yet confirmed; ari-code-rhetoric must halt and escalate if it hits these>

## Proto visual reference
<one line per major section describing what the proto renders — derived from screenshots if server was reachable, from source reading if not>
playwright: proto-server-not-reached  ← include only when server was unreachable

## Playwright verification
login_url: <proto or prod login URL>
feature_url: <URL for this feature in the target environment>
checks:
  - claim: "<Claim N — name>"
    steps: "<human-readable interaction steps>"
    expect: "<specific content elements that must be present — title, badge, button label, count, etc.>"
```

Block schema, the `expect`-field rules, and a worked example: see `playwright-spec.md` in this skill's directory — the canonical spec, referenced rather than restated here.

**`Schema deps:` is what GATE-SCHEMA verifies before freeze (step 4c).** Every claim entry names the prod entities/fields/enums its rule logic depends on — not a guess about implementation, a declared assumption about what data prod actually has. A claim built on a field that doesn't exist is a break the pipeline must catch at contract-time, not at execution-time: two run4 breaks (a `subject` field and an "open-slots" concept) were both invented by the prototype's mock UI, backed nothing in prod, and rode unverified into a frozen contract — detonating late, once at plan-time and once mid-execution as a CONTRACT-BREAK. Declaring the dependency here makes it checkable before that happens.

## Escalation / Notes

Branch-scoping exists because multiple branches can be mid-port off the same prototype at once — each gets its own contract even though they share the spine. Don't write to a singleton `contract.md`.

Once written with no open Open Questions, the contract is frozen for the session and ready for ari-code-rhetoric. If ari-code-rhetoric later finds the contract contradicted by the real code (not just incomplete), it will halt and hand the specific delta back to this skill — treat that as new evidence, not as a do-over of step 3 from scratch.
