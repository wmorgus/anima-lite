# Execution Plan: Monthly Report
Contract: .anima-lite/contracts/monthly-report.md
Generated: 2026-07-02

## Claim changes

- **CLAIM-1 (server-side persist review state)**: `MonthlyReportServlet.java` (new) — GET loads insight status from `TutorAiInsightItem.status` (LOCKED/UNDER_REVIEW/REVIEWED) via existing `TutorAiInsightService`; passes serialized state to JSP as JSON attribute; `monthly_report.js` initializes state machine from server-provided state rather than starting at reviewedCount=0
- **CLAIM-2 (record feedback ratings)**: `MonthlyReportServlet.java` — POST action `submitInsightFeedback` updates `TutorAiInsightItem.status` to REVIEWED + saves `TutorAiInsightFeedbackItem` (rating=helpful/not_helpful/inaccurate) via existing services; same code path TutorReviewServlet uses
- **CLAIM-3 (no "View Recording" button)**: `monthly_report.jsp` — no "View Recording" button in the expanded card body; session reference timestamp rendered as static text only

## Substrate translations

- React JSX → JSP + jQuery + Bootstrap 4.1.3 — prod formal pattern
- PLUS DS Badge/Button/Alert/Progress → Bootstrap equivalents (badge, btn, alert, progress)
- React useState (reviewedCount, activeKey) → JS variables initialized from server-provided JSON; state machine preserved client-side
- PageLayout/sidebarConfig → `<%@ include file="/jsp_pl2/pl2_head.jspf" %>` + topbar.jspf + sidebar_nav.jspf
- useNavigate → href links to servlet URLs
- SCSS + design tokens → Sass stylesheet (`monthly_report.scss`) + Bootstrap CSS vars
- FA Free icons — direct transfer, no change
- MonthlyReportPage + MonthlyReportsListPage → two JSP paths: `/PLUS/MonthlyReport` (detail) + `/PLUS/MonthlyReports` (list)
- Mock data → servlet fetches real insight data via `TutorAiInsightService.findByAdvisorAndPeriod()`; session metrics (sessions, hours, students, schools) via `TutorSessionService`; impact metrics (skills mastered, learning time) stub in servlet (no existing aggregation service confirmed)

## Order of operations

1. Feature branch `monthly-report` in prod repo
2. `MonthlyReportServlet.java` — handles GET (page load, serialize insight state as JSON) and POST (insight feedback actions); reuses `TutorAiInsightService` + `TutorAiInsightFeedbackService`
3. `web.xml` — add servlet registration + URL mappings for `/PLUS/MonthlyReport` (detail) + `/PLUS/MonthlyReports` (list)
4. `monthly_report.scss` → compile to `css-build/monthly_report.css`
5. `monthly_report.jsp` (detail page) — progressive disclosure layout, insights from JSON req attribute, no View Recording button
6. `monthly_reports_list.jsp` (list page) — table of available periods from servlet, status badges, pagination
7. `monthly_report.js` — state machine initialized from server JSON; POST on feedback; updates DOM; handles all-reviewed gate for training section; type="module"
8. Substrate commit — all substrate files
9. CLAIM-1 commit — insight state loading + JS initialization from server
10. CLAIM-2 commit — feedback POST + DB write
11. CLAIM-3 is implicit (no View Recording button in JSP) — noted in CLAIM-1 commit

## Blockers

- Session metrics aggregation (sessions count, hours, students, schools): no `MonthlySessionMetricsService` confirmed in prod. Will stub values in servlet with a BLIP logged. Full metrics need a separate data query implementation.
- Training recommendations: no confirmed prod data source for per-tutor training recommendations. Will render the training section structure but populate with placeholder content (a BLIP will flag this).
- Time allocation: no DB source confirmed. Will stub breakdown data with a BLIP.
