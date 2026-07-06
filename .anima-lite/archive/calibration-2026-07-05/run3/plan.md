# Execution Plan: weekly-report
Contract: .anima-lite/contracts/weekly-report.md
Generated: 2026-07-05

## Claim changes
- **CLAIM-2 — Three feedback options**: WeeklyReportServlet.submitInsightFeedback mirrors MonthlyReportServlet (already supports all three ratings). JS must render three buttons: Helpful, Not Helpful, Inaccurate. Rating value posted to server as-is.
- **CLAIM-3 — Training section visible-locked**: JS computes `allReviewed = (reviewedCount >= totalInsights)` from server DTO on page load. CSS class `training-section--locked` disables pointer-events + reduces opacity + shows lock icon when not all reviewed. Toggled on feedback-submit AJAX response.
- **CLAIM-5 — Evidence quote block + no View Recording**: `quotedExcerpt` + `sessionReference` from TutorAiInsightItem render in expanded card. No `recordingUrl` field in DTO → View Recording button absent entirely (not hidden conditionally — field never present, so condition always false).
- **CLAIM-7 — Get More Sessions CTA**: Deferred — no scheduling destination found in prod. Section omitted. Review-suggested blip logged.
- **CLAIM-8 — Per-period completion counts on list page**: New `findByAdvisorAndPeriodType(advisor, periodType)` method added to TutorAiInsightService interface + impl. WeeklyReportServlet.getWeeklyReportsList groups by period, computes reviewedCount/totalInsights per period. JS renders N/total in table.

## Substrate translations
- WeeklyReportServlet.java: new file, follows MonthlyReportServlet pattern. Two URL mappings: /PLUS/WeeklyReports (list) and /PLUS/WeeklyReport (detail). doGet/doPost both route. Three requestingMethod handlers: getWeeklyReportsList, getWeeklyReportData, submitInsightFeedback (same logic as MonthlyReportServlet.submitInsightFeedback — reuse verbatim).
- weekly_reports_list.jsp + weekly_report.jsp: new JSP files, follow monthly_reports_list.jsp + monthly_report.jsp pattern. Include prod shell fragments.
- weekly_report.js: ES module (type="module"), routes list/detail by pathname. Mirrors monthly_report.js shape. Imports PlusInterface from general_interface.js per spine-prod/formal.md §4.
- weekly_report.scss: Sass stylesheet compiled via ant deploy. No prod-side asset commit needed.
- web.xml: servlet-class + servlet-mapping for WeeklyReportServlet (two mappings: /PLUS/WeeklyReports and /PLUS/WeeklyReport). Pattern from existing monthly-report entries.
- PL2UserLogger: add VIEW_WEEKLY_REPORT and SUBMIT_WEEKLY_INSIGHT_FEEDBACK constants (pattern from monthly-report additions in prior port).
- applicationContext.xml: no change needed — service wiring already exists for TutorAiInsightService/TutorAiInsightFeedbackService.
- TutorAiInsightService interface + impl: add findByAdvisorAndPeriodType(advisor, periodType) method. DAO query: WHERE advisor=? AND periodType=? ORDER BY periodStart DESC, displayOrder ASC.

## Order of operations
1. TutorAiInsightDao + TutorAiInsightDaoHibernate additions (findByAdvisorAndPeriodType) — substrate commit — needed before service impl compiles. Add method to both interface and Hibernate impl. HQL: `FROM TutorAiInsightItem WHERE advisor=:advisor AND periodType=:periodType ORDER BY periodStart DESC, displayOrder ASC`.
2. TutorAiInsightService interface + impl (add findByAdvisorAndPeriodType delegating to DAO) — substrate commit with step 1.
3. PL2UserLogger constants (VIEW_WEEKLY_REPORT, SUBMIT_WEEKLY_INSIGHT_FEEDBACK) — substrate commit with steps 1–2.
4. WeeklyReportServlet.java — new file, substrate commit. For getWeeklyReportsList: call findByAdvisorAndPeriodType(advisor, "weekly"), group by (periodStart, periodEnd) server-side — do NOT recompute week boundaries; use the periodStart/periodEnd already on TutorAiInsightItem. Compute reviewedCount and totalInsights per period group. For submitInsightFeedback: verbatim copy from MonthlyReportServlet — logic identical. For getWeeklyReportData: same shape as getMonthlyReportData, pass periodStart+periodEnd as params, filter periodType="weekly" in service.
5. web.xml servlet registration — substrate commit with step 4. Two mappings: /PLUS/WeeklyReports and /PLUS/WeeklyReport. applicationContext.xml: no change (TutorAiInsightDao bean already registered — new method is on existing bean).
6. weekly_reports_list.jsp + weekly_report.jsp — substrate commit. JSP builds JSON directly (MonthlyReportServlet precedent — no DtoHelper layer in this feature tier).
7. weekly_report.js + weekly_report.scss — substrate commit.
8. CLAIM-2+CLAIM-3 (three feedback buttons, training locked state) — single claim commit.
9. CLAIM-8 (completion counts rendered in list) — claim commit.

## Notes on plan gaps resolved
- DAO layer: step 1 now names TutorAiInsightDao + TutorAiInsightDaoHibernate explicitly.
- Weekly period calculation: periods read from DB fields, no server-side date arithmetic.
- DtoHelper: MonthlyReportServlet builds JSONObject directly; same pattern here. No DtoHelper needed.
- CLAIM-5: `recordingUrl` field absent from TutorAiInsightItem; button omitted entirely. Blip: "conditionally hidden per contract; condition always false until recordingUrl added to DTO."

## Blockers
- None. TutorAiInsightFeedbackItem.rating already supports "inaccurate" — CLAIM-2 open question resolved.
- CLAIM-7 has no prod destination — deferred with blip, not a blocker.
- No recording URL in TutorAiInsightItem — CLAIM-5 button always absent (correct per contract: conditionally hidden).
