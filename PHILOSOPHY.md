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

Every spine also carries a fifth file, `scaffold.md` — but it is not a fifth cause added to this list. It's a coordinate backbone (`(scenario, path, step)`) that the material/formal/efficient cells above attach to, naming how a repo's process actually moves scenario-by-scenario rather than adding a new axis of what the repo is. See `ari-map/scaffold-spec.md` for the full schema.

The same lens applies one level up: the skill pipeline is the four-cause decomposition of "make a software change," where software is an argument. Intake supplies the final cause (what the change is for — telos sharpened, everything argued for; built as `/ari-intake`, PIN-27). Map supplies the material cause (the mapped codebase as matter). Argue supplies the formal cause (the contract as the change's essence — which claims, what promise). Port supplies the efficient cause (execution from the contract). The two levels nest without conflict: the spine is the four causes of the repo; the pipeline is the four causes of the change.

Naming carries the same asymmetry (ratified and executed 2026-07-07, PIN-26): argue and port were renamed to **ari-argue-rhetoric** and **ari-code-rhetoric** — formal cause makes the claim, efficient cause makes it real, and "rhetoric" is the shared root because both are where an argument is actively made or materialized. Intake and map stay bare: they surface facts (telos sharpened, spine read) rather than making an argument, so neither carries the name.

---

**The resolution — one sentence, sovereign.** Above the telos doc in authority sits `RESOLUTION.md`: a one-sentence sovereign description of the repo, ratified by the operator (PIN-33). The authority runs in one direction only — the sentence is ground truth, the code is fallible embodiment, `telos.md` is fallible commentary. "Live" here means continuously-checked accuracy, not frequent edits: the resolution is maximally ember, changing only by constitutional growth, and its accuracy is re-verified at every intake rather than assumed. A divergence at this layer is adjudicated, never smoothed over: **drift** names the work item or code as wrong (fix it, ordinary custodial work); **growth** names the sentence itself as needing to change, and growth is never bundled with the change that provoked it — a resolution edit is its own workstream, separate intake, separate commit, explicit operator ratification recorded in `RESOLUTION.md`'s own ratification line, with the provoking change blocked until the question resolves. The guard this exists to hold: never quietly edit the resolution to match code that drifted — that would launder drift as growth. Mechanically this lives as GATE-TELOS's apex layer (`.claude/skills/ari-intake/SKILL.md`), checked before the telos layer, one gate, two authority levels. anima-lite is the only repo with a `RESOLUTION.md` today; target repos getting their own is ratified direction, not yet built. The concept also generalizes beyond this repo — every repo could carry a one-sentence sovereign description above its own telos doc, a teleological-software claim in its own right — captured here as a paper-shaped direction, not built.

---

**The five fields — canonical home (PIN-34).** Every reconstruction and every change reasons from the same five fields, tiled once here so both registers can cite it instead of restating it:

1. **User intent** — the ask as asked, verbatim, then confirmed.
2. **Ratified intent** — the promise layer: `RESOLUTION.md` → spine `telos.md` → contracts → confirmed claims. What the system should be.
3. **Belief** — the map: spines and docs. Best-faith approximation of what and where we believe the system to be, including where those beliefs end — the confidence edge is part of the field. `/ari-map` authors belief, not truth.
4. **Reality** — live data: code as it sits, runtime behavior, the target repos. Always sampled, never held in full — which is why belief exists.
5. **The record** — the diachronic trail: git history, blips, `RESOLUTION.md`'s ratification line, done pins, the backlog ledger. Append-only fact of how the present came to be; not belief, not intent, not present state.

**Register flows.** The write register (`/ari-intake` → `/ari-map`/`/ari-argue-rhetoric` → `/ari-code-rhetoric`) spends belief to change reality and appends to the record. The read register (`/ari-read`) spends reality to repair belief and audits the record. Neither subsumes the other — a work item is a change or a question, never both at once.

**The generative check.** The five fields taken pairwise are not just a taxonomy — each divergence between two fields already names a piece of machinery this harness has, or is building:
- user intent × ratified intent — GATE-TELOS (does the ask conflict with what the repo is for?)
- belief × reality — GATE-HASH, stale-spine detection, blips (a blip is a belief edge hit mid-work)
- ratified intent × reality — drift or debt, the custodian's core object
- the record × everything — the compliance-vs-substance reading: did a gate actually get engaged, or just checked off? (`/ari-read`'s record question-shape is the first machinery built for this pairing)
- user intent × belief — reconstruction's ontology step: which parts of what we believe actually bear on what was asked

**Mode honesty.** Every work item enters through a declared register, never through an undeclared default underneath: an intent to change the repo enters via `/ari-intake`; a question about the repo enters via `/ari-read`. Each doorway names the fork explicitly and routes to the other rather than absorbing work that isn't its shape. Nothing enters unargued (intake's discipline); one level up, nothing enters unregistered.

---

**The spine self-corrects (PIN-37).** Belief × reality is a named divergence above (`GATE-HASH, stale-spine detection, blips`); this states the standing procedure for repairing it, so a future re-probe doesn't have to be re-litigated as its own design question the way PIN-23 was. `scaffold.md` follows the same comprehensive-by-intent, exactly-one-per-repo, refreshed-not-accreted discipline as the other four spine files (`telos`/`material`/`formal`/`efficient.md`) — the feature ledger stays the only accretive artifact in this family. Four parts:
1. **Detection.** Every spine rule and named finding carries a `lives-in: <path[s]>` tag (`ari-map/SKILL.md` Output) — a pointer to the file(s) that embody it, never a cached copy of the code itself. A diff touching a tagged path is a candidate stale rule, checkable by grep against the spine's `Commit:` hash — mechanical, not something a human has to notice and remember to flag.
2. **Judgment.** A flagged rule is a candidate, not a verdict — whether the change actually altered what's promised (stale) or left it standing (cosmetic) is a human/agent call, the same conservative-default posture as everywhere else in this harness. Detection does not auto-rewrite anything.
3. **Execution.** A full `/ari-map` re-run is still how a judged-stale rule actually gets re-probed and rewritten. But detection itself is no longer deferred to that re-run alone (PIN-40): `ari-code-rhetoric`'s own Step 2 now runs a reverse-index check inline, on every path it touches, against the `lives-in:` targets recorded across all ingested spines — logging any implicated promise straight into that step's blip (`Spine promise touched:`, `Severity: info`). This supersedes the standalone-script framing this section used to describe, not just still-defers it: the check is a real, built mechanism that fires during ordinary port/harness-change execution, not a future direction awaiting its own tooling. Incremental, per-section re-probing — driven by which `lives-in:` paths actually changed, replacing the full re-run itself — is still the direction PIN-25 ratified but not yet built; naming it here is not building it.
4. **Exclusion.** The spine stays a clean current-state snapshot — belief, not a diff. What changed and why is the record, and belongs in the commit message or the pin's Resolution field, never baked into the spine artifact itself. This is the belief/record split above, applied to the spine's own maintenance rather than restated as a separate rule.

---

**The operator role: the claim court.** The engineer is the claim court — yes, no, here's why. The agent does everything that isn't judgment.

---

**Conservative default.** When uncertain, preserve. A missed claim change is recoverable — visible, arguable, correctable. A silently changed claim is invisible until a user relies on the old promise and the system fails them.
