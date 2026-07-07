# Reorientation — the resolution

Captured 2026-07-07, built same day — canonical operative text is `RESOLUTION.md` + `.claude/skills/ari-intake/SKILL.md` GATE-TELOS apex layer; this doc is the design record. Tracked as PIN-33.

---

## What it names

Every repo the custodian works on has, implicitly, one final claim above all others: a one-sentence description of what the repo *is for*, sovereign over its own telos doc. anima-lite's telos.md and the four-cause spine describe the repo in detail; the resolution names it in one breath, at the top of the authority stack. It caps the identity work in `identity.md` and the four-cause frame in `four-causes.md`: the final cause has a final cause of its own.

**Authority inversion.** The sentence is ground truth. The code is fallible embodiment of it. `telos.md` is fallible commentary on it — stale-able, hash-checked, correctable. A mismatch between code and the resolution indicts the code or the workstream, never the sentence, by default. "Live" means continuously-checked accuracy, not frequent edits — the resolution is maximally ember: it changes only by constitutional growth, and every intake re-verifies its accuracy rather than assuming it.

## Ratified decisions (2026-07-07, operator round)

1. **Home.** The resolution lives in its own artifact at repo root, `RESOLUTION.md` — the sentence plus a ratification line (date + operator), nothing else. Smallest file, highest authority; other docs cite it, never restate it. anima-lite only for now — target repos getting one is future work, not built.
2. **Text.** anima-lite's resolution sentence: "agentic harness using aristotelean decomposition to build software that admits change only as argument." States an enforced property (nothing enters the pipeline unargued), not an aspiration.
3. **Mechanism.** The per-intake terminal check — does the repo this change produces still answer to the resolution? — folds into GATE-TELOS as its apex layer: ari-intake reads `RESOLUTION.md` first, then `telos.md`. One gate, two authority layers; no new gate ID. Bootstrap posture: if the target repo has no `RESOLUTION.md`, the apex layer is recorded absent, never fabricated.
4. **Adjudication (constitutional).** A resolution-layer failure is named **drift** (the change/code is wrong — fix it, ordinary custodial work) or **growth** (the resolution itself must change). Growth is never bundled: a resolution edit is its own workstream — separate intake, separate commit, explicit operator ratification recorded in `RESOLUTION.md`'s ratification line — and the change that provoked the divergence stays blocked until the resolution question resolves.

## The guard

Founder-exemption trap shape: the risk isn't that the resolution is wrong, it's that the sentence gets quietly rewritten to match whatever the code has already drifted into — laundering drift as growth so no one has to fix anything. The adjudication fork exists specifically to block that move: growth requires its own workstream and explicit operator ratification, on the record, every time. A silent `RESOLUTION.md` edit is never a valid outcome of ordinary work.

## Capture-only: generalization / paper-shaped claim

The resolution concept generalizes beyond anima-lite — every repo could carry a one-sentence sovereign description above its own telos doc. This is a teleological-software claim: recorded here and in `PHILOSOPHY.md` as ratified direction, not built. No machinery for other repos exists yet; `ari-map` does not emit a `RESOLUTION.md` template, and no target repo has one.
