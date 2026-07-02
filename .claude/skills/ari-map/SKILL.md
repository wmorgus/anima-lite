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

**Minimum probe before writing.** Spine files look authoritative regardless of probe depth — a shallow probe misleads ari-port's substrate decisions just as confidently as a deep one. Before writing any cause file, run these steps:

1. `find <repo> -type f | head -200` (or equivalent) — enumerate actual structure; don't infer from README
2. Per layer in the formal cause, read at least 2 representative files to confirm the pattern holds, not just the most prominent one
3. For any pattern claim in `formal.md`, grep to confirm it before asserting — e.g., if claiming "all servlets extend AbstractServlet," grep for `extends AbstractServlet` and count; if there are exceptions, name them as findings
4. For `material.md` library entries, grep package manifests, lock files, or vendor dirs for version strings — don't assert a version you haven't confirmed
5. If `.anima-lite/features/` exists, read any ledger files relevant to the current probe before writing `formal.md` and `telos.md`. Treat as soft reference — explicitly softer than the spine. Source is port-generated, not independently probed. Use ledger entries as pointers to confirm, not as authority to copy. If the probe confirms a ledger observation, it may graduate into the spine; if the probe contradicts it, the spine wins and the ledger entry was stale — note it as a finding.

**Parallel probe subagents (large repos).** After step 1 completes, assess scope: if the repo has >500 files or the probe would require reading >10 files per cause, spawn three parallel subagents — one per cause — rather than probing serially. For smaller repos, single-agent probe is fine.

