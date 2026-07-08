# anima-lite — GitHub Copilot instructions

Argument-preserving port toolkit. When helping with a feature port in this repo, apply these rules consistently.

## Core commitment

Code is a structure of promises to a user. Translation has to preserve the promises, not just the mechanics. A port that changes the argument without noticing feels complete — mechanics work, tests pass — but the promise changed. This is the failure mode.

## The fundamental cut

Every implementation detail is either **substrate** or **claim**.

**Substrate** — the medium. Translate freely: library swap, rename, file restructure, styling, colors, fonts, animation library, test framework. Wording is substrate only when the semantic register is unchanged — two phrasings of the same promise.

**Claim** — the argument itself. Requires explicit user confirmation before changing: dropping a confirmation step, relaxing a validation, removing a UI element the prototype had, changing reversible to permanent, changing who gets notified. When unsure: would a user who understood the feature's promise notice a difference in the promise? If yes — claim.

Three categories that consistently look like substrate but are not:

**Interaction model.** How the user physically moves through the feature — collapse/expand, auto-advance, one-at-a-time focus, toggle behavior. Classify interaction patterns as claims by default; only call them substrate if the specific pattern demonstrably doesn't affect the promise. When writing the contract, name the invariant the interaction enforces AND the sub-tasks — not just the sub-tasks. A contract that names only sub-tasks passes to ari-code-rhetoric without stating what they exist to enforce.

**Semantic register.** Register shift is a claim: endorsement → disclaimer, celebration → warning, brand confidence → liability caveat. Two different promises, not two phrasings of the same promise.

**Structural visual hierarchy.** Colors and fonts are substrate. Whether the primary metrics live in a prominent hero block versus a flat card grid is not — it reflects what the feature argues the user should feel is important. Confirm before flattening.

**Conservative default.** When uncertain, preserve. A missed claim change is recoverable. A silently changed claim is invisible until a user relies on the old promise and the system fails them.

## Workflow

Ports run in three phases. Each produces artifacts the next phase reads.

### Phase 1: ari-map
Run for each repo in the port pair. Produces `spine-proto/` and `spine-prod/` directories in `.anima-lite/`, each containing four files.

**`telos.md`** — coding-agent entry point. Carries the commit hash, the repo's purpose as a decision constraint, and don't-contradict rules (imperative constraints new code must not violate). Load this first.

**`material.md`**, **`formal.md`**, **`efficient.md`** — analytical reference depth for ari-argue-rhetoric and ari-code-rhetoric. The formal file is the primary guide for substrate translations. Both spine directories must be current (commit-hash matched in telos.md) before phase 2.

### Phase 2: ari-argue-rhetoric
Reads both telos files + both formal files + the feature. Identifies what the feature is arguing (not what it does — what it promises). Classifies every detail as substrate or claim. Confirms each claim change with the user one at a time, never bundled. Produces `.anima-lite/contracts/<branch-slug>.md`. Contract is frozen once phase 3 begins.

If a telos conflict is detected (the feature contradicts the prod telos's Purpose or don't-contradict rules): surface the conflict, name whether it's a telos error or scope creep, wait for explicit confirmation. Do not write the contract until acknowledged.

### Phase 3: ari-code-rhetoric
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

- One contract per feature. Multiple features on the same branch fine — each needs its own ari-argue-rhetoric pass.
- Claim changes: one at a time, never bundled.
- Never proceed past a missing or stale spine/contract without surfacing the problem to the user.
