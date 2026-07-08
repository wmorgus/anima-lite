---
name: ari-map
description: Produces .anima-lite/spine-<label>/ — a four-file spine directory containing telos.md (coding-agent entry point) and three cause files (material, formal, efficient). Called by ari-lite before any port begins, and re-called whenever the precondition check below fails.
---

# ari-map

Spine-finding: probe a repo's material, formal, efficient, and final causes and write the result to a spine directory. The telos file is the coding-agent-facing entry point; the cause files are analytical reference for ari-argue-rhetoric and ari-code-rhetoric.

## Inputs

- Repo path and label (any slug — determines output directory name; `proto` and `prod` are conventional for port pairs, but arbitrary labels like `anima-lite` are valid).
- The corresponding telos file if it already exists (`.anima-lite/spine-<label>/telos.md`) — read the `Commit:` field to determine refresh-vs-create.

## Preconditions

Invoke this skill when any of the following hold:

- `.anima-lite/spine-<label>/` does not exist yet.
- `telos.md`'s `Commit:` hash doesn't match current HEAD.
- A file outside the spine's declared module boundaries now imports into it (formal cause shifted).
- Build/CI config changed since the spine's `Commit:`.
- Caller or user flags the spine as wrong.

If none hold and a current spine directory exists, do not invoke — proceed directly to ari-argue-rhetoric.

## Active orientations

**Lite face.** The `formal.md` file is where the lite face does its work. Document inconsistencies between stated and actual patterns as named findings — "The README claims X; the actual code does Y" — not as hedges. Eliding an inconsistency is not neutrality; it misleads ari-argue-rhetoric's telos check and ari-code-rhetoric's substrate translations downstream.

**Scope fence.** This spine maps one repo only. Do not reference the other repo in the port pair, compare to the proto, or anticipate what ari-argue-rhetoric will find. Cross-repo comparison is ari-argue-rhetoric's job. Name what this repo does; leave what it means for the port to ari-argue-rhetoric.

**Bidirectional audit.** Reading a prior spine (the refresh case) or a feature-ledger entry (during a probe) is also an audit of that artifact, not just a source to build on. Drift runs both directions: the artifact may be stale (reality moved since it was written) or it may have been wrong at write time (a probe or classification error that predates any code change). Never silently correct drift into the new spine — name it as a finding with the direction stated, e.g. "formal.md previously claimed X; code now shows Y (stale)" versus "formal.md claimed X; grep shows this was never true (wrong at write time)." Process step 6's ledger rule ("if the probe contradicts it, the spine wins and the ledger entry was stale — note it as a finding") is one instance of this orientation, applied to the spine/ledger pair; this generalizes it to any upstream artifact a probe touches.

## Process

**Minimum probe before writing.** Spine files look authoritative regardless of probe depth — a shallow probe misleads ari-code-rhetoric's substrate decisions just as confidently as a deep one. Before writing any cause file, run these steps:

1. `find <repo> -type f | head -200` (or equivalent) — enumerate actual structure; don't infer from README
2. Per layer in the formal cause, read at least 2 representative files to confirm the pattern holds, not just the most prominent one
3. For any pattern claim in `formal.md`, grep to confirm it before asserting — e.g., if claiming "all servlets extend AbstractServlet," grep for `extends AbstractServlet` and count; if there are exceptions, name them as findings
4. For `material.md` library entries, grep package manifests, lock files, or vendor dirs for version strings — don't assert a version you haven't confirmed
5. For entities in the neighborhood of identified features (not all entities in the repo), enumerate fields and FKs by reading the entity/mapping pairs (e.g. `*Item.java` / `*.hbm.xml`) — this is what populates material.md §7's inventory table. Also enumerate the enums directory (e.g. `enums/`) as domain vocabulary for §9 — an enum class is a closed, code-derived list of what a noun can be, and belongs in the glossary rather than being re-derived per port.
6. If `.anima-lite/features/` exists, read any ledger files relevant to the current probe before writing `formal.md` and `telos.md`. Treat as soft reference — explicitly softer than the spine. Source is port-generated, not independently probed. Use ledger entries as pointers to confirm, not as authority to copy. If the probe confirms a ledger observation, it may graduate into the spine; if the probe contradicts it, the spine wins and the ledger entry was stale — note it as a finding.

