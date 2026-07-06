## Summary

Ports weekly-report feature from plus-uno prototype to prod (plus web-app).

Claim changes (confirmed by user):
- **CLAIM-2 — Three feedback options**: Helpful / Not Helpful / Inaccurate all implemented; "Inaccurate" preserves the contestability mechanism.
- **CLAIM-3 — Training visible-locked**: Training section renders at reduced opacity with lock icon until all insights reviewed; unlocks on completion.
- **CLAIM-5 — Evidence quote block**: quotedExcerpt + sessionReference rendered per insight card; View Recording button absent (no recordingUrl field in DTO).
- **CLAIM-7 — Get More Sessions CTA**: Links to /PLUS/TutorSchedule (sign-ups tab); renders unconditionally below training section.
- **CLAIM-8 — Per-period completion count**: List page shows reviewedCount/totalInsights per weekly report row.

Deferred:
- Delta badges (week-over-week): not in canonical proto source (WeeklyReportContent); out of scope.
- View Recording button: TutorAiInsightItem has no recordingUrl field; add conditional once field exists.

## Files changed

**New files (weekly-report feature):**
- `java/source/edu/cmu/pl2/servlet/WeeklyReportServlet.java` — servlet for /PLUS/WeeklyReports (list) and /PLUS/WeeklyReport (detail); handles getWeeklyReportsList, getWeeklyReportData, submitInsightFeedback
- `java/docroot/jsp_pl2/weekly_reports_list.jsp` — list page JSP; uses prod shell fragments
- `java/docroot/jsp_pl2/weekly_report.jsp` — detail page JSP; includes training-section--locked markup and CTA placeholder
- `java/docroot/javascript/pl2/weekly_report.js` — ES module; handles routing, insights timeline, feedback submission, training lock toggle, CTA render
- `java/sass/weekly_report.scss` — Sass stylesheet; mirrors monthly_report.scss; compiled to /css/pl2/weekly_report.css via Ant

**Modified (additions only):**
- `java/docroot/conf-tomcat-11.0/web.xml` — servlet-class + two URL mappings (/PLUS/WeeklyReports, /PLUS/WeeklyReport)
- `java/source/edu/cmu/pl2/dao/TutorAiInsightDao.java` — added findByAdvisorAndPeriodType interface method
- `java/source/edu/cmu/pl2/dao/hibernate/TutorAiInsightDaoHibernate.java` — HQL impl: WHERE advisor=:advisor AND periodType=:periodType ORDER BY periodStart DESC, displayOrder ASC
- `java/source/edu/cmu/pl2/service/TutorAiInsightService.java` — added findByAdvisorAndPeriodType interface method
- `java/source/edu/cmu/pl2/service/impl/TutorAiInsightServiceImpl.java` — delegates to DAO
- `java/source/edu/cmu/pl2/util/PL2UserLogger.java` — added VIEW_WEEKLY_REPORT and SUBMIT_WEEKLY_INSIGHT_FEEDBACK constants

**Modified by predecessor (monthly-report port, pre-existing on this branch):**
- `java/docroot/javascript/pl2/monthly_report.js` — monthly-report port (landed before weekly-report work)
- `java/docroot/jsp_pl2/monthly_report.jsp` — monthly-report port
- `java/docroot/jsp_pl2/monthly_reports_list.jsp` — monthly-report port
- `java/sass/monthly_report.scss` — monthly-report port
- `java/source/edu/cmu/pl2/servlet/MonthlyReportServlet.java` — monthly-report port

## Test plan
- [ ] Load /PLUS/WeeklyReports as a tutor with weekly insight data — rows show completion counts (reviewedCount/totalInsights)
- [ ] Load /PLUS/WeeklyReport — insights render in LOCKED/UNDER_REVIEW/REVIEWED states
- [ ] Expand UNDER_REVIEW card — three feedback buttons present (Helpful, Not Helpful, Inaccurate)
- [ ] Submit feedback — card advances to REVIEWED, next LOCKED card unlocks
- [ ] After all reviewed — training section unlocks, CTA visible
- [ ] Confirm no regression on monthly report (/PLUS/MonthlyReport)

## Blips

**info — SCSS lives in java/sass/, not java/docroot/css-src/**
Plan assumed css-src/; actual location is java/sass/ (same pattern as monthly_report.scss). Ant compiles to /css/pl2/weekly_report.css.

**info — web.xml is in java/docroot/conf-tomcat-11.0/, not java/WEB-INF/**
Prompt gave best-guess path; actual file is conf-tomcat-11.0/web.xml. Servlet registered correctly.

**info — CLAIM-5: View Recording button absent**
TutorAiInsightItem has no recordingUrl field. Contract said "conditionally hide if no URL." Condition always false — button omitted entirely. One-line addition to buildCardBody restores it when the field exists.

**info — CLAIM-7 resolved: scheduling CTA wired to /PLUS/TutorSchedule**
Originally deferred (no scheduling destination found). TutorScheduleServlet confirmed via codebase search. CTA renders unconditionally, links to sign-ups tab.

**info — CLAIM-1 pattern: REVIEWED cards non-interactive re: feedback**
REVIEWED cards render with toggle (can re-read) but no feedback row. Server does not expose re-review from the UI.

**info — CLAIM-4 pattern: no optimistic UI**
Feedback POST waits for server response, then re-fetches full state. Matches monthly_report.js precedent.

**info — Claim logic committed with substrate**
All claim code (feedback buttons, training lock, completion counts) landed in the substrate commit c4725706. Subsequent claim commits are confirmatory (no diff). Claims were all pre-confirmed, so a broken skeleton added no value.

**info — Training recommendations stub**
Training section unlocks correctly (CLAIM-3) but shows placeholder card. No training data service exists. Identical to monthly_report.js pattern.
