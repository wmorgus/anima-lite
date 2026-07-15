---
name: ari-arete-pan
description: Sorts an existing repo's code against an already-ratified arete statement into a three-way verdict — nugget (kept), ore (real pressure, doesn't serve cleanly, rewritten from a recorded pressure-note), slag (no signal, discarded). Produces a draft cut, iterates it with the operator, and holds a single batch-ratification gate over the whole cut before any code moves — a different judgment shape from /ari-argue-rhetoric's per-claim confirm, because everything here dies by the absence of a defending telos, not by an argued change. Independent entry point: runnable any time an arete statement exists, not only right after /ari-arete.
---

# ari-arete-pan

Named for shitcorping's panning/smelting vocabulary (`corpora/anima/process.md`) — sorting raw material by what it's worth, before anything is rebuilt. This skill is where an arete statement stops being a standard on paper and starts being a verdict on the actual repo it was founded for.

**Bare name, not `-rhetoric`.** This skill produces a judgment — a sorted cut — not an argument for changing a promise. Same reasoning that keeps `/ari-intake`, `/ari-map`, `/ari-arete`, and `/ari-diagnose` bare (`PHILOSOPHY.md`).

**Adjacent to `/ari-diagnose`, not a mode of it — stated in full, not by cross-reference.** `/ari-diagnose`'s four primitives (spec/epistemic/world-drift/craft) all classify a divergence *from* a telos the code once had and has since drifted away from — every one of those primitives presupposes a because that used to hold. This skill's target never had a because to drift from in the first place; the arete statement is brand new, authored by `/ari-arete` specifically because none existed. Sorting code against a telos it was never oriented by is a different judgment than sorting code against a telos it fell out of alignment with. That difference is the whole reason this is its own skill rather than a fifth primitive bolted onto `/ari-diagnose`'s four.

## Inputs

- **A ratified arete statement** — `.anima-lite/work/<arete-slug>/arete-statement.md`, with its Ratification line filled. This is the only hard precondition (see below) — it does not have to have been produced in this same session, or even recently.
- **The target repo**, read-only throughout this entire skill. Every file this skill inspects is inspected, never edited — this skill's output is a judgment about the repo, not a change to it.
- **This repo's own spine** (`spine-<label>/`), if one exists — `ari-map`'s probe is useful evidence for locating code units and understanding what a piece of code currently does, but the *verdict* is never read off the spine the way a port's substrate/claim classification reads off a prod spine. The spine tells you what's there; the arete statement tells you whether it should stay. If the spine includes a `scaffold.md` (`ari-map/scaffold-spec.md`), it is evidence in the same sense — a unit's coordinate in the scaffold informs, never overrides, the nugget/ore/slag call.

## Preconditions

- **An arete statement exists for this repo, period.** Not "an `/ari-arete` pass just ran in this session." This skill is an independent entry point — its precondition names a state of the world (a ratified statement on disk), not a preceding step in one continuous flow. A re-pan against an unchanged statement (periodic drift check — arete's version of `/ari-map`'s re-probe) and a pan against a statement authored in a different session entirely are both first-class, ordinary invocations, not degraded or unusual paths.
- If no ratified arete statement exists for the target repo, halt and route to `/ari-arete` — this skill does not found a telos on the operator's behalf as a shortcut; founding and judging stay separate skills even when one operator wants to run them back to back.

## Active orientations

**Everything dies by absence, not by argument.** A claim gets confirmed or rejected in `/ari-argue-rhetoric` because someone argued for or against a specific change. Nothing here is argued in that sense — a piece of code is nugget, ore, or slag because the arete statement does or doesn't defend it, and that's a different kind of call: closer to "does this have a citation" than "is this a good idea." Don't reach for argue-rhetoric's per-item confirm reflexively; this skill's own batch gate (below) is the right-shaped check for this judgment, not a missing step.

**Ore is common, not exceptional.** Expect to find plenty of it. A large share of real code was written under real pressure — something needed doing, and no easier path existed at the time — without ever being checked against a telos, because the telos didn't exist yet to check against. Throwaway utility scripts are the canonical case (operator observation, 2026-07-14): no defending telos, but a real, nameable pressure behind them. Treat ore as the expected, ordinary bulk of the cut, not a corner case to special-case around.

**Draft before ratify — the gate is not the operator's first exposure.** The cut goes through the same shape of iteration `/ari-arete` uses for the statement itself: draft, present in full, let the operator reassign items or sharpen ore's pressure-notes, and only then ratify. A cut that goes straight from "I sorted everything" to a single yes/no is skipping the iteration this skill's process requires — see step 3, below.

**Read-only means read-only.** This skill's judgment never touches the target repo's files. If mid-pan a piece of code turns out ambiguous enough that inspecting it more closely would help, that's still read-only inspection — never a speculative edit "to see what breaks." The repo stays untouched until execution, downstream, in `/ari-code-rhetoric`'s arete posture.