Each subagent receives:
- The repo path
- The probe steps for its cause only (steps 2–3 for formal, step 4 for material, build/CI configs for efficient)
- This instruction: return structured findings with three fields — `confirmed` (what was verified in code), `unconfirmed` (what couldn't be pinned), `named_findings` (inconsistencies, gaps, or surprises worth carrying into the spine)

Subagent assignments:
- `probe:material` — grep manifests and lock files for versions; read package files; confirm dependency versions; return findings in the three-field format
- `probe:formal` — read representative files per layer; grep for pattern claims; confirm seam protocols; return findings
- `probe:efficient` — read build configs and CI workflow files; confirm targets and deploy paths; return findings

The main agent waits for all three, synthesizes the findings, then writes the four spine files and feature ledger stubs. The initial `find` enumeration (step 1) stays with the main agent — it determines scope before fanning out.

These steps don't need to be exhaustive. They need to be enough that each assertion in the output is code-derived, not plausible-from-memory.

Probe the repo and answer all four causes. Don't skip one because it seems obvious — obvious causes go stale silently.

**Material — what it's made of.** Languages, frameworks, data structures, schemas, key dependencies, state shape. Load-bearing parts only. Test: if this material were swapped for an equivalent, would the software still make the same argument?

**Formal — what pattern organizes it.** Layering, module boundaries, dominant design patterns, control flow, the shape of a typical change. Identify the actual pattern from what the code does, not what the README claims. Note where the pattern is inconsistently applied — those seams are where ports go wrong.

**Efficient — what acts on it.** CI/CD pipeline, branching model, build tooling, how changes get deployed. Most often missing from architecture docs; most likely to silently break a port.

**Final — what it's for (the telos).** Inferred backward from the other three, not a declared mission statement. State confidence and evidence. Where evidence conflicts or is thin, say so.

From the Final cause, derive **don't-contradict rules** — imperative constraints a coding agent must not violate. These are statements like "do not introduce X," "all Y must go through Z," "new entities require step A and step B." They are the telos translated into action constraints.

**Comprehensive feature map.** Attempt a comprehensive feature map — identify every user-facing feature in the repo, not just the ones tied to the current port. For each identified feature, create a stub in `.anima-lite/features/` at the deepest level the probe can confirm without over-claiming. "The feature exists and its entry point is X" is a valid `stub:1`. Do not require full-chain visibility before creating a stub; require only that every populated field was confirmed in code.

How to identify features: trace entry points (servlet URL mappings, route configs, JSP file inventory) and group them by user-facing function. A feature is a user-facing capability — not a utility, not a shared service. When in doubt whether something is a feature or infrastructure, ask: does a human user interact with this directly? If yes, it is a feature.

ari-map writes the stub. ari-port enriches it. Two sessions may touch the same file; the `stub:` header makes coverage state legible at a glance.

**The different-feature test.** Before writing any observation into a cause file, ask: would this be useful to an agent working on a different feature in the same repo? Yes → it belongs in the spine. No → it belongs in the contract or blips for the feature that surfaced it.

Pass example: "All servlets return AJAX responses wrapped in a `{status, data}` envelope" — true across the repo, useful to any port touching any servlet. Spine.

Fail example: "The monthly-report servlet returns an empty array when session count is below five" — true only of this feature's logic, useful only to this port. Contract.

When in doubt, keep it out. Wrong in a contract costs one feature; wrong in the spine misleads every future port.

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
Load-bearing parts only. Organized for lookup, not for narrative reading.

Version pin rule: every library or framework entry must include a version if one
is detectable (package.json, pom.xml, build.gradle, lock file, vendor dir, CDN
URL). Write "Bootstrap 4.x" not "Bootstrap". If version is genuinely undetectable,
write "Bootstrap (version unknown)" — an absent version is a gap, not a default.
Version strings matter at port time: syntax choices (e.g. data-toggle vs
data-bs-toggle) are version-specific and a reviewer cannot verify them without this.>
```

---

**`formal.md`** — analytical reference. The most important cause file for ari-port's substrate translations.

```markdown
# Formal: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)

<Architecture pattern, layering, module boundaries, dominant design patterns,
the shape of a typical change. Named inconsistencies as findings.

Provenance rule: tag each finding as (code-derived) or (README-stated).
- (code-derived): you grepped or read files and the pattern is confirmed in actual code
- (README-stated): the README or docs claim this; you have not verified it in code

ari-port treats formal.md as ground truth for substrate decisions. A README-stated
pattern that the code contradicts silently misdirects translations. The tag lets
ari-port and human reviewers know which claims need a verification pass before
acting on them.

Seam protocol rule: documenting that layers exist is not documenting what crosses
between them. A layer diagram without seam protocols is scaffolding — it names
boundaries but omits the load-bearing content a port must translate. For each
major layer boundary, state the communication protocol: the shape of data as it
crosses. Examples: servlet→JS (AJAX response envelope shape), JSP→browser
(static asset path conventions), Java→Hibernate (entity wiring requirements).
Where a seam exists but protocol could not be confirmed from code, say so as a
named gap — not a missing entry. A port that gets the layers right and the seam
wrong produces code that compiles and fails at the boundary.

Concrete example rule: the telos file's don't-contradict rules include "new X
requires..." checklists. Ground each such checklist here with one concrete
instantiation from the actual codebase — trace a real entity through every step
the checklist names, with file paths. The purpose is not to document that
feature; it is to make the pattern inspectable, so a future agent can verify
each step against a known-good example rather than trusting an abstract list.>
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

## Feature Ledger

Features live at `.anima-lite/features/<slug>.md` — at the anima-lite root, not under any repo spine. A cross-repo feature (a change spanning two webapps) has a natural home there; a single-repo feature declares its repo in the header. Spines do not contain features; spines reference them by slug.

The ledger is a different artifact from the spine. The spine answers "what is true repo-wide." The ledger answers "what is true about this one feature." The different-feature test is the boundary: an observation that passes the test lives in the spine; one that fails lives in the ledger.

Future mechanism (not required now): hash-controlled versioned copies per repo, so each port pins to the feature-doc version it used. Note the intent; do not build the versioning yet.

### Stub depth

ari-map creates a comprehensive feature map — every feature it can identify in the repo, stubbed as deep as it can decisively assert, no more. The failure mode is not the shallow stub. It is the dishonest stub: fields filled with assertions the agent cannot confirm. A shallow honest stub is a correct artifact; a deep dishonest one is a trap that reads as authority.

Stub levels (use these exact labels in the file header):
- `stub:0` — feature identified, existence confirmed, nothing else
- `stub:1` — entry point confirmed (URL mapping → servlet or equivalent)
- `stub:2` — entry point + primary data structure confirmed (DTO class + key fields)
- `stub:3` — full observable chain confirmed by ari-map probe, or enriched by ari-port

At `stub:3`, the `source:` field distinguishes probe-confirmed from port-distilled. A reader trusting a `stub:3` entry must check `source:` before treating it as probe-grade.

Every field not yet confirmed is written as `not traced` — never left blank. Blank reads as absence; `not traced` reads as unknown. The distinction is load-bearing.

### Feature ledger file template

`.anima-lite/features/<slug>.md`:

~~~markdown
# Feature: <feature name>
slug: <feature-slug>
repo(s): <repo slug, or comma-separated for cross-repo features>
stub: <0|1|2|3>
source: <ari-map-probe | ari-port-enriched | manual>
prod-commit: <short hash at time of population>
goes-stale: <one line — what would invalidate this, e.g. "DTO schema change, servlet rename">

## Identity
<one sentence — what this feature does for the user. not traced if unconfirmed.>

## Entry points
<URL mapping → servlet/controller → template path; confirmed from routing config.
 not traced if unconfirmed.>

## Primary data structure
<DTO or equivalent class + key fields observed. not traced if unconfirmed.>

---
Everything below is enriched by ari-port after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
<entry → service → data layer → entity chain, with class names. not traced.>

## Client-side wiring
<JS/TS files involved, render function names, data binding pattern. not traced.>

## State machine
<if a multi-step user flow: states and transitions. not traced or n/a.>

## Feature gates
<flags, conditions, admin-only guards — anything that conditions availability.
 not traced or none.>

## Seam-specific protocols
<communication patterns unique to this feature's boundaries. Repo-wide seam
 protocols live in the spine, not here. not traced.>

## Known quirks
<observations that surprised — not general patterns. Each entry names the
 contract or blip it was distilled from. not traced or none.>

## Port provenance
<contract slug + prod commit hash this enrichment was distilled from. n/a until
 first port.>
~~~

Field ownership:
- **ari-map** populates at probe time: all header fields, Identity, Entry points, Primary data structure, and status markers (`not traced` on all unconfirmed fields)
- **ari-port** enriches after a port run: Full data flow, Client-side wiring, State machine, Feature gates, Seam-specific protocols, Known quirks, Port provenance — and updates `stub:`, `source:`, and `prod-commit:` to reflect the enrichment

## Escalation / Notes

Each spine directory is shared, repo-level state. Commit the full directory rather than gitignoring it. Merge conflicts on spine files are a legitimate signal that two sessions' mental models diverged — resolve by re-probing fresh, not by picking a side.

Both `spine-proto/` and `spine-prod/` must be current before ari-argue can run. ari-argue's contracts pin to the `Commit:` hash in `spine-proto/telos.md`.

On refresh, re-probe fully rather than patching — and note what changed versus the previous version.
