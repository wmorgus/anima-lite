---
trigger: manual
description: Probe a repo and write a four-cause spine (material, formal, efficient, final). Run once for each repo in the port pair before ari-argue.
---

# ari-map

Spine-finding: probe a repo's material, formal, efficient, and final causes and write the result to a named spine file.

## Inputs

- Repo path and label (`proto` or `prod` — determines output filename).
- The corresponding spine file if it already exists — read to determine refresh-vs-create.

## When to run

- No spine file exists yet for this repo.
- The existing spine's `Commit:` hash doesn't match current HEAD.
- A file outside the spine's declared module boundaries now imports into it.
- Build/CI config changed since the spine's `Commit:`.
- Caller or user flags the spine as wrong.

## Active orientations

**Lite face.** Document inconsistencies between stated and actual patterns as named findings in the Formal section — "The README claims X; the actual code does Y" — not as hedges. Eliding an inconsistency misleads ari-argue's telos check and ari-port's substrate translations.

**Scope fence.** This spine maps one repo only. Do not reference the other repo in the port pair, compare to the proto, or anticipate what ari-argue will find. Cross-repo comparison is ari-argue's job. Name what this repo does; leave what it means for the port to ari-argue.

## Process

Probe the repo and answer all four causes. Don't skip one because it seems obvious.

**Material — what it's made of.** Languages, frameworks, data structures, schemas, key dependencies. Load-bearing parts only. Test: if this material were swapped for an equivalent, would the software still make the same argument?

**Formal — what pattern organizes it.** Layering, module boundaries, dominant design patterns, control flow. Identify the actual pattern from what the code does, not what the README claims. Note where it's inconsistently applied — those seams are where ports go wrong.

**Efficient — what acts on it.** CI/CD, branching model, review process, build tooling. Most often missing from docs; most likely to silently break a port.

**Final — what it's for.** The telos, inferred backward from the other three. State confidence and evidence explicitly. Where evidence conflicts or is thin, say so.

## Output

Write `.anima-lite/spine-<label>.md`:

```markdown
# Spine: <repo-name> (<label>)
Generated: <date>
Commit: <short git hash>
Confidence: <high|medium|low>
Refresh trigger: <the specific condition that should invalidate this spine>

## Material
## Formal
## Efficient
## Final
**Evidence:** <what you traced backward from>
**Confidence:** <high|medium|low>, with reasoning

## Disclaimers
This spine points in a direction. It is not a guarantee.
```

Cap at ~150 lines. Both `spine-proto.md` and `spine-prod.md` must be current before ari-argue runs.
