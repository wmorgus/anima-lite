# run5 plan — anima-lite monthly-report fresh port (A/B calibration)

Date: 2026-07-07

## Baseline

- Prod repo: `/Users/wmorgus/Desktop/other research dev/plus web-app`
- Baseline commit: `dev` @ `29d41e50`
- Working branch for run5: `anima-lite-monthly-report-run5` (created off `dev`, currently at `29d41e50`, confirmed free of any monthly-report files)

## A/B comparison target

- **Naive baseline** (what run5 is being compared against): prod branch `monthly-report`, tip `90e0ff79`.
  Tagged as `naive-monthly-report-v0` so it can't be lost to branch cleanup.
- **"Good" benchmark** (superseded, aborted — do not treat as ground truth, but available for reference):
  prod branch `anima-lite-monthly-report` / artifact set formerly at `.anima-lite/ports/monthly-report-v1/`.
  Now relocated to `.anima-lite/_run5_isolated/ports/monthly-report-v1/` (isolation, not deletion).

## Proto source

- Path: `/Users/wmorgus/Desktop/anima/anima-core/plus-uno/playground/monthly-report/src/`
  (NOT `monthly-report-demo` — that directory does not exist; don't go looking for it.)
- Canonical entry components (confirmed by tracing `main.jsx` → `App.jsx` → render):
  - `MonthlyReportPage.jsx` (detail view)
  - `MonthlyReportsListPage.jsx` (list view)
  - `App.jsx` switches between the two on a `page` prop (`'list'` vs default `'detail'`).
- Duplicates / decoys — do NOT treat as canonical:
  - `MonthlyReportsListContent.jsx` (same dir) — a content-only variant for shell-embedded use
    (imports `ShellContext` from `home-redesign`), NOT referenced by `App.jsx`, NOT rendered by the demo.
  - `home-redesign/src/components/MonthlyReportsListPage.jsx` — a decoy living in the wrong playground
    (`home-redesign`, not `monthly-report`), same filename, near-duplicate content. This is stale/misplaced,
    not the source of truth.

## Isolated artifacts (anima-lite's own memory of prior monthly-report work)

Moved out of ari-map's scan paths (`.anima-lite/features/`, `.anima-lite/ports/`) so run5 cannot
read anima-lite's own prior answers. See `.anima-lite/_run5_isolated/RESTORE.md` for the exact
moved-path list and the `git mv` commands to restore them after run5 concludes.

## Comparison dimensions for judging run5's port vs. the naive port

1. **Architectural discovery** — did run5 find and extend the existing `tutor_review` feature
   rather than build a redundant parallel servlet (as the naive port did with
   `MonthlyReportServlet.java`)?
2. **Wiring completeness** — did run5 use existing-but-dormant infra (e.g. commented-out
   time-allocation HBM/service/DAO in `applicationContext.xml`) before declaring "no data source,"
   or did it give up / stub data the way the naive port did?
3. **Security/behavioral parity** — did run5 carry forward the `existsForAdvisor` gate (or
   equivalent authorization check) rather than dropping it?
4. **Claim fidelity vs. proto** — does the ported behavior match what the proto component set
   (`MonthlyReportPage.jsx` + `MonthlyReportsListPage.jsx`) actually argues for, not the decoy
   or the content-variant?
5. **Commit discipline** — one commit per claim, vs. the naive port's 2-commit collapse
   (everything squashed into two undifferentiated commits).
6. **Blip honesty/severity routing** — are blips (implementation surprises/deviations) logged
   honestly and routed at the right severity, not smoothed over?
7. **Full artifact-set completeness** — does run5 produce the complete port artifact set
   (contract, plan, blips, catchup, pr — matching the shape of prior port dirs) rather than a
   partial record?

## Do not touch (still live, other side of A/B or dependent branches)

- prod `monthly-report` branch (naive baseline — now also tagged `naive-monthly-report-v0`)
- prod `anima-lite-monthly-report` branch
- prod `weekly-report` branch (depends on `monthly-report`; must survive untouched)
