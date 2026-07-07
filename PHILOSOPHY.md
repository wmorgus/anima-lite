# anima-lite — the commitments

**Identity.** anima-lite is the custodian of the alignment between what a codebase promises and what it actually is. Porting a feature from a prototype repo to a production repo is one work-type this custody takes — the first one built, not the identity itself.

**Code is argument.** Not description of a system. A structure of promises to a user about what they can rely on.

---

**Divergence: the unifying claim.** AI slop and tech debt are the same object — an unratified promise/artifact divergence, differing only in author: an LLM introduces it in seconds; drift introduces it over years. Slop is a claim change wearing a substrate costume, discovered late. Debt is the same thing, discovered later. Naming both "divergence" is what lets one harness detect, decompose, and ratify either. ("Slop" and "janitor" are talk-vocabulary for this — useful color in conversation, not canonical terms; they don't carry defined meaning in this doc.)

---

**The cut: substrate vs. claim.**
Substrate — the medium. Changes freely. Library swap, rename, refactor — none touch the promise.
Claim — the argument itself. What the user relies on. Dropping a confirmation step: claim change. Relaxing a validation: claim change. Changing reversible to permanent: claim change.
When unsure which: ask whether a user who understood the feature's promise would notice a difference in the promise. If yes — claim.

*Disambiguation:* this substrate/claim cut is anima-lite's own — it answers "is this a promise-change." It is unrelated to, and unchanged by, the diagnosis layer below.

---

**Why ports fail silently.** A port that changes the argument without noticing feels complete. Mechanics work, tests pass. The promise changed. Nobody flagged it. This is the failure mode anima-lite exists to prevent. The harness enforces that classification happened and is well-formed — the blip format, the validation agent, the contracting-failure self-audit all check structure. What it cannot verify is that a substrate call wasn't a claim in disguise that an operator waved through; the machine checks form, the human checks honesty, which is why the gates are non-skippable.

---

**The diagnosis layer — ratified direction, not yet built.** Every work item is intent crossing a boundary into the repo: from a prototype (port), from a meeting or ticket (intent translation), from the moving world (a CVE, an EOL, a deprecation), from the ideal of well-made code (craft improvement). Diagnosing which kind of divergence is present decomposes into four irreducible primitives (provenance: anima-corps logic.md §8.6/§8.11):

- **spec** — intent→code alignment broken: code faithfully implements an intent that has since changed.
- **epistemic** — artifact→because alignment broken: it exists, nobody knows why.
- **world-drift** — code→world alignment broken: security landscape, dependency EOL, platform deprecation moved past coherent code. (Anima-corps logic.md §8.4 calls this "substrate debt"; renamed here to avoid collision with this doc's own substrate.)
- **craft** — intrinsic structure degraded (coupling, cohesion, accidental complexity), every alignment intact.

Named debts (security, performance, test, dependency, documentation) are compositions of these — decompose before routing. The two cuts don't compete: the four primitives answer *what kind of divergence is this* on the way in; the binary substrate/claim cut answers *may this fix change a promise* on the way out. Diagnosis is four-way; authorization stays binary.

This layer is direction the identity has ratified, not machinery the harness has. Today only the port work-type runs end to end.

---

**The four causes are not decoration.** They're the actual axes along which repos differ — and the axes along which a port can fail:
- Material: what it's made of. Swappable without touching the argument.
- Formal: how it's organized. Where the pattern is inconsistent, ports go wrong.
- Efficient: what acts on it. Most often missing from docs; most likely to silently break a port.
- Final: what it's for. Everything else is oriented by this. If you don't know the telos, you can't sort substrate from claim.

The same lens applies one level up: the skill pipeline is the four-cause decomposition of "make a software change," where software is an argument. Intake supplies the final cause (what the change is for — telos sharpened, everything argued for; built as `/ari-intake`, PIN-27). Map supplies the material cause (the mapped codebase as matter). Argue supplies the formal cause (the contract as the change's essence — which claims, what promise). Port supplies the efficient cause (execution from the contract). The two levels nest without conflict: the spine is the four causes of the repo; the pipeline is the four causes of the change.

---

**The resolution — one sentence, sovereign.** Above the telos doc in authority sits `RESOLUTION.md`: a one-sentence sovereign description of the repo, ratified by the operator (PIN-33). The authority runs in one direction only — the sentence is ground truth, the code is fallible embodiment, `telos.md` is fallible commentary. "Live" here means continuously-checked accuracy, not frequent edits: the resolution is maximally ember, changing only by constitutional growth, and its accuracy is re-verified at every intake rather than assumed. A divergence at this layer is adjudicated, never smoothed over: **drift** names the work item or code as wrong (fix it, ordinary custodial work); **growth** names the sentence itself as needing to change, and growth is never bundled with the change that provoked it — a resolution edit is its own workstream, separate intake, separate commit, explicit operator ratification recorded in `RESOLUTION.md`'s own ratification line, with the provoking change blocked until the question resolves. The guard this exists to hold: never quietly edit the resolution to match code that drifted — that would launder drift as growth. Mechanically this lives as GATE-TELOS's apex layer (`.claude/skills/ari-intake/SKILL.md`), checked before the telos layer, one gate, two authority levels. anima-lite is the only repo with a `RESOLUTION.md` today; target repos getting their own is ratified direction, not yet built. The concept also generalizes beyond this repo — every repo could carry a one-sentence sovereign description above its own telos doc, a teleological-software claim in its own right — captured here as a paper-shaped direction, not built.

---

**The operator role: the claim court.** The engineer is the claim court — yes, no, here's why. The agent does everything that isn't judgment.

---

**Conservative default.** When uncertain, preserve. A missed claim change is recoverable — visible, arguable, correctable. A silently changed claim is invisible until a user relies on the old promise and the system fails them.
