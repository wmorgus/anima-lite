# Feature: Weekly Report
slug: weekly-report
repo(s): plus-web-app
stub: 3
source: ari-port-enriched
prod-commit: 176d11b0
goes-stale: TutorAiInsightItem schema change (especially recordingUrl addition), WeeklyReportServlet renamed, /PLUS/WeeklyReport URL mapping changed, TutorScheduleServlet URL or tab structure changed

## Identity
Tutor-facing weekly self-review page: sequential review of AI-generated coaching dimension insights with feedback capture (Helpful / Not Helpful / Inaccurate), and a recommended training section that unlocks only after all insights are reviewed. List page shows all historical weekly reports with per-row completion counts. Motivational loop closes with a "Get More Sessions" CTA linking to the tutor scheduling page.

## Entry points
/PLUS/WeeklyReports → WeeklyReportServlet.java → weekly_reports_list.jsp (list view)
/PLUS/WeeklyReport?periodStart=...&periodEnd=... → WeeklyReportServlet.java → weekly_report.jsp (detail view)
(confirmed: web.xml has both mappings at port commit; servlet + JSPs exist)

## Primary data structure
TutorAiInsightItem: id, advisor (FK), periodStart, periodEnd, periodType ("weekly"), constructName, constructDescription, insightText, quotedExcerpt, sessionReference, status (LOCKED/UNDER_REVIEW/REVIEWED), displayOrder
TutorAiInsightFeedbackItem: id, insight (FK), advisor (FK), rating (helpful/not_helpful/inaccurate), feedbackText, dateCreated
(shared with monthly-report; periodType field distinguishes weekly vs. monthly insights)

---
Everything below is enriched by ari-port after a port run.

## Full data flow

List page: WeeklyReportServlet.getWeeklyReportsList → TutorAiInsightService.findByAdvisorAndPeriodType(advisor, "weekly") → group by (periodStart, periodEnd) in LinkedHashMap → compute reviewedCount/totalInsights per group → JSON array → weekly_reports_list.jsp → weekly_report.js:initListPage → table render with PROGRESS column (N/total)

Detail page: WeeklyReportServlet.getWeeklyReportData → TutorAiInsightService.findByAdvisorAndPeriod + TutorSessionService.findByAdvisorSortedBetweenDates → TutorAiInsightFeedbackService.findByInsightAndAdvisor per insight → JSON → weekly_report.js:renderDetailPage → insights timeline + session metrics + training lock state + CTA

Feedback: weekly_report.js:submitFeedback POST → WeeklyReportServlet.submitInsightFeedback → TutorAiInsightFeedbackService.saveOrUpdate (rating) + TutorAiInsightService.saveOrUpdate (UNDER_REVIEW → REVIEWED) + promote first LOCKED → UNDER_REVIEW → JSON ok → JS re-fetches full state, auto-expands next UNDER_REVIEW card

## Client-side wiring
java/docroot/javascript/pl2/weekly_report.js — type="module"; imports PlusInterface from plus_components/general_interface.js; single file handles both list and detail routing via `window.location.pathname.includes("WeeklyReports")`; event delegation on document for `.feedback-btn` clicks (not per-card listeners)

## State machine
Insight states (per TutorAiInsightItem.status): LOCKED → UNDER_REVIEW → REVIEWED
- Initial state: first insight UNDER_REVIEW, rest LOCKED (set by insight generation pipeline)
- Advance: submitInsightFeedback marks current UNDER_REVIEW → REVIEWED, promotes first LOCKED → UNDER_REVIEW (breaks on first match)
- Training section: ships locked (`training-section--locked`); unlocks when `reviewedCount >= totalInsights && total > 0`; locked = `opacity: 0.5; pointer-events: none` + lock icon + hint text; unlocked = class removed + placeholder training card rendered
- REVIEWED cards: expandable (show insight + evidence) but no feedback buttons — server does not re-expose feedback submission once REVIEWED
- Feedback submitted on already-REVIEWED insight (unreachable from UI): rating updated, status-advance skipped, `statusChanged: false` returned
- State persists server-side (CLAIM-1); page reload resumes where tutor left off
- No optimistic UI: feedback POST completes before re-fetch; buttons disabled during in-flight POST

## Feature gates
TutorAiInsightService.existsForAdvisor gate: NOT implemented (same gap as monthly report). Any authenticated advisor can reach /PLUS/WeeklyReport regardless of whether insight data exists. Empty state: detail page renders with no insight cards; list page renders "No weekly reports available yet." Consider adding the gate in a follow-up.

## Seam-specific protocols
Servlet→JS (detail): `{ dateRange, periodStart, periodEnd, reviewedCount, totalInsights, insights: [{id, constructName, constructDescription, insightText, quotedExcerpt, sessionReference, status, displayOrder, feedbackRating}], sessionMetrics: {sessionCount, hours, schoolCount, studentCount(-1 stub), learningTimeMin(-1 stub), skillsMastered(-1 stub)} }`

Servlet→JS (list): `{ periods: [{periodStart, periodEnd, dateRange, weekNumber, reviewedCount, totalInsights, status("not_viewed"|"viewed")}] }`

Servlet→JS (feedback response): `{ status: "ok", rating, insightId, statusChanged }` or `{ status: "error", message }`

## Known quirks
- studentCount, learningTimeMin, skillsMastered return -1 (rendered as "—") — stubs only; no single-pass aggregation confirmed; same as monthly report
- Training recommendations section shows placeholder when unlocked — no lesson-to-dimension mapping service; same as monthly report
- URI-based page routing in servlet: `req.getRequestURI().contains("WeeklyReports")` — fragile to context-path changes; same as monthly report
- existsForAdvisor gate not ported — empty-state behavior unspecified
- View Recording button permanently absent — `TutorAiInsightItem` has no `recordingUrl` field; add `if (insight.recordingUrl)` guard in `buildCardBody` when field exists
- Claims committed with substrate (commit c4725706) — CLAIM-2/3/7/8 claim commits (b287cc49, 2fd3fca7, 176d11b0) are confirmatory with no diff; all claim code is in the substrate commit
- findByAdvisorAndPeriod used in getWeeklyReportData does not filter by periodType — period date boundaries implicitly isolate weekly data; relies on week-scoped periodStart/periodEnd being unique to weekly periods

## Port provenance
Contract slug: weekly-report, spine commit: 9c02f5e8, prod commit range: c4725706–176d11b0
