# Feature: Monthly Report
slug: monthly-report
repo(s): plus-web-app
stub: 3
source: ari-port-enriched
prod-commit: 90e0ff79
goes-stale: TutorAiInsightItem schema change, MonthlyReportServlet renamed, /PLUS/MonthlyReport URL mapping changed

## Identity
Tutor-facing monthly self-review page: sequential review of AI-generated coaching dimension insights with feedback capture, and a recommended training section that unlocks only after all insights are reviewed.

## Entry points
/PLUS/MonthlyReports → MonthlyReportServlet.java → monthly_reports_list.jsp (list view)
/PLUS/MonthlyReport?periodStart=...&periodEnd=... → MonthlyReportServlet.java → monthly_report.jsp (detail view)
(confirmed: web.xml, servlet + JSPs exist at port commit)

## Primary data structure
TutorAiInsightItem: id, advisor (FK), periodStart, periodEnd, periodType, constructName, constructDescription, insightText, quotedExcerpt, sessionReference, status (LOCKED/UNDER_REVIEW/REVIEWED), displayOrder
TutorAiInsightFeedbackItem: id, insight (FK), advisor (FK), rating (helpful/not_helpful/inaccurate), feedbackText, dateCreated
(confirmed: entity files + HBM mappings + service interfaces)

---
Everything below is enriched by ari-port after a port run.

## Full data flow
List page: MonthlyReportServlet.getAvailablePeriods → TutorAiInsightService.findDistinctPeriodsByAdvisor → JSON array → monthly_reports_list.jsp → monthly_report.js:initListPage → table render

Detail page: MonthlyReportServlet.getMonthlyReportData → TutorAiInsightService.findByAdvisorAndPeriod + TutorSessionService.findByAdvisorSortedBetweenDates → JSON → monthly_report.js:renderDetailPage → insights timeline + session metrics

Feedback: monthly_report.js:submitFeedback POST → MonthlyReportServlet.submitInsightFeedback → TutorAiInsightFeedbackService.saveOrUpdate + TutorAiInsightService.saveOrUpdate (status update) → JSON ok → JS re-fetches full state

## Client-side wiring
java/docroot/javascript/pl2/monthly_report.js — type="module"; imports PlusInterface from plus_components/general_interface.js; single file handles both list and detail routing via window.location.pathname check

## State machine
Insight states (per TutorAiInsightItem.status): LOCKED → UNDER_REVIEW → REVIEWED
- Initial state set by insight generation pipeline (first insight UNDER_REVIEW, rest LOCKED)
- Advance: submitInsightFeedback marks current UNDER_REVIEW → REVIEWED, promotes first LOCKED → UNDER_REVIEW
- Training section: locked until reviewedCount >= totalInsights
- State persists server-side (CLAIM-1); page reload resumes where tutor left off

## Feature gates
TutorAiInsightService.existsForAdvisor gate: NOT implemented in MonthlyReportServlet (it exists in TutorReviewServlet but was not ported here). Any tutor can navigate to /PLUS/MonthlyReport regardless of whether they have insight data. If no data exists, the page renders empty sections. Consider adding the existsForAdvisor gate in a follow-up.

## Seam-specific protocols
Servlet→JS (detail): JSON shape: `{ periodLabel, periodStart, periodEnd, reviewedCount, totalInsights, insights: [{id, constructName, constructDescription, insightText, quotedExcerpt, sessionReference, status, displayOrder, feedbackRating}], sessionMetrics: {sessionCount, hours, schoolCount, studentCount(-1 stub), learningTimeMin(-1 stub), skillsMastered(-1 stub)} }`
Servlet→JS (feedback response): `{ status: "ok", rating, insightId, statusChanged }` or `{ status: "error", message }`
Servlet→JS (periods list): `{ periods: [{periodStart, periodEnd, label}] }`

## Known quirks
- studentCount, learningTimeMin, skillsMastered return -1 (rendered as "—") — no single-pass aggregation confirmed; distilled from blip `session-metrics-stub` in monthly-report blips
- Training recommendations section shows placeholder when unlocked — no lesson-to-dimension mapping service; distilled from blip `training-recommendations-stub` in monthly-report blips
- URI-based page routing in servlet: `req.getRequestURI().contains("MonthlyReports")` — fragile to context-path changes; distilled from catchup-monthly-report.md §"What to focus on in review"
- existsForAdvisor gate not ported from TutorReviewServlet — empty-state behavior unspecified; distilled from port observation

## Port provenance
Contract slug: monthly-report, prod commit: 90e0ff79
