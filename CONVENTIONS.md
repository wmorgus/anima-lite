# anima-lite conventions

Argument-preserving port toolkit. Read this before helping with any feature port.

## What this is

Code is a structure of promises to a user. Translation has to preserve the promises, not just the mechanics. Most port failures are silent — the mechanics work, the argument changed, nobody noticed.

## The cut

Every implementation detail is **substrate** or **claim**.

**Substrate** — translate freely. Library swap, rename, file restructure, styling, test framework. Doesn't touch the promise.

**Claim** — explicit user confirmation required. Dropping a confirmation step, relaxing a validation, removing a UI element, changing reversible to permanent. When unsure: would a user who understood the feature's promise notice a difference in what it promises? Yes → claim.

**When uncertain: preserve.** A missed claim change is recoverable. A silently changed claim is invisible until someone relies on the old promise.

## Workflow

```
ari-map   → probe each repo, write spine-proto.md + spine-prod.md
ari-argue → read both spines + feature, classify details, confirm claim changes, write contract
ari-port  → translate substrate freely, implement confirmed claims exactly, log blips
```

### ari-map
Four-cause spine per repo: Material, Formal (including inconsistencies), Efficient, Final (inferred telos + evidence + confidence). Hash-pinned. Both must be current before ari-argue.

### ari-argue
Identifies what the feature argues (not does — argues). Classifies all details. Confirms claim changes one at a time, never bundled. Telos conflict with prod spine → surface, name it, wait for confirmation before proceeding. Produces `.anima-lite/contracts/<branch-slug>.md`.

### ari-port
Substrate: translate freely using prod spine's formal cause. Claims: implement exactly as confirmed. Uncovered cases: log as blip, default conservative. Contract contradicted (not just incomplete): halt, `CONTRACT-BREAK`, re-run ari-argue.

Blips go to `.anima-lite/blips/<branch-slug>.md`:
```
## Blip: <title>
Severity: info | review-suggested | CONTRACT-BREAK
Location: <file:line>
What happened: / Why: / Downstream consequence:
Contracting failure?: <what should have been in the contract, or "n/a">
```

## Artifacts

```
.anima-lite/spine-proto.md       committed, shared, commit-pinned
.anima-lite/spine-prod.md        committed, shared, commit-pinned
.anima-lite/contracts/<branch>   branch-scoped, frozen once port begins
.anima-lite/blips/<branch>       branch-scoped translation log
```

## Rules

- One contract per feature. Multiple features per branch fine — each gets its own contract.
- Claim changes: one at a time, never bundled.
- Never proceed with a missing or stale spine/contract without surfacing it.
- Spine refresh collisions = merge conflicts. Intentional. Resolve by re-probing, not by picking a side.
