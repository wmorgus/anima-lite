---
trigger: manual
description: Read both spines and the feature, classify every detail as substrate or claim, confirm claim changes with the user, write a branch-scoped contract.
---

# ari-argue

Argumentation: determine what a feature is claiming to the user, separate from how it happens to be implemented, and get the human to confirm anything that would change if the claim itself moved.

## Inputs

- `.anima-lite/spine-proto.md` and `.anima-lite/spine-prod.md` (both must be current — if either is missing or stale, run ari-map first).
- The feature/diff/branch being ported.
- Current git branch name.

## Active orientations

**Ari face.** Check the feature's argument against the prod spine's final cause before classifying anything. A feature that contradicts the prod telos is a routing question (scope creep vs. telos error), not a classification question.

**Builder face.** Substrate vs. claim is determined by whether the user's understanding of what the feature promises would change — not "does this look different" but "does this promise different."

## Process

**1. Read both spines.** If a telos conflict is detected: present the conflict, name whether it's a telos error or scope creep, wait for explicit confirmation. Do not write the contract until acknowledged.

**2. Identify the argument.** What promise is this feature establishing with the user — not what it does mechanically.

**3. Classify every detail.** Substrate (free to translate): widget library swap, renaming, file restructuring, styling, colors, fonts, animation library. Wording is substrate only when the semantic register is unchanged. Claim (requires confirmation): removing a UI element, dropping a confirmation step, relaxing validation, changing reversible to permanent. Three categories that consistently look like substrate but are not:

**Interaction model.** How the user physically moves through the feature — collapse/expand, auto-advance, one-at-a-time focus, toggle behavior. Classify interaction patterns as claims by default.

**Semantic register.** Register shift is a claim: endorsement → disclaimer, celebration → warning, brand confidence → liability caveat. Two different promises, not two phrasings.

**Structural visual hierarchy.** Colors are substrate; whether primary metrics live in a hero block versus a flat grid is not — it reflects the feature's argument about what matters. Confirm before flattening.

When ambiguous, escalate to step 4.

**4. Confirm every claim change with the user.** One at a time, never bundled. If the user is unreachable, default to preserving the claim — never silently resolve ambiguity.

## Output

Write `.anima-lite/contracts/<branch-slug>.md`:

```markdown
# Contract: <feature-name>
Branch: <branch-slug>
Generated: <date>
Spine commit: <Commit: hash from spine-proto.md>
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue

## The argument
## Substrate changes (free to translate)
- <detail> — <why this is medium, not claim>
## Claim changes (confirmed with user)
- <detail> — Decision: <preserve|change-to-X> — Confirmed: <yes/default-preserve, with date>
## Open questions
<ari-port must halt and escalate if it hits these>
```

Once written with no open questions, the contract is frozen for the session.
