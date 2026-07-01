---
name: ari-map
description: Produces .anima-lite/spine-<label>/ — a four-file spine directory containing telos.md (coding-agent entry point) and three cause files (material, formal, efficient). Called by ari-lite before any port begins, and re-called whenever the precondition check below fails.
---

# ari-map

Spine-finding: probe a repo's material, formal, efficient, and final causes and write the result to a spine directory. The telos file is the coding-agent-facing entry point; the cause files are analytical reference for ari-argue and ari-port.

## Inputs

- Repo path and label (`proto` or `prod` — determines output directory name).
- The corresponding telos file if it already exists (`.anima-lite/spine-<label>/telos.md`) — read the `Commit:` field to determine refresh-vs-create.

## Preconditions

Invoke this skill when any of the following hold:

- `.anima-lite/spine-<label>/` does not exist yet.
- `telos.md`'s `Commit:` hash doesn't match current HEAD.
- A file outside the spine's declared module boundaries now imports into it (formal cause shifted).
- Build/CI config changed since the spine's `Commit:`.
- Caller or user flags the spine as wrong.

If none hold and a current spine directory exists, do not invoke — proceed directly to ari-argue.

## Active orientations

**Lite face.** The `formal.md` file is where the lite face does its work. Document inconsistencies between stated and actual patterns as named findings — "The README claims X; the actual code does Y" — not as hedges. Eliding an inconsistency is not neutrality; it misleads ari-argue's telos check and ari-port's substrate translations downstream.

**Scope fence.** This spine maps one repo only. Do not reference the other repo in the port pair, compare to the proto, or anticipate what ari-argue will find. Cross-repo comparison is ari-argue's job. Name what this repo does; leave what it means for the port to ari-argue.

## Process

Probe the repo and answer all four causes. Don't skip one because it seems obvious — obvious causes go stale silently.

**Material — what it's made of.** Languages, frameworks, data structures, schemas, key dependencies, state shape. Load-bearing parts only. Test: if this material were swapped for an equivalent, would the software still make the same argument?

**Formal — what pattern organizes it.** Layering, module boundaries, dominant design patterns, control flow, the shape of a typical change. Identify the actual pattern from what the code does, not what the README claims. Note where the pattern is inconsistently applied — those seams are where ports go wrong.

**Efficient — what acts on it.** CI/CD pipeline, branching model, build tooling, how changes get deployed. Most often missing from architecture docs; most likely to silently break a port.

**Final — what it's for (the telos).** Inferred backward from the other three, not a declared mission statement. State confidence and evidence. Where evidence conflicts or is thin, say so.

From the Final cause, derive **don't-contradict rules** — imperative constraints a coding agent must not violate. These are statements like "do not introduce X," "all Y must go through Z," "new entities require step A and step B." They are the telos translated into action constraints.

## Output

Write four files to `.anima-lite/spine-<label>/`:

---

**`telos.md`** — coding-agent entry point. Short. Imperative. This is what Cursor, Windsurf, Copilot, and Aider load first.

```markdown
# Telos: <repo-name> (<label>)
Commit: <short git hash of HEAD>
Confidence: <high|medium|low>
Refresh trigger: <the specific condition that should invalidate this spine>

## Purpose
<2-3 sentences: what this codebase exists to do, written as a decision constraint.
Not a mission statement — a constraint. New work either serves this purpose or contradicts it.>

## Don't contradict
- <imperative rule — what new code must not do, derived from the telos>
- <imperative rule>
- <imperative rule — 3-5 rules total. Concrete and checkable, not vague principles.>

## Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
```

---

**`material.md`** — analytical reference for ari-argue and ari-port.

```markdown
# Material: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)

<Languages, frameworks, data structures, schemas, key dependencies, state shape.
Load-bearing parts only. Organized for lookup, not for narrative reading.>
```

---

**`formal.md`** — analytical reference. The most important cause file for ari-port's substrate translations.

```markdown
# Formal: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)

<Architecture pattern, layering, module boundaries, dominant design patterns,
the shape of a typical change. Named inconsistencies as findings.>
```

---

**`efficient.md`** — analytical reference.

```markdown
# Efficient: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)

<CI/CD pipeline, branching model, build tooling, how changes get deployed.
How to verify a change works in this repo.>
```

---

Cap each cause file at ~50 lines. If you're exceeding that, you're over-promising precision. Cut to load-bearing facts.

## Escalation / Notes

Each spine directory is shared, repo-level state. Commit the full directory rather than gitignoring it. Merge conflicts on spine files are a legitimate signal that two sessions' mental models diverged — resolve by re-probing fresh, not by picking a side.

Both `spine-proto/` and `spine-prod/` must be current before ari-argue can run. ari-argue's contracts pin to the `Commit:` hash in `spine-proto/telos.md`.

On refresh, re-probe fully rather than patching — and note what changed versus the previous version.
