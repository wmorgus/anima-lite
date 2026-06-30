# anima-lite

Argument-preserving feature port toolkit for Claude Code.

Ports a feature from a prototype repo to a production repo while preserving what the feature *argues* — not just what it does. Code is a structure of promises to a user. Translation has to preserve the promises, not just the mechanics.

## Three skills

**`/ari-map`** — probe a repo and write a four-cause spine (material, formal, efficient, final). Run once for each repo in the port pair. Produces `spine-proto.md` and `spine-prod.md`. Must be current before anything else runs.

**`/ari-argue`** — read both spines plus the feature, identify what it's arguing, and classify every implementation detail as substrate (medium — translate freely) or claim (argument — requires explicit user confirmation). Produces a branch-scoped contract. One contract per feature.

**`/ari-port`** — translate substrate freely using the prod spine's formal cause as the guide, implement confirmed claim changes exactly as confirmed, log everything else as a blip. Halts back to ari-argue if the contract is actively contradicted by the real code.

## The key distinction

**Substrate** — the medium. Library swap, rename, file restructure, test framework. None of these change what the software promises.

**Claim** — the argument itself. Dropping a confirmation step, relaxing a validation, changing reversible to permanent. These change what the user relies on. Always confirmed explicitly, one at a time, never bundled.

## Artifacts

```
.anima-lite/
  spine-proto.md          # four-cause map of the prototype repo
  spine-prod.md           # four-cause map of the production repo
  contracts/<branch>.md   # feature contract, branch-scoped, frozen for session
  blips/<branch>.md       # translation log with contracting-failure self-audit
```

Spines are shared repo-level state — commit them. Refresh collisions across branches surface as merge conflicts (intentional signal). Contracts and blips are branch-scoped.

## Agent

`.claude/agents/ari-lite.md` defines the ari-lite agent — the face the toolkit wears. Three orientations always active: ari (telos-holding), builder (argument-aware), lite (philosophical audit / halt condition).

## Philosophy

See `PHILOSOPHY.md`.
