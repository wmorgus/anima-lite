# Reorientation — the read register

Captured 2026-07-07, built same day — canonical operative text is `.claude/skills/ari-read/SKILL.md`; this doc is the design record. Tracked as PIN-34.

---

## What it names

`/ari-intake` — the new major upstream, everything change-shaped enters through it — only ever existed in write-register mode: work that changes a repo and ends in a change contract. There was no doorway for question-shaped work: "what is this system now?", "does prod still honor what a run ported?", "did that gate get engaged or just checked off?", "is this a drift or a growth?" The read register — `/ari-read` — is that doorway. Its work-type is **reconstruction**: truth about the system is scattered across the codebase, the spine, and live data, and a question asks for it back in one place.

One work-type covers four question-shapes, cut by what the resulting judgment *feeds*:
1. **state** — "what is this system now?" Feeds nothing; the answer to the human is the deliverable.
2. **honoring** — "does prod still honor what a run ported?" A failure feeds the write register: a pin, then a debt-work intent.
3. **record** — "did that gate get engaged or just checked off?" A compliance-vs-substance reading of the harness's own record; feeds calibration.
4. **adjudication** — "resolution divergence: drift or growth?" (PIN-33's first consumer.) A prepared adjudication the operator ratifies; feeds a blocked gate.

All four share one spine — verbatim question → intent confirmation → reconstruction with cited-by provenance → telos-matching judgment — so this is one work-type; the destination differences are fields on the artifact, not separate doorways.

## The five-field tiling, in full

Both registers reason from the same five fields (canonical home: `PHILOSOPHY.md`):

1. **User intent** — the ask as asked, verbatim, then confirmed.
2. **Ratified intent** — the promise layer: resolution → telos → contracts → confirmed claims. What the system should be.
3. **Belief** — the map: spines and docs. Best-faith approximation of what and where we believe the system to be, including where those beliefs end — the confidence edge is part of the field. `/ari-map` authors belief, not truth.
4. **Reality** — live data: code as it sits, runtime behavior, databases. Always sampled, never held in full — which is why belief exists.
5. **The record** — the diachronic trail: git history, blips, ratification lines, done pins, the ledger. Append-only fact of how the present came to be.

**Register flows:** the write register spends belief to change reality and appends to the record; the read register spends reality to repair belief and audits the record. Neither subsumes the other.

**The generative check** — pairwise divergences map onto existing machinery:

| Divergence pair | Machinery |
|---|---|
| user intent × ratified intent | GATE-TELOS |
| belief × reality | GATE-HASH / stale spine / blips (a blip is a belief edge hit mid-work) |
| ratified intent × reality | drift / debt — the custodian's core object |
| the record × everything | the compliance-vs-substance reading — no machinery until this pin (question-shape 3) |
| user intent × belief | reconstruction's ontology step |

## Mode honesty

Every work item enters through a declared register — forced mode selection, no undeclared default underneath. Named failure this guards against (the Kiro shape): vibe/spec modes with a chatbot escape hatch where work happens in no register and leaves no record. Intake's discipline — nothing enters unargued — survives the register flip as: nothing enters unregistered. `/ari-intake` and `/ari-read` are the only two doorways; each names the fork explicitly and routes to the other.

## Instrument, not reader

Ground control is a human reading function, not an agent topology slot (corpus provenance: §6.16, §15.18) — an agent occupying the "ground control" role itself is explicitly ruled out. The skill is the reader's instrument: it prepares the judgment artifact; the operator remains the reader; the artifact terminates in *presented for the operator's reading*, never self-certified. Per §15.18's Socratic-transcript amendment, the question is recorded verbatim before any ontology-building, so intent-correction stays distinguishable from intent-replacement. The judgment artifact is §15.17's staked-vs-laundered reading made material — belief-repair structure (believed / observed / where belief ends) is that reading applied to the harness's own map.

## The ratified decisions

- **Name:** `/ari-read` — the read-register entry doorway, sibling to `/ari-intake`. Skill roster 5 → 6.
- **Artifact:** `work/<slug>/judgment.md`, self-contained, written in stages — verbatim question recorded first, before intent confirmation or ontology-building. `/ari-read` mints the slug.
- **Gates:** GATE-QUERY (at the door — question recorded verbatim, intent confirmed without being staked for the asker; halts until confirmed) and GATE-MATCH (at the return — judgment checked against confirmed intent, then presented for the operator's reading; halts until read).
- **Tiling home:** canonical narrative in `PHILOSOPHY.md`; this doc is the design record only.

## Calibration target

The operator's idealized output to a superior: a natural-language question about the system produces either a natural-language answer, or a file that is itself an argument and a promise — "this honors what you requested." `/ari-read` exists to make that shape mechanical without pretending it is a search engine: it is a discipline the agent follows with ordinary reading tools, not retrieval machinery. No query/retrieval system is built or implied by this pin.
