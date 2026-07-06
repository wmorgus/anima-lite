# Catch-Up: weekly-report port

## What this is

A port of the weekly report feature from plus-uno (React prototype) to plus web-app (prod Java/JSP app). The feature lets tutors review AI-generated coaching insights from their week, submit feedback on each, and unlock a training recommendations section only after all insights are reviewed. The list page shows all historical weekly reports with per-row completion counts.

## Repo context

- **Prod repo:** `plus web-app` (Java 21 / Jakarta Servlet / JSP / Bootstrap 4.1.3 / jQuery / ES modules)
- **Branch:** `weekly-report` (branches from `dev` at commit `29d41e50`, v11.3.0.4 for QA)
- **Predecessor port on this branch:** `monthly-report` (commits 7f7c54c3 and 90e0ff79) — this feature follows identical structural patterns and the monthly-report files are the primary precedent
- **Proto source:** `WeeklyReportContent.jsx` (canonical) in plus-uno; `WeeklyReportPage.jsx` was older/less polished and not ported

## What changed and why

### Substrate

All new files follow the `MonthlyReportServlet` / `monthly_report.*` pattern verbatim. No new patterns introduced.

**New files:**
- `java/source/edu/cmu/pl2/servlet/WeeklyReportServlet.java` — handles two URL mappings: `/PLUS/WeeklyReports` (list) and `/PLUS/WeeklyReport` (detail). Three AJAX handlers: `getWeeklyReportsList`, `getWeeklyReportData`, `submitInsightFeedback`. `submitInsightFeedback` is a verbatim copy from `MonthlyReportServlet`.
- `java/docroot/jsp_pl2/weekly_reports_list.jsp` — list page; static skeleton only; JS populates on load. Includes `pl2_content_start.jspf` / `pl2_content_end.jspf`.
- `java/docroot/jsp_pl2/weekly_report.jsp` — detail page; static skeleton with all section containers; JS populates on load. Training section ships with `training-section--locked` CSS class already applied (server will toggle).
- `java/docroot/javascript/pl2/weekly_report.js` — ES module (`type="module"`). Imports `PlusInterface` from `general_interface.js`. Routing: `window.location.pathname.includes("WeeklyReports")` → list, else → detail.
- `java/sass/weekly_report.scss` — Sass source; compiled by Ant to `/css/pl2/weekly_report.css`. **Note:** plan assumed `java/docroot/css-src/`; actual directory is `java/sass/` (same as `monthly_report.scss`).

**Modified (additions only):**
- `java/docroot/conf-tomcat-11.0/web.xml` — two servlet-mapping entries for `/PLUS/WeeklyReports` and `/PLUS/WeeklyReport`. **Note:** plan said `java/WEB-INF/web.xml`; actual file is `conf-tomcat-11.0/web.xml`.
- `java/source/edu/cmu/pl2/dao/TutorAiInsightDao.java` and `TutorAiInsightDaoHibernate.java` — added `findByAdvisorAndPeriodType(advisor, periodType)`. HQL: `FROM TutorAiInsightItem WHERE advisor=:advisor AND periodType=:periodType ORDER BY periodStart DESC, displayOrder ASC`.
- `java/source/edu/cmu/pl2/service/TutorAiInsightService.java` and `TutorAiInsightServiceImpl.java` — delegates new method to DAO.
- `java/source/edu/cmu/pl2/util/PL2UserLogger.java` — added `VIEW_WEEKLY_REPORT` and `SUBMIT_WEEKLY_INSIGHT_FEEDBACK` constants.

### Claim changes

**CLAIM-2 — Three feedback options (Helpful / Not Helpful / Inaccurate)**

All three buttons render in `buildCardBody` when `stateLc === "under_review"`. Rating values posted: `helpful`, `not_helpful`, `inaccurate`. `TutorAiInsightFeedbackItem.rating` field already supported all three (open question resolved before porting). "Inaccurate" is the contestability mechanism — it is the button by which a tutor can dispute an AI observation.

Code: `weekly_report.js:buildCardBody` — feedback button block.
Verify: expand an UNDER_REVIEW card; confirm three buttons render with correct labels and data-rating values.

