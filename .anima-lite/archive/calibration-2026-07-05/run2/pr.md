## Summary

Ports Monthly Report feature from plus-uno prototype to prod. Adds two pages (`/PLUS/MonthlyReports` list, `/PLUS/MonthlyReport` detail) backed by a new servlet reusing the existing `TutorAiInsightService` + `TutorAiInsightFeedbackService` infrastructure.

Claim changes (confirmed by user):
- **CLAIM-1 — Server-side review state**: Progressive disclosure state (LOCKED/UNDER_REVIEW/REVIEWED) is loaded from DB on every page load. Review progress persists across page reloads. Previously: proto tracked state client-side only (reset on reload).
- **CLAIM-2 — Feedback ratings recorded**: Each feedback button (Helpful/Not Helpful/Inaccurate) POSTs the rating to the servlet, which saves it as a `TutorAiInsightFeedbackItem`. Previously: proto feedback was advance-only, no data captured.
- **CLAIM-3 — No "View Recording" button**: Removed. Proto had a non-functional `#` link implying recording playback. Can be added later when recording infrastructure exists.

Deferred:
- Student count, learning time, skills mastered: stubbed as "—" — no single-pass aggregation service confirmed in prod (see blip: session-metrics-stub)
- Training recommendations: section unlocks correctly after all insights reviewed, but shows placeholder — no lesson-to-dimension mapping service exists yet (see blip: training-recommendations-stub)
- Time allocation breakdown: omitted — no DB source for session activity breakdown confirmed

## Files changed
- `MonthlyReportServlet.java` (new) — handles GET (page load, data fetch) and POST (feedback submission) for both pages; reuses existing insight and feedback services
- `monthly_report.js` (new) — ES module; progressive disclosure state machine; list + detail page routing; feedback POST; re-fetches server state after each feedback action
- `monthly_report.jsp` (new) — detail page shell; Bootstrap 4.1.3 layout; sections populated by JS
- `monthly_reports_list.jsp` (new) — list page shell; table populated by JS
- `monthly_report.scss` (new) — styles for both pages
- `web.xml` — servlet registration + URL mappings for `/PLUS/MonthlyReport` and `/PLUS/MonthlyReports`
- `PL2UserLogger.java` — adds `VIEW_MONTHLY_REPORT` constant + registers in `ACTIONS_USE_NEXT_TIME`

## Test plan
- [ ] Navigate to `/PLUS/MonthlyReports` as a tutor with AI insight data — list of available periods renders
- [ ] Click a period → navigates to `/PLUS/MonthlyReport?periodStart=...&periodEnd=...`
- [ ] Detail page loads with correct period label and impact stats (sessions, hours, schools show real data; student count + impact metrics show "—" — expected)
- [ ] Growth insights render with correct locked/under_review/reviewed state matching DB
- [ ] Click "Helpful" on the first UNDER_REVIEW card → card advances to REVIEWED, next card unlocks; refresh page → state persists (CLAIM-1)
- [ ] Verify TutorAiInsightFeedbackItem saved with correct rating in DB (CLAIM-2)
- [ ] Confirm no "View Recording" button or link anywhere on detail page (CLAIM-3)
- [ ] After all insights reviewed: training section unlocks (lock icon disappears, placeholder card appears)
- [ ] Confirm no regression on `/PLUS/TutorReview` — shares same insight services but different servlet

## Blips
**review-suggested — session-metrics-stub** (`MonthlyReportServlet.java:193–196`): `studentCount`, `learningTimeMin`, `skillsMastered` return -1 (rendered as "—"). Sessions, hours, schools are real data. Stub needs a follow-up service method or HQL query to complete.

**review-suggested — training-recommendations-stub** (`monthly_report.js:199–207`): Training section unlocks correctly but shows a placeholder card. Needs a lesson-to-dimension recommendation mapping layer.
