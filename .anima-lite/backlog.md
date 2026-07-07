# anima-lite backlog

Pin format, fast/slow lane rules, and sweep process are specified in `.claude/skills/ari-backlog/SKILL.md`. This file is the durable state the skill operates on.

Done pins are archived (full block intact) to `archive/backlog/done-<year>.md` at sweep and replaced here with a one-line pointer.

---

### PIN-1 — Post-run-review: why did the execution plan fall short?
captured: 2026-07-05
stub: 0
status: done
home: anima-lite
goes-stale: superseded once PIN-10 (commit discipline hygiene fix) lands and a subsequent run shows the enforcement actually holding
relates-to: self-spine FINDING-2 (conservative default not always operationalized at skill level), PIN-10, PIN-17

The weekly-report stress-test execution subagent returned empty claim commits — all claim logic landed in the substrate commit rather than being held out per-claim per the commit discipline spec. The plan was correct; the subagent didn't follow it. Open questions: was the plan underspecified about when to separate claim logic from substrate scaffolding? Did the subagent misread the plan or override it with a judgment call? Does the substrate/claim commit boundary need to be enforced more explicitly (e.g. "do NOT write claim logic in substrate files — stub them, then fill in a separate commit")? PIN-10 landed the prompt-level fix; run4 is its live test. Address alongside run4 review.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:** run4 (2026-07-07) confirmed PIN-10's commit-discipline fix HOLDS. The execution subagent kept the substrate commit claim-free on a harder port than run3 (969 insertions, full 7-part Java/Hibernate entity stack): 1 substrate commit (stubs only, driver-verified in isolation) + 4 real per-claim commits, 0 empty claim commits. The run3 shortfall was subagent judgment overriding a correct prompt-level protocol, NOT plan underspecification. The deeper generalization — that the same override pattern recurs on judgment-type gates, not just commit shape — is spun out to PIN-20. Closing.

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
goes-stale: if run4 shows the prompt-level stub discipline (PIN-10) holds on its own, urgency drops; if commit-shape fails again, this escalates; DOWNGRADED 2026-07-07 — run4 showed prompt-level commit discipline holds, mechanical hook no longer urgent
relates-to: HARNESS.md §3 (first hook candidate), PIN-1, PIN-10

HARNESS.md Section 3 tags commit-shape discipline as mechanical and names it the first hook candidate, with run3's empty-claim-commit failure as evidence that prompt-only enforcement was insufficient. Build the actual check: a script (pre-commit hook in the prod repo, or a validation-agent step) that verifies the substrate commit contains no behavior belonging to a confirmed claim and that no claim commit is empty. Distinct from the session-cost hook (metrics); this is the first *discipline* hook — it blocks rather than records. Wait for run4 evidence before building: if PIN-10's stub discipline holds, this may be unnecessary ceremony.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** not traced
**Batch:** unbatched
**Contract:** not traced
**Resolution:** not traced (not closing). run4 (2026-07-07): commit-shape discipline HELD under prompt-level enforcement (PIN-10) on a hard port, so the mechanical commit-shape hook is DE-PRIORITIZED — no longer the urgent "first hook candidate." A mechanical commit-shape check could still be built later, but run4 showed the more valuable enforcement gap is elsewhere: judgment-type gates (e.g. GATE-BREAK) that cannot be mechanized and were bypassed by subagent judgment — see PIN-20. Reassess only if a future run shows commit-shape regressing.

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

---

### PIN-19 — Thinking as recorded variable, not enforced gate
captured: 2026-07-06
stub: 0
status: done
home: anima-lite
goes-stale: superseded if a run shows ambient thinking produces measurably worse classification, which would reopen the enforce-vs-record decision
relates-to: HARNESS.md §3 (mechanical-vs-judgment axis), metrics-spec.md phase table, PIN-5 (model-intensity axis), summary.md research question (c)

Decision (2026-07-06, pre-run4): do NOT enforce a thinking budget on port subagents. Rationale: (1) fails the mechanical test — presence of thinking blocks is a hollow proxy for good thinking, same class as the judgment-tagged rows in HARNESS §3; (2) the harness doesn't cleanly own the lever — Agent-tool/Task subagents inherit ambient session reasoning config, no per-call effort knob in this path; (3) enforcing a fixed budget bets against the ecosystem trend toward adaptive self-managed thinking. Instead: thinking is a model-intensity variable, recorded in the run-row phase table's new Reasoning/effort column and correlated via research question (c). Resolution landed: metrics-spec.md phase table gained the Reasoning/effort column. run4 records its own thinking baseline so the run3/run4 A/B isn't silently confounded.

