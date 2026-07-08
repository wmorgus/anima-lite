---
trigger: manual
description: Translate the feature from proto to prod using spine and contract as binding context. Runs only after ari-map and ari-argue-rhetoric have produced current, hash-matched artifacts.
---

# ari-code-rhetoric

Execution: the hard epistemic work happened upstream — this should feel mechanical. If it feels ambiguous, the contract was incomplete.

## Inputs

- `.anima-lite/spine-proto.md` and `.anima-lite/spine-prod.md`
- `.anima-lite/contracts/<branch-slug>.md`
- The prototype code being translated

## Preconditions

1. Both spines exist and are current. If not: halt, run ari-map.
2. Contract exists, status is not "DRAFT," no unconfirmed Open Questions. If not: halt, run ari-argue-rhetoric.
3. Contract's `Spine commit:` matches `spine-proto.md`'s `Commit:`. If mismatched: surface the diff and ask whether the contract still holds — don't auto-fail or proceed silently.

## Active orientations

**Ari face (self-policing).** Every blip carries a `Contracting failure?` field. Each uncovered case is an occasion to ask whether the contract was incomplete. A blip that skips this question exempts the contracting phase from the quality sweep.

## Process

- **Substrate** — translate freely using the prod spine's formal cause as the guide.
- **Claim changes** — implement exactly per the contract's confirmed decision. Do not relitigate.
- **Uncovered cases** — log as blip, default conservative.
- **Contract contradicted** — halt. Write as `CONTRACT-BREAK`, report execution paused, re-run ari-argue-rhetoric with the specific contradiction.

## Output

Append to `.anima-lite/blips/<branch-slug>.md`:

```markdown
## Blip: <short title>
Severity: <info|review-suggested|CONTRACT-BREAK>
Location: <file:line>
What happened: <the decision>
Why: <reasoning>
Downstream consequence: <what this means going forward>
Contracting failure?: <what should have been in the contract — or "n/a">
```

At session end: summarize grouped by severity leading with `review-suggested`/`CONTRACT-BREAK`; state which claim changes were exercised.
