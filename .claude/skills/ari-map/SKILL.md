---
name: ari-map
description: Produces .anima-lite/spine.md, a four-cause map (material, formal, efficient, final) of the repo being ported from. Called by ari-lite before any port begins, and re-called whenever the precondition check below fails. Output is a fallible, commit-pinned orientation artifact — it points in a direction, it does not guarantee architectural truth.
---

# ari-map

Spine-finding: probe a repo's material, formal, efficient, and final causes and write the result to a single shared artifact other skills read before doing anything else.

## Inputs

- Repo path and label (`proto` or `prod` — determines output filename).
- The corresponding spine file if it already exists (`.anima-lite/spine-proto.md` or `.anima-lite/spine-prod.md`) — read to determine refresh-vs-create.

## Preconditions

Invoke this skill when any of the following hold:

- No spine file exists yet for this repo (`spine-proto.md` or `spine-prod.md` depending on label).
- The existing spine's `Commit:` hash doesn't match current HEAD.
- A file outside the spine's declared module boundaries now imports into it (formal cause violation — the architecture moved).
- Build/CI config changed since the spine's `Commit:`.
- Caller or user flags the spine as wrong.

If none hold and a current spine exists, do not invoke — the caller should proceed directly to ari-argue with the existing spine.

## Active orientations

**Lite face.** The Formal section is where the lite face does its work. Document inconsistencies between stated and actual patterns as named findings — "The README claims X; the actual code does Y" — not as hedges or qualifications. Eliding an inconsistency is not neutrality; it is omission that will mislead ari-argue's telos check and ari-port's substrate translations downstream.

## Process

Probe the repo and answer all four causes. Don't skip one because it seems obvious — obvious causes are exactly the ones that go stale silently.

**Material — what it's made of.** Languages, frameworks, data structures, schemas, key dependencies, state shape. Load-bearing parts only, not a full dependency tree. Test: if this material were swapped for an equivalent, would the software still make the same argument? (Postgres→MySQL is material; relational→document may be formal, since it changes what relationships are easy or hard to express.)

**Formal — what pattern organizes it.** Layering, module boundaries, dominant design pattern(s), control flow, the shape of a typical change. Identify the repo's actual pattern from what the code does, not its aspirational pattern from what the README claims. Note where the pattern is inconsistently applied — those seams are where ports go wrong.

**Efficient — what acts on it.** CI/CD pipeline, branching model, what/who reviews changes, build tooling, how prototypes here normally graduate to prod. Most often missing from architecture docs, most likely to silently break a port: correct material and formal causes with wrong efficient-cause assumptions fail in ways that look unrelated to the port itself.

**Final — what it's for.** The telos, inferred backward from the other three, not a declared mission statement. State confidence and evidence explicitly. Evidence sources: routing/entry points, surviving comments and naming, test names and what they assert is "correct," what gets the most defensive code (a proxy for what the authors feared breaking). Where evidence conflicts or is thin, say so — low-confidence is more useful than confidently wrong.

## Output

Write `.anima-lite/spine-<label>.md` (where `<label>` is `proto` or `prod`):

```markdown
# Spine: <repo-name> (<label>)
Generated: <date>
Commit: <short git hash of HEAD when this spine was generated>
Confidence: <high|medium|low>
Refresh trigger: <the specific condition that should invalidate this spine>

## Material
<what it's made of>

## Formal
<the pattern, including where it's inconsistently applied>

## Efficient
<what builds/tests/deploys it>

## Final
<inferred telos>
**Evidence:** <what you traced backward from>
**Confidence:** <high|medium|low>, with reasoning

## Disclaimers
This spine points in a direction. It is not a guarantee. Treat any claim
here that materially affects a port decision as worth a quick verification
pass against the actual code, not as settled fact.
```

Cap content at ~150 lines. If you're exceeding that, you're over-promising precision this skill isn't built to deliver — cut to load-bearing facts and flag the rest as "not traced, low relevance."

## Escalation / Notes

Each spine file is shared, repo-level state. Commit both to the repo rather than gitignoring them. If two branches regenerate a spine independently, the resulting merge conflict is a legitimate signal that two sessions' mental models diverged — resolve by re-probing fresh against current HEAD, not by picking one side.

Both `spine-proto.md` and `spine-prod.md` must be current before ari-argue can run. Because ari-argue's contracts pin to a specific spine `Commit:` hash, a spine refresh doesn't silently invalidate other branches' contracts — their next ari-port run detects the hash mismatch and flags it for review.

If staleness fires, re-run the full probe rather than patching the old file, and diff the new spine against the old one in your output so the change is visible.
