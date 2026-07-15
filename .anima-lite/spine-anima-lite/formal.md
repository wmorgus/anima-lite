# Formal: anima-lite (self)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Layered architecture
Eight skills, not layers in the traditional sense — a pipeline of registers, entered at one of two doorways (change vs. question), with one orthogonal maintenance skill, plus a third doorway pair (found vs. judge) for the arete work-type. Two-level four-cause nesting (PHILOSOPHY.md): the skill pipeline is itself the four-cause decomposition of "make a software change" — intake=final, map=material, argue=formal, port=efficient — one level up from each target repo's own four-cause spine.

## §2 Module boundaries
Each skill is a self-contained `SKILL.md` (Inputs → Preconditions → Active orientations → Process → Output → Escalation/Notes). Three support files are canonical sub-specs, not restated in their owning skill: `ari-map/ledger-spec.md`, `ari-argue-rhetoric/playwright-spec.md`, `ari-code-rhetoric/metrics-spec.md`. `HARNESS.md` owns cross-skill metadata (gate registry, spec ownership, enforcement levels, doc ownership) and never carries operative behavioral prose (its own governing rule).

## §3 Per-skill strata (code-derived)

### ari-intake
Mints the workstream slug, sharpens change-telos against `RESOLUTION.md` (apex) and the target spine `telos.md` (§1/§2), enumerates claims with `argued-by:` provenance, writes `intent.md`. Fires GATE-TELOS at full strength — the primary check, not a backstop.
Seams: harness-change posture (PIN-32/PIN-36) is fully specified; debt-work posture is explicitly not built — the skill says so plainly rather than fabricating a diagnosis pass (Preconditions/Per-work-type-posture).

### ari-map
Enumerates the target repo, probes four causes (fanning out to 3 parallel subagents on >500-file repos), writes the four-file spine plus feature-ledger stubs. Domain-central features get stub:2 at map-time; others stop at stub:1.
Seams: `stub-depth field honesty` is tagged `judgment` in HARNESS.md §3 — no mechanical proxy exists for "was the probe actually deep enough," and this self-spine is itself evidence of the risk (a probe grading its own depth).

