# Session backlog — working order

Operator-owned working order for live sessions. The backlog proper (`backlog.md` + `pins/`) deliberately asserts no priority ranks — batches and status only, per `.claude/skills/ari-backlog/SKILL.md`. This file is where the intra-session order actually lives: a ladder of pointers, re-cut freely at any working session. Pin files stay the source of truth for content; this file only asserts order. Committed like everything under `.anima-lite/`, but cheap to rewrite — no shaping ceremony, no lifecycle.

Updated: 2026-07-07

## Ladder

1. **PIN-26 ripple — prove it** — machinery built (renames executed, intent-artifact mode, per-leg execution + coherence check, ledger shared-origin entry). Stays open until a real N-leg feature runs through it end to end.
2. **PIN-23 self-spine re-probe** — spine stale at 28d8464; held until after 26 lands so the re-probe runs once, not per-change.
3. **PIN-30 run5 resume** — paused A/B port; proves PIN-21/22 spine-completeness work. Manifest re-check mandatory on resume — write pipeline has changed under it.
4. **PIN-25c** — incremental spine maintenance design (spine as product, update-on-change). Design-only; pairs with 23's fresh baseline.

## Wider tab (outside this repo, parked per run-through-Anima ruling)

- anima-core self-directed backlog — chunking + semantic retrieval is #1
- self-ingest step 2 — constellation cites wiring
- Tier-1 merge + backfill
- papers — 031 next build task
