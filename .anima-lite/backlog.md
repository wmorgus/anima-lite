# anima-lite backlog

Pin format, fast/slow lane rules, and sweep process are specified in `.claude/skills/ari-backlog/SKILL.md`. This file is the durable state the skill operates on.

---

### PIN-1 — Post-run-review: why did the execution plan fall short?
captured: 2026-07-05
stub: 0
status: open
home: anima-lite
goes-stale: superseded once PIN-10 (commit discipline hygiene fix) lands and a subsequent run shows the enforcement actually holding
relates-to: self-spine FINDING-2 (conservative default not always operationalized at skill level)

The weekly-report stress-test execution subagent returned empty claim commits — all claim logic landed in the substrate commit rather than being held out per-claim per the commit discipline spec. The plan was correct; the subagent didn't follow it. Open questions: was the plan underspecified about when to separate claim logic from substrate scaffolding? Did the subagent misread the plan or override it with a judgment call? Does the substrate/claim commit boundary need to be enforced more explicitly (e.g. "do NOT write claim logic in substrate files — stub them, then fill in a separate commit")? Address next session, before the calibration run.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:**

---

### PIN-2 — "Software as research programme" sensors
captured: 2026-07-05
stub: 1
status: open
home: anima-lite
goes-stale: superseded once the sensors sprint (PIN-2/3/4/5) actually ships a metrics/ directory with a first run row
relates-to: none yet

Anima-lite currently treats each run as an isolated event. It should accumulate measurements across runs. Before the next calibration run, add: failing review rate (validation FAIL results per N runs), blip severity distribution per run (review-suggested vs info vs CONTRACT-BREAK counts), gate utilization (which required/optional gates fired, which were skipped), spine staleness rate (how often ari-map was triggered by staleness vs fresh map), and contract amendment rate (how often CONTRACT-BREAK fired per N runs). Measurement artifacts should live in `.anima-lite/metrics/` and be committed. Each run produces a `run-<date>-<feature>.md` row; a `summary.md` aggregates.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the five sensor categories named above, landing as committed files under `.anima-lite/metrics/`. Out — dashboarding, alerting, or any UI over the metrics; this is data collection only.
**Batch:** sensors-sprint
**Contract:** not traced
**Resolution:**

---

### PIN-3 — Per-run token analysis as instrumentation
captured: 2026-07-05
stub: 1
status: open
home: anima-lite
goes-stale: superseded once token counts are flowing into `.anima-lite/metrics/` from at least one real run
relates-to: none yet

Add token usage tracking to each run as part of research programme sensors (see PIN-2). Each calibration run should record total tokens consumed per pipeline phase (ari-map, ari-argue, ari-port steps 1–5), token cost per subagent invocation, and trend across calibration runs (better quality at similar token cost, or regressing?). This surfaces the economic dimension of harness improvements: a better harness that costs 3x more tokens is a different tradeoff than one that costs the same. Implementation: subagents return token counts in handoff; main agent logs to `.anima-lite/metrics/` alongside other sensors.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — token counts per phase and per subagent invocation, logged alongside PIN-2's sensors. Out — cost-optimization decisions themselves; this pin only builds the measurement.
**Batch:** sensors-sprint
**Contract:** not traced
**Resolution:**

---

### PIN-4 — Agentic reasoning measurements from epistles 051 + 053
captured: 2026-07-05
stub: 1
status: elsewhere
home: anima-corps
goes-stale: superseded once exported, or once epistle-051/053 content changes materially before export
relates-to: /Users/wmorgus/Desktop/anima/anima-corps/epistles/epistle-051.md, epistle-053.md

Epistle-051 (whole thing) and epistle-053 (phronesis, hamartia) contain frameworks for measuring agentic reasoning quality. This belongs in Anima-proper's measurement infrastructure, not anima-lite's: phronesis (practical wisdom — is the agent making contextually appropriate judgment calls, not just rule-following?) and hamartia (error pattern — what class of mistake is the agent making: hubris, ignorance, misjudgment of scope?) are qualitative measurement axes that complement the quantitative sensor data in PIN-2/3.

**Export note: export target: anima-corps backlog equivalent, not yet created.**

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — porting the phronesis/hamartia measurement framework as qualitative axes. Out — building anima-lite's own copy; this is corps-side infrastructure.
**Batch:** sensors-sprint
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**