**Cutover is not this skill's business, ever.** This skill sorts code into nugget/ore/slag against a telos. It does not plan, name, or gesture at how the eventual new repo gets deployed, pointed to by DNS, or adopted by downstream consumers — that is permanently out of scope for the whole arete work-type, not just deferred past this skill.

## Process

**1. Read the arete statement and the target repo.** The statement in full (it's short); the repo broadly enough to enumerate distinct code units worth judging separately — modules, scripts, files, or larger groupings, whichever grain the repo's own structure supports. Use the repo's spine if one exists, for orientation only.

**2. Draft the cut.** For every unit enumerated in step 1, assign one of three verdicts:
   - **Nugget** — cleanly serves the statement as authored. No pressure-note needed; the reason it's a nugget is that it already matches the standard.
   - **Ore** — a real pressure produced this, but it doesn't serve the statement cleanly as-is. Name the pressure specifically — what need was being filled, and why no easier path existed at the time. This note is what stops the eventual rewrite from reinventing a solution to a pressure nobody wrote down. Where this repo has a `scaffold.md` (`ari-map/scaffold-spec.md`), also record a `Scaffold signal: <coordinate> — <tag>` — a unit can serve the statement but sit at a tangled, unattributable spot in the scaffold (e.g. a step several scenarios all pass through with no clean single owner); that tangle is evidence feeding this same nugget/ore/slag call, never a second verdict axis of its own. Recorded as its own field, not folded into `Pressure:` — closed-taxonomy-shaped facts (a coordinate plus a short tag) belong in their own field, not buried in free prose that can't be counted later. Absent (not "none") when no scaffold exists for this repo or the unit's scaffold coordinate carries no signal.
   - **Slag** — no real signal to carry forward; doesn't serve the statement and there's no pressure worth preserving either. State briefly why it's slag, not just that it is — "no signal" is a finding, not a shrug.

**3. Present the draft cut in full and iterate.** Every unit, its verdict, and (for ore) its pressure-note — shown to the operator as one document, not item by item. Let the operator reassign any unit between buckets, or sharpen an ore pressure-note that undersells or oversells the pressure behind it. Return to this step until the cut is stable — this is not a single presentation-and-done, it's a real revision loop, the same shape `/ari-arete`'s statement-authoring pass uses.

> **⛔ REQUIRED GATE — GATE-ARETE-CUT (batch cut ratification)**
> Once the draft cut is stable, present the full nugget/ore/slag assignment as one batch and require explicit operator ratification of the whole cut before any code moves or any nugget/ore item is handed to `/ari-argue-rhetoric`. This is deliberately not per-item — everything here dies by the absence of a defending telos, which is a different judgment shape from argue-rhetoric's per-claim confirm and deserves to be seen as a batch, not buried in individual confirms. The gate fires once, over the stabilized result from step 3, not once per unit.
> The pipeline halts here. Do not proceed until the whole cut is explicitly ratified.

**4. Hand off.** Nuggets and ore, together with their (for ore) pressure-notes, become `/ari-argue-rhetoric`'s input under the arete posture (see that skill's own posture section) — each still gets stated and confirmed there, one at a time, exactly as any other claim would, because that per-claim confirm is a different check (does this claim hold, as stated) from this skill's batch cut (does anything here even have standing to be considered). Slag is simply dropped — it never reaches argue-rhetoric.

## Output

Write `.anima-lite/work/<slug>/cut.md`:

```markdown
# Arete cut: <target repo>
Slug: <slug>
Generated: <date>
Arete statement: .anima-lite/work/<arete-slug>/arete-statement.md
Target repo: <path>, read-only throughout

## Nuggets
- <unit> — <one line: why it already matches the statement>

## Ore
- <unit> — Pressure: <what need was being filled, why no easier path existed at the time> — Scaffold signal: <coordinate> — <tag>

## Slag
- <unit> — <one line: why no signal is worth carrying forward>

## Ratification
Ratified: <date> — operator (<name>), whole cut as a batch (GATE-ARETE-CUT)
```

## Escalation / Notes

**This is not `/ari-diagnose`'s fifth primitive.** Restated plainly, not just cross-referenced (see Active orientations above): the four primitives all classify drift from an existing telos. This skill classifies against a telos that never existed until `/ari-arete` founded one. If a future reader is tempted to fold this skill's cut into `diagnosis.md`'s `Primitive(s):` field, that's the exact category error this note exists to block.

**A stale ratified statement is a legitimate reason to re-pan, not a blocker.** Because this skill's only precondition is "a ratified statement exists," an operator can re-run this skill against the same repo and the same statement at any later point — the periodic-recheck case. A cut that comes back materially different from a prior pan against the same statement is itself a finding worth a blip or a backlog pin, not something to silently overwrite.

**Cutover stays out of scope even when the cut is done.** A ratified, fully-handed-off cut still says nothing about deploy, DNS, consumers, secrets, or CI for the eventual new repo — those remain a separate workstream every time, per the arete work-type's own permanent exclusion.