**Parallel probe subagents (large repos).** After step 1 completes, assess scope: if the repo has >500 files or the probe would require reading >10 files per cause, spawn three parallel subagents — one per cause — rather than probing serially. For smaller repos, single-agent probe is fine.

Each subagent receives:
- The repo path
- The probe steps for its cause only (steps 2–3 for formal, steps 4–5 for material, build/CI configs for efficient)
- The tentative telos inferred by the main agent before fanning out
- This instruction: return structured findings with four fields — `confirmed` (what was verified in code), `unconfirmed` (what couldn't be pinned), `named_findings` (inconsistencies, gaps, or surprises worth carrying into the spine), `skeptical_findings` (things that looked off while doing the primary probe — see below)

Subagent assignments:

- `probe:material` — grep manifests and lock files for versions; read package files; confirm dependency versions; for entities in the neighborhood of identified features, read entity/mapping pairs to populate the §7 field/FK inventory and enumerate the enums directory for the §9 vocabulary glossary; return findings in the four-field format. **Skeptical read (secondary):** flag any version entry that looks like a timed fact rather than a stable syntax pin — EOL claims, security advisory status, and deprecation judgments expire at the source and must not be frozen into the spine. Flag any dependency that appears in the code but not in the manifest, or vice versa. The skeptical read is free because the subagent is already reading.

- `probe:formal` — read representative files per layer; grep for pattern claims; confirm seam protocols; return findings. **Skeptical read (secondary):** flag any place where the actual code contradicts what the spine currently says (if a prior spine exists), or any internal inconsistency in the patterns found (e.g., "9 servlets extend AbstractServlet, 27 extend HttpServlet directly" — the inconsistency itself is a finding, not just the count). The skeptical read is free because the subagent is already reading.

- `probe:efficient` — read build configs and CI workflow files; confirm targets and deploy paths; return findings. **Skeptical read (secondary):** flag any hidden build dependency or surprising constraint found — a compile-time blocker not mentioned in the README, a CI check that runs on conditions not obvious from the config, an implicit environment assumption baked into a target. The skeptical read is free because the subagent is already reading.

Skeptical findings from all three subagents surface as named findings in the relevant cause file (`named_findings`) or as notes in the appropriate section. They are not a separate output artifact — they are part of the same structured return.

The main agent waits for all three, synthesizes the findings, then writes the four spine files and feature ledger stubs. The initial `find` enumeration (step 1) stays with the main agent — it determines scope before fanning out.

These steps don't need to be exhaustive. They need to be enough that each assertion in the output is code-derived, not plausible-from-memory.

Probe the repo and answer all four causes. Don't skip one because it seems obvious — obvious causes go stale silently.

**Final — what it's for (the telos).** Probe this first. Final cause is not a peer in a flat list — it is the frame that makes the other three legible. Begin by reading high-signal evidence: entry points (what URLs/routes exist and what they serve), naming conventions, and what code gets the most defensive handling (comments, null-guards, retry logic, test coverage — a proxy for what the authors feared breaking). From this, state an initial telos tentatively. Then probe Material, Formal, and Efficient through that lens — not just "what patterns exist" but "which patterns are load-bearing for the inferred telos, and which are incidental?" After those three probes, revisit and refine the Final cause; evidence from the probe may sharpen or correct the initial inference. State confidence and evidence. Where evidence conflicts or is thin, say so.

From the Final cause, derive **don't-contradict rules** — imperative constraints a coding agent must not violate. These are statements like "do not introduce X," "all Y must go through Z," "new entities require step A and step B." They are the telos translated into action constraints.

**Material — what it's made of.** Languages, frameworks, data structures, schemas, key dependencies, state shape. Load-bearing parts only. Probe through the telos lens: which dependencies are load-bearing for what the software argues, and which are incidental choices? Test: if this material were swapped for an equivalent, would the software still make the same argument?

**Formal — what pattern organizes it.** Layering, module boundaries, dominant design patterns, control flow, the shape of a typical change. Probe through the telos lens: a formal pattern only earns a spot in formal.md once you can say how it serves or contradicts the telos. Identify the actual pattern from what the code does, not what the README claims. Note where the pattern is inconsistently applied — those seams are where ports go wrong.

**Efficient — what acts on it.** CI/CD pipeline, branching model, build tooling, how changes get deployed. Probe through the telos lens: which build constraints protect the telos's load-bearing paths? Most often missing from architecture docs; most likely to silently break a port.

**Comprehensive feature map.** Attempt a comprehensive feature map — identify every user-facing feature in the repo, not just the ones tied to the current port. For each identified feature, create a stub in `.anima-lite/features/` at the deepest level the probe can confirm without over-claiming. "The feature exists and its entry point is X" is a valid `stub:1`. Do not require full-chain visibility before creating a stub; require only that every populated field was confirmed in code.

**Domain-central features go to stub:2 at map-time.** For features built on domain-central entities — recurring nouns that show up across the repo (sessions, students, institutions, and similar) — probe to `stub:2` (entry point + primary data structure + key fields, per ledger-spec.md), not `stub:1`. Stopping at stub:1 for these defers field-depth to ari-code-rhetoric, which runs after the contract freezes — too late for ari-argue-rhetoric to catch a claim built on a field that doesn't exist. The ledger is uncapped and per-feature, so it absorbs this field-level volume without pressuring the cause-file cap. This does not relax the honest-stub rule: populate `Primary data structure` at stub:2 only with fields the probe actually confirmed — a dishonest stub:2 is worse than an honest stub:1.

How to identify features: trace entry points (servlet URL mappings, route configs, JSP file inventory) and group them by user-facing function. A feature is a user-facing capability — not a utility, not a shared service. When in doubt whether something is a feature or infrastructure, ask: does a human user interact with this directly? If yes, it is a feature.

ari-map writes the stub. ari-code-rhetoric enriches it. Two sessions may touch the same file; the `stub:` header makes coverage state legible at a glance.

**The different-feature test.** Before writing any observation into a cause file, ask: would this be useful to an agent working on a different feature in the same repo? Yes → it belongs in the spine. No → it belongs in the contract or blips for the feature that surfaced it.

Pass example: "All servlets return AJAX responses wrapped in a `{status, data}` envelope" — true across the repo, useful to any port touching any servlet. Spine.

Fail example: "The monthly-report servlet returns an empty array when session count is below five" — true only of this feature's logic, useful only to this port. Contract.

When in doubt, keep it out. Wrong in a contract costs one feature; wrong in the spine misleads every future port.

## Output

Write four files to `.anima-lite/spine-<label>/`. Section numbers make spine findings citable by ari-argue-rhetoric and ari-code-rhetoric — cite the section, not just the file.

---

**`telos.md`** — coding-agent entry point. Short. Imperative. This is what Cursor, Windsurf, Copilot, and Aider load first. Probed first tentatively (from entry points, naming, and defensive-handling signals), then refined after Material, Formal, and Efficient are probed.

```markdown
# Telos: <repo-name> (<label>)
Commit: <short git hash of HEAD>
Confidence: <high|medium|low>
Refresh trigger: <the specific condition that should invalidate this spine>

## §1 Purpose
<2-3 sentences: what this codebase exists to do, written as a decision constraint.
Not a mission statement — a constraint. New work either serves this purpose or contradicts it.>

## §2 Don't contradict
- <imperative rule — what new code must not do, derived from the telos> `lives-in: <path[s] that enforce this rule>`
- <imperative rule> `lives-in: <path[s]>`
- <imperative rule — 3-5 rules total. Concrete and checkable, not vague principles.> `lives-in: <path[s]>`

## §3 Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## §4 Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
```

---

**`material.md`** — analytical reference for ari-argue-rhetoric and ari-code-rhetoric.

```markdown
# Material: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Languages
## §2 Backend frameworks
## §3 Frontend libraries
## §4 Key dependencies
## §5 Data structures / schemas
## §6 State shape

<Languages, frameworks, data structures, schemas, key dependencies, state shape.
Load-bearing parts only. Organized for lookup, not for narrative reading.

Version pin rule: every library or framework entry must include a version if one
is detectable (package.json, pom.xml, build.gradle, lock file, vendor dir, CDN
URL). Write "Bootstrap 4.x" not "Bootstrap". If version is genuinely undetectable,
write "Bootstrap (version unknown)" — an absent version is a gap, not a default.
Version strings matter at port time: syntax choices (e.g. data-toggle vs
data-bs-toggle) are version-specific and a reviewer cannot verify them without this.
Version pins (e.g. "Bootstrap 4.1.3", "jQuery 3.5.1") are stable spine facts —
correct at probe time and relevant for syntax decisions. EOL status, advisory status,
and security currency are timed facts: they expire at the source and must not be
frozen into the spine. For these, record where to check (the project's dependency
manifest, the upstream advisory feed) rather than a judgment that will silently go stale.>

## §7 Entity/field inventory

| entity | backing table | key fields | FKs | notes |
|---|---|---|---|---|
| <EntityName> | <table_name> | <field: type, field: type, ...> | <fk → target> | <gap/caveat, or blank> |

<One row per load-bearing entity reachable from a confirmed feature entry point —
not every entity in the repo, only those in the neighborhood of identified features.
This is a lookup appendix, not narrative: a required table makes a missing field a
visible blank instead of a silent omission. This is the section that catches "field
X doesn't exist" at contract-time, before a claim gets written against a noun the
spine never confirmed or denied. Populate fields from the same probe that grounds
§5, not from inference — a field you didn't read is a field you don't have.>

## §8 Capabilities prod does NOT have

<Bounded negative-space list. Record an absence only if (a) it's adjacent to a
confirmed domain noun AND (b) a naive port would plausibly assume it exists —
e.g. student-side capacity, a notification channel, a subject/course taxonomy.
This is not an invitation to enumerate everything the repo lacks; an unbounded
absence list is as useless as no list. Absences that pass this test are repo-wide
by definition, so they automatically pass the different-feature test below.

- <domain noun> does NOT have <capability a naive port would assume> — <one-line evidence: grep/read that confirms absence, e.g. "no `subject` column on SessionItem or its .hbm.xml; grepped `item/` and `enums/` for `Subject`, zero hits">
- <domain noun> does NOT have <capability> — <evidence>>

## §9 Domain vocabulary

<Glossary of real domain nouns and their backing, so downstream skills use real
nouns instead of rediscovering them. One line per noun.

- <noun> = <what it actually is, e.g. "enrollment = row in StudentSessionItem">
- <noun> = <what it actually is, e.g. "capacity = tutor-staffing only, not student-side">>
```

---

**`formal.md`** — analytical reference. The most important cause file for ari-code-rhetoric's substrate translations.

```markdown
# Formal: <repo-name> (<label>)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Layered architecture
## §2 Module boundaries
## §3 Dominant patterns
### Backend
### Frontend
### Data flow
## §4 Seam protocols
## §5 Named findings

<Architecture pattern, layering, module boundaries, dominant design patterns,
the shape of a typical change. Named inconsistencies as findings.

§3 is per-stratum, not a flat list: state the dominant pattern separately for
Backend, Frontend, and Data flow, because these are the substrates ari-code-rhetoric
translates independently — "what to translate this layer INTO" is the question
each subsection answers. This per-layer idiom map is the canonical source
ari-argue-rhetoric's substrate-changes classification is derived from; without it, each
port hand-derives the same layer-by-layer mapping (React→JSP, useState→
round-trips, PLUS DS→Bootstrap) from scratch instead of reading it off the spine.

Each of Backend / Frontend / Data flow must end with a required line:

`Seams: <where this layer's own pattern is inconsistently applied — the class of
finding like "most servlets extend AbstractServlet, but ReflectionServlet extends
HttpServlet directly">` — or the literal `Seams: none found`.

A required line makes an omission visible instead of silent — same trick as the
material.md §7 inventory table. Do not skip the line because nothing came up in
probe; write `none found` and mean it.

This per-layer `Seams:` line is WITHIN-layer pattern-consistency (does Backend
follow its own stated pattern everywhere?) — distinct from §4 Seam protocols
below, which is CROSS-layer: the shape of data as it crosses a boundary between
layers. Don't collapse them: a backend that's 100% consistent internally can
still have an unconfirmed or broken cross-layer protocol, and vice versa.

Provenance rule: tag each finding as (code-derived) or (README-stated).
- (code-derived): you grepped or read files and the pattern is confirmed in actual code
- (README-stated): the README or docs claim this; you have not verified it in code

ari-code-rhetoric treats formal.md as ground truth for substrate decisions. A README-stated
pattern that the code contradicts silently misdirects translations. The tag lets
ari-code-rhetoric and human reviewers know which claims need a verification pass before
acting on them.

Connective-tissue rule: every §5 named finding also carries a `lives-in: <path[s]>`
tag pointing at the file(s) that embody it — same discipline as §2's don't-contradict
rules above. This is a pointer, not a cache: never copy the code or snippet into the
spine, only the path. The spine already treats code-derived material as liquid by
default (PHILOSOPHY.md); storing the file it lives in is stable and cheap, storing
the code itself just creates a second staleness surface to track. If one finding is
enforced at 3 or more call sites, flag it during authoring as a smell — the rule is
probably too coarse and should split into narrower findings, not silently accepted
as one finding with a long path list. This tag is what makes the spine's own
staleness mechanically detectable: a diff touching a tagged path is a candidate stale
rule, checkable by grep instead of a full re-read. See PHILOSOPHY.md's spine
self-correction paragraph for the procedure this feeds.

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

## §1 Build tooling
## §2 Key targets
## §3 CI/CD
## §4 Branching model
## §5 Deploy path

<CI/CD pipeline, branching model, build tooling, how changes get deployed.
How to verify a change works in this repo.>
```

---

Cap each cause file's narrative sections at ~50 lines. If you're exceeding that, you're over-promising precision. Cut to load-bearing facts.

**Cap exemption.** The narrative sections — material.md §1–§6, formal.md §1–§5 — must stay ≤~50 lines combined per file. material.md's §7 entity/field inventory, §8 capabilities-NOT-present, and §9 domain vocabulary are lookup APPENDICES, not narrative, and are EXEMPT from the cap: a table row is a confirmed fact, not prose that can bloat. The cap and the required tables do not contradict each other — the cap bounds how much gets asserted in flowing text; the tables absorb the field-level volume that used to either get crammed into narrative (blowing the cap) or dropped (causing silent incompleteness). The feature ledger (uncapped, per-feature) absorbs anything more granular than repo-wide — see "Domain-central features go to stub:2 at map-time" above.

## Feature Ledger

During probe, attempt a comprehensive feature map (see "Comprehensive feature map" above) and create an honest stub in `.anima-lite/features/<slug>.md` for every feature identified — deep as the probe can decisively confirm, no deeper. The failure mode is not the shallow stub; it is the dishonest stub, where a field is filled with an assertion the agent cannot confirm. A shallow honest stub is a correct artifact.

Format, stub levels, and field ownership: see `ledger-spec.md` in this skill's directory.

> **◎ OPTIONAL GATE — GATE-SPINE-REVIEW (spine review)**
> Spine written — review before ari-argue-rhetoric runs? (skip to proceed). Especially recommended on first-time repos where probe depth is uncertain.

## Escalation / Notes

Each spine directory is shared, repo-level state. Commit the full directory rather than gitignoring it. Merge conflicts on spine files are a legitimate signal that two sessions' mental models diverged — resolve by re-probing fresh, not by picking a side.

Both the proto and prod spine directories must be current before ari-argue-rhetoric can run. ari-argue-rhetoric's contracts pin to the `Commit:` hash in `spine-proto/telos.md` (or whatever label is used for the prototype repo).

On refresh, re-probe fully rather than patching — and note what changed versus the previous version.
