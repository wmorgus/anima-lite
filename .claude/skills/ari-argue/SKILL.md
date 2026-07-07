---
name: ari-argue
description: Reads .anima-lite/spine.md and a target feature, classifies every implementation detail as a substrate change (medium, free to translate) or a claim change (argument-altering, requires confirmation), and writes a branch-scoped contract. Called by ari-lite after ari-map has produced a current spine and before ari-port touches any code. Never silently drops or alters what a feature argues for.
---

# ari-argue

**This skill runs as a subagent spawned by the main pipeline agent — not as the main agent itself.** By the time ari-argue runs, the main agent carries ari-map probe context (spine reasoning, cause analysis). The classification loop and user back-and-forth are isolated here so the main agent's context stays clean.

The spawning agent passes to this subagent: both spine directories (`spine-proto/` and `spine-prod/`, full contents), the proto feature source files being ported, and the current git branch name. On completion, this subagent returns a handoff summary to the main agent: contract path written, number of claim changes confirmed, and whether a telos conflict was found and how it was resolved.

Argumentation: determine what a feature is claiming to the user, separate from how it happens to be implemented, and get the human to confirm anything that would change if the claim itself moved.

## Inputs

- `.anima-lite/spine-proto/telos.md` and `.anima-lite/spine-prod/telos.md` — read first; telos check happens here.
- `.anima-lite/spine-proto/formal.md` and `.anima-lite/spine-prod/formal.md` — read for substrate classification (what patterns the prod spine uses informs what's a free translation vs. a structural claim).
- Pull `material.md` or `efficient.md` from either spine directory if a specific detail requires it.
- The feature/diff/branch being ported.
- Current git branch name (for output naming).

## Preconditions

- The spine(s) relevant to this work item's comparison exist and `telos.md` in each is current (Commit: hash matches HEAD) — two spines for a port, one for single-repo debt work (the repo's own spine), zero additional spines for a pure world-drift check (the comparison is against the world, not another spine). Port is the only work-type fully specified today: both `spine-proto/` and `spine-prod/` directories must exist. Single-repo debt work and pure world-drift checks are ratified direction, not yet built — this skill does not yet run them end to end. If a required spine is missing or stale, halt and request ari-map for the affected repo.
- A specific feature/diff is identified to argue about. This skill operates on one feature per invocation.

## Active orientations

**Ari face.** Telos authority is senior here. Check the feature's argument against the prod spine's final cause before classifying anything. A feature that contradicts the prod telos is a routing question — scope creep or telos error — not a classification question. Route it before proceeding to step 3.

**Builder face.** Classification is argument-work. The substrate vs. claim distinction is determined by whether the user's understanding of what the feature promises would change — not "does this look different" but "does this promise different."

