# Catch-Up: Monthly Report port

## What this is

This PR ports the Monthly Report feature from the plus-uno React prototype to the plus web-app Java production codebase. The feature gives tutors a structured, monthly self-review: a list of historical monthly reports and a detail view for each month showing impact metrics, AI-generated coaching insights (with progressive disclosure), and recommended training. The progressive disclosure design — you unlock one insight at a time by giving feedback — is the core argument of the feature.

## Repo context

- **Proto (plus-uno)**: Vite + React prototyping environment for the PLUS design system — produces high-fidelity UI prototypes using real PLUS components and design tokens, not production features.
- **Prod (plus web-app)**: Server-side Java web application (Spring/Hibernate/Tomcat) with JSP templates, jQuery, Bootstrap 4.1.3 — delivers tutoring, student management, and AI-assisted coach review to educators.
- **Key translation constraint**: React/Vite component state management (useState, useNavigate) → server-fetched JSON + client-side JS state machine; PageLayout + PLUS DS components → pl2_head.jspf + topbar.jspf + Bootstrap 4.1.3; no client-side router.
- **Framework versions relevant to this PR**: Bootstrap 4.1.3 (`data-toggle`/`data-target`, not `data-bs-*`); jQuery 3.5.1; ES modules (`type="module"` script tags — the dominant pattern for feature-level JS in prod, contrary to prior spine; see FINDING-3 correction).
- **Diff base**: `git diff 29d41e50..HEAD` — 2 commits on branch `monthly-report` against `dev` at `29d41e50` (v11.3.0.4 for QA).

## What changed and why

### Substrate (translate freely — no argument change)

- React JSX → JSP + jQuery DOM manipulation — framework swap, argument survives
- PLUS DS components (Badge, Button, Alert, Progress, Pagination) → Bootstrap 4.1.3 equivalents (`.badge`, `.btn`, `.alert`, `.progress`)
- `MonthlyReportPage` + `MonthlyReportsListPage` → `monthly_report.jsp` + `monthly_reports_list.jsp`
- `monthly_report.js` uses `import { PlusInterface }` from `plus_components/general_interface.js` — ES module pattern, consistent with `students.js`, `strategy.js`, `schedule/` in prod
- SCSS + PLUS design tokens → `monthly_report.scss` (Bootstrap CSS vars + custom rules)
- `useNavigate` → `window.location.href` / `<a href>` links
- FA Free icons — direct transfer unchanged
- Shell load animation → omitted (no equivalent pattern in prod; plain content-start jspf handles layout)
- Session metrics (sessions, hours, schools) → `TutorSessionService.findByAdvisorSortedBetweenDates()` — real data
- `findDistinctPeriodsByAdvisor()` for list page periods — reuses existing service method

### Claim changes (confirmed by user — argument is preserved)

**CLAIM-1 — Server-side review state persistence**
- Argument: The sequential unlock (locked → under_review → reviewed) resumes where the tutor left off on every page load. The report is a structured self-review you return to, not a one-shot experience.
- Why it's a claim: Proto state was client-side only (useState, reset on reload). Moving it server-side changes when/whether continuity exists for the user.
- Invariant: `MonthlyReportServlet.getMonthlyReportData()` reads `TutorAiInsightItem.status` for each insight and returns it in the JSON response; `monthly_report.js:renderInsightsTimeline()` initialises `_reviewedCount` from `data.reviewedCount` (server value), not from 0 — `MonthlyReportServlet.java:183–204`, `monthly_report.js:117–119`.
- Old behavior: Not present in prod before this commit.
- Implementation: `MonthlyReportServlet.java` (new file, lines 120–209); `monthly_report.js` lines 117–133 (state init) and 288–327 (re-fetch after feedback).

**CLAIM-2 — Feedback ratings recorded to DB**
- Argument: The tutor's assessment of each insight (helpful/not helpful/inaccurate) is captured and stored. The feedback loop is real, not a UI affordance.
- Why it's a claim: Proto feedback buttons were advance-only — they incremented reviewedCount but sent no data. Recording changes the purpose of the interaction.
- Invariant: `MonthlyReportServlet.submitInsightFeedback()` creates or updates a `TutorAiInsightFeedbackItem` with `rating` set before calling `saveOrUpdate` — `MonthlyReportServlet.java:355–374`. JS POSTs the `rating` param — `monthly_report.js:292–296`.
- Old behavior: Not present in prod before this commit.
- Implementation: `MonthlyReportServlet.java` lines 330–416 (full `submitInsightFeedback` method); `monthly_report.js` lines 266–327 (`submitFeedback` + feedback button wiring).

