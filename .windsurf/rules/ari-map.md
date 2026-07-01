---
trigger: manual
description: Probe a repo and write a four-file spine directory (telos + material + formal + efficient). Run once for each repo in the port pair before ari-argue.
---

# ari-map

Spine-finding: probe a repo's four causes and write the result to `.anima-lite/spine-<label>/`. The telos file is the coding-agent-facing entry point; cause files are analytical reference for ari-argue and ari-port.

## Inputs

- Repo path and label (`proto` or `prod` — determines output directory).
- `.anima-lite/spine-<label>/telos.md` if it exists — read `Commit:` to determine refresh-vs-create.

## When to run

- `.anima-lite/spine-<label>/` does not exist yet.
- `telos.md`'s `Commit:` hash doesn't match current HEAD.
- A file outside the spine's declared module boundaries now imports into it.
- Build/CI config changed since the spine's `Commit:`.
- Caller or user flags the spine as wrong.

## Active orientations

**Lite face.** `formal.md` is where the lite face does its work. Document inconsistencies as named findings — "The README claims X; the actual code does Y." Eliding an inconsistency misleads ari-argue's telos check and ari-port's substrate translations.

**Scope fence.** This spine maps one repo only. Do not reference the other repo or anticipate what ari-argue will find. Cross-repo comparison is ari-argue's job.

## Process

Probe all four causes. Don't skip one because it seems obvious.

**Material — what it's made of.** Languages, frameworks, key dependencies. Load-bearing parts only.

**Formal — what pattern organizes it.** Layering, module boundaries, dominant patterns, control flow. Identify from what the code does, not what the README claims. Name inconsistencies as findings.

**Efficient — what acts on it.** CI/CD, build tooling, deploy. How to verify a change works.

**Final — what it's for (telos).** Inferred backward. State confidence and evidence. Derive don't-contradict rules: imperative constraints a coding agent must not violate.

## Output

Write four files to `.anima-lite/spine-<label>/`:

**`telos.md`** — coding-agent entry point. Short. Imperative.
```markdown
# Telos: <repo-name> (<label>)
Commit: <short git hash>
Confidence: <high|medium|low>
Refresh trigger: <condition>

## Purpose
<2-3 sentences: what this codebase exists to do, as a decision constraint>

## Don't contradict
- <3-5 imperative rules derived from telos — concrete and checkable>

## Cause files (reference depth)
- [material.md](material.md)
- [formal.md](formal.md)
- [efficient.md](efficient.md)

## Disclaimers
Telos is inferred, not declared.
```

**`material.md`**, **`formal.md`**, **`efficient.md`** — analytical reference, ~50 lines each.
```markdown
# <Cause>: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)
```

Commit the full directory. Both `spine-proto/` and `spine-prod/` must be current before ari-argue runs.
