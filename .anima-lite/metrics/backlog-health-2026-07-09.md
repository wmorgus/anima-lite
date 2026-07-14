# Backlog health: 2026-07-09

Per `.claude/skills/ari-code-rhetoric/metrics-spec.md` backlog-health row spec. Second sweep (prior: 2026-07-06).

## Open pin count by stub level
Open = status `open` only (PIN-4 counted under elsewhere, PIN-30 under paused, neither here).
- stub:0 — 3 (PIN-6, PIN-8, PIN-17)
- stub:1 — 3 (PIN-7, PIN-18, PIN-20)
- stub:2 — 4 (PIN-21, PIN-22, PIN-24, PIN-26)

Non-open, for reference: PIN-4 is stub:1, status elsewhere. PIN-30 is stub:1, status paused.

## Count by status
- open: 10 (PIN-6, 7, 8, 17, 18, 20, 21, 22, 24, 26)
- scheduled: 0
- in-progress: 0
- done: 14 (PIN-1, 19, 23, 25, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37)
- superseded: 0
- elsewhere: 1 (PIN-4)
- **paused: 1 (PIN-30) — not in this spec's status enum.** The enum above (open/scheduled/in-progress/done/superseded/elsewhere) predates PIN-29's `paused` status (added 2026-07-07, same day as this spec's backlog-health section was presumably last touched). Flagging rather than silently folding PIN-30 into "open" or dropping it from the count — the schema owes `paused` a line.

Total live pins: 26 (10 + 14 + 1 + 1).

## Age of oldest open pin
PIN-6 — captured 2026-07-06 — 3 days old (tied with PIN-7, PIN-8, PIN-17, PIN-18, all captured the same day).

## Capture-to-done latency (pins closed since last sweep)
**Caveat on this row's rigor:** dates below are the self-reported dates in each pin's Resolution paragraph, not git-log-verified commit dates against the Resolution line specifically — this sweep did not run a per-file `git log` pass. Per the honest-stub rule, flagging this gap rather than presenting these as verified. A future sweep should either script this (git blame the Resolution line) or accept self-reported dates as the standing convention and say so in the spec.

| Pin | Captured | Resolution date (self-reported) | Latency |
|---|---|---|---|
| PIN-1 | 2026-07-05 | 2026-07-07 | 2 days |
| PIN-19 | 2026-07-06 | 2026-07-07 | 1 day |
| PIN-23 | 2026-07-07 | 2026-07-08 | 1 day |
| PIN-25 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-27 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-28 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-29 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-31 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-32 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-33 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-34 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-35 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-36 | 2026-07-07 | 2026-07-07 | 0 days |
| PIN-37 | 2026-07-08 | 2026-07-08 | 0 days |

Median latency: 0 days, same pattern as the first sweep — the reorient batch (PIN-25 through PIN-37) was captured and closed same-day, repeatedly. Latency signal still isn't meaningful yet; every closed pin so far belongs to a fast-moving design sprint, not a backlog item that sat and waited.

## Un-exported elsewhere count
1 — PIN-4 (home: anima-corps; export target backlog still does not exist — confirmed this sweep, `anima-corps/` has no backlog directory). Resurfaces every sweep per cross-repo handling rule until exported or re-dated.
