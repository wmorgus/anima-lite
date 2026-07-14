# Metrics summary

Standing header — the research questions this data serves. Schema for every artifact under `.anima-lite/metrics/`: `.claude/skills/ari-code-rhetoric/metrics-spec.md`.

- (a) Harness cost-benefit threshold — at what feature complexity does the ceremony (spine + contract + plan + validation + reconcile) pay for itself, versus a lighter-weight approach costing less for the same quality?
- (b) Quality-vs-token trend across calibration runs — is the harness getting better outcomes (fewer FAILs, fewer review-suggested blips) at similar or falling token cost, or is quality improvement being bought with token inflation?
- (c) Model-intensity correlation — does model tier per phase correlate with blip rate or validation failure rate? Does a cheaper model in a given phase produce measurably worse outcomes, or is tier choice currently arbitrary relative to outcome?

One line per run row, appended when a run row is written (.anima-lite/metrics/run-<date>-<slug>.md):

| Run ID | Gates fired | Blips (info/review/BREAK) | Validation | Total subagent tokens |
|---|---|---|---|---|
| run-2026-07-07-recommend-sessions | 5 | 2/1/1 | PASS-pending | ~658,667 |
| run-2026-07-14-arete-skills | 2 (GATE-TELOS, GATE-HASH) | 3/0/0 | PASS | not traced |

Rows begin at run4 — run1-3 predate instrumentation; see archive/calibration-* for their artifacts. No fabricated backfill rows.

Anti-paperwork rule: a metrics artifact nobody reads in the next calibration diff is a candidate for deletion. This data exists to answer the three questions above, not to accumulate. If a field goes unread across several calibration diffs, raise dropping it at the next ari-backlog sweep rather than letting it silently persist.
