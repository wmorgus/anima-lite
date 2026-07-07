### PIN-34 — ari-intake only exists in vibe-engineer mode; needs ground-control mode too
captured: 2026-07-07
stub: 1
status: open
home: anima-lite
goes-stale: superseded once intake (or a sibling doorway) defines a reading-register entry — a work-type or mode whose output is validation/drift-finding rather than a change contract
relates-to: PIN-27 (intake build), PIN-32 (work-type enum gap — adjacent), PIN-33 (resolution divergence adjudication — natural first consumer), .claude/skills/ari-intake/SKILL.md, anima-corps corpora/anima/logic.md §11.6–11.7 (vibe engineering / ground control registers)

Will's observation (2026-07-07): ari-intake — the new major upstream, everything enters through it — only exists in vibe-engineer mode (anima vocab, logic.md §11.6: the acting/writing register). All three work-types (port, ripple, debt-work) are intents to *change* a repo; the pipeline's only output shape is a contract that leads to code. There is no ground-control mode (§11.7: the reading/validating register — watching at the scale of the whole, validating that actions are going somewhere, distinguishing structural compliance from substantive ratification, noticing drift). Work items like "check whether prod still honors what run4 ported," "adjudicate resolution divergence — drift or growth?" (PIN-33), or "audit spine currency against reality" have no doorway: they'd either be forced into a change-shaped intent.md or bounce. For a custodian of promise/artifact alignment this is half an identity — the reading half is the custody; the writing half is its consequence.

Will's answers to the two deferred questions (2026-07-07, same session):

**If a write is a ripple, a read is a reconstruction.** Truth has been scattered — in the codebase, the spine, the live databases. The read-register work-type reassembles it: understand the user's argument, confirm the intent of the query, make a best-faith attempt to honor it, and be ready to show your work if asked. Fourth-work-type-vs-separate-skill stays open, but it's now downstream of a named prerequisite: decompose what ground control actually needs before choosing the container.

**Terminal artifact is telos matching — a "this is what it is, and here's why" judgment.** Each query creates an information ontology stemming from "what is it?" — which elements and arguments from the whole live information system best get at what this question is posing. The agent returns only when it can confidently say the prepared response aligns with the teleological intent of the question. Calibration target: Will's idealized output to superiors — natural-language question about the system → natural-language answer (or a file, which is itself an argument and a promise: "this honors what you requested"). So the reconstruction terminates in a judgment artifact, not a contract — provenance held, shown on demand rather than shipped by default.

Structural note (agent, same session): the query-intent confirmation step is GATE-TELOS's read-register analog, and "show your work if asked" is `argued-by:` provenance pointed backward — cited-by for reconstruction elements. Intake's discipline (nothing enters unargued) appears to survive the register flip intact. Corpus resonance: the judgment artifact is §15.17's staked-vs-laundered reading made material, and query-intent confirmation at the door inherits §15.18's telos-colonization risk (confirming intent ≠ staking it for the asker).

**Decomposition (2026-07-07, agent draft, operator-accepted).** What ground control needs, cut by question-shape; the load-bearing axis is what the judgment *feeds*:
1. **State questions** — "what is this system now?" Terminal: an answer to the human; feeds nothing downstream.
2. **Honoring questions** — "does prod still honor what run4 ported?" Artifact chain vs. live reality; a failure feeds the write register (pin → debt-work intent).
3. **Record questions** — "did that gate get engaged or checked off?" Staked-vs-laundered reading of the harness's own record (§15.17); feeds calibration.
4. **Adjudication questions** — "resolution divergence: drift or growth?" (PIN-33, first consumer). Prepared adjudication the operator ratifies; feeds a blocked gate.
All four share one spine — verbatim question → intent confirmation → reconstruction with cited-by provenance → telos-matching judgment — so this is ONE work-type; the destination differences are fields on the judgment artifact, not separate doorways.

**Field tiling (2026-07-07, ratified in discussion).** The five fields every agent reasons from — both registers, complementary flows:
1. **User intent** — the ask as asked, verbatim, then confirmed.
2. **Ratified intent** — the promise layer: resolution → telos → contracts → confirmed claims. What the system *should* be.
3. **Belief** — the map: spines and docs. Best-faith approximation of what and where we believe the system to be, *including where those beliefs end* — the confidence edge is part of the field. ari-map authors belief, not truth. (Operator's move: brought "belief" in explicitly; map analogy apt.)
4. **Reality** — live data: code as it sits, runtime behavior, databases. Always sampled, never held in full — which is why belief exists.
5. **The record** — the diachronic trail: git history, blips, ratification lines, done pins, ledger. Append-only fact of how the present came to be; not belief, not intent, not present state.
Generative check — pairwise divergences map onto existing machinery: user-intent×ratified-intent = GATE-TELOS; belief×reality = GATE-HASH/stale-spine/blips (a blip is a belief edge hit mid-work); ratified-intent×reality = drift/debt, the custodian's core object; record×everything = the §15.17 reading, no machinery yet (this pin's question-shape 3); user-intent×belief = reconstruction's ontology step. Register flows: **the write register spends belief to change reality and appends to the record; the read register spends reality to repair belief and audits the record.** Neither subsumes the other (§11.7), now mechanical.

**Container decided (2026-07-07, operator): sibling entry skill** that mirrors intake's discipline — not a fourth work-type inside ari-intake. Reason: the shared spine survives the register flip, but everything downstream of intake is write-shaped (intent.md exists to be contracted from; reconstruction never reaches ari-argue/ari-port). Requirement that comes with it, operator-named: **mode honesty** — the system must be honest about which register it's in; forced mode selection, no undeclared default underneath (the Kiro failure: vibe/spec modes with a chatbot escape hatch where work happens in no register and leaves no record). Nothing enters unargued, one level up: nothing enters unregistered. Skills stay separate; agent identities stay honest.

**Instrument, not reader (corpus constraint, §6.16 + §15.18).** Ground control is a human reading function, not an agent topology slot; "Hermes-as-ground-control" is explicitly ruled out. The skill is the reader's instrument: the agent prepares the judgment artifact, the operator remains ground control, and the artifact terminates in *presented for the operator's reading*, never self-certified. Same operator-as-claim-court structure the write register already has.

**What belief buys the artifact:** three-part honesty structure — what was believed (spine, cited), what reality showed (probes, cited), where belief ends (the unverified boundary, stated: the map's edge drawn on the map). Provenance is the belief-repair trail. Per §15.18's Socratic-transcript amendment, the question is recorded verbatim before any ontology-building, keeping intent-correction distinguishable from intent-replacement.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — sibling entry skill for the read register (container decided 2026-07-07, above); reconstruction as the read-register work-type, one work-type covering all four question-shapes; telos-matching judgment artifact spec (verbatim question + believed/observed/belief-edge + cited-by provenance held, shown on demand); mode-honesty norm (forced register selection, no undeclared default); field tiling recorded (home TBD, ratification round); instrument-not-reader guard in spec text. Out — building retrieval/query machinery; anima-core semantic retrieval (separate track); resolving §15.14/§15.18 corpus-side; any self-certifying terminal state.
**Batch:** unbatched
**Contract:** not traced
**Resolution:**
