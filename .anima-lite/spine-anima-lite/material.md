# Material: anima-lite (self)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Language and format
- Markdown (.md) — all skill logic, artifact templates, gate text, documentation; no application code, no compiled output
- YAML frontmatter — skill metadata (`name`, `description`) in each `SKILL.md`; also used in `.claude/agents/ari-lite.md` (`name`, `description`, `model`, `color`, `memory`)
- Mermaid — the pipeline diagram embedded in README.md

## §2 Runtime
- Claude Code skill runner — `/ari-<name>` invocation loads and executes the matching `.claude/skills/<name>/SKILL.md` in the active agent context; nine skills exist today (§9), corrected here from a pre-existing "six" count that had already fallen behind `ari-diagnose`'s build (PIN-39) before this probe
- Agent face: `ari-lite` (`.claude/agents/ari-lite.md`), model `opus` — three orientations (ari/builder/lite) always active, weighted by phase
- Skills invoke subagents via the Agent tool; subagents are ephemeral, isolated, no shared session context (e.g. ari-argue-rhetoric's classification loop, ari-code-rhetoric's execute/validate/completeness-critic agents)

## §3 Deployment targets (code-derived: file enumeration)
- Claude Code: `.claude/skills/{ari-intake,ari-map,ari-argue-rhetoric,ari-code-rhetoric,ari-backlog,ari-read,ari-diagnose,ari-arete,ari-arete-pan}/SKILL.md` + `.claude/agents/ari-lite.md` + `.claude/hooks/session-cost.py`
- Cursor: `.cursor/rules/{ari-map,ari-argue,ari-port,ari-lite}.mdc` — four files, old skill names (`ari-argue`/`ari-port`, pre-PIN-26 rhetoric rename)
- Windsurf: `.windsurf/rules/{ari-argue-rhetoric,ari-code-rhetoric,ari-lite,ari-map}.md` — four files, current rhetoric names
- GitHub Copilot: `.github/copilot-instructions.md` — single file
- No CI/CD of any kind — no `.github/workflows/`, no lint/test config anywhere in the repo (confirmed by enumeration)
- No sync mechanism between `.claude/skills/` sources and the Cursor/Windsurf/Copilot deployment targets — PIN-7 (generator, un-built) and PIN-18 (doc-drift check, un-built) track this; Cursor's `.mdc` files are already stale against the current skill names, a live instance of the gap

## §4 Artifact data structures
All committed, durable state (only `.anima-lite/work/*/screenshots/*.png` is gitignored — the prose manifest `screenshots.md` is the committed record):
- `spine-<label>/{telos,material,formal,efficient}.md` — four cause files per repo; `telos.md` is hash-pinned to that repo's HEAD
- `spine-<label>/scaffold.md` — fifth spine file, always produced, depth-gated; not a fifth cause — coordinate backbone the four cause files' cells attach to (`ari-map/scaffold-spec.md`)
- `work/<slug>/{intent,contract,plan,blips,catchup,pr,judgment}.md` — per-workstream artifacts, not all present for every slug (§7)
- `features/<slug>.md` — feature ledger, stub:0–3
- `backlog.md` + `pins/PIN-<n>.md` — the backlog index and one file per pin
- `metrics/{run-<date>-<slug>,backlog-health-<date>}.md`, `metrics/sessions/*.md`, `metrics/summary.md`
- `archive/calibration-<date>/`, `archive/backlog/done-<year>.md` — point-in-time snapshot and archived-pin channel, not a live-state substitute
- `RESOLUTION.md` — repo root, one sentence, sovereign over every `telos.md`

## §5 State shape
- Git is the only persistence mechanism — no database, no server, no build step, no lock files, no dependency resolution
- Every artifact directory above is committed; spine refresh collisions across branches are intentional merge conflicts, not a bug to route around
- No workstream concurrency lock: two sessions against the same branch-slug is an accepted "don't," not infrastructure (ari-code-rhetoric Escalation/Notes)

## §6 Versioning
- No version field in any `SKILL.md`, contract, blip, or pin (PIN-8, open) — a running session cannot tell what harness version produced an artifact it's reading
- Spine `telos.md`'s `Commit:` field is the only staleness signal the pipeline actually checks (GATE-HASH); it pins spine state to a repo HEAD, not to a harness version

