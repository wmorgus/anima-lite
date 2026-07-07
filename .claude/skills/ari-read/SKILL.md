---
name: ari-read
description: The read-register doorway — reconstruction, the harness's answer to "what is this system, and why?" A question goes in, verbatim, and a telos-matched judgment comes out. Confirms the question's intent without staking it for the asker (GATE-QUERY), then returns only when the prepared judgment aligns with that confirmed intent and presents it for the operator's own reading (GATE-MATCH). Mints the workstream slug and writes the judgment artifact at work/<slug>/judgment.md. Sibling to /ari-intake, not a step inside it — if the work item is an intent to change the repo, this skill halts and routes to /ari-intake instead.
---

# ari-read

Read is the reconstruction skill: truth about the system is scattered — across the codebase, the spine, the live data, the git record — and a question asks for it back in one place. Where the write register spends belief to change reality and appends to the record, the read register spends reality to repair belief and audits the record. Neither register subsumes the other; a work item is one or the other, never neither.

**The fork, named at the door.** Every work item enters through a declared register — no undeclared default underneath. If the work item in front of you is an intent to change the repo — a feature to port, a change to author, a divergence to fix — it does not belong here: halt and route it to `/ari-intake`. This skill only takes question-shaped work: "what is this system now?", "does prod still honor what a run ported?", "did that gate get engaged or just checked off?", "is this divergence drift or growth?" Nothing enters unregistered.

**Read answers:** what does the whole information system say about this question, and does the prepared answer actually match what was asked? It does not answer whether anything should change — a reconstruction that surfaces a divergence hands that judgment to the write register or to a blocked gate; it does not resolve the divergence itself.

## Inputs

- The question as asked — verbatim, in the asker's own words, before any restatement.
- The five fields every reconstruction reasons from (canonical narrative: `PHILOSOPHY.md`):
  1. **User intent** — the ask as asked, then confirmed.
  2. **Ratified intent** — the promise layer: `RESOLUTION.md` → spine `telos.md` → contracts → confirmed claims. What the system should be.
  3. **Belief** — the map: spines and docs, including where those beliefs end.
  4. **Reality** — live data: the repo as it sits, runtime behavior, target-repo state.
  5. **The record** — the diachronic trail: git history, blips, ratification lines, done pins, the backlog ledger.
- `RESOLUTION.md`, the relevant `.anima-lite/spine-<label>/` directories, and `.anima-lite/pins/PIN-<n>.md` / `.anima-lite/backlog.md` — the ratified-intent and belief fields.
- The live target repo(s) and this repo as they sit on disk — the reality field.
- Git history, `work/<slug>/blips.md` files, `RESOLUTION.md`'s ratification line, and `.anima-lite/backlog.md`'s done/archived pins — the record field.

## Preconditions

- The work item is question-shaped, not change-shaped. If it asks for something to be different rather than asks what something is, that is a change intent — halt and route to `/ari-intake`.
- A spine is not required to start. If no spine exists yet for a repo the question touches, proceed anyway and state plainly that the belief field is empty for this reconstruction — a reconstruction can run against reality and the record alone. Do not halt to demand `/ari-map` the way `/ari-intake` does; belief's absence is itself an honest finding here, not a blocker.
- No slug exists yet for this question. If one does and `work/<slug>/judgment.md` already exists unchanged, do not re-run read; the judgment already presented stands until the operator asks again.

## Active orientations

**Instrument, not reader.** The operator is the reader; this skill is the reader's instrument. The agent prepares the judgment — it never self-certifies one. A judgment is not done when the agent believes it's right; it's done when it has been presented and the operator has read it. This is the same operator-as-claim-court structure the write register already has.

**No colonization at the door.** Confirming the question's intent at GATE-QUERY is not staking it for the asker. Do not hand the operator a synthesis of "what the question should really be asking," and do not pre-load the reconstruction's frame before intent is confirmed. Confirm the question the operator actually asked, then go reconstruct against that — not against a better-sounding question standing in for it.

**Conservative default, read-register form.** An uncertain reconstruction element is marked uncertain in the judgment, never smoothed into confident prose. A missing belief field is stated as missing, not silently backfilled from assumption.

**Provenance held, not shipped.** Every reconstruction element carries a cited-by line, but the judgment's body reads as a judgment, not a citation dump — provenance lives in its own section, shown on demand rather than paraded by default.

## Process

**1. Record the question verbatim.** This is the first write to the artifact and mints the slug — `work/<slug>/` does not exist before this step. Write the question exactly as asked, before any intent-confirmation or ontology-building, so intent-correction later stays distinguishable from intent-replacement now.

**2. Run GATE-QUERY.**

