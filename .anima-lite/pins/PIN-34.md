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

Structural note (agent, same session): the query-intent confirmation step is GATE-TELOS's read-register analog, and "show your work if asked" is `argued-by:` provenance pointed backward — cited-by for reconstruction elements. Intake's discipline (nothing enters unargued) appears to survive the register flip intact, which leans toward the fourth-work-type answer — but the decomposition Will named comes first; don't pre-decide. Corpus resonance: the judgment artifact is §15.17's staked-vs-laundered reading made material, and query-intent confirmation at the door inherits §15.18's telos-colonization risk (confirming intent ≠ staking it for the asker).

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — decomposition of what ground control needs (prerequisite, named by Will); reconstruction as the read-register work-type (design); telos-matching judgment artifact spec (format + provenance/show-your-work discipline); the container decision (fourth work-type inside ari-intake vs. separate entry skill) made *after* the decomposition. Out — building retrieval/query machinery; anima-core semantic retrieval (separate track); resolving §15.14/§15.18 corpus-side.
**Batch:** unbatched
**Contract:** not traced
**Resolution:**
