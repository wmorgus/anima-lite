# anima-lite backlog

Pin format, fast/slow lane rules, and sweep process are specified in `.claude/skills/ari-backlog/SKILL.md`. This file is the durable state the skill operates on.

Done pins are archived (full block intact) to `archive/backlog/done-<year>.md` at sweep and replaced here with a one-line pointer.

---

### PIN-1 — Post-run-review: why did the execution plan fall short?
captured: 2026-07-05
stub: 0
status: open
home: anima-lite
goes-stale: superseded once PIN-10 (commit discipline hygiene fix) lands and a subsequent run shows the enforcement actually holding
relates-to: self-spine FINDING-2 (conservative default not always operationalized at skill level), PIN-10, PIN-17

The weekly-report stress-test execution subagent returned empty claim commits — all claim logic landed in the substrate commit rather than being held out per-claim per the commit discipline spec. The plan was correct; the subagent didn't follow it. Open questions: was the plan underspecified about when to separate claim logic from substrate scaffolding? Did the subagent misread the plan or override it with a judgment call? Does the substrate/claim commit boundary need to be enforced more explicitly (e.g. "do NOT write claim logic in substrate files — stub them, then fill in a separate commit")? PIN-10 landed the prompt-level fix; run4 is its live test. Address alongside run4 review.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:**

---

### PIN-2 — "Software as research programme" sensors → done, archived: archive/backlog/done-2026.md

### PIN-3 — Per-run token analysis as instrumentation → done, archived: archive/backlog/done-2026.md

---

### PIN-4 — Agentic reasoning measurements from epistles 051 + 053
captured: 2026-07-05
stub: 1
status: elsewhere
home: anima-corps
goes-stale: superseded once exported, or once epistle-051/053 content changes materially before export
relates-to: /Users/wmorgus/Desktop/anima/anima-corps/epistles/epistle-051.md, epistle-053.md

Epistle-051 (whole thing) and epistle-053 (phronesis, hamartia) contain frameworks for measuring agentic reasoning quality. This belongs in Anima-proper's measurement infrastructure, not anima-lite's: phronesis (practical wisdom — is the agent making contextually appropriate judgment calls, not just rule-following?) and hamartia (error pattern — what class of mistake is the agent making: hubris, ignorance, misjudgment of scope?) are qualitative measurement axes that complement the quantitative sensor data in PIN-2/3.

**Export note: export target: anima-corps backlog equivalent, not yet created. RESURFACED at sweep 2026-07-06 — still un-exported (target repo backlog does not yet exist). Not archived per cross-repo handling rule.**

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — porting the phronesis/hamartia measurement framework as qualitative axes. Out — building anima-lite's own copy; this is corps-side infrastructure.
**Batch:** sensors-sprint
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**

---

### PIN-5 — Model-intensity compute-substrate axis instrumentation (epistle-040) → done, archived: archive/backlog/done-2026.md

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

### PIN-7 — Deployment-config generator (Cursor/Windsurf/Copilot sync)
captured: 2026-07-06
stub: 1
status: open
home: anima-lite
goes-stale: superseded once the generator ships and all three configs are regenerated with a generated-banner, or once explicitly deferred with new reasoning
relates-to: spine-anima-lite/formal.md §5, FINDING-5, HARNESS.md §3 (doc-drift check row), HARNESS.md §4, PIN-18

Deployment targets (Cursor `.cursor/rules/*.mdc`, Windsurf `.windsurf/rules/*`, Copilot `.github/copilot-instructions.md`) restate skill/doc content for other coding tools and have drifted badly (doc audit 2026-07-06 found single-file spine descriptions, old flat layout, no backlog/gates — worse than README's drift). Design decided (docs-strategy proposal, approved 2026-07-06): **generate, don't hand-sync.** Hand-sync is exactly the mechanism that already failed here. A generator converts this from HARNESS §3's "judgment" column to "mechanical."

Design: build `scripts/gen-deployment-configs.py` that stitches one shared markdown fragment (the facts meant to be identical across all four surfaces per HARNESS §4 — four-causes lens, skill roster, commitments) into each target's own template wrapper (Cursor `.mdc` frontmatter, Windsurf `trigger: always_on` frontmatter, Copilot plain markdown). Mark every generated file with `<!-- GENERATED — do not edit by hand; source: scripts/gen-deployment-configs.py -->`. Honest boundary: only kills drift for facts meant to be identical; genuinely tool-specific content (e.g. Copilot's extra claim-trap examples) stays hand-authored and can still drift — that's the right boundary, not full automation.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the generator script, a shared fact-fragment source, regenerating all three configs with generated-banners. Out — the mechanical drift *check* that diffs committed-vs-regenerated (that's PIN-18, ari-backlog sweep step 8); and any tool-specific hand-authored content, which the generator deliberately leaves alone.
**Batch:** docs-strategy
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**