> **⛔ REQUIRED GATE — GATE-QUERY (question intent)**
> The question is recorded verbatim above this gate, not after it. State back, in one or two sentences, what you understand the question to be asking — without reframing it into a different, better-posed question and without proposing what the answer will turn out to be. This is a restatement for confirmation, not a synthesis for approval. Halt here until the operator confirms the restatement matches what they meant, or corrects it. Confirming intent is not staking it: do not let the confirmed restatement smuggle in a frame the operator didn't supply.
> The pipeline does not proceed to reconstruction until intent is confirmed.

**3. Build the question's ontology.** Once intent is confirmed, decide which elements from which of the five fields actually bear on answering it, and classify the question-shape:

- **state** — "what is this system now?" Feeds nothing downstream; the answer is the deliverable.
- **honoring** — "does prod still honor what a run ported?" A failure feeds the write register (a pin, then a debt-work intent).
- **record** — "did that gate get engaged or just checked off?" A compliance-vs-substance reading of the harness's own record; feeds calibration.
- **adjudication** — "is this resolution divergence drift or growth?" A prepared adjudication the operator ratifies; feeds a blocked gate.

Name the shape and the fields consulted explicitly before reconstructing — this is the ontology step, and it is where user-intent meets belief: what the question is asking, matched against what we believe we know about where the answer lives.

**4. Reconstruct, with cited-by provenance per element.** Assemble the judgment from the fields identified in step 3. Every element of the reconstruction carries a `cited-by:` line pointing at its source (a file + line/section, a commit, a pin ID, a probe you ran just now). An element with no source is not ready for the judgment — either find where it actually comes from or mark it as an open gap.

**5. Write the belief-repair section.** Three parts, each stated plainly:
- **Believed** — what the spine/docs said, cited.
- **Observed** — what a direct probe of reality showed, cited.
- **Where belief ends** — the unverified boundary: what this reconstruction could not confirm against reality, stated rather than glossed over. The map's edge, drawn on the map.

**6. Run GATE-MATCH, then present.**

> **⛔ REQUIRED GATE — GATE-MATCH (telos match + operator reading)**
> Before presenting: does the prepared judgment actually align with the confirmed intent from GATE-QUERY — "this is what it is, and here's why," matched to what was asked, not to a nearby question that was easier to answer? Do not present until this holds; if it doesn't, return to step 4.
> Once it holds, the judgment is presented for the operator's reading — not self-certified as final. The artifact is not terminal until the operator has read it and the Operator reading section is filled. The agent's job ends at presentation; the operator's reading is a separate, required step, not a formality assumed to happen.

**7. Record the destination.** State plainly in the judgment's `Feeds:` field what this judgment feeds, per its question-shape: nothing, a pin/debt-work handoff, calibration, or a blocked gate. If it feeds the write register, fire the fast-lane pin per `/ari-backlog`, citing the judgment's path as what surfaced it.

## Output

Write `.anima-lite/work/<slug>/judgment.md`:

```markdown
# Judgment: <short name for the question>
Question (verbatim): <the question exactly as asked>
Slug: <slug>
Question-shape: <state | honoring | record | adjudication>
Generated: <date>
Confirmed intent: <filled after GATE-QUERY — the restatement the operator confirmed>
Feeds: <nothing | pin/debt-work handoff (PIN-<n>) | calibration | blocked gate (name it)>

## Ontology
<which of the five fields were consulted and why; the question-shape classification's reasoning>

## Reconstruction
<the judgment itself — "this is what it is, and here's why." Prose, not a field dump.
Uncertain elements marked uncertain, not smoothed.>

## Belief repair
**Believed:** <what the spine/docs said, cited>
**Observed:** <what a direct probe of reality showed, cited>
**Where belief ends:** <the unverified boundary — stated plainly>

## Provenance
<cited-by list, one line per reconstruction element — held here, not repeated in the
Reconstruction section above; shown on demand>

## Operator reading
<filled only at GATE-MATCH clearance — date + operator note. The judgment is not
terminal until this section is filled.>
```

## Escalation / Notes

**Adjudication-shape judgments hand off, they don't decide.** A judgment whose question-shape is adjudication (e.g. resolution drift-vs-growth, per `RESOLUTION.md`'s GATE-TELOS apex layer) is handed to that gate's own clearing procedure once presented — the judgment prepares the adjudication, the operator makes it. This skill does not clear GATE-TELOS or any other write-register gate on its own authority.

**Slug ownership.** Same rule as `/ari-intake`: once minted, the slug is this reconstruction's name for its full life. Do not rename mid-workstream; a scope change big enough to need a new name is itself a new question — reopen GATE-QUERY on the new question rather than silently renaming.

**Route-out is not a failure.** Discovering mid-read that a "question" is actually a change request is a normal outcome, not an error state — halt, name it plainly, and send the work item to `/ari-intake` rather than forcing a judgment artifact out of a change-shaped ask.
