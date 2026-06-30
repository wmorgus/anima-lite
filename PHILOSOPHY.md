# anima-lite — the commitments

**Code is argument.** Not description of a system. A structure of promises to a user about what they can rely on.

---

**The cut: substrate vs. claim.**
Substrate — the medium. Changes freely. Library swap, rename, refactor — none touch the promise.
Claim — the argument itself. What the user relies on. Dropping a confirmation step: claim change. Relaxing a validation: claim change. Changing reversible to permanent: claim change.
When unsure which: ask whether a user who understood the feature's promise would notice a difference in the promise. If yes — claim.

---

**Why ports fail silently.** A port that changes the argument without noticing feels complete. Mechanics work, tests pass. The promise changed. Nobody flagged it. This is the failure mode anima-lite exists to prevent.

---

**The four causes are not decoration.** They're the actual axes along which repos differ — and the axes along which a port can fail:
- Material: what it's made of. Swappable without touching the argument.
- Formal: how it's organized. Where the pattern is inconsistent, ports go wrong.
- Efficient: what acts on it. Most often missing from docs; most likely to silently break a port.
- Final: what it's for. Everything else is oriented by this. If you don't know the telos, you can't sort substrate from claim.

---

**Conservative default.** When uncertain, preserve. A missed claim change is recoverable — visible, arguable, correctable. A silently changed claim is invisible until a user relies on the old promise and the system fails them.