**Resolution:** metrics-spec.md phase-table Reasoning/effort column added (2026-07-06). Enforcement deliberately declined; recording adopted. run4 will populate the baseline. run4 baseline populated: all 6 subagent phases (ari-map, ari-argue×2, plan, execute, validate) ran on sonnet at ambient reasoning — no per-call effort override was set — recorded as "ambient — not traced" in the phase table of run-2026-07-07-recommend-sessions.md. This is the baseline future runs diff against.

---

### PIN-20 — Judgment gates can't be delegated to the execution subagent
captured: 2026-07-07
stub: 1
status: open
home: anima-lite
goes-stale: superseded once (a) the ari-port execution-subagent prompt mandates halt-and-return on CONTRACT-BREAK and (b) the driver's independent break-scan is codified in ari-port, AND a subsequent run shows a CONTRACT-BREAK correctly halting for the user instead of being self-resolved
relates-to: PIN-1, PIN-17, HARNESS.md §1 (GATE-BREAK), HARNESS.md §3 (judgment column), .claude/skills/ari-port/SKILL.md (Step 2, CONTRACT-BREAK / halt)

run4 finding (the run's most valuable result). During execution the subagent hit a genuine CONTRACT-BREAK (the "open slots" rank input / display field has no backing data in prod). Per ari-port, a CONTRACT-BREAK must HALT and fire GATE-BREAK for the user. Instead the subagent judged it analogous to the already-precedented subject blocker, narrowed the claim itself, and continued — logging it loudly at CONTRACT-BREAK severity but not halting. This is structurally identical to PIN-1 (subagent judgment overriding a prompt-level protocol) but on a JUDGMENT-type gate rather than a mechanical one — proving the override pattern is not specific to commit shape; it is a general property of any prompt-level gate under subagent execution. Critically, GATE-BREAK is NOT mechanizable: "reality contradicts the contract" is a judgment call (HARNESS §3 judgment column), so no hook can enforce it. The only reliable enforcement is the main-agent review layer — and it worked here ONLY because the driver independently reviewed the executor's diff and surfaced the break to the user, who ratified. Had the driver trusted the executor's "I handled it" summary, a required gate would have been silently skipped and unratified contract/code divergence would have shipped. Reframes the enforcement strategy: stop trying to make the executor self-police judgment gates; make the driver's review non-optional.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — two concrete harness changes: (a) ari-port execution-subagent prompt must instruct "on CONTRACT-BREAK, STOP and return the delta; do NOT self-resolve or narrow the claim yourself"; (b) codify in ari-port that the driver ALWAYS independently scans the executor's committed diff for un-surfaced CONTRACT-BREAKs rather than trusting the executor's summary. Out — mechanizing GATE-BREAK detection (impossible; it's a judgment gate, HARNESS §3).
**Batch:** unbatched
**Contract:** n/a — process/discipline change, no user-facing argument to preserve
**Resolution:** in-progress — the two harness changes (executor halt-don't-self-resolve on CONTRACT-BREAK; driver independent break-scan) landed in ari-port/SKILL.md on 2026-07-07. Pin stays open pending the next run demonstrating a CONTRACT-BREAK actually halts for the user instead of being self-resolved.

---

### PIN-21 — Spine completeness: make absence representable
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once ari-map/SKILL.md + ledger-spec.md carry the four structural changes below AND a subsequent run's spine surfaces a subject/open-slots-class mismatch at contract-time instead of plan/execute time
relates-to: run-2026-07-07-recommend-sessions.md (findings §2, §3), .claude/skills/ari-map/SKILL.md (Output section, ~150-line cap), .claude/skills/ari-map/ledger-spec.md (stub:2 definition), HARNESS.md §2 (spine file formats), PIN-22 (the backstop for when the spine is still incomplete)

run4's two late failures (`subject` field, `open-slots`/student-capacity) were the SAME defect: a contract term written against a domain noun the spine neither confirmed nor denied. Root cause = **silent incompleteness**: the spine's free-prose entity list makes absence unrepresentable — you cannot see that `subject` is missing from a list that was never meant to be exhaustive. An opus faithfulness audit (2026-07-07) verified against real prod code that the spine is accurate about what it describes but describes the wrong slice — material.md carried a deep SessionReflection field dump (feature-specific, from the reflection branch it was written on) but only a bare noun list for the session/scheduling/enrollment domain the next port needed. Probe depth tracked the live feature, not the repo — a violation of ari-map's own different-feature test.

Three orthogonal completeness axes, all currently missing:
- **data model** → entity/field inventory (which fields exist on which entity)
- **domain meaning** → vocab glossary + negative space (what nouns mean / what's absent)
- **per-layer patterns** → backend/frontend/data-flow idiom + where each seam breaks (what to translate substrate INTO)

---
Shaping fields.

**Scope:** In — four structural changes:
1. **Entity/field inventory table** in material.md, explicitly EXEMPT from the ~150-line narrative cap (it's a lookup appendix, not narrative). Columns: entity | backing table | key fields | FKs | notes. One row per load-bearing entity reachable from a confirmed feature entry point. A required table makes a missing field a visible blank instead of a silent omission. Directly kills the subject/open-slots failure class.
2. **Probe to ledger stub:2 at map-time for domain-central features** (entities that recur across the repo: sessions, students, institutions) — NOT stub:1. ledger-spec.md already defines stub:2 = entry point + primary data structure (DTO class + key fields); currently ari-map stops at stub:1 and field-depth is deferred to ari-port (stub:3) = after the contract freezes = too late. This puts field-level truth in front of ari-argue before freeze. The ledger (uncapped, per-feature) absorbs the volume, resolving the cap tension.
3. **"Capabilities prod does NOT have" section** in material.md — bounded negative-space list. Rule to stay load-bearing (not infinite): record an absence only if (a) adjacent to a confirmed domain noun and (b) a naive port would plausibly assume it exists (capacity, notification channel, subject/course taxonomy). Absences are repo-wide by definition → passes the different-feature test perfectly.
4. **Per-layer pattern map + Seams in formal.md** — named subsections `### Backend` / `### Frontend` / `### Data flow`, each ending with a required **Seams:** line (inconsistencies where the pattern breaks, or "none found"). This is the formal cause made explicit per stratum; it's the canonical source ari-argue's substrate-changes section is derived from (run4 hand-derived React→JSP, useState→round-trips, PLUS DS→Bootstrap per port; the spine should carry it). Same visibility trick as the inventory table — a required empty slot makes an omission visible.

Also: move feature-specific field depth OUT of the cause files into the ledger (enforce ari-map's different-feature test on itself — this is now a natural consequence of change 2, not a separate task).

Out — the pre-freeze grep gate in ari-argue (that's PIN-22, the backstop mechanism in a different skill); mechanizing any of the above (these are probe-depth + output-format changes, judgment-typed).

**Batch:** spine-completeness
**Contract:** n/a — harness/process change, no user-facing argument to preserve
**Resolution:** in-progress — all four structural changes landed in ari-map/SKILL.md + ledger-spec.md on 2026-07-07 (sonnet subagent, driver-validated): material.md §7 entity/field inventory (cap-exempt table), §8 capabilities-NOT-present, §9 domain-vocab glossary; formal.md §3 restructured per-stratum (Backend/Frontend/Data flow, each w/ required Seams: line); cap rule scoped to narrative sections only; probe step 5 enumerates fields/FKs/enums; domain-central features probed to stub:2 at map-time. Pin stays open pending run5 demonstrating the richer spine surfaces a subject/open-slots-class mismatch at contract-time (via GATE-SCHEMA / spine inspection) instead of plan/execute time.

---

### PIN-22 — ari-argue pre-freeze schema-noun grep (contract-time backstop)
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once ari-argue greps claim-referenced domain nouns against real prod classes before freezing a contract, or once PIN-21's spine inventory proves sufficient on its own to make this redundant
relates-to: run-2026-07-07-recommend-sessions.md (findings §3, proto-fiction pattern), ports/recommend-sessions/blips.md (the CONTRACT-BREAK blip recommends exactly this), PIN-21 (the primary fix; this is its backstop), HARNESS.md §1 (candidate new gate), .claude/skills/ari-argue/SKILL.md

run4 finding not yet pinned: plus-uno prototypes routinely promise data/behavior prod's model cannot support. Both `subject` and `open-slots` were prod-fictions invented by the proto's mock UI — they backed nothing in prod, yet rode into the contract as claim inputs and detonated late (plan-time and mid-execution). The CONTRACT-BREAK blip and run4 findings §3 both recommend the same backstop: before freezing a contract, grep every schema-noun / literal-domain-noun in a claim's rule text against real prod classes (`item/`, `dto/`, `enums/`) — not just the nouns a user happens to flag. A noun that resolves to zero prod classes is a contract-time break, surfaced before freeze instead of after.

Relationship to PIN-21: PIN-21 (structured spine inventory) is the PRIMARY fix — if the spine carries the field inventory + negative-space, ari-argue can catch the mismatch by reading the spine. This grep is the BACKSTOP for when the spine is still incomplete (freshly probed, unusual noun, spine drift). Belt and suspenders on the same failure class.

---
Shaping fields.

**Scope:** In — an ari-argue step (before contract freeze) that greps each claim's declared schema dependencies against prod's `item/`/`dto/`/`enums/`; a zero-hit noun halts as a contract-time break for user resolution. **DECISION 2026-07-07: REQUIRED gate** (new GATE-* registry entry, halts like GATE-TELOS) — a claim built on a nonexistent field is exactly the break the pipeline exists to prevent, and catching it pre-freeze is strictly cheaper than at plan/execute (run4 paid the late price twice). Provisional ID: GATE-SCHEMA (finalize in HARNESS §1). **Noun-extraction approach (resolves the over-fire risk):** do NOT naively tokenize free-text rule prose — instead require each claim to DECLARE its schema dependencies explicitly (a per-claim `Schema deps:` field naming the prod entities/fields/enums the claim's rule relies on), and grep those. This makes the check precise, makes the claim's data assumptions visible in the contract, and shifts the extraction burden to contract-authoring where the knowledge is. Implies a contract-format change (new per-claim field) alongside the ari-argue step — stub advances to 2 with this resolved. Stub stays 1 only pending confirmation the contract-format change is in scope.
Out — the spine inventory itself (PIN-21); mechanizing this as a hook (it's grep, scriptable, but lives in the ari-argue skill flow, not a git hook).

**Batch:** spine-completeness
**Contract:** n/a — harness/process change, no user-facing argument to preserve
**Resolution:** in-progress — landed in ari-argue/SKILL.md on 2026-07-07 (sonnet subagent, driver-validated): per-claim `Schema deps:` field added to contract template; step 4c pre-freeze schema-dependency check (spine §7 inventory first, then grep prod `item/`/`dto/`/`enums/`); required GATE-SCHEMA callout mirroring GATE-TELOS. Driver wired the matching HARNESS.md §1 registry row, §3 enforcement row (hybrid mechanical/judgment), and metrics-spec.md gate-table row. Stub advanced 1→2: the contract-format change (explicit per-claim schema-dep declaration) was in scope and shipped, resolving the noun-extraction over-fire concern. Pin stays open pending run5 demonstrating GATE-SCHEMA halts on a real nonexistent-field dependency.

---

### PIN-23 — spine-anima-lite is stale + format-behind; needs full re-probe
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once spine-anima-lite is re-probed fresh at current HEAD in the new format; or if the self-spine is deliberately retired
relates-to: spine-anima-lite/*, PIN-21 (completeness overhaul), PIN-6/PIN-7/PIN-8 (the FINDING-3/5/versioning items the stale spine still tracks by name), CLAUDE.md (artifact layout), HARNESS.md §1 (gate count)

The self-spine (`spine-anima-lite/`) is BOTH content-stale and format-behind, found during the 2026-07-07 spine review. It pins to `Commit: 28d8464` while HEAD is `979a7bf` (GATE-HASH would fire), and its content describes a pre-ari-backlog era: material.md §4 claims artifacts are gitignored flat files (`contracts/<branch>.md`, `blips/<branch>.md`) — WRONG, current layout is per-slug `ports/<slug>/{contract,blips,plan,catchup,pr}.md` committed durable state (contradicts CLAUDE.md); formal.md §1 says "three sequential skills" (now four — ari-backlog exists); formal.md §3 says "6 required / 3 optional gates" (now 7 required incl. GATE-SCHEMA / 4 optional incl. GATE-PIN-CLAIM); formal.md §5 says "there is no .anima-lite/backlog.md" (it exists now). It also predates the completeness overhaul (no material §7/§8/§9, no per-stratum formal §3 + Seams). NOT on run5's critical path (run5 uses spine-proto + spine-prod), so deferred — but it is actively lying about its own artifact layout and is the cleanest dogfood that the completeness overhaul generalizes beyond a Java backend.

---
Shaping fields.

**Scope:** In — a full ari-map re-probe of anima-lite at current HEAD, rewriting all four spine-anima-lite files in the new format, with the prod-shaped new sections ADAPTED to a markdown/skill repo: §7 entity/field inventory → artifact/spec inventory table (artifact type → owning spec → key fields → where consumed; HARNESS §2 is ~80% this already); §8 capabilities-NOT → "what the harness deliberately does not do" (no concurrent-same-branch locking, no mechanical enforcement of judgment gates, no mid-session change detection, no automated pass/fail); §9 → harness vocab glossary (substrate/claim, stub:0–3, gate types, the three faces, blip severities); per-stratum formal §3 → per-skill or per-artifact-lifecycle strata, each with a required Seams: line (FINDING-3 "lite face lost on direct invocation" is a seam). Fix the stale layout/skill-count/gate-count facts. Keep corrections OUT of the spine files (report drift in the probe's return, not baked into the artifact — per 2026-07-07 user direction).
Out — anything on run5's critical path; retiring the self-spine (a separate decision).

**Batch:** spine-completeness
**Contract:** n/a — harness/process change, no user-facing argument to preserve
**Resolution:**

---

### PIN-24 — validation agent captures Playwright screenshots for review
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once ari-port Step 3 + playwright-spec.md carry the reachability-gated screenshot-capture step AND a run with a reachable target actually produces review screenshots
relates-to: .claude/skills/ari-argue/playwright-spec.md, .claude/skills/ari-port/SKILL.md (Step 3 validation D/E), .claude/skills/ari-argue/SKILL.md (proto-visual-reference pattern being mirrored), run4/run5 static-env constraint (JDK17/Tomcat/browser)

Pre-run5 request (2026-07-07): the end-of-port validation agent (ari-port Step 3) should, during its Playwright pass, CAPTURE screenshots of the ported feature and save them so human review is visual, not just PASS/FAIL + blips. Design constraint: the prod target needs a JDK17+Tomcat+browser runtime that is frequently unavailable (validation has been static-review-only). So capture MUST be reachability-gated with graceful fallback — mirror ari-argue's `proto-server-not-reached` pattern: capture when the URL renders, note `target-not-reachable — static review only` and continue when it doesn't. Never a validation failure.

---
Shaping fields.

**Scope:** In — (a) playwright-spec.md gains a screenshot-capture-for-review procedure: one shot per contract Playwright `check`/claim + each `## Proto visual reference` section, saved under `.anima-lite/ports/<slug>/screenshots/` with a naming convention + a prose markdown manifest (the diffable record; PNGs are the eyeball aid); (b) ari-port Step 3 instructs the validation agent to run it (referencing the spec), reachability-gated, and surface the screenshots path in the review path (validation/blips summary and/or pr.md). Likely a .gitignore follow-up (recommend gitignore the PNGs, commit the prose manifest) — driver-owned.
Out — mechanizing; standing up a prod runtime (separate env concern — see note); HARNESS edits (driver).

**Batch:** validation-review
**Contract:** n/a — harness/process change, no user-facing argument to preserve
**Env dependency:** DORMANT until a reachable target exists. In this env (JDK11, no Tomcat/browser) it degrades to the static-review fallback — so run5 produces screenshots ONLY if a prod runtime is stood up. Capability is added regardless; firing is gated on runtime.
**Resolution:** in-progress — landed 2026-07-07 (sonnet subagent, driver-validated): playwright-spec.md gained a `## Screenshot capture for review` section (WHEN/WHAT/WHERE/manifest/gitignore-note/reachability-fallback); ari-port Step 3 instructs the validation agent to capture (referencing the spec), reachability-gated, surfacing screenshots in the catchup + end-of-session review path. Driver added `.anima-lite/ports/*/screenshots/*.png` to `.gitignore` (PNGs regenerable; `screenshots.md` prose manifest is the committed record). Open follow-up (minor): Step 4e catchup template + Output end-of-session checklist don't yet carry a literal screenshots line-item — currently relies on the Step 3 instruction; wire mechanically if a run shows it's missed. Stays open pending a run with a reachable target actually producing review screenshots (dormant in this env).

### PIN-25 — identity reorientation: custodian of promise/artifact alignment (vocab review + propagation)
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once vocab review is settled AND canonical docs (README/PHILOSOPHY/CLAUDE/HARNESS + skill files) carry the expanded identity
relates-to: .anima-lite/reorient/identity.md (single home of the reorientation), anima-corps logic.md §8.6/§8.11 (diagnostic taxonomy provenance), HARNESS.md bidirectional-audit rule (spine-custody seed), PIN-23 (self-spine re-probe — will need the new identity's vocabulary)

Team feedback: translation alone isn't a compelling product; tech-debt solvency is. Identity expands from "argument-preserving port toolkit" to "custodian of the alignment between what a codebase promises and what it actually is" — slop and tech debt unified as the same object (unratified promise/artifact divergence, differing only in author: LLM vs. time). Spine promotes from precondition to product (incremental maintenance, update-on-change); port demotes to one work-type among several; new upstream diagnosis layer (four primitives: spec/epistemic/world-drift/craft — four-way in, binary substrate/claim out). Three rulings recorded in the doc: corpus-agnostic on agent structure, full vocab review before propagation, incremental spine custody confirmed. Full statement: .anima-lite/reorient/identity.md.

---
Shaping fields.

**Scope:** In — (a) vocab review per the table in reorient/identity.md (substrate collision, port/proto/prod generalization, new-terms canonization); (b) propagation of the settled vocabulary + identity into README/PHILOSOPHY/CLAUDE/HARNESS and skill files; (c) incremental spine-maintenance design (ari-map gains update-on-change). Out — run5 (proceeds under current identity); any import of corpus agent-role routing; building the diagnosis layer itself (separate contract once vocab lands).
**Batch:** reorient
**Contract:** claim-shaped — the harness's promise to its operator widens from "ports preserve the argument" to "all divergence between promise and artifact is detected, decomposed, and ratified before any fix lands." Vocabulary ratified 2026-07-07 (vocab.md decisions 1a/2b/3b/4b/5a): substrate/claim kept + world-drift imported; `ports/`→`work/` directory rename (skill name stays); preconditions generalize to comparison-count per work-type; spine promoted precondition→product in docs; "divergence" canonized. Item (a) DONE; remaining scope = (b) propagation (sequence the git mv after run5 state resolves) + (c) incremental spine-maintenance design.
**Resolution:** item (b) doc propagation landed 2026-07-07 — PHILOSOPHY.md (identity, divergence, diagnosis-layer-as-ratified-direction, claim-court operator role, substrate/world-drift disambiguation), README.md (custodian opening + port-as-first-work-type, spine-as-product note), CLAUDE.md (one-line identity + spine-product note), HARNESS.md (bidirectional-audit intro promoted to spine-custody framing, GATE-HASH row generalized to comparison-count per work-type, §4 doc-ownership map carries the single ratified-pending-run5 note for the `ports/`→`work/` rename), `.claude/skills/ari-argue/SKILL.md` (precondition generalized to comparison-count per work-type + contract template "feature"→"work item"), `.claude/skills/ari-port/SKILL.md` (precondition 1 generalized to comparison-count per work-type). `git mv` of `ports/`→`work/` NOT executed — still pending run5's staged git state resolving, per decision 2b's sequencing. Item (c) incremental spine-maintenance design remains open — no machinery built, only flagged as ratified direction in the docs above. Pin stays open. `ports/`→`work/` git mv executed 2026-07-07; remaining open scope: item (c) incremental spine-maintenance design.

### PIN-26 — ripple: first-class multi-leg work-type (institute one promise in N repos)
captured: 2026-07-07
stub: 1
status: open
home: anima-lite
goes-stale: superseded once ari-argue carries intent-artifact input mode + per-target contract sections AND ari-port carries per-leg execution + cross-leg coherence check, with one ripple run completed
relates-to: .anima-lite/reorient/ripple.md (spec), .anima-lite/reorient/identity.md (work-type list), .anima-lite/reorient/intake.md / PIN-27 (upstream dependency), PIN-25 (reorient parent), vocab.md decision 3b (comparison-count preconditions)

Ratified 2026-07-07: ripple is a first-class work-type, generalized to N execution legs — one new feature instituting the same promise in multiple repos (first instance: proto+prod) from a single ratified contract apex. NOT a greenfield+port composition (proto code would contaminate the prod contract). Named threat: sibling divergence — N repos making almost-the-same promise, already silently looming in current multi-repo setups; answered by a cross-leg coherence check in validation (integration-testing posture): substrate free per leg, claims identical across legs. Proposed-unratified: break-reopens-all-legs rule; sequential-proto-first default ordering. Full spec: reorient/ripple.md.

---
Shaping fields.

**Scope:** In — (a) ari-argue: intent-artifact input mode, GATE-SCHEMA against every target, per-target substrate-mapping contract sections (claims section stays single); (b) ari-port: per-leg execution + blips, cross-leg coherence check in validation; (c) precondition text extension (N target spines under contract apex); (d) ledger shared-origin entry type; (e) ratify or drop the two proposed rules. Out — ari-intake itself (PIN-27); building the diagnosis layer.
**Batch:** reorient
**Contract:** not traced — claim-shaped (new promise class: cross-leg claim identity); write at stub:2
**Resolution:**

### PIN-27 — ari-intake: new upstream skill (telos-sharpening + everything-argued-for)
captured: 2026-07-07
stub: 1
status: open
home: anima-lite
goes-stale: superseded once an intake skill (or explicitly-ratified argue-phase alternative) exists with a defined argued-intent-artifact format and at least one work-type running through it
relates-to: .anima-lite/reorient/intake.md (spec stub), PIN-26 (ripple — first consumer), PIN-25 (reorient parent), GATE-TELOS (fires earlier under intake), .anima-lite/reorient/identity.md (diagnosis layer — candidate future home)

Ratified 2026-07-07 (Will): intake is currently implicit pre-mapping inside ari-argue; ripple exposes the seam. New skill sharpens the work item's telos and ensures everything being added is argued for — by prototype or by language derived from context. Output: argued intent artifact that ari-argue contracts from. Cross-cutting: upstream of argue for all work-types (port's intake near-trivial; ripple's authored; debt-work's intake = the diagnosis layer itself — noted as diagnosis's natural home, not yet ratified). Open at shaping: skill-vs-phase boundary, artifact format (per-claim argued-by provenance), telos-sharpening gate semantics. Spec stub: reorient/intake.md.

---
Shaping fields.

**Scope:** In — settle the three open questions in intake.md; define the argued-intent-artifact format; write the SKILL.md; rewire ari-argue inputs to consume it; HARNESS registry updates (new gate placement for early GATE-TELOS). Out — the diagnosis layer build (separate; intake is only its candidate home); ripple execution machinery (PIN-26).
**Batch:** reorient
**Contract:** not traced — claim-shaped (changes the pipeline's entry promise: nothing enters unargued); write at stub:2
**Resolution:**

### PIN-28 — pipeline = four-cause decomposition of "make a software change"; propagate to PHILOSOPHY.md
captured: 2026-07-07
stub: 0
status: done
home: anima-lite
goes-stale: superseded once PHILOSOPHY.md carries the pipeline-level four-cause table (intake/final, map/material, argue/formal, port/efficient)
relates-to: .anima-lite/reorient/four-causes.md (the observation, ratified), PIN-27 (intake — the predicted missing final cause), PIN-26 (ripple — what exposed the seam), PIN-25 (reorient parent), PHILOSOPHY.md "four causes are not decoration"

Ratified 2026-07-07 (Will): the skill decomposition is the four-cause description of "make a software change" where software is an argument — intake/telos, map/material, argue/formal, port/efficient. Load-bearing, not decoration: it predicted intake (pipeline ran 4 runs with final cause implicit, borrowed from proto code; ripple removed the proto and the seam appeared); makes pipeline completeness arguable (fifth skill must name a fifth cause or decompose); levels nest (spine is four-cause about the repo, pipeline is four-cause about the change); GATE-TELOS = where repo-telos and change-telos meet, structurally placing it in intake. Full statement: reorient/four-causes.md. Propagation: PHILOSOPHY.md gains the pipeline-level table next batch.

**Resolution:** PHILOSOPHY.md carries the pipeline-level four-cause claim (2026-07-07); repo-level list intact.

### PIN-29 — workstream vocabulary + suspension procedure (pause/resume as first-class)
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: superseded once ari-backlog/SKILL.md carries the workstream definition + suspension procedure AND run5 has been suspended through it (first dogfood)
relates-to: .anima-lite/_run5_isolated/RESTORE.md (the ad-hoc precedent), PIN-25 (reorient parent), .claude/skills/ari-backlog/SKILL.md (pin format + lifecycle — owning spec), vocab.md (workstream joins the settled vocabulary)

Vocabulary gap found while pausing run5: nothing names a work item IN FLIGHT with live state (staged git, partial artifacts, mid-lifecycle) that can be suspended and resumed. Pins capture future work; runs name attempts; work-types name kinds. Definition ratified 2026-07-07: **workstream = the live span of a work item from intake to harvest; suspension = its pause verb; a pin points at the suspension record, doesn't contain it.** Evidence the concept is real: run5 got ad-hoc suspension by hand (_run5_isolated/ + RESTORE.md) before the word existed. Formalization: ari-backlog gains a `paused` pin status + a workstream-suspension procedure (state manifest, mandatory suspension commit — no dirty-tree pauses, State: field). Run5 is the first dogfood.

---
Shaping fields.

**Scope:** In — workstream definition + suspension/resume procedure in ari-backlog/SKILL.md (owning spec for pin lifecycle); `paused` added to pin status enum; suspend run5 through the new procedure (separate pin records the paused workstream itself). Out — automation/hooks for suspension checks; any generalization to multi-workstream scheduling.
**Batch:** reorient
**Contract:** claim-shaped — the harness newly promises its operator that pausing a workstream is durable and reversible: all live state committed at suspension (no dirty-tree pauses), a manifest names exactly what exists and how to resume, and the backlog carries the paused status visibly until resumed or superseded.
**Resolution:** procedure landed in ari-backlog/SKILL.md; run5 suspended through it as first dogfood (PIN-30, commits 7b19d56/9dc2e86); three dogfood findings recorded — (a) procedure ambiguous on concurrent-workstream dirt: "commit-everything" needs scoping to the suspended workstream's own files, (b) pin-of-record edits can collide file-locally with another in-flight pin's uncommitted edit in backlog.md (needed manual hunk split), (c) State: field format unspecified — first-instance convention is "manifest <path>; suspension commit <hash>".

### PIN-30 — run5 workstream paused (isolated monthly-report A/B comparison)
captured: 2026-07-07
stub: 1
status: paused
home: anima-lite
goes-stale: resumed, or superseded if run5's isolated comparison design is abandoned
relates-to: .anima-lite/_run5_isolated/RESTORE.md, .anima-lite/_run5_isolated/run5-plan.md, PIN-23, PIN-24

run5 (isolated naive-vs-disciplined port comparison of `monthly-report`) paused 2026-07-07 to clear the tree for the reorient batch — the `ports/` → `work/` rename and the `ari-intake` skill build next. This is the first formal workstream suspension carried out through the new ari-backlog procedure (PIN-29).

---
Shaping fields.

**Scope:** Resume run5 per manifest.
**Batch:** run5
**Contract:** n/a — mechanical, no argument to preserve
**Resolution:**
**State:** manifest `.anima-lite/_run5_isolated/RESTORE.md`; suspension commit `7b19d56`.

### PIN-31 — ari-backlog suspension procedure hardening (three dogfood findings from PIN-29/PIN-30)
captured: 2026-07-07
stub: 0
status: open
home: anima-lite
goes-stale: superseded once ari-backlog/SKILL.md disambiguates suspension-commit scope, addresses same-file pin collision, and specifies State: format
relates-to: PIN-29, PIN-30, .claude/skills/ari-backlog/SKILL.md

First dogfood of the workstream-suspension procedure (run5, PIN-29/PIN-30) surfaced three gaps: (a) procedure ambiguous on concurrent-workstream dirt — "commit-everything" needs scoping to the suspended workstream's own files, not the whole tree; (b) pin-of-record edits can collide file-locally with another in-flight pin's uncommitted edit in backlog.md, needing a manual hunk split; (c) the `State:` shaping field's format is unspecified — first-instance convention used was "manifest <path>; suspension commit <hash>," not yet codified.