## §7 Artifact/spec inventory

Base: `HARNESS.md` §2 (spec-ownership map) names the canonical location and owner/reader of each spec; this table adds the field-level shape HARNESS.md §2 deliberately does not carry (its governing rule keeps behavioral prose out of that file).

| Artifact | Owning spec | Key fields | Consumed by |
|---|---|---|---|
| `work/<slug>/intent.md` | ari-intake SKILL.md (Output) | Slug, Work-type, Target spine, Target telos commit, Telos statement, Sources, Claims (each with `argued-by:`), Notes | ari-argue-rhetoric (primary input; refuses claims with no `argued-by:` line) |
| `work/<slug>/judgment.md` | ari-read SKILL.md (Output) | Question (verbatim), Slug, Question-shape, Confirmed intent, Feeds, Ontology, Reconstruction, Belief repair (Believed/Observed/Where belief ends), Provenance, Operator reading | Operator (GATE-MATCH reading is terminal), ari-backlog (when a judgment feeds a pin) |
| `spine-<label>/telos.md` | ari-map SKILL.md (Output) | Commit, Confidence, Refresh trigger, §1 Purpose, §2 Don't contradict, §3 Cause files, §4 Disclaimers | ari-intake (GATE-TELOS), ari-argue-rhetoric (Inputs), ari-code-rhetoric (Inputs) |
| `spine-<label>/material.md`, `formal.md`, `efficient.md` | ari-map SKILL.md (Output) | Per-cause §-numbered sections; formal.md's §3 also carries required per-stratum `Seams:` lines | ari-argue-rhetoric (classification evidence), ari-code-rhetoric (substrate-translation guide) |
| `spine-<label>/scaffold.md` | ari-map/scaffold-spec.md | Per-scenario tables, rows keyed by `(scenario, path, step)`, three formal/material/efficient columns, per-scenario `stub:0-3`, `Filled by:` reverse pointer | ari-arete-pan (evidence, `Scaffold signal:`), ari-argue-rhetoric (arete posture) |
| `features/<slug>.md` | ari-map/ledger-spec.md | slug, repo(s), stub, source, prod-commit, goes-stale, Identity, Entry points, Primary data structure, (stub:3+) Full data flow, Client-side wiring, State machine, Feature gates, Seam-specific protocols, Known quirks, Port provenance; ripple variant adds `origin: shared-origin` and per-leg bullets | ari-map (writes stub), ari-code-rhetoric (Step 5 harvest, enriches to stub:3) |
| `work/<branch-slug>/contract.md` | ari-argue-rhetoric SKILL.md (Output) | Branch, Generated, Spine commit, Source of truth, Status, The argument, Substrate changes, Claim changes (each with `Schema deps:`, ripple adds per-target substrate-mapping), Open questions, Proto visual reference, Playwright verification block | ari-code-rhetoric (Inputs, all steps) |
| `.claude/skills/ari-argue-rhetoric/playwright-spec.md` | ari-argue-rhetoric (support file) | Block schema, `expect`-field rules, worked example | ari-code-rhetoric (Step 3, validation D/E) |
| `work/<branch-slug>/plan.md` | ari-code-rhetoric SKILL.md (Step 1 Output) | Contract, Generated, Claim changes (files + what changes), Substrate translations, Order of operations, Blockers | ari-code-rhetoric (own Step 2 execution), GATE-BLOCKERS |
| `work/<branch-slug>/blips.md` (or `blips-<leg-label>.md` for ripple) | ari-code-rhetoric SKILL.md (Output) | Severity, Location, What happened, Why (must cite spine § or state none applies), Downstream consequence, Contracting failure? | ari-argue-rhetoric (none — downstream of it), the validation agent, ari-backlog (pin sourcing) |
| `work/<branch-slug>/pr.md`, `catchup.md`, `screenshots.md` | ari-code-rhetoric SKILL.md (Steps 4d/4e/D-E) | pr.md: Summary, Files changed, Test plan, Blips. catchup.md: What this is, Repo context, What changed and why, Deferred, Blips, What to focus on in review, How to verify. screenshots.md: prose manifest, one line per capture or `target-not-reachable` | GATE-PR reviewer, completeness-critic subagent (catchup.md only, in isolation), human PR reviewer |
| `backlog.md` (index) + `pins/PIN-<n>.md` | ari-backlog SKILL.md (Pin format) | Index line: PIN-n, status, stub, batch, semantic hook. Pin file: captured, stub, status, home, goes-stale, relates-to, body paragraph, Scope, Batch, Contract, Resolution, (paused) State | ari-intake (pin as candidate source), ari-argue-rhetoric (GATE-PIN-CLAIM review), all skills (cite gate IDs, per HARNESS §2) |
| `work/<slug>/diagnosis.md` | ari-diagnose SKILL.md (Output) | Slug, Entry mode, Generated, Spine checked, Primitive(s), Divergence, Scan, Evidence, Open questions | ari-intake (debt-work's source) |
| `work/<slug>/arete-statement.md` | ari-arete SKILL.md (Output) | Slug, Generated, Parent, Seed context, Statement, Provenance (asserted-not-argued, no `argued-by:`), Cascade note, Ratification | ari-arete-pan (Inputs, only hard precondition), ari-argue-rhetoric (arete posture, step 2 — the argument) |
| `work/<slug>/cut.md` | ari-arete-pan SKILL.md (Output) | Slug, Generated, Arete statement, Target repo, Nuggets, Ore (each with Pressure:), Slag, Ratification (GATE-ARETE-CUT, whole cut as a batch) | ari-argue-rhetoric (arete posture, primary input) |
| `RESOLUTION.md` | RESOLUTION.md itself (the sentence + ratification line) | The one-sentence description, `Ratified:` line | ari-intake (GATE-TELOS apex layer), every doc that cites the sentence rather than restating it |
| `metrics/run-<date>-<slug>.md`, `backlog-health-<date>.md`, `sessions/*.md`, `summary.md` | ari-code-rhetoric/metrics-spec.md | Run row: phase table (usage/duration/model per subagent spawn), gate table (every HARNESS §1 gate ID, fired or not). Backlog-health row: open-pin counts by stub/status, oldest-open age, capture-to-done latency, un-exported elsewhere count. Session-cost row: per-session token totals by model | ari-backlog (backlog-health row), `SessionEnd` hook (session-cost row), calibration diffs |

## §8 What the harness deliberately does not do

- No concurrent-same-branch locking — two sessions running against the identical branch-slug simultaneously is an accepted "don't," not infrastructure to build (ari-code-rhetoric SKILL.md, Escalation/Notes: "This skill does not implement locking... If that happens, the right answer is 'don't,' not new infrastructure"; ari-lite.md Governing rules: "No real concurrency locking. Known, accepted limitation")
- No mechanical enforcement of judgment gates — GATE-BREAK, substrate/claim classification, and stub-depth honesty are tagged `judgment` in HARNESS.md §3 because "no hook can decide whether reality contradicts a claim" (ari-code-rhetoric SKILL.md, Escalation/Notes) or whether a stub claim is actually confirmed without re-running the probe; only the main-agent's own re-read enforces these, never a script
- No mid-session change detection — if a `SKILL.md` is edited while a session is in progress, the running session has no signal; the only hook that exists is `SessionEnd` (`.claude/hooks/session-cost.py`, cost capture only), confirmed by enumerating `.claude/settings.json`'s hooks block and `.claude/hooks/`
- No automated pass/fail on validation — the validation agent's PASS / PASS (pending review) / FAIL determination (ari-code-rhetoric SKILL.md Step 3) is agent judgment reading real diffs, not a script; HARNESS.md §3 tags every discipline in this chain `judgment` except the two explicitly marked `mechanical` (session-cost capture, and the GATE-SCHEMA resolve-check half)
- No CI/CD — no test runner, linter, or validation pipeline of any kind; confirmed by enumeration (no `.github/workflows/`, no `*.yml`/`*.yaml` anywhere in the repo)
- No deployment-target sync — Cursor (`.cursor/rules/*.mdc`), Windsurf (`.windsurf/rules/*.md`), and Copilot (`.github/copilot-instructions.md`) are hand-maintained copies of skill content; the Cursor files are already stale against the post-rhetoric-rename skill names (PIN-7, PIN-18, both open and un-built)

## §9 Domain vocabulary

- **substrate** = the medium — library swap, rename, file restructure, styling; translates freely because a user's understanding of the promise wouldn't change (README.md "The key distinction"; PHILOSOPHY.md "The cut")
- **claim** = the argument itself — what a user relies on; any change here requires explicit, one-at-a-time confirmation (same sources)
- **divergence** = the unifying object of this harness's custody — an unratified promise/artifact gap; slop (LLM-introduced, seconds) and debt (drift-introduced, years) are the same object under different authorship (PHILOSOPHY.md)
- **stub:0–3** (feature ledger depth, `ledger-spec.md`) — 0 = existence confirmed only; 1 = entry point confirmed; 2 = entry point + primary data structure confirmed; 3 = full observable chain confirmed (by ari-map probe) or enriched (by ari-code-rhetoric)
- **stub:0–2** (pin shaping depth, ari-backlog SKILL.md) — 0 = raw capture; 1 = shaped (Scope + Batch named); 2 = contracted (Contract paragraph written, ready to schedule) — a distinct scale from feature-ledger stubs sharing the same numeral vocabulary; the artifact type disambiguates which scale applies
- **gate types**: **required** (pipeline halts, e.g. GATE-TELOS, GATE-HASH, GATE-SCHEMA, GATE-BLOCKERS, GATE-BREAK, GATE-BLIPS, GATE-PR, GATE-QUERY, GATE-MATCH, GATE-SEED-CONTEXT, GATE-ARETE-CUT — 11 total per HARNESS.md §1) vs. **optional** (user may inspect or skip, e.g. GATE-SPINE-REVIEW, GATE-PLAN-REVIEW, GATE-CATCHUP-REVIEW, GATE-PIN-CLAIM — 4 total); orthogonally, HARNESS.md §3 tags each underlying discipline **mechanical** (checkable by a hook in principle) or **judgment** (prompt-only, no reliable mechanical check)
- **the three faces**: **ari** (telos-holding — senior on routing and gate-holding, junior to the codebase's own content), **builder** (argument-aware — sorts substrate vs. claim, writes in builder register), **lite** (philosophical audit — the halt condition; distinguishes a contract *gap* from a contract *contradiction*) — always simultaneously active in the `ari-lite` agent face, weighted by phase (`.claude/agents/ari-lite.md`)
- **blip severities**: `info` (noted, doesn't block), `review-suggested` (surfaced to user, must be acknowledged before PASS — GATE-BLIPS), `CONTRACT-BREAK` (reality contradicts a confirmed claim — halts execution, never self-resolved)
- **work-types** (`intent.md`'s `Work-type:` field): **port** (prototype → prod, argument already exists in code), **ripple** (one promise instituted in N repos at once, no source leg — `reorient/ripple.md`), **debt-work** (a diagnosed divergence fix, sourced from `ari-diagnose`'s `diagnosis.md`), **harness-change** (the harness changing its own skills/gates/specs; single-spine posture, PIN-32/PIN-36). **Arete** (founding a telos by language for a repo with none on record, then judging existing code against it — `reorient/arete.md`) sits alongside these four but does not carry an `intent.md`/`Work-type:` value of its own; it has no `ari-intake` pass — `ari-arete`'s `arete-statement.md` and `ari-arete-pan`'s `cut.md` are its own artifact chain, feeding `ari-argue-rhetoric`'s arete posture directly.
- **the five-field tiling** (canonical in PHILOSOPHY.md, PIN-34): **user intent** (the ask as asked, confirmed) / **ratified intent** (RESOLUTION.md → spine telos.md → contracts → confirmed claims) / **belief** (spines and docs, including where they end) / **reality** (live code and runtime, always sampled) / **the record** (git history, blips, ratification lines, done pins — append-only)
- **register flows**: the **write register** (`/ari-intake` → `/ari-map`/`/ari-argue-rhetoric` → `/ari-code-rhetoric`) spends belief to change reality and appends to the record; the **read register** (`/ari-read`) spends reality to repair belief and audits the record — neither subsumes the other, a work item is one or the other, never both (PHILOSOPHY.md "Mode honesty")
- **workstream** = the live span of a work item from intake to harvest, with state on disk; distinct from a **pin** (captures future work) and a **run** (names an attempt) — a workstream is the thing that can be *paused* (`in-progress ⇄ paused`, ari-backlog SKILL.md)