---

### PIN-5 — Model-intensity compute-substrate axis instrumentation (epistle-040)
captured: 2026-07-05
stub: 1
status: open
home: anima-lite
goes-stale: superseded once model-tier tracking is live in the sensor suite from at least one real run
relates-to: /Users/wmorgus/Desktop/anima/anima-corps/epistles/epistle-040.md

Epistle-040 describes a model-intensity / compute-substrate axis. This is anima-lite instrumentation work derived from that anima-corps epistle: track which pipeline phases use which model tier (Opus vs Sonnet vs Haiku), measure whether model choice correlates with output quality (blip rate, validation FAIL rate), and let the "compute-substrate axis" inform harness decisions about where to spend model budget.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — per-phase model tier logging and correlation with blip/FAIL rate, alongside PIN-3's token analysis. Out — any automated model-selection policy; this pin only measures.
**Batch:** sensors-sprint
**Contract:** not traced
**Resolution:**

---

### PIN-6 — Lite face lost on direct skill invocation
captured: 2026-07-06
stub: 0
status: open
home: anima-lite
goes-stale: superseded once a mechanism decision is made and implemented, or once confirmed as intentional design and closed
relates-to: spine-anima-lite/formal.md §5, FINDING-3

Lite face authority is only active via ari-lite agent invocation; direct skill invocation loses it. This may be by design — a skill invoked directly is presumed to already have the right orientation active — but that's a decision that hasn't been made explicitly, only tabled. Needs: a decision on whether skills should self-declare face requirements in their frontmatter, and if so, what enforces it.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:**

---

### PIN-7 — Deployment target sync (Cursor/Windsurf/Copilot)
captured: 2026-07-06
stub: 0
status: open
home: anima-lite
goes-stale: superseded once a concrete sync mechanism is designed and either implemented or explicitly deferred with reasoning
relates-to: spine-anima-lite/formal.md §5, FINDING-5

Deployment targets (Cursor, Windsurf, Copilot) have no sync mechanism with SKILL.md sources — if a skill file changes, nothing propagates that change to the equivalent config for other coding agents. Tabled pending a concrete sync mechanism design; no design has been attempted yet.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:**

---

### PIN-8 — Versioning fields in contracts/blips
captured: 2026-07-06
stub: 0
status: open
home: anima-lite
goes-stale: superseded once harness versioning is designed, or reconfirmed low-priority at a future sweep
relates-to: spine-anima-lite/formal.md §5

No version field exists in SKILL.md files, contracts, or blips. Low immediate impact, medium future impact as harness versions accumulate and old contracts/blips become hard to date against the skill version that produced them. Tabled at the self-spine review; no design attempted yet.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:**

---

### PIN-9 — Hygiene: blip Why must cite spine §
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once ari-port's blip format requires and enforces a spine-section citation in the Why field
relates-to: none yet

Blips currently allow a "Why" explanation without requiring it to cite the spine section it rests on, the same discipline ari-argue already applies to substrate/claim classifications. A blip that asserts a reason without a citable spine fact is unverifiable the same way a bare classification is — a reviewer has to trust the agent's memory instead of checking a cited fact. Fix: require the blip format's Why field to name a spine §, or explicitly state "no spine section applies; reasoning is by telos inference," mirroring the rule already in ari-argue.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the blip format's Why field in ari-port's SKILL.md output section. Out — retroactively rewriting existing archived blips.
**Batch:** hygiene
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:** Blip `Why:` field now requires a spine-section citation or an explicit "no spine section applies" statement, mirrored from ari-argue's classification-citation rule — commit 64fa1c7.

---

### PIN-10 — Hygiene: commit discipline enforcement
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once a run demonstrates claim logic correctly held out of the substrate commit under the new instruction
relates-to: PIN-1

