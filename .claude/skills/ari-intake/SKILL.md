---
name: ari-intake
description: Sharpens a work item's telos and ensures everything entering it is argued for — by prototype (the proto feature's code carries the argument) or by language derived from context (meeting outcomes, tickets, specs, the operator's own translation). Mints the workstream slug and writes the argued-intent artifact at work/<slug>/intent.md. Called first, before ari-map or ari-argue touch anything — nothing enters the pipeline unargued.
---

# ari-intake

Intake is the final-cause skill: it establishes what the work item is *for*, before anything downstream asks what may change. Every work-type passes through here — port, ripple, and debt-work alike — because every work item is intent crossing a boundary into a repo, and that intent has to be legible and argued before classification can start.

**Intake answers:** where does this intent come from, and is every part of it argued for? Nothing enters the pipeline unargued — no invented behavior, no "while we're at it."

**Argue answers:** may this intent change or institute promises? Classification and one-at-a-time ratification are unchanged, and stay entirely inside `/ari-argue`. Intake does not classify substrate vs. claim — it only establishes that a claim exists and is sourced.

## Inputs

- The raw intent source(s) for this work item — proto feature source (port), meeting notes/tickets/specs/an operator's own translation of a runaround email (ripple), or a diagnosed divergence (debt-work — see posture note below).
- The target repo's `RESOLUTION.md` (the one-sentence sovereign description) — for self-changes to anima-lite, that's this repo's own `RESOLUTION.md` at repo root. Read this before the spine's `telos.md`; it is GATE-TELOS's apex layer. If the target repo has none, note it absent — do not fabricate one.
- The target spine(s), especially `telos.md` — `.anima-lite/spine-<label>/telos.md` for whichever repo(s) this work item touches. Read before sharpening the change's own telos; GATE-TELOS checks the two against each other.
- `.anima-lite/backlog.md`, if this work item originates from a pin — read the pin's body and Contract field (if shaped past stub:0) as a candidate source, not as a substitute for gathering the actual sources it points to.

## Preconditions

- A work item has been identified — a feature to port, a ripple to author, or a diagnosed divergence — but no slug exists for it yet. If a slug and `work/<slug>/intent.md` already exist and nothing about the intent has changed, do not re-run intake; proceed to `/ari-argue`.
- At least one candidate spine is reachable for the telos check. If no spine exists yet for a repo this work item touches, halt and request `/ari-map` for that repo before continuing — GATE-TELOS cannot fire against a telos that hasn't been probed.

## Per-work-type posture

Intake is upstream of argue for every work-type, but the amount of work intake does varies sharply:

- **Port.** Near-trivial. The prototype's code already carries the argument — intake's job is to verify that argument is actually there (not assumed) and sharpen the change's telos statement, not to construct the argument from scratch. Most claims will carry `argued-by: prototype <path>`.
- **Ripple.** Authored. There is no source code to read the argument off of — intake is real work here: translating language (a ticket, a meeting outcome, a spec, an operator's own paraphrase of a runaround email) into an argued intent. Most claims will carry `argued-by: language <source>`.
- **Debt-work.** The diagnosis layer (identifying which of spec/epistemic/world-drift/craft divergence is present, per `PHILOSOPHY.md`) is the natural home for debt-work's intake — the diagnosis IS the argued intent for a fix. **This is ratified direction, not yet built.** Do not run debt-work intake as if the diagnosis layer exists; if a debt-work item reaches this skill today, say plainly that diagnosis machinery isn't built and route it back to backlog/human judgment rather than fabricating an intake pass.

## Active orientations

**Ari face.** Telos authority is senior here too, and earlier than in argue — GATE-TELOS fires in this skill, before any contracting exists to protect. A work item whose telos conflicts with the repo's telos is a routing question at the door, not something to discover mid-classification.

**No invented behavior.** The single discipline this skill exists to enforce: every claim in the intent artifact has a named source. "This seems like a good idea while we're here" is not a source. If a claim has no prototype path and no language source, it does not belong in `intent.md` — cut it, or go find where it actually came from.

**Gate-fatigue guard, held forward.** GATE-TELOS fires once, here, at full strength. It is not meant to fire again by default in `/ari-argue` — see that skill's conditional backstop. Doing the telos work carefully here is what earns argue the right to treat it as settled.

## Process

**1. Mint the slug.** Choose a slug for the workstream (branch-name-shaped: lowercase, hyphens). This is the first artifact of the workstream — `work/<slug>/` does not exist before this step and does exist after it. Port and ripple slugs should be recognizable from the feature/change name; debt-work slugs from the divergence being addressed.

**2. Gather sources.** Collect every source this work item draws on: proto feature source files (port), tickets/meeting notes/specs/the operator's own translation (ripple), or the diagnosed divergence record (debt-work, once built). Read them fully before sharpening telos — a telos sharpened against a partial read is a telos sharpened against a partial understanding of what's being asked for.

**3. Sharpen the telos.** State what this work item is *for* — its change-telos — in one or two sentences, the same register as a spine's `telos.md` §1 Purpose: a decision constraint, not a mission statement. First check it against the target repo's `RESOLUTION.md`, if one exists — does the repo this change produces still answer to the resolution? Then read the target spine's `telos.md` §1 and §2 (Purpose, Don't contradict) and check the change-telos against that.

**4. Run GATE-TELOS.** One gate, two authority layers, checked in order:

> **⛔ REQUIRED GATE — GATE-TELOS (telos conflict)**
> **Apex layer — RESOLUTION.md.** Does the repo this change produces still answer to the target repo's resolution sentence? If the target repo has no `RESOLUTION.md`, record the apex layer as *absent* in `intent.md`'s telos statement — do not fabricate one, and this absence does not block the gate. If a `RESOLUTION.md` exists and the change conflicts with it, the conflict is named constitutionally, not as telos-error/scope-creep:
> - **drift** — the work item or the target code is wrong relative to the resolution. Fix it; this is the custodian's normal work, and the pipeline may proceed once fixed.
> - **growth** — the resolution sentence itself must change. This is never bundled: halt, and the resolution edit becomes its own workstream (separate intake, separate commit, explicit operator ratification recorded in `RESOLUTION.md`'s ratification line). This work item stays **blocked** until that workstream resolves — do not write `intent.md` for the original item in the meantime.
> Asymmetry: `telos.md` is fallible commentary (staleness is a known, hash-tracked state); `RESOLUTION.md` is sovereign and presumed correct. A mismatch against it indicts the change, never the sentence — quietly editing the resolution to match drifted code is exactly the failure this layer guards against.
>
> **Telos layer — spine `telos.md`.** If the work item's change-telos conflicts with the target repo's telos or don't-contradict rules (§1/§2), present the conflict explicitly and name whether it reads as telos error (the spine's purpose is wrong) or scope creep (the work item is beyond what this repo is for). Do not write `intent.md` until the user resolves it.
>
> The pipeline halts here on either layer. Do not proceed until explicitly cleared.

**5. Enumerate claims, each with provenance.** List every distinct thing this work item is asking for. For each, write an `argued-by:` line:
- `argued-by: prototype <path>` — the claim is read directly off working prototype code at that path.
- `argued-by: language <source>` — the claim is derived from a named non-code source (a ticket ID, a meeting date + attendees, a spec section, or "operator translation of <email/conversation description>" when the operator is doing the translating themselves).

A claim with neither is not ready for `intent.md`. Either find its real source or drop it — do not manufacture a provenance line to fill the field.

**6. Write `work/<slug>/intent.md`** (template below).

**7. Hand off to `/ari-argue`.** Intake's output is argue's primary input. Do not perform substrate/claim classification here — that judgment belongs entirely to argue, unchanged by this skill's existence.

## Output

Write `.anima-lite/work/<slug>/intent.md`:

```markdown
# Intent: <work item name>
Slug: <slug>
Work-type: <port | ripple | debt-work>
Generated: <date>
Target spine: <spine-<label>/telos.md path this was checked against>
Target telos commit: <the Commit: hash from the target spine's telos.md at time of writing>

## Telos statement
<1-2 sentences: what this work item is for, checked against the target spine's §1 Purpose
and §2 Don't-contradict rules. State the check's outcome — clean, or GATE-TELOS resolution
summary if a conflict was raised and cleared. Also state the apex layer's outcome — clean,
conflict-resolved (drift fixed or growth workstream ratified), or absent (target repo has
no RESOLUTION.md).>

## Sources
- <source 1 — proto path, ticket ID, meeting date + attendees, spec section, or named operator translation>
- <source 2>

## Claims
- <claim 1 — what this work item asks for, stated as a promise, not an implementation detail>
  argued-by: prototype <path> | language <source>
- <claim 2>
  argued-by: prototype <path> | language <source>

## Notes
<anything intake surfaced that argue should know going in — ambiguity in a source,
a source that only partially covers a claim, a posture note for debt-work items
routed here before the diagnosis layer exists>
```

## Escalation / Notes

**Slug ownership.** Once minted, the slug is the workstream's name for its full life (intake → argue → port → harvest). Do not rename mid-workstream; if the work item's scope changes enough to need a new name, that is itself a telos question — reopen GATE-TELOS, don't silently rename.

**Claims without provenance are refused downstream, not just discouraged here.** `/ari-argue` enforces this on its own input — see its Inputs/Preconditions. Intake enforcing it at the source is the cheap place to catch it; argue enforcing it again is the backstop, not a redundant duplicate check invented independently.

**Debt-work is honesty-gated, not feature-gated.** Until the diagnosis layer is built, this skill should say so plainly to anyone who invokes it for a debt-work item, rather than producing an `intent.md` that dresses up an undiagnosed divergence as an argued one.
