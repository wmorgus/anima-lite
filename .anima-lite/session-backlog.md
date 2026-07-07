# Session backlog — working order

Operator-owned working order for live sessions. The backlog proper (`backlog.md` + `pins/`) deliberately asserts no priority ranks — batches and status only, per `.claude/skills/ari-backlog/SKILL.md`. This file is where the intra-session order actually lives: a ladder of pointers, re-cut freely at any working session. Pin files stay the source of truth for content; this file only asserts order. Committed like everything under `.anima-lite/`, but cheap to rewrite — no shaping ceremony, no lifecycle.

Updated: 2026-07-07

## Ladder

1. **PIN-26 ripple** — the remaining big build. Multi-leg work-type: ari-argue multi-target intent, per-target substrate sections, ari-port per-leg execution + cross-leg coherence check, ledger shared-origin entries. Two unratified proposals to settle at design time: break-reopens-all-legs, sequential-proto-first. RESOLUTION.md now exists as the ripple apex — 33 feeds 26 directly.
2. **PIN-23 self-spine re-probe** — spine stale at 28d8464; refresh trigger fired 3× on 2026-07-07 (intake, resolution, read). Deliberately held until after 26 lands so the re-probe runs once, not per-change. Good `/ari-map` rerun.
3. **PIN-30 run5 resume** — paused A/B port; proves PIN-21/22 spine-completeness work. The whole write pipeline changed since suspension (intake, resolution, read) — manifest re-check mandatory on resume.
4. **PIN-25c** — incremental spine maintenance design (spine as product, update-on-change). Design-only; pairs with 23's fresh baseline.

**Opportunistic (ride along with any commit):** PIN-32 — intent.md work-type enum needs `harness-change` (hit twice).

## Wider tab (outside this repo, parked per run-through-Anima ruling)

- anima-core self-directed backlog — chunking + semantic retrieval is #1
- self-ingest step 2 — constellation cites wiring
- Tier-1 merge + backfill
- papers — 031 next build task