### ari-argue-rhetoric
Runs as an isolated subagent. Reads `intent.md` + both spines + the feature (or, for ripple, `intent.md` alone), classifies every detail substrate/claim with mandatory spine-§ citation, confirms claims one at a time, runs GATE-SCHEMA before freezing. Writes `work/<branch-slug>/contract.md`.
Seams: refuses any claim lacking `argued-by:` (backstops ari-intake's own enforcement) — a two-skill redundancy on the same discipline, intentional per the skill's own text, not accidental duplication.

### ari-code-rhetoric
Four steps (plan → execute → validate → reconcile) plus harvest and instrument. Execution runs in a clean-context subagent so contract gaps surface as blips instead of being silently papered over by carried context. CONTRACT-BREAK halts and hands back to ari-argue-rhetoric rather than self-resolving.
Seams: "Driver's independent break-scan is not optional" (Escalation/Notes) exists precisely because GATE-BREAK is a judgment gate that "cannot be mechanized" — the main agent, not a hook, is the only enforcement layer, and a self-policing executor is explicitly stated as insufficient on its own.

### ari-backlog
Two-speed: fast lane (zero-ceremony `stub:0` pin capture, any time) and slow lane (sweep — advance stubs, classify Contract, archive done pins, write the backlog-health row). Orthogonal to the port pipeline, run before every calibration.
Seams: "No priority ranks" — batch + status are the only ordering the backlog itself asserts; the actual working order lives in an operator-owned, unshaped `session-backlog.md` outside this skill's discipline entirely.

### ari-arete
Founds a telos by iterative language for a repo with no final cause on record — bare, asserts rather than argues. Hard-precondition GATE-SEED-CONTEXT (starting rule: index file, list grows by design) gates a draft→iterate→ratify pass producing a caveman-dense arete statement, cascading top-down (system, then each derived component). Writes `work/<slug>/arete-statement.md`.

**Telos-growth propagation (two-tier reopen, borrowed from `reorient/ripple.md` ruling 4).** On a ratified system-level arete-statement growth event, the cascade to components and to any `scaffold.md` scenario does not automatically re-run in full, and it does not stay silently un-reconsidered either — two tiers:
- **Tier 1 — mandatory reconsideration, always.** Every cascaded component statement and every scaffold scenario gets a reconsideration pass ("does this still follow from the new parent?"), and the judgment is logged even when the answer is no-rework-needed. This pass is not optional or skippable just because a component "probably isn't affected" — the judgment itself, yes or no and why, is the record.
- **Tier 2 — re-founding/re-walking, only where dependency is real.** A component statement or scaffold scenario only gets re-founded or re-walked where tier 1's judgment concludes it actually depended on what changed. Where tier 1 concludes no dependency, the existing statement/scenario stands as-is.

This is the same two-tier shape ripple's ruling 4 uses for a CONTRACT-BREAK's cross-leg reopen, borrowed directly rather than independently invented for arete's cascade. **The log's concrete artifact is not decided here** — ripple's own ruling 4 doesn't name a dedicated artifact for this either (it logs into the ordinary contract-amendment record); naming and scoping a durable log format for this class of triggered, coordinate-keyed, append-only observation is deferred to **PIN-49**.
Seams: does not judge existing code against the statement it produces — that's `ari-arete-pan`'s exclusive job, kept deliberately separate rather than folded in as a final step of the same pass (arete.md ruling 1).

### ari-arete-pan
Sorts an existing repo's code against a ratified arete statement into nugget/ore/slag; draft→iterate→ratify a single batch cut (GATE-ARETE-CUT) before any code moves or any item reaches `ari-argue-rhetoric`. Independent entry point — precondition is a ratified statement existing, not `ari-arete` having just run. Writes `work/<slug>/cut.md`.
Seams: explicitly not a fifth `ari-diagnose` primitive — the skill's own Active orientations states the category distinction in its own words (drift-from-existing-telos vs. founding-into-nothing) rather than by cross-reference alone, per the contract that built it.

### ari-read
Sibling doorway to ari-intake, not a step inside the pipeline. Confirms question intent (GATE-QUERY) without staking it for the asker, reconstructs from the five fields, presents (never self-certifies) at GATE-MATCH. Writes `judgment.md`; terminal only once the operator fills Operator reading.
Seams: "Route-out is not a failure" — discovering mid-read that a question is actually a change request is a named normal outcome, not an error, and hands off to ari-intake; this is the mirror of ari-intake's own halt-and-route-to-ari-read precondition.

## §4 Seam protocols (cross-skill)
- intake → map: intake's Preconditions halt and request `/ari-map` if no spine is reachable for the telos check — map is a hard precondition, not an optional enrichment.
- intake → argue: `intent.md`'s `Claims` (each with `argued-by:`) is argue's primary input; argue's own Preconditions independently refuse an unsourced claim rather than trusting intake's enforcement (deliberate redundancy, §3 above).
- argue → port: `contract.md` crosses frozen — `Status: FROZEN FOR SESSION`; port's Preconditions re-check the `Spine commit:` hash against the live spine before trusting the contract (GATE-HASH).
- port → argue (reverse seam): CONTRACT-BREAK sends a specific delta back, not a redo signal — ari-argue-rhetoric treats it as "new evidence" and writes an amendment, never a from-scratch re-contract (ari-argue-rhetoric Escalation/Notes).
- port → backlog: blips and catchup gaps are candidate pin sources; ari-backlog's Inputs name "whatever surfaced the pin" including a blip.
- read → backlog / intake: a `judgment.md` with `Feeds: pin/debt-work handoff` fires a fast-lane pin (per ari-read step 7) or routes to intake if the read discovers a change-shaped ask mid-reconstruction.
- arete → arete-pan: `arete-statement.md`, ratified, is `ari-arete-pan`'s only hard precondition — not "ari-arete just ran," a state-of-the-world check rather than a same-session handoff (arete.md ruling 11).
- arete-pan → argue (arete posture): `cut.md`'s nuggets and ore, never slag, become argue-rhetoric's primary input under its arete posture — replacing intent.md's claim list entirely for this work-type (no ari-intake pass exists for arete).
- argue (arete posture) → code (arete posture): the frozen contract crosses the same way a port's does, but code-rhetoric's arete posture targets a new, empty repo rather than translating into the existing one — the old repo stays read-only evidence, never re-entered as a live target.
Seams: none found beyond the above — every cross-skill boundary observed carries an explicit artifact-shape contract (frozen contract, hash pin, `argued-by:` line, `Feeds:` field, ratified-statement precondition); no boundary was found passing bare prose with no checkable field.

## §5 Named findings

- **FINDING-3 (code-derived, live seam — PIN-6, status: open, stub:0)**: the three faces (ari/builder/lite) are fully active only inside the `ari-lite` agent invocation (`.claude/agents/ari-lite.md`); none of the six `SKILL.md` files carries frontmatter or process text that self-declares or enforces a face requirement when invoked directly as `/ari-<name>`. A direct skill invocation is presumed to already have the right orientation active, but this is an unexamined assumption, not a decision — PIN-6 remains open with no mechanism proposed.
- **FINDING (code-derived, doc drift)**: `.claude/agents/ari-lite.md`'s own three-phase narrative (Phase 1 cartography-spine / Phase 2 argumentation-contract / Phase 3 execution-port) still names the skills `ari-argue` and outputs `.anima-lite/contracts/<branch-slug>.md`, `.anima-lite/blips/<branch-slug>.md` in its Phase 2/3 templates — pre-rhetoric-rename (PIN-26) and pre-work/ layout (2026-07-07 rename, HARNESS.md §4) naming, alongside other passages in the same file that do use the current `ari-argue-rhetoric`/`ari-code-rhetoric` names and `work/<slug>/` paths. The file is internally inconsistent between old and new vocabulary — a live instance of exactly the doc-drift class HARNESS.md's bidirectional-audit rule exists to catch.
- **FINDING (code-derived)**: deployment-target drift — `.cursor/rules/*.mdc` still uses the pre-rename skill names (`ari-argue.mdc`, `ari-port.mdc`) while `.windsurf/rules/*.md` uses the current rhetoric names; both are hand-maintained with no generator (PIN-7) or drift-check (PIN-18), both open.
