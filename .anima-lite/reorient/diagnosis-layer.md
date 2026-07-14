# The diagnosis layer — spec stub

Captured: 2026-07-14. Status: **all five shaping questions ratified 2026-07-14; built same day as `.claude/skills/ari-diagnose/SKILL.md` (PIN-39).** Named as debt-work's candidate intake home since the identity reorientation (`identity.md`), explicitly left out of scope by both PIN-27 (ari-intake build) and PIN-26 (ripple build). Picked up now as PIN-39, after PIN-26 was shelved with a real ripple run mid-flight. Not yet dogfooded — no real divergence has been run through it end to end.

---

## What it names

Every other work-type starts with intent already legible: port's intent is sitting in the prototype's code, ripple's intent is authored from a meeting or ticket, harness-change's intent comes from a live design round. Debt-work has no such starting point — the whole job is finding and decomposing a divergence nobody has named yet. The diagnosis layer is the thing that turns "something's off here" into an argued intent ari-intake can actually process: which of the four primitives (`identity.md`) is present, and what specifically diverged.

- **spec** — intent→code alignment broken: code faithfully implements an intent that has since changed
- **epistemic** — artifact→because alignment broken: it exists, nobody knows why
- **world-drift** — code→world alignment broken: CVE, EOL, deprecation moved past coherent code
- **craft** — intrinsic structure degraded, every alignment intact

Named debts (security, performance, test, dependency, documentation) are compositions of these — decomposition is the first diagnostic move, not a fifth primitive.

`ari-intake/SKILL.md` currently honesty-gates this: if a debt-work item shows up, it says plainly the machinery isn't built and routes back to human judgment rather than fabricating a pass. This pin is what would close that gate for real.

## Ratified decisions (2026-07-14)

**1. Container — separate skill.** `/ari-diagnose`, upstream of `/ari-intake` for debt-work only (port/ripple/harness-change skip it, same as they skip nothing today). Bare name, no `-rhetoric` suffix — diagnosis surfaces a fact (which primitive, what evidence) rather than making an argument, same reasoning that kept intake and map bare (`PHILOSOPHY.md`).

**3. Output artifact — own committed artifact.** `work/<slug>/diagnosis.md`: divergence located, primitive(s) assigned, evidence cited. Debt-work's equivalent of port's prototype — something `/ari-intake` reads as a source, not something intake reasons into existence itself.

**4. Primitives are not independent — scan order is epistemic → spec → world-drift → craft.** Rejects treating the four as an unordered checklist. Corpus §8.12 leaves orthogonal-vs-ordered explicitly open ("unresolved... may not hold"); this ruling closes it for anima-lite's diagnosis layer specifically, on the operator's judgment that the causes relate to each other — ratified 2026-07-14. Reasoning, off the §1.12 chain (`because → intent → code ← world`): epistemic first (is the *because* even recoverable — without it, spec can't be judged against a real upstream), then spec (intent vs. code), then world-drift (code vs. world, orthogonal axis, checkable independent of the intent chain), then craft last (intrinsic — only meaningful once the relational three are cleared, so structural judgment isn't confounded by a relational failure wearing a craft costume).

**5. Evidence bar — per primitive.** No uniform citation rule. Each primitive's evidence bar gets specified on its own terms when the skill is built (world-drift's is already obviously strongest: external checkable record, CVE/EOL/deprecation notice; spec/epistemic need their own bar defined, likely weaker-but-still-cited).

Craft's bar is the hardest of the four to define, and the reason is structural, not just under-specification. The other three primitives each name a broken *relation* — spec is intent↔code, epistemic is artifact↔because, world-drift is code↔world. Craft is defined negatively instead: "intrinsic structure degraded, every alignment intact" — no relation failing, just structure. That's consistent with why decision 4 scans it last (a relational failure can wear a craft costume, so craft is only asserted once the other three are cleared) — but it also means craft has no natural "what would falsify this" citation shape the way world-drift has a CVE number.

Worth naming before the evidence bar gets written: the harness already leans on modularity discipline heavily elsewhere — the doc-ownership map (`HARNESS.md`), `lives-in:` as pointer-never-copy (`spine-self-correction.md`) — and never once calls it craft. It's justified as divergence-prevention (duplication manufactures the exact promise/artifact drift this custodian exists to fight), not as a coupling/cohesion virtue in its own right. anima-lite practices the discipline craft would formalize without having built craft's machinery yet. Whatever evidence bar gets written for craft should probably borrow from *that* internal practice (name the specific divergence a coupling/cohesion problem would eventually cause) rather than importing external code-quality metrics that have no relational grounding in this harness's own vocabulary.

**2. Entry point — operator-nominated and read-register handoff, both in scope; self-triggered scan out.** Ratified 2026-07-14. `/ari-diagnose` accepts two entry shapes: (a) operator-nominated — a pointer to a file/module, "diagnose this"; (b) `/ari-read` handoff — an honoring-question failure that already feeds "pin → debt-work intent" per `read-register.md` lands as a diagnosis-layer input, confirming/classifying what the read flagged. (c) self-triggered scan (diagnosis crawling a spine unprompted for drift) is explicitly out of PIN-39 — different scale of commitment (trigger cadence, cost model, false-positive tolerance, closer to continuous spine custody than work-item intake) and spins out to its own future pin if picked up.

## Not yet decided

All five questions are ratified as of 2026-07-14. Nothing below stub:1 is contractable yet — PIN-39 still needs scope named formally (in/out per the shaping-fields format) before it can move to stub:2.
