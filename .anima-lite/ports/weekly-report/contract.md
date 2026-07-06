# Contract: weekly-report
Branch: weekly-report
Generated: 2026-07-05
Spine commit: 9c02f5e8
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue

## The argument
This week's teaching performance is legible and actionable: dimensions are reviewed sequentially, each backed by an evidence quote from a real session, and training resources unlock only once all dimensions are engaged. The feature promises that AI observation leads to structured reflection, and structured reflection unlocks improvement resources.

## Source of truth
`WeeklyReportContent.jsx` is the canonical component. `WeeklyReportPage.jsx` exists but is the older, less polished version. Port WeeklyReportContent.

## Substrate changes (free to translate)
- React component tree → JSP + jQuery DOM rendering — argument survives rendering engine swap
- PLUS DS design tokens → Bootstrap 4.1.3 utility classes + prod SCSS variables — visual values are substrate
- Framer Motion count-up animations (metrics, stats counters) → CSS transition or no animation — flourish, not argument
- Page-entry reveal animation (staggered revealIn keyframes) → no animation or CSS fade — delight layer, not argument
- Client-side state (reviewedCount, activeKey, feedbackSelections) → server-persisted TutorAiInsightItem.status (LOCKED/UNDER_REVIEW/REVIEWED) — prod schema already encodes the sequential-gating argument
- PLUS DS spec components (RecommendedLessons, etc.) → Bootstrap card markup — substrate re-skin
- Cross-playground asset imports (from home-redesign/src/assets/) → prod-local asset paths via /v/<version>/... — named proto inconsistency, clean substrate fix
- Inline `<style>` keyframe injection → external SCSS — named proto inconsistency, architecture cleanup
- React Router (list/detail SPA navigation) → prod servlet URLs (/PLUS/WeeklyReports, /PLUS/WeeklyReport) — prod already has the two-URL/one-servlet pattern from MonthlyReportServlet
- ShellContext/PageLayout → prod JSP fragments (pl2_head.jspf, topbar.jspf, sidebar) — standard prod shell
- FILTERED_TRAINING constant (proto shows 3 of 4 items) → server-side filtering in DtoHelper/Service — business logic location, not argument
- PLUS DS Pagination → Bootstrap pagination or inline links — navigation control, argument survives

## Claim changes (confirmed with user)

- **CLAIM-2 — Three feedback options (Helpful / Not Helpful / Inaccurate)**: all three options must be ported; "Inaccurate" is the contestability mechanism. — Decision: preserve all three — Confirmed: yes, 2026-07-05. Pre-port check required: verify TutorAiInsightFeedbackItem schema supports an `inaccurate` type (or add it).

- **CLAIM-3 — Training section visible-locked**: training section renders visible but inaccessible (opacity 0.5, pointer-events: none, lock icon) until ALL dimensions are in REVIEWED status. The visible-but-locked state communicates "there is something waiting — earn it." — Decision: preserve (option a) — Confirmed: yes, 2026-07-05.

- **CLAIM-5 — Evidence quote block + View Recording button**: each expanded dimension card shows an evidence quote with session metadata. "View Recording" button is conditionally hidden if no recording URL is available in the DTO — not rendered as a dead link. — Decision: preserve quote block; conditionally hide button — Confirmed: yes, 2026-07-05.

- **CLAIM-6 — Delta badges (week-over-week)**: WeeklyReportContent (canonical source) does not include delta badges — only the older WeeklyReportPage.jsx has them. Deltas are out of scope for this port. — Decision: deferred (not in canonical source) — Confirmed: yes, 2026-07-05.

- **CLAIM-7 — "Get More Sessions" scheduling CTA**: proto shows a CTA to schedule more tutoring sessions at the bottom of the report. Destination in prod unknown. — Decision: preserved by default, pending confirmation — Confirmed: default-preserve, 2026-07-05. ari-port: investigate whether a scheduling destination exists; if not, log review-suggested blip and defer the section.

- **CLAIM-8 — Per-report completion count on list page**: list view shows N/total dimensions reviewed per report (e.g. "5/5") as a progress indicator — tracks historical engagement. Requires server DTO to expose reviewedCount per weekly report. — Decision: preserve — Confirmed: yes, 2026-07-05.

## Substrate-treated decisions (logged as blips, not confirmed claims)

- **CLAIM-1 pattern (feedback irreversibility)**: prod schema already models sequential gating; UI should reflect REVIEWED cards as non-interactive. Whether the server allows status downgrade is an implementation detail — UI does not expose re-review. Log as info blip.
- **CLAIM-4 pattern (optimistic advance)**: recommend optimistic UI (advance on click, POST async, rollback on error) to preserve the "commit and move forward" rhythm. Architecture decision, not argument change. Log as info blip.

## Open questions
- Does `TutorAiInsightFeedbackItem` schema support `inaccurate` as a feedback type? If not, schema addition required before CLAIM-2 can be implemented. ari-port must verify before implementing feedback submission.
- Does a session-scheduling destination exist in prod for CLAIM-7 CTA? ari-port investigates; if absent, section is deferred with review-suggested blip.

## Playwright verification
login_url: http://localhost:8080/demo?pl2-demo-type=tutor&demo-category=toolkit
feature_url: http://localhost:8080/PLUS/WeeklyReport
checks:
  - claim: "CLAIM-2 — three feedback options"
    steps: "Expand first dimension card; look for feedback buttons"
    expect: "Three buttons render: Helpful, Not Helpful, Inaccurate"
  - claim: "CLAIM-3 — training section locked"
    steps: "Load detail page with no reviewed dimensions; scroll to training section"
    expect: "Training section visible at reduced opacity with lock icon; not interactive"
  - claim: "CLAIM-3 — training section unlocked"
    steps: "With all dimensions in REVIEWED status, reload page; scroll to training section"
    expect: "Training section fully interactive; lock icon absent"
  - claim: "CLAIM-5 — View Recording conditional"
    steps: "Expand a dimension card; check for View Recording button"
    expect: "Button present if recording URL in DTO; absent if no URL"
  - claim: "CLAIM-8 — completion count on list"
    steps: "Load /PLUS/WeeklyReports list page"
    expect: "Each row shows N/total reviewed count for that week's report"
