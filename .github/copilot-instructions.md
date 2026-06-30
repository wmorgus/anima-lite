# anima-lite — GitHub Copilot instructions

Argument-preserving port toolkit. When helping with a feature port in this repo, apply these rules consistently.

## Core commitment

Code is a structure of promises to a user. Translation has to preserve the promises, not just the mechanics. A port that changes the argument without noticing feels complete — mechanics work, tests pass — but the promise changed. This is the failure mode.

## The fundamental cut

Every implementation detail is either **substrate** or **claim**.

**Substrate** — the medium. Translate freely: library swap, rename, file restructure, styling, test framework, error message wording (not its existence). These don't change what the software promises.

**Claim** — the argument itself. Requires explicit user confirmation before changing: dropping a confirmation step, relaxing a validation, removing a UI element the prototype had, changing reversible to permanent, changing who gets notified. When unsure: would a user who understood the feature's promise notice a difference in the promise? If yes — claim.

**Conservative default.** When uncertain, preserve. A missed claim change is recoverable. A silently changed claim is invisible until a user relies on the old promise and the system fails them.

## Workflow

Ports run in three phases. Each produces artifacts the next phase reads.

### Phase 1: ari-map
Run for each repo in the port pair. Produces `spine-proto.md` and `spine-prod.md` in `.anima-lite/`.

Each spine is a four-cause map: **Material** (what it's made of), **Formal** (the architecture pattern — including where it's inconsistently applied), **Efficient** (build/CI/deploy), **Final** (inferred telos with evidence and confidence). Both spines must be current (commit-hash matched) before phase 2.

### Phase 2: ari-argue
Reads both spines + the feature. Identifies what the feature is arguing (not what it does — what it promises). Classifies every detail as substrate or claim. Confirms each claim change with the user one at a time, never bundled. Produces `.anima-lite/contracts/<branch-slug>.md`. Contract is frozen once phase 3 begins.

If a telos conflict is detected (the feature contradicts the prod spine's final cause): surface the conflict, name whether it's a telos error or scope creep, wait for explicit confirmation. Do not write the contract until acknowledged.

### Phase 3: ari-port
Translates substrate freely using the prod spine's formal cause as the guide. Implements confirmed claim changes exactly as confirmed. Logs anything not covered by the contract as a blip in `.anima-lite/blips/<branch-slug>.md`. Halts if the contract is actively contradicted by the real code — that's a `CONTRACT-BREAK`, not a blip.

**Blip format:**
```
## Blip: <title>
Severity: info|review-suggested|CONTRACT-BREAK
Location: <file:line>
What happened / Why / Downstream consequence
Contracting failure?: <what should have been in the contract — or "n/a">
```

## Artifacts

```
.anima-lite/
  spine-proto.md          # four-cause map of the prototype repo (shared, commit-pinned)
  spine-prod.md           # four-cause map of the production repo (shared, commit-pinned)
  contracts/<branch>.md   # feature contract (branch-scoped, frozen for session)
  blips/<branch>.md       # translation log with self-audit
```

Spines are committed to the repo. Refresh collisions across branches = merge conflicts (intentional).

## Rules

- One contract per feature. Multiple features on the same branch fine — each needs its own ari-argue pass.
- Claim changes: one at a time, never bundled.
- Never proceed past a missing or stale spine/contract without surfacing the problem to the user.
