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