**Spike-first (blocker before stub:2):** unverified whether `.cursor/*.mdc` frontmatter and Windsurf `trigger: always_on` have quirks (length limits, required per-file ordering) that make a shared-fragment generator harder than it looks. Short spike on the two frontmatter formats before committing to the generator's exact interface. This is why the pin sits at stub:1, not stub:2 — scope is named but the interface isn't nailed.

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

### PIN-9 — Hygiene: blip Why must cite spine § → done, archived: archive/backlog/done-2026.md

### PIN-10 — Hygiene: commit discipline enforcement → done, archived: archive/backlog/done-2026.md

### PIN-11 — Hygiene: source-of-truth declaration in ari-argue → done, archived: archive/backlog/done-2026.md

### PIN-12 — Gate registry: single HARNESS.md at repo root → done, archived: archive/backlog/done-2026.md

### PIN-13 — Spec ownership consolidation → done, archived: archive/backlog/done-2026.md

### PIN-14 — Enforcement-level tags: mechanical vs judgment → done, archived: archive/backlog/done-2026.md

### PIN-15 — Artifact layout cleanup → done, archived: archive/backlog/done-2026.md

### PIN-16 — Bidirectional audit orientation → done, archived: archive/backlog/done-2026.md

---

Formalization of this backlog's own process resolved via the ari-backlog skill (`.claude/skills/ari-backlog/SKILL.md`) — see commit introducing that skill.

### PIN-17 — Commit-shape discipline hook (first discipline hook)
captured: 2026-07-06
stub: 0
status: open
home: anima-lite
goes-stale: if run4 shows the prompt-level stub discipline (PIN-10) holds on its own, urgency drops; if commit-shape fails again, this escalates
relates-to: HARNESS.md §3 (first hook candidate), PIN-1, PIN-10

HARNESS.md Section 3 tags commit-shape discipline as mechanical and names it the first hook candidate, with run3's empty-claim-commit failure as evidence that prompt-only enforcement was insufficient. Build the actual check: a script (pre-commit hook in the prod repo, or a validation-agent step) that verifies the substrate commit contains no behavior belonging to a confirmed claim and that no claim commit is empty. Distinct from the session-cost hook (metrics); this is the first *discipline* hook — it blocks rather than records. Wait for run4 evidence before building: if PIN-10's stub discipline holds, this may be unnecessary ceremony.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:** not traced

---

### PIN-18 — Doc-drift check as ari-backlog sweep step 8
captured: 2026-07-06
stub: 1
status: open
home: anima-lite
goes-stale: superseded once the check is built and ari-backlog's sweep runs it; or if PIN-7's generator is dropped (then half the check has nothing to diff against)
relates-to: HARNESS.md §3 (doc-drift check row, tagged mechanical/UNBUILT 2026-07-06), HARNESS.md §4, PIN-7

HARNESS.md §3 now tags a doc-drift check as mechanical/unbuilt. Build it, homed in ari-backlog's **slow-lane sweep as step 8** (periodic housekeeping cadence — NOT a per-session hook like session-cost.py; doc drift is sweep-cadence, not session-cadence). The check: (a) grep README.md/CLAUDE.md for layout-path strings and confirm they match the real `ports/<slug>/` pattern on disk rather than a hardcoded stale pattern; (b) diff committed deployment configs against fresh generator output (depends on PIN-7's generator existing — until then, part (b) is a no-op stub). Distinct from session-cost (metrics hook) and from the commit-shape discipline hook (PIN-17): this guards documentation legibility, the inward-facing version of the legibility the harness demands outward.

This is the drift-prevention half of the docs-strategy proposal (approved 2026-07-06); the doc-layer content fixes already landed, this makes re-drift mechanically catchable instead of relying on the next reader noticing.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — the check script (or inline sweep logic) + adding step 8 to ari-backlog/SKILL.md's slow-lane sweep. Out — the generator itself (PIN-7); building doc-drift checks for docs beyond README/CLAUDE/configs (start with the ones in HARNESS §4's ownership map).
**Batch:** docs-strategy
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**