**CLAIM-3 — Training section visible-locked**

The training section (`#training-section`) ships with CSS class `training-section--locked` applied in JSP. `training-section--locked` sets `opacity: 0.5; pointer-events: none`. JS calls `updateTrainingSectionState(reviewedCount, total)` on page load and after each feedback POST.

DOM in the locked state: `<section id="training-section" class="training-section training-section--locked">` — lock icon (`#training-lock-icon`) visible, hint text (`#training-hint`) "Unlock after reviewing all insights" visible, training grid empty.

Unlock condition: `reviewedCount >= total && total > 0`. When met: `training-section--locked` class removed, lock icon and hint hidden, training grid populated with placeholder card ("Training recommendations coming soon" — no data source connected yet).

Code: `weekly_report.js:updateTrainingSectionState`, `weekly_report.scss:.training-section--locked`, `weekly_report.jsp:#training-section`.
Verify: load page with zero reviewed — section visible but dim, non-interactive. After reviewing all — section brightens, lock icon disappears.

**CLAIM-5 — Evidence quote block (View Recording absent)**

`buildCardBody` renders `insight.quotedExcerpt` in a `.quote-block` and `insight.sessionReference` below it when those fields are non-empty. No View Recording button is rendered — `TutorAiInsightItem` has no `recordingUrl` field. The contract specified "conditionally hide if no URL"; since the field never exists in the DTO, the condition is permanently false. A single `if (recordingUrl)` guard in `buildCardBody` is all that would be needed when the field is added.

Code: `weekly_report.js:buildCardBody` — `hasEvidence` / `hasSession` / `evidenceHtml` / `sessionHtml`.

**CLAIM-7 — "Get More Sessions" CTA**

`renderCtaSection()` writes a CTA card to `#weekly-report-cta-section`. Link target: `/PLUS/TutorSchedule`. CTA renders unconditionally (not gated on `allReviewed`). Initially deferred because no scheduling destination was found; `TutorScheduleServlet` confirmed via codebase search and the blip was updated to `info` severity.

Code: `weekly_report.js:renderCtaSection`, `weekly_report.jsp:#weekly-report-cta-section`.

**CLAIM-8 — Per-period completion count on list page**

`getWeeklyReportsList` in `WeeklyReportServlet` groups insights by `(periodStart, periodEnd)` using a `LinkedHashMap`, counts `status === "REVIEWED"` entries per group, and emits `reviewedCount` / `totalInsights` per period object. JS list renderer writes `period.reviewedCount + "/" + period.totalInsights` into `.completion-count` span in the PROGRESS column.

`reviewedCount`/`totalInsights` are **server-computed** (not client-computed). The servlet does the arithmetic from the `TutorAiInsightItem` records fetched via `findByAdvisorAndPeriodType`.

Code: `WeeklyReportServlet.java:getWeeklyReportsList` (grouping + counting logic), `weekly_report.js:renderListPage` (CLAIM-8 block).

## Edge cases

**Feedback on an already-REVIEWED insight:**
REVIEWED cards render with no feedback buttons (`buildCardBody` only emits the feedback row when `stateLc === "under_review"`). The path is unreachable from the UI. If a POST reaches `submitInsightFeedback` anyway (e.g. direct HTTP call), the server saves/updates the rating via `saveOrUpdate` but the status-advance block is skipped (`if ("UNDER_REVIEW".equals(insight.getStatus()))` is false). Response includes `statusChanged: false`. No double-advance possible.

Code: `WeeklyReportServlet.java:submitInsightFeedback` — status guard block; `weekly_report.js:buildCardBody` — `feedbackHtml` conditional on `stateLc === "under_review"`.

**List page with no weekly insights (empty state):**
`getWeeklyReportsList` returns `{ periods: [] }`. `renderListPage([])` writes a single colspan row: "No weekly reports available yet." No error state, no redirect. The header row and table container are still shown (JS removes the loading spinner and shows them unconditionally).

Code: `weekly_report.js:renderListPage` — `if (periods.length === 0)` block.

## Deferred

