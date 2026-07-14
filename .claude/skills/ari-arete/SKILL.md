---
name: ari-arete
description: Founds a telos by iterative language for a repo that has none on record — the context-starved case, distinct from every other work-type's already-legible intent. Enforces a seed-context gate before drafting begins, runs a draft-and-ratify pass producing a caveman-dense arete statement, and cascades the same pass top-down from a system-level statement to each derived component. Does not judge existing code against the statement — that is /ari-arete-pan, downstream.
---

# ari-arete

Every other work-type hands intake a legible intent: port's sits in the prototype's code, ripple's is authored from a meeting or ticket, harness-change's comes from a live design round, debt-work's comes from `/ari-diagnose`. Arete's target has none of that — the repo has material and efficient cause (it does something) but no final cause on record, nobody ever wrote down what it's *for*. This skill founds that record by language, rather than reading it off code that was never oriented by one.

**Bare name, not `-rhetoric`.** This skill asserts a founding artifact into existence; it does not argue a change to something that already promises. Same reasoning that keeps `/ari-intake`, `/ari-map`, and `/ari-diagnose` bare (`PHILOSOPHY.md`).

**Founds, doesn't judge.** This skill produces the standard. It does not sort existing code against it — that cut, and the batch gate over it, belongs entirely to `/ari-arete-pan`, downstream and independently invocable. Do not let a founding pass drift into judging the repo it's founding a telos for; that is a category error this skill's own scope exists to prevent.

## Inputs

- **The seed context** — whatever the operator points this skill at: a grant proposal, a design doc, a set of tickets, a prior codebase's own docs, an operator's own explanation. Gathered and organized by the operator *before* invocation (Process, pre-pass) — this skill reads it, it does not go looking for it.
- **The parent arete statement**, if this invocation is a cascade step rather than the system-level founding pass — `.anima-lite/work/<parent-slug>/arete-statement.md`. Absent for the first, system-level invocation.
- **This repo's own spine**, if one exists (`spine-<label>/`) — read for context on what the repo currently does, never as a source for what it's *for*. Arete's whole premise is that the telos is not derivable from the code; a spine informs the founding conversation, it does not substitute for it.

## Preconditions

> **⛔ REQUIRED GATE — GATE-SEED-CONTEXT (seed-context readiness)**
> Before any drafting begins, the seed context the operator has assembled must satisfy the current starting rule list — today, exactly one rule: **there must be an index file** naming what every other file in the seed context is and why it's there. This list starts small and is expected to grow as gaps are found in practice (ratified 2026-07-14) — do not treat "one rule" as a loophole to wave through thin context; the gate exists because "better seed, better outcome" is the single most important epistemic-janitoring step in the whole arete work-type, and a missing index file is the cheapest, most legible thing to check before anything more subjective. If the check fails: halt, name specifically what's missing, and do not proceed to drafting — even informally, even as a "quick first pass." There is no soft-fail path here; the gate is hard, not advisory.
> The pipeline halts here. Do not proceed until the seed context passes.

- A slug exists or is minted for this workstream (system-level: name it for the system, e.g. the project; component-level cascade: name it for the component, and record the parent slug it derives from).
- For a cascade step (component-level), the parent arete statement must already be ratified and committed — `.anima-lite/work/<parent-slug>/arete-statement.md` exists with a filled ratification line. Do not found a component's statement against a still-drafting parent; the cascade is top-down and each level's ratification is a precondition for the next, not a formality.

## Active orientations

**Language, not extraction.** The statement is built by the operator and this skill talking, not by this skill reading the seed context and reporting back what it infers. The seed context sharpens the conversation; it does not pre-write the answer. An agent that drafts a v1 statement without having asked a single clarifying question has skipped the actual work this skill exists to do.

**Caveman-dense, not prose.** The target register for the statement itself is concise and conceptually maximal — closer to `RESOLUTION.md`'s one sentence than to a mission-statement paragraph. Iteration exists to compress and sharpen, not to elaborate. If a draft is getting longer with each round, that is a signal the iteration is going the wrong direction.

**Asserted, not argued.** The arete statement's epistemic status is different from every claim `/ari-intake` produces: it is a ratified value judgment, defended by the operator's own conviction, not by a cited source. Do not attach an `argued-by:` line to it, and do not ask "where did this come from" the way `/ari-argue-rhetoric` would ask of a claim — the honest answer is "the operator decided this is the standard," and that is sufficient provenance for this artifact type.

**Cascade fidelity.** A component-level statement is a derivation, not an independent founding. It must be checkable against its parent the way a claim is checkable against its source — a component statement that doesn't visibly follow from its parent's terms is a sign the cascade skipped a step, not a sign the component is special.

