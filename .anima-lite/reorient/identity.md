# Reorientation — anima-lite identity expansion

Captured: 2026-07-07. Status: **doc propagation done — git mv executed 2026-07-07.** Vocab review complete and ratified 2026-07-07 (see `vocab.md` in this directory: decisions 1a/2b/3b/4b/5a). Propagation into PHILOSOPHY.md, README.md, CLAUDE.md, HARNESS.md, ari-argue/SKILL.md, and ari-port/SKILL.md landed 2026-07-07 (PIN-25 item b). The `ports/`→`work/` directory rename (decision 2b) was executed 2026-07-07 once run5's staged git state resolved; disk is now `work/<slug>/`, noted as done at HARNESS.md §4's doc-ownership map. Incremental spine-maintenance design (PIN-25 item c) is still open.

Context: team feedback — greenfield/translation work alone isn't a compelling product; tech-debt solvency is. This doc records the identity shift that answers it, and the rulings that bound it.

---

## Identity

**Before:** argument-preserving feature port toolkit. Ports a feature proto→prod while preserving what it argues.

**After:** custodian of the alignment between what a codebase promises and what it actually is. An engineer's companion that detects divergence between promise and artifact, decomposes it into individually ratifiable decisions, and executes only what a human confirms. Porting was the first divergence-type it handled, not the identity.

The operator's craft shifts accordingly: the engineer is the claim court — yes/no/here's why — and the agent does everything that isn't judgment.

---

## The unifying claim: slop and debt are the same object

Slop is an unconfirmed claim-change wearing a substrate costume — the promise changed and nobody said so. Tech debt is the same divergence at a different timescale: code whose intent shifted with nobody re-ratifying, code the world drifted past while it still argues against an origin point that no longer exists, a promise whose *because* is lost. AI slop is promise/artifact divergence introduced in seconds by generation; debt is the same divergence introduced over years by drift. Different author — an LLM versus time — same object.

The janitor doesn't care who left the mess. Tech-debt solvency is therefore not a feature bolt-on; it is the same job description.

---

## What inverts

**The spine becomes the product, not the precondition.** Currently disposable input — regenerate per port, hash-check, move on. In the expanded identity, the spine IS the asset: docs provably current against code, code legible against its own stated argument. Janitoring is spine maintenance. The seed already exists — HARNESS.md's bidirectional-audit rule (every doc read is also an audit) is spine custody in embryo; it gets promoted from hygiene rule to core function. Consequence: spine maintenance must become incremental (update-on-change), not regenerate-on-demand — per-port re-probing doesn't scale to continuous custody. This is confirmed direction (ruling 3), and it is new machinery ari-map doesn't have yet.

**Port becomes one work-type among several.** Every work item is intent crossing a boundary into the repo: from a proto repo (port), from a meeting or email (intent translation), from the moving world (CVE, EOL, deprecation), from the ideal of well-made code (craft improvement). The harness invariant is unchanged: intent crosses the boundary and nothing else sneaks across with it.

---

## What stays invariant

Everything that makes the guardrails credible survives untouched: verified map before work; every promise-level decision surfaced to a human one at a time, never bundled; halt-and-ask over guess; conservative default; contract as inspectable receipt. The expansion is MORE conservative than the port tool, not less — the "what's wrong with this code" analysis now also arrives as decomposed, cited, individually ratifiable decisions rather than a monolithic "AI says refactor this."

---

## What's genuinely new: the diagnosis layer

Ports never needed diagnosis — the work item was handed in ("port this feature"). Debt work starts by finding and decomposing the divergence. The diagnostic taxonomy (provenance: anima-corps logic.md §8.6/§8.11 — four irreducible primitives; named debts are compositions, decompose before routing):

- **spec** — intent→code alignment broken: code faithfully implements an intent that has since changed
- **epistemic** — artifact→because alignment broken: it exists, nobody knows why
- **world-drift** — code→world alignment broken: security landscape, dependency EOL, platform deprecation moved past coherent code *(corpus calls this "substrate debt" — renamed here to avoid collision with anima-lite's substrate; see vocab review)*
- **craft** — intrinsic structure degraded (coupling, cohesion, accidental complexity) with every alignment intact

Named debts (security, performance, test, dependency, documentation) are compositions of these — decomposition is the first diagnostic move.

The two cuts do not compete. The four primitives answer *what kind of divergence is this* on the way in; the binary substrate/claim cut answers *may this fix change a promise* on the way out. Diagnosis is four-way; authorization stays binary. The existing gate survives and gains an upstream.

---

## Rulings (2026-07-07)

1. **Corpus-agnostic on agent structure.** anima-lite imports the diagnostic taxonomy from anima-corps logic §8 but NOT the corpus's agent-role routing (which primitive belongs to which named corpus agent). Those named roles carry epistemic obligations anima-lite is not claiming. anima-lite is a harness-only expression — skills, hooks, markdown — making no claim about the corpus's agent separation.
2. **Full vocab review before propagation.** The reorientation triggers a vocabulary audit across all docs and skills (scope below). No new-identity prose lands in canonical docs until vocabulary is settled.
3. **Incremental spine maintenance is the direction.** Continuous custody, update-on-change. Was already leaning this way; now confirmed as how it should be.

---

## Vocab review scope

Terms in tension, to be settled before any doc propagation:

| Term | Tension |
|---|---|
| **substrate** | anima-lite: medium, free to change. Corpus §8.4: code↔world debt — near-opposite. One renames. Provisional: keep anima-lite's substrate/claim (it's the authorization vocabulary, load-bearing in every contract); import the debt primitive as **world-drift** |
| **port** | skill name (ari-port), dir layout (`ports/<slug>/`), repo self-description ("port toolkit") — all narrower than the new identity. Rename vs. keep-as-one-work-type |
| **proto / prod** | spine labels assume a two-repo pairing; debt work is single-repo. Label scheme needs to generalize |
| **spine** | survives, promoted from precondition to product — docs must reflect the promotion |
| **contract / blip / claim** | likely survive unchanged; confirm each reads correctly under the wider identity |
| **slop / divergence / janitor / added intent / added cruft** | new terms in (talk vocabulary). Decide which become canonical doc language vs. stay presentation-layer |
| **anima-lite / ari-*** | does the name still describe the thing; low priority, decide last |

---

## What this does NOT change yet

*(Updated 2026-07-07 — doc propagation has since landed; see status line.)* Still pending: the `ports/`→`work/` git mv (sequenced after run5 state resolves); the diagnosis layer itself (not built — docs mark it ratified direction); incremental spine maintenance (PIN-25 item c, design open). Run5 proceeds under the port work-type unchanged. The canonical docs now carry the identity; this doc remains the record of the shift and its rulings.