- **Delta badges (week-over-week):** present in the older `WeeklyReportPage.jsx` but absent from canonical source `WeeklyReportContent.jsx`. Out of scope per contract.
- **View Recording button:** `TutorAiInsightItem` has no `recordingUrl` field. Button omitted. Add once field exists in DTO.
- **Training recommendations data source:** training section unlocks correctly but shows a stub card. No lesson-to-dimension mapping service exists (same state as monthly report). Requires a future data sprint.
- **existsForAdvisor gate:** not ported from `TutorReviewServlet` (same gap as monthly report). Tutors with no insight data see an empty page rather than a redirect.
- **studentCount / learningTimeMin / skillsMastered metrics:** return `-1` (rendered as "—"). Stubs only — no single-pass aggregation path confirmed. Same state as monthly report.

## Blips

All blips are `info` severity; no `review-required` items:
- SCSS path correction: `java/docroot/css-src/` → `java/sass/`
- web.xml path correction: `java/WEB-INF/` → `java/docroot/conf-tomcat-11.0/`
- CLAIM-5: View Recording permanently absent (no `recordingUrl` in DTO)
- CLAIM-7: CTA initially deferred (no destination found) → resolved (TutorScheduleServlet confirmed)
- CLAIM-1 pattern: REVIEWED cards non-interactive re: feedback (readable but not re-reviewable)
- CLAIM-4 pattern: no optimistic UI; POST → re-fetch pattern from monthly_report.js preserved
- Claim code committed with substrate (all claims pre-confirmed; separate claim commits are confirmatory with no diff; claim code is in commit `c4725706`)
- Training recommendations stub: placeholder card, identical to monthly report

## What to focus on in review

1. **Sequential unlock integrity** (`WeeklyReportServlet.java:submitInsightFeedback` lines ~290–310): the server promotes the first LOCKED insight to UNDER_REVIEW after marking the current UNDER_REVIEW as REVIEWED. Verify: only one insight should be in UNDER_REVIEW at any time. The loop breaks on the first LOCKED match — confirm no off-by-one if insights are unsorted at that point. (`findByAdvisorAndPeriod` returns period insights; order is by `displayOrder` from DAO sort, but the servlet does not re-sort the list before promoting.)
2. **Authorization boundary** (`submitInsightFeedback`): verifies `insight.getAdvisor().getId().equals(advisor.getId())` before saving feedback. Correct, but note that `MonthlyReportServlet` uses the same pattern — no role-based check, only ownership check.
3. **URI-based routing fragility** (`doPost`, page-dispatch block): `req.getRequestURI().contains("WeeklyReports")` — same fragility as monthly report; sensitive to context-path changes.
4. **`periodInsights` sort order in unlock step**: `findByAdvisorAndPeriod` HQL does not guarantee a sort order — confirm DAO impl orders by `displayOrder` (it does; `TutorAiInsightDaoHibernate` adds `ORDER BY displayOrder ASC`).

## How to verify

**Prerequisites:** local server running at `http://localhost:8080`; demo tutor with weekly insight data seeded.

```
Login URL: http://localhost:8080/demo?pl2-demo-type=tutor&demo-category=toolkit
```

1. **List page:** `http://localhost:8080/PLUS/WeeklyReports` — confirm table rows render with PROGRESS column showing N/total values.
2. **Detail page:** `http://localhost:8080/PLUS/WeeklyReport` — confirm insights timeline renders with LOCKED/UNDER_REVIEW/REVIEWED states. Training section at bottom should be dim (opacity ~0.5) with lock icon.
3. **Feedback flow:** expand the first UNDER_REVIEW card (auto-expanded on load). Three buttons: "Helpful", "Not Helpful", "Inaccurate". Click one — card should move to REVIEWED, next card should open. Repeat until all reviewed.
4. **Training unlock:** after all insights reviewed, confirm training section brightens, lock icon disappears, placeholder card renders.
5. **CTA:** confirm "Get More Sessions" CTA renders below training section at all times; link points to `/PLUS/TutorSchedule`.
6. **REVIEWED card behavior:** click a REVIEWED card — it should expand (show insight text + evidence) but show no feedback buttons.
7. **Monthly report regression:** `http://localhost:8080/PLUS/MonthlyReport` — confirm no regressions.
