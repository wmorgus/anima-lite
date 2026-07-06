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