Substrate commits should be scaffolding-only; claim behavior should be stubbed in the substrate commit and filled in a separate, later claim commit. PIN-1 documented a run where this discipline collapsed — the execution subagent put all claim logic in the substrate commit. This pin is the fix: make the instruction explicit enough in ari-port's SKILL.md that a subagent can't quietly override it as a judgment call — e.g. "do NOT write claim logic in substrate files; stub them, then fill in a separate commit."

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — ari-port's execution step instructions around commit sequencing. Out — retroactively fixing prior runs' commit history.
**Batch:** hygiene
**Contract:** Promises that ari-port's substrate commits will never silently carry claim behavior — an operator inspecting the substrate commit alone can rely on it containing no argument-bearing logic, only scaffolding. This changes what "substrate commit" means as a guarantee, not just as a style preference.
**Resolution:** Commit discipline block now requires substrate commits to stub claim behavior, bans empty claim commits as a discipline failure, and adds a pre-substrate-commit self-check — commit 64fa1c7.

---

### PIN-11 — Hygiene: source-of-truth declaration in ari-argue
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once ari-argue's contract format requires a source-of-truth declaration whenever multiple proto components exist
relates-to: none yet

When a feature being argued has multiple proto components (e.g. two components that both partially implement overlapping behavior), ari-argue currently has no requirement to declare which one is treated as the source of truth for classification purposes. Without this, two components disagreeing about behavior can produce a contract that silently picked one arbitrarily. Fix: require the contract to name which component is authoritative and why, whenever more than one exists.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — ari-argue's process/output sections, for the multi-component case only. Out — resolving disagreements between components; this pin only requires declaring which one wins.
**Batch:** hygiene
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:** Added step 1a (source-of-truth check, confirmed with user) and a Source of truth contract header line, required whenever multiple candidates existed — commit 64fa1c7.

---

### PIN-12 — Gate registry: single HARNESS.md at repo root
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once HARNESS.md exists and lists all current required/optional gates by ID; goes stale again if a skill adds or removes a gate without updating the registry
relates-to: none yet

Gates are currently defined inline in each skill's SKILL.md with no central index — a reviewer has to read all four skill files to know the full set of required and optional gates in the harness. Add a single `HARNESS.md` at the repo root listing every gate: ID, required or optional, owning skill, and trigger condition. Skills continue to define gate behavior in their own SKILL.md but cite the registry ID rather than being the sole record of the gate's existence.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — a new root-level HARNESS.md, plus adding an ID reference to each existing gate callout in the four skill files. Out — changing any gate's actual behavior; this is a registry, not a redesign.
**Batch:** structural
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:** HARNESS.md added at repo root with a 10-row gate registry (GATE-TELOS, GATE-HASH, GATE-BLOCKERS, GATE-BREAK, GATE-BLIPS, GATE-PR, GATE-SPINE-REVIEW, GATE-PLAN-REVIEW, GATE-CATCHUP-REVIEW, GATE-PIN-CLAIM), a spec ownership map, and enforcement-level tags; every inline gate callout across the four skill files now carries its ID — commit 176b84d.

---

### PIN-13 — Spec ownership consolidation
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once the feature-ledger spec and the playwright verification block each have one canonical home with other files referencing rather than restating
relates-to: none yet