**Bidirectional audit.** Both spines are read here as classification authority — but reading them against the actual proto feature source is a live check of the spines themselves, not just an application of them. If the feature source contradicts a spine claim (a pattern the spine asserts that doesn't hold in the code being classified), that is not only a classification problem to route around — flag it explicitly, either as an Open Question in the contract or as a note back to the caller recommending an ari-map refresh, and state the direction: spine stale (code moved since the probe) or spine wrong at write time (the probe misread the code). Do not classify against a spine claim you have just watched fail; a classification built on a claim known to be false is worse than one built on no claim at all.

## Process

**1. Read both telos files.** Check the feature's argument against both purposes and don't-contradict rules — what the proto telos says this feature is for, and whether the prod telos leaves room for it. If a telos conflict is detected: present the conflict to the user, name whether it reads as a telos error (the spine's purpose is wrong) or scope creep (the feature is beyond what this repo is for), and wait for explicit confirmation before continuing. Do not write the contract until the user has acknowledged the conflict. Neither outcome is a silent continue. Note the proto telos's `Commit:` hash; the contract will pin to it.

> **⛔ REQUIRED GATE — GATE-TELOS (telos conflict)**
> If the feature conflicts with the prod telos, present the conflict explicitly and name whether it reads as telos error or scope creep. Do not write the contract until the user resolves it.
> The pipeline halts here. Do not proceed until explicitly cleared.

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

When writing a contract for an interaction model claim, name the invariant the interaction enforces — not just the implementation sub-tasks. "One card expanded at a time" is an invariant; "auto-expand UNDER_REVIEW, toggle on click" are the sub-tasks. A contract that names only the sub-tasks passes to ari-port without stating what the sub-tasks exist to enforce. ari-port will implement the sub-tasks and miss the invariant. Name both.

**Semantic register of labels and attribution.** Wording is substrate when it's two phrasings of the same thing. Register shift is a claim: endorsement → disclaimer, celebration → warning, brand confidence → liability caveat. "Powered by PLUS AI Coach" and "generated by AI, which may make mistakes!" are not two phrasings of the same promise — they are different promises. Surface the shift, confirm it.

**Structural visual hierarchy.** Colors and fonts are substrate. Whether the primary metrics live in a prominent hero block versus a flat card grid is not — it reflects the feature's argument about what the user should feel is important. When the proto's layout visually weights one section differently from how prod would naturally render it, that weighting is a claim about significance. Confirm before flattening.

When ambiguous, don't guess — escalate to step 4.

**4. Confirm every claim change with the user.** One at a time, never bundled. Frame concretely: state what the prototype does, what the prod pattern would do instead, and that this is an argument-level decision, not a style choice. If the user is unreachable synchronously, default to preserving the claim and mark it "preserved by default, pending confirmation" — never silently resolve ambiguity by guessing it away.

**Third path — route, don't violate.** If the subagent believes a claim in the prototype looks wrong — not just different in the prod context, but misguided as a design decision — that claim is neither preserved-by-default nor silently dropped. It is surfaced as an Open Question in the contract, with the reasoning stated plainly. The user resolves it before the contract is frozen. Silently satisfying a claim you believe is wrong is worse than either confirming or challenging it: the corpus calls this "route, don't violate" — principled challenge goes through the cycle, not around it. The Open Questions section exists as the halt surface for exactly this case.

**Calibration note — lighter pass.** The full classification pass is the default. A lighter pass is available only when all of the following hold:
1. Both spines are current and have been fully read.
2. The proto feature source has been fully read and no candidate claim changes are visible in any of: state management, reversibility, validation, confirmations, who-sees-what, data persistence.
3. The feature type is well-understood — pure styling, naming, or file restructure with no behavioral change.

This is a signal-clarity condition, not an efficiency shortcut. A full pass on 40 obvious substrate changes before reaching 0 claims generates noise that dulls attention to actual claims. The lighter pass exists to protect focus, not to save time.

Even on a lighter pass, the subagent must produce a positive claim: not "no claims found" but "I looked for claim candidates in [state management, reversibility, validation, confirmations, who-sees-what, data persistence] and found none." The absence of claims is a documented finding, not a silence. This is epistemic hygiene: the skeptical attention is on record even when it finds nothing.

If any of the three conditions is not met, run the full pass.

**4c. Schema-dependency check (pre-freeze).** For every claim's declared `Schema deps:`, verify each named entity/field/enum actually exists in prod before the contract is written. Check the prod spine's entity/field inventory first, if present (`spine-prod/material.md`, per PIN-21's spine-completeness work) — a current, complete spine often settles this by inspection alone. When the spine doesn't cover the dependency, or is silent rather than confirming absence, grep the prod repo directly (path from this project's `CLAUDE.md`, Target repos table) under its schema-bearing directories — `item/`, `dto/`, `enums/` — for the named entity/field/enum. A declared dependency that resolves to zero prod classes or fields is a contract-time break, not a wording detail to smooth over: HALT, surface it to the user for resolution — drop the claim, amend it, or confirm the field exists under a different name — before freezing the contract. This is a backstop, not the primary defense: the spine's entity/field inventory and negative-space list are meant to catch this by the time ari-argue reads them; this check exists for when the spine is still incomplete — a fresh probe, an unusual noun, or drift since the last map. Declaring a `Schema deps:` value is not the same as confirming it resolves — do not skip this step by trusting the claim author's own list.

> **⛔ REQUIRED GATE — GATE-SCHEMA (schema dependency)**
> If a claim's declared `Schema deps:` entry resolves to zero prod classes or fields, halt and surface it to the user for resolution — drop the claim, amend it, or confirm the field exists under another name. Do not freeze the contract until the user resolves it.
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

Write `.anima-lite/ports/<branch-slug>/contract.md`, where `<branch-slug>` is the current git branch (sanitized: lowercase, slashes to dashes) or a feature-name slug if not in git:

```markdown
# Contract: <feature-name>
Branch: <branch-slug>
Generated: <date>
Spine commit: <the Commit: hash from spine-proto/telos.md at time of writing>
Source of truth: <component/file confirmed canonical in step 1a — required whenever multiple candidates existed; "n/a — single source" otherwise>
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue

## The argument
<one or two sentences: what is this work item claiming to the user>

## Substrate changes (free to translate)
- <detail> — <why this is medium, not claim>

## Claim changes (confirmed with user)
- <detail> — Decision: <preserve|change-to-X> — Confirmed: <yes/default-preserve, with date>
  Schema deps: <prod entities/fields/enums this claim's rule logic relies on, e.g. "SessionItem.sessionStart, StudentSessionItem, InstitutionItem" — or "none" if the claim relies on no prod schema (pure UI/interaction)>

## Open questions
<anything not yet confirmed; ari-port must halt and escalate if it hits these>

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

Once written with no open Open Questions, the contract is frozen for the session and ready for ari-port. If ari-port later finds the contract contradicted by the real code (not just incomplete), it will halt and hand the specific delta back to this skill — treat that as new evidence, not as a do-over of step 3 from scratch.
