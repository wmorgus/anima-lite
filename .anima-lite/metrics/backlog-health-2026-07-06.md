# Backlog health: 2026-07-06

First sweep (pre-run4). Per `.claude/skills/ari-port/metrics-spec.md` backlog-health row spec.

## Open pin count by stub level
Open = status `open` only (PIN-4 counted under elsewhere, not here).
- stub:0 — 5 (PIN-1, PIN-6, PIN-7, PIN-8, PIN-17)
- stub:1 — 0
- stub:2 — 0 (all stub:2 pins closed this sweep)

Non-open, for reference: PIN-4 is stub:1, status elsewhere.

## Count by status
- open: 5 (PIN-1, PIN-6, PIN-7, PIN-8, PIN-17)
- scheduled: 0
- in-progress: 0
- done: 11 (PIN-2, 3, 5, 9, 10, 11, 12, 13, 14, 15, 16 — all archived this sweep)
- superseded: 0
- elsewhere: 1 (PIN-4)

## Age of oldest open pin
PIN-1 — captured 2026-07-05 — 1 day old

## Capture-to-done latency (pins closed since last sweep)
No prior sweep — this is the first. All 11 done pins closed and archived this cycle.

| Pin | Captured | Resolution commit date | Latency |
|---|---|---|---|
| PIN-2 | 2026-07-05 | 2026-07-06 (1e349fa) | 1 day |
| PIN-3 | 2026-07-05 | 2026-07-06 (0dc5102) | 1 day |
| PIN-5 | 2026-07-05 | 2026-07-06 (0dc5102) | 1 day |
| PIN-9 | 2026-07-06 | 2026-07-06 (64fa1c7) | 0 days |
| PIN-10 | 2026-07-06 | 2026-07-06 (64fa1c7) | 0 days |
| PIN-11 | 2026-07-06 | 2026-07-06 (64fa1c7) | 0 days |
| PIN-12 | 2026-07-06 | 2026-07-06 (176b84d) | 0 days |
| PIN-13 | 2026-07-06 | 2026-07-06 (cb2b461) | 0 days |
| PIN-14 | 2026-07-06 | 2026-07-06 (176b84d) | 0 days |
| PIN-15 | 2026-07-06 | 2026-07-06 (cb2b461) | 0 days |
| PIN-16 | 2026-07-06 | 2026-07-06 (226bed8) | 0 days |

Median latency: 0 days. All work captured and closed within the sprint that opened it — expected for a backlog built and burned down in two sessions; latency signal only becomes meaningful once pins survive across sessions.

## Un-exported elsewhere count
1 — PIN-4 (home: anima-corps; export target backlog does not yet exist). Resurfaced this sweep; will resurface every sweep until exported or re-dated per cross-repo handling rule.