**CLAIM-3 — No "View Recording" button**
- Argument: Recording playback infrastructure doesn't exist in prod at this commit. The button implied a capability that can't be delivered; removing it is more honest than a non-functional link.
- Why it's a claim: The button in the proto was part of the evidence presentation — each insight could be traced back to a specific session clip. Removing it changes what the tutor can do from an expanded insight card.
- Invariant: No "View Recording" button, link, or anchor in `monthly_report.jsp` or `monthly_report.js`. The `buildCardBody` function in `monthly_report.js:171` has an explicit comment confirming this.
- Old behavior: Not present in prod before this commit.
- Implementation: Absence — confirmed in both `monthly_report.jsp` and `monthly_report.js:buildCardBody`.

## Deferred

- **Student count** (`MonthlyReportServlet.java:196`): Returns -1; rendered as "—". Needs aggregation against `TutorStudentSessionAssignment` per tutor per period.
- **Learning time + skills mastered** (`MonthlyReportServlet.java:194–195`): Stubbed; no single-pass aggregation service confirmed.
- **Training recommendations** (`monthly_report.js:199`): Section unlocks correctly, shows placeholder. Needs a dimension→lesson mapping layer.
- **Time allocation breakdown**: Omitted entirely — no DB source for activity-type breakdown (Active Tutoring / Goal Setting / etc.) confirmed.

## Blips

**review-suggested — session-metrics-stub** (`MonthlyReportServlet.java:193–196`): Three of six impact metrics (studentCount, learningTimeMin, skillsMastered) are stubbed as -1. The UI renders "—" for these. Reviewer should confirm the three real metrics (sessionCount, hours, schoolCount) are computing correctly from `TutorSessionService`. The three stubbed metrics need a follow-up service method or HQL query — not a regression, but incomplete.

**review-suggested — training-recommendations-stub** (`monthly_report.js:199–207`): Training section gate works correctly (locked until all insights reviewed). When unlocked, shows one placeholder card. No lesson recommendation data source connected — reviewer should confirm the gate behavior is correct and the placeholder is acceptable for V1.

## What to focus on in review

- `MonthlyReportServlet.java:355–416` (submitInsightFeedback): This is the core of CLAIM-1+2. Verify (1) `TutorAiInsightFeedbackItem` is saved with the correct rating before status is changed, (2) the "unlock next LOCKED" scan operates on the correct period's insights sorted by `displayOrder`, and (3) the auth check (`insight.getAdvisor().getId().equals(advisor.getId())`) prevents cross-advisor manipulation.
- `monthly_report.js:288–327` (re-fetch after feedback): After each feedback POST, the JS re-fetches the full server state before re-rendering. If the fetch fails silently, the UI would show stale state. Verify the error path (`result.status === "error"`) re-enables buttons and does not leave the UI in a broken state.
- `MonthlyReportServlet.java:160–175` (page routing): The servlet uses `req.getRequestURI().contains("MonthlyReports")` to choose list vs. detail JSP. Verify this is robust to context-path variations.

## How to verify

1. `ant deploy` from `java/` directory — deploys servlet + JSPs + JS to local Tomcat
2. Log in at `http://localhost:8080/login` as a tutor with AI insight data
3. Navigate to `http://localhost:8080/PLUS/MonthlyReports` — list page renders with available periods
4. Click a period → navigates to `/PLUS/MonthlyReport?periodStart=...&periodEnd=...`
5. Detail page: confirm insight cards render with correct locked/under_review/reviewed state
6. Click Helpful on the first UNDER_REVIEW card → card advances; refresh page → state persists (CLAIM-1 check)
7. Inspect DB: `SELECT * FROM tutor_ai_insight_feedback WHERE advisor_id = ?` — confirm row inserted with correct rating (CLAIM-2 check)
8. Confirm no "View Recording" button visible on any expanded card (CLAIM-3 check)
9. Review all insights → confirm training section unlocks (lock icon disappears, placeholder appears)
10. Navigate to `/PLUS/TutorReview` — confirm no regression (shared services, separate servlet)

Note: `studentCount`, `learningTimeMin`, `skillsMastered` will display "—" — this is expected per the deferred stub, not a bug.
