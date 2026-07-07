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
