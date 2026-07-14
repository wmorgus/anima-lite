---
name: ari-diagnose
description: Debt-work's intake, upstream of /ari-intake. Locates a divergence, classifies which of the four primitives (spec/epistemic/world-drift/craft) is present, and cites the evidence — turning "something's off here" into an artifact /ari-intake can read as debt-work's source, the same role prototype plays for port. Two entry modes only — operator-nominated pointer, or /ari-read honoring-failure handoff. Does not authorize a fix; that stays /ari-argue-rhetoric's binary substrate/claim cut, downstream.
---

# ari-diagnose

Diagnosis is debt-work's missing starting point. Every other work-type hands intake a legible intent: port's intent sits in the prototype's code, ripple's is authored from a meeting or ticket, harness-change's comes from a live design round. Debt-work has none of that — the whole job is finding and naming a divergence nobody has argued yet. This skill surfaces that fact; it does not argue whether to fix it.

**Diagnose answers:** which of the four primitives is this, and what's the evidence? Not a fifth-thing catalog (security/performance/test/dependency/documentation debt are compositions of the four — decomposition is the first move, per anima-corps `logic.md` §8.11), and not an authorization to change anything. The four-way cut and the substrate/claim cut do not compete: diagnosis is four-way on the way in, authorization stays binary on the way out, downstream in `/ari-argue-rhetoric` (`reorient/identity.md` §"What's genuinely new").

**Bare name, not `-rhetoric`.** Diagnosis surfaces a fact — same reasoning that kept `/ari-intake` and `/ari-map` bare (`PHILOSOPHY.md`).

## The four primitives

Provenance: anima-corps `logic.md` §8.6/§8.11, imported corpus-verbatim except one rename (§ below).