The feature-ledger template and the playwright verification block are each partially specified in more than one place (feature ledger: referenced from ari-map's output section and touched again by ari-port's enrichment step; playwright block: specified in ari-argue's output and consumed by a verification step elsewhere). Multiple homes for the same spec risk drifting out of sync when one is edited and the other isn't. Consolidate each to one canonical file section; other files reference it by pointer instead of restating the shape.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the feature-ledger template and playwright verification block specifically. Out — auditing every other possibly-duplicated spec in the harness; that's a separate future pass if this one finds more instances.
**Batch:** structural
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:** Feature-ledger spec moved to `.claude/skills/ari-map/ledger-spec.md` (ari-map keeps a short pointer paragraph; ari-port Step 5 points to the same file). Playwright verification block spec moved to `.claude/skills/ari-argue/playwright-spec.md` (ari-argue's Output section and ari-port's validation D both point to it instead of restating the schema/example) — commit cb2b461.

---

### PIN-14 — Enforcement-level tags: mechanical vs judgment
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once harness rules carry enforcement-level tags and at least the commit-shape check is hooked
relates-to: none yet

Harness rules currently don't distinguish which ones could be mechanically enforced (hookable — a script could check them) from which ones require judgment (prompt-only, no reliable mechanical check). Tag each rule accordingly so future hook work has a prioritized list rather than starting from scratch. The commit-shape check (substrate commit contains no claim logic — see PIN-10) is the first hook candidate, since it's structurally checkable (diff the substrate commit against a claim-logic pattern) rather than requiring semantic judgment.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — tagging existing rules across the four SKILL.md files as mechanical or judgment, and building the first hook for commit-shape. Out — building hooks for every mechanical-tagged rule; that's future work this pin only scopes.
**Batch:** structural
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:** HARNESS.md Section 3 tags each harness discipline mechanical or judgment; commit-shape discipline is named the first hook candidate, with PIN-1's run3 failure cited as evidence. No hook was built — hook implementation is noted explicitly as future pin work — commit 176b84d.

---

### PIN-15 — Artifact layout cleanup
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once root residue is relocated and the gitignore-vs-archive contradiction is resolved
relates-to: none yet

Root-level residue (`catchup-*.md`, `pr-*.md`) currently sits loose in `.anima-lite/` rather than under a run or feature subdirectory, and there's a live contradiction between what `.gitignore` excludes (contracts/, blips/, plans/, pr-*.md, catchup-*.md) and what the archive directory preserves (calibration-2026-07-05 archives full run contents including contracts, blips, plans, catchup, and pr files). Gitignored files that later get archived means the archive is the only copy — worth resolving explicitly rather than leaving as an accident of how archiving happened to work.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — relocating catchup-*.md and pr-*.md into structured subdirectories, and deciding (and documenting) whether archived copies of gitignored artifacts are intentional policy. Out — changing what gets gitignored during an active run; only the post-run archive state is in scope.
**Batch:** structural
**Contract:** Clarifies what "gitignored" means once a run is archived — currently a session artifact that's supposed to be ephemeral (contract, blip) can end up permanently committed via the archive path, which is a different retention promise than the .gitignore implies on its face.
**Resolution:** Root residue relocated: `.anima-lite/` restructured to per-slug `ports/<slug>/{contract,blips,plan,catchup,pr}.md` (slugs: main, monthly-report, monthly-report-v1, weekly-report); `catchup-monthly-report-v1.md` deleted as a superseded draft. Gitignore-vs-archive contradiction resolved by policy: everything under `.anima-lite/` is now committed durable state — `.gitignore`'s contracts/blips/plans/pr-*/catchup-* rules removed; `archive/` remains calibration-snapshot-only, not a backup channel — commit cb2b461. Gate cleared in-session: user approved commit-everything policy + per-slug layout 2026-07-06.

---

### PIN-16 — Bidirectional audit orientation
captured: 2026-07-06
stub: 2
status: done
home: anima-lite
goes-stale: superseded once all three skills (ari-map, ari-argue, ari-port) state the bidirectional-audit orientation explicitly rather than it being implicit in how skeptical reads currently work
relates-to: none yet

Currently, skeptical reads happen in specific named spots (ari-map's probe subagents, ari-argue's substrate classification check) rather than as a standing orientation. The proposal: every artifact read by any skill is also implicitly an audit of that artifact — drift should be flagged in both directions (spine says X, code says Y is already handled in ari-map; but the reverse direction — a contract or blip that turns out to falsify something the spine asserted — isn't currently named anywhere as an expected outcome). Generalize the orientation across all three skills so a stale or wrong upstream artifact gets caught by whichever skill reads it next, not only by the skill that originally wrote it.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — adding a bidirectional-audit orientation statement to ari-map, ari-argue, and ari-port's Active Orientations sections. Out — building any automated drift-detection tooling; this is a reading discipline, not a mechanism.
**Batch:** audit-orientation
**Contract:** Promises that reading an upstream artifact (spine, contract, ledger) is never a passive trust operation in this harness — every read carries an obligation to flag contradictions found, even ones the reading skill didn't set out to look for. This is a stronger promise than "skeptical reads happen where currently specified."
**Resolution:** Added a Bidirectional audit paragraph to ari-map, ari-argue, and ari-port's Active Orientations sections, generalizing ari-map's ledger-vs-spine check (step 5) and ari-argue's substrate skeptical read into a standing orientation; ari-port's execution and validation agent input lists each got a one-line pointer. Drift flows through existing channels only (named findings, Open Questions, blips) — no new gates or fields — commit 226bed8. Gate cleared in-session: user approved batch 2026-07-06.

---

Formalization of this backlog's own process resolved via the ari-backlog skill (`.claude/skills/ari-backlog/SKILL.md`) — see commit introducing that skill.
