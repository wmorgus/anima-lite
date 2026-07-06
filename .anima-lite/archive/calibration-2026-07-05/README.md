# Calibration baseline — 2026-07-05

Harness commit: c4deebf
Feature ported: monthly-report (plus-uno → plus web-app)
Prod repo HEAD at port time: 29d41e50

## What this captures

Two runs of the same feature through the same harness, used to stress-test harness improvements made mid-session.

**run1/** — pre-harness-improvement run. Branch discipline bug (commits landed on `dev` not feature branch). Contracts slugged as `main` not `monthly-report`. Spine at time: c21f08b1 (pre-refresh). Harness lacked: feature branch discipline, per-claim commits, catch-up doc, feature ledger, section citations, telos primacy, probe subagents, human gates.

**run2/** — clean-slate re-run after harness improvements. Feature branch `monthly-report` created. 2 commits (substrate + CLAIM-1+2). Spine refreshed to 29d41e50 with 3 corrections (ES modules widespread, servlet hierarchy split, seam protocols). Feature ledger created. Validation PASS (pending review). 2 acknowledged blips.

## Key deltas run1 → run2

- Contract: 118 lines (had playwright block embedded) → 28 lines (cleaner, playwright block moved to harness template)
- Blips: 34 lines (3 blips) → 41 lines (4 blips — harness caught 2 additional substrate decisions v1 missed)
- Spine: FINDING-3 wrong in v1 (ES modules = tutor_review/ only) → corrected in v2 (widespread)
- Branch: commits on `dev` in v1 → correct feature branch in v2

## Diff command for next calibration run

```
diff -u .anima-lite/archive/calibration-2026-07-05/run2/contract.md .anima-lite/contracts/monthly-report.md
diff -u .anima-lite/archive/calibration-2026-07-05/run2/blips.md .anima-lite/blips/monthly-report.md
diff -u .anima-lite/archive/calibration-2026-07-05/run2/catchup.md .anima-lite/catchup-monthly-report.md
```

For spine changes: `git diff c4deebf .anima-lite/spine-prod/`