- **spec** — intent→code alignment broken: code faithfully implements an intent that has since changed.
- **epistemic** — artifact→because alignment broken: it exists, nobody knows why.
- **world-drift** — code→world alignment broken: CVE, EOL, deprecation moved past coherent code. *(Corpus calls this "substrate debt" — renamed here to avoid collision with anima-lite's own substrate/claim vocabulary, PIN-25 vocab review.)*
- **craft** — intrinsic structure degraded, every alignment intact. The only primitive defined negatively (no relation failing, just structure) — this is why it scans last, see Process step 3.

## Inputs

- The divergence pointer — a file/module path (entry mode a) or a `/ari-read` judgment artifact whose honoring-question failed (entry mode b, see below).
- This repo's own spine (`spine-<label>/`), especially `material.md` (entity/field inventory, capabilities-NOT-present) and `formal.md` (dominant patterns) — the belief field diagnosis classifies against.
- Git history and blips, when spec or epistemic classification needs to establish what an intent used to be or whether a because was ever recorded.
- For world-drift specifically: an external checkable record (CVE database, vendor EOL notice, deprecation announcement) — not this repo's own state.

## Preconditions

- Work-type is debt-work. Port, ripple, and harness-change do not route through this skill — they already have a legible intent by the time they'd reach it.
- Exactly one of the two in-scope entry modes applies (see Process step 1). If neither applies — an unprompted, self-triggered scan of a spine for drift — halt: that's a different commitment shape (trigger cadence, cost model, false-positive tolerance) and is explicitly out of this skill's scope (PIN-39 contract, claim 4). Route it to backlog as a new pin candidate instead of running it here.
- A spine exists for the repo the pointer names. If none does, halt and request `/ari-map` first — classification without a current spine is guessing, not diagnosing.

## Active orientations

**Ari face.** This skill does not run GATE-TELOS — that fires downstream, in `/ari-intake`, once the diagnosis becomes an intent. Diagnosis's own authority is narrower: is the classification correct and cited, not whether a fix should happen.

**Route, don't fabricate.** If evidence doesn't clearly support any one primitive, or supports more than one at once, say so plainly in `diagnosis.md` rather than forcing a single label. A wrong classification is worse than an honest "primitives spec and epistemic both partially apply, here's why" — the downstream fix will be shaped by whichever primitive gets named here.

**Authorization stays downstream.** Naming a divergence and its primitive is not itself permission to change anything. `diagnosis.md` is `/ari-intake`'s source, not a shortcut around intake or argue — a diagnosis with clean evidence still has to pass GATE-TELOS and, later, one-at-a-time claim confirmation like every other work item.

## Process

**1. Confirm entry mode.** Exactly two are in scope:
   - **(a) Operator-nominated.** The operator names a pointer directly — "diagnose this file," "diagnose this module." Proceed straight to step 2 against the named pointer.
   - **(b) `/ari-read` honoring-failure handoff.** A `judgment.md` whose question-shape was `honoring` ("does prod still honor what a run ported?") came back with a failure — per `ari-read/SKILL.md`'s own routing, that already feeds "pin, then a debt-work intent." Read the judgment's `Reconstruction` and `Belief repair` sections as the starting evidence, not as a substitute for step 2's own read of the divergence.

   If the work item doesn't fit either shape, halt per Preconditions — do not invent a third mode.

**2. Locate the divergence precisely.** Name the specific artifact (file, function, config, dependency entry) where the promise/artifact gap sits — not the general area. A diagnosis that names "the auth module" is not yet a diagnosis; a diagnosis that names `auth/session.ts:createSession` and the specific gap is.

**3. Scan the four primitives in fixed order — epistemic → spec → world-drift → craft.** Not a checklist to run in any order: this sequence is enforced, per PIN-39's contract, claim 3.
   - **Epistemic first.** Is the *because* recoverable at all — git history, a comment, a linked ticket, a spine finding? If no because can be found, that's epistemic, and stop: spec can't be judged against a because that doesn't exist, so checking spec next would be judging code against a fabricated upstream.
   - **Spec next**, only once epistemic clears (a because exists). Does the code still faithfully serve that recovered intent, or has the intent moved out from under faithfully-implemented code?
   - **World-drift next.** Orthogonal to the intent chain — checkable independently of steps 1-2. Does an external record (CVE, EOL notice, deprecation) show the code has fallen behind the world regardless of whether its internal intent chain is intact?
   - **Craft last**, only once the first three are ruled out. Structure can look degraded while actually being a relational failure wearing a craft costume (per PIN-39.md's note on this) — asserting craft before the relational three are cleared risks exactly that misattribution.

   Stop scanning once a primitive is confirmed with citable evidence, unless evidence suggests more than one applies — see "Route, don't fabricate" above.

**4. Cite evidence per the primitive's own bar.** No uniform rule (PIN-39 contract, claim 5):
   - **World-drift** — external-record-strong: name the CVE ID, EOL date, or deprecation notice directly, with a link or exact citation. This is the only bar fixed by PIN-39's contract; the other three are specified here, at build time, as follows.
   - **Epistemic** — cite the search performed and its result: which git range/blame was checked, which docs/tickets were searched, and that nothing was found — "no because" is a finding, not a shrug, and must show its work.
   - **Spec** — cite the recovered because (from step 3's epistemic pass) and the specific code path that no longer serves it, naming the delta between what the because asks for and what the code does now.
   - **Craft** — cite the specific structural symptom (a coupling point, a duplicated pattern, a violated modularity boundary the spine's `formal.md` names elsewhere) and confirm, explicitly, that steps 3's epistemic/spec/world-drift passes found no relational failure — craft's citation is incomplete without that negative confirmation.

**5. Write `work/<slug>/diagnosis.md`** (template below). Mint the slug here if one doesn't already exist (named for the divergence, not the eventual fix).

**6. Hand off to `/ari-intake`.** Diagnosis's output is intake's source for debt-work, the same relationship prototype has to port. Do not write `intent.md` here — that step, including GATE-TELOS, belongs entirely to `/ari-intake`.

## Output

Write `.anima-lite/work/<slug>/diagnosis.md`:

```markdown
# Diagnosis: <short name for the divergence>
Slug: <slug>
Entry mode: <operator-nominated | read-register handoff (judgment: work/<judgment-slug>/judgment.md)>
Generated: <date>
Spine checked: <spine-<label>/ path and Commit: hash>
Primitive(s): <spec | epistemic | world-drift | craft — or more than one, named explicitly if evidence doesn't cleanly settle on one>

## Divergence
<the specific artifact and the specific gap — not the general area>

## Scan
<one line per primitive actually reached before stopping, in order epistemic → spec →
world-drift → craft — what was checked and why the scan stopped or continued past it>

## Evidence
<per the primitive's own bar — external record citation for world-drift, search-performed
result for epistemic, because-vs-code delta for spec, structural symptom + negative
confirmation for craft>

## Open questions
<anything the evidence doesn't cleanly settle — ambiguity between primitives, a because
that's partially recoverable, evidence that's suggestive but not yet citable>
```

## Escalation / Notes

**This artifact is not an intent.** `diagnosis.md` names what diverged and why it's classified that way; it does not enumerate claims or run GATE-TELOS. `/ari-intake` reads it and does that work, same as it reads a prototype's code for a port — do not pre-empt intake's job here by drafting claims in this file.

**Self-triggered scanning is out of scope.** If, mid-diagnosis, the work turns up other divergences nearby that nobody asked about, do not fold them into this diagnosis or start diagnosing them unprompted — note them in Open Questions or hand them to backlog as new pin candidates. This skill diagnoses what it was pointed at, per PIN-39's contract claim 4.

**Provenance:** built per `work/pin39-diagnose-contract/contract.md` (PIN-39). Five claims formalized there: skill container (this file existing, bare-named, upstream of intake), the `diagnosis.md` artifact type, the fixed scan order, the two entry modes, and the per-primitive evidence bar. Full rulings: `.anima-lite/reorient/diagnosis-layer.md`.