**Cutover is not this skill's business, ever.** Nothing in this skill's process touches deploy config, DNS, downstream consumers, secrets, or CI. If the seed context or the operator's own language starts drifting toward those topics mid-draft, note it and steer back — this skill founds a telos, it does not plan an operational transition.

## Process

**1. Confirm the seed context is assembled.** This is the operator's obligation, stated to them plainly if they arrive without it: gather everything relevant — the more and the cleaner, the better — into one place, with an index file labeling what's there. This skill does not assemble the seed context on the operator's behalf; it checks it.

**2. Run GATE-SEED-CONTEXT.** See Preconditions. Halt on failure.

**3. Read the seed context in full.** Not a skim — every file the index names. This is the read that grounds the clarifying questions in step 4; a question asked without having read the material it should already answer is wasted motion.

**4. Ask clarifying questions.** Whatever the seed context leaves ambiguous about what this repo (or system) is *for* — not what it does, what it's *for*. Keep asking until the ambiguity that matters to the statement's content is resolved; do not draft against known gaps just to have something to show.

**5. Draft v1.** One or two sentences, caveman-dense, in the register of `RESOLUTION.md`'s own sentence ("agentic harness using aristotelean decomposition to build software that admits change only as argument" — same shape of density, different subject). Present it plainly.

**6. Iterate by language.** Operator and agent revise the statement together — compress, sharpen, correct — until the operator confirms it matches their intent. This is not a single round; return to step 4 if a revision surfaces a new ambiguity rather than patching around it.

**7. Ratify.** Operator states explicitly that the statement is ready to commit. Write `arete-statement.md` (Output, below) with the ratification line filled — date and operator, same shape as `RESOLUTION.md`'s own ratification line. The artifact is not terminal until this line is filled; a drafted-but-unratified statement is not usable downstream by `/ari-arete-pan` or the cascade's next node.

**8. Cascade, if applicable.** Once a system-level statement is ratified, re-invoke this skill per derived component, each time with: the parent statement as input, a fresh (component-scoped) seed context passing its own GATE-SEED-CONTEXT check, and steps 3–7 run again for that component specifically. Do not batch multiple components' statements into one pass — each is its own workstream, named with its own slug, even though every one derives from the same parent.

## Output

Write `.anima-lite/work/<slug>/arete-statement.md`:

```markdown
# Arete statement: <system or component name>
Slug: <slug>
Generated: <date>
Parent: <parent-slug, or "none — system-level founding pass">
Seed context: <path(s) the operator assembled, and the index file confirmed at GATE-SEED-CONTEXT>

## Statement
<the ratified sentence(s) — caveman-dense, the standard this repo/component is held to>

## Provenance
Asserted, not argued: this is a ratified value judgment, not a claim with a cited source.
The operator's own conviction is the defense; there is no `argued-by:` line because none applies.

## Cascade note
<for a component-level statement: one or two sentences on how this derives from the parent
statement — what the parent fixes that this component inherits, what's specific to this
component. "n/a — system-level" for the first, system-level statement.>

## Ratification
Ratified: <date> — operator (<name>)
```

**This artifact is the input `/ari-arete-pan` requires to exist** (its own precondition — see that skill's SKILL.md) — but this skill does not invoke it, and does not assume it will be invoked next in the same session. A ratified statement with no pan pass run against it yet is a complete, valid terminal state, not a dangling half-finished workstream.

## Escalation / Notes

**Not a mode of `/ari-diagnose`.** `/ari-diagnose` classifies a divergence against an *existing* telos the code drifted from. This skill's whole premise is that no telos exists yet to drift from — there is nothing to diagnose here, only something to found. Do not route a "this repo seems context-starved" observation through `/ari-diagnose`; it belongs here.

**Seed-context rule growth is expected, not a gap to silently patch.** When a founding pass turns up a way thin seed context produced a bad statement, that's a candidate for a new starting rule — capture it as a backlog pin (`/ari-backlog`, fast lane) naming the gap concretely, rather than encoding a one-off fix into this skill's prose. The rule list is meant to grow from real cases, not from anticipated ones.

**Independent of `/ari-intake`.** This skill does not fold into the write register's usual `/ari-intake` → `/ari-argue-rhetoric` → `/ari-code-rhetoric` chain — it produces a founding artifact, not an argued intent to change something. `/ari-arete-pan`, downstream, is what eventually feeds nuggets and ore back into `/ari-argue-rhetoric` as ordinary confirmed claims once the cut is ratified.
