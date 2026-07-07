# Contract: Monthly Report
Branch: monthly-report
Generated: 2026-07-02
Spine commit: 9c02f5e8
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue

## The argument
The monthly report gives tutors a structured, sequential self-review: each coaching dimension must be acknowledged before the next unlocks, and training recommendations appear only after all insights are reviewed. Discovery is earned, not immediately available.

## Substrate changes (free to translate)
- React JSX → JSP + jQuery DOM manipulation — framework swap, argument survives
- PLUS DS components (Badge, Button, Alert, Progress, Pagination) → Bootstrap 4.1.3 equivalents — component library swap, same UI roles
- React useState for review progress → server-side DB + client-side JS to reflect persisted state — mechanism changes per Claim 1, but sequential structure preserved
- PageLayout/sidebarConfig/topBarConfig → pl2_head.jspf + topbar.jspf + sidebar_nav.jspf — layout wiring only
- useNavigate → href links / server-side navigation — routing mechanism
- SCSS + design tokens → Sass + Bootstrap CSS vars — styling system swap
- FA Free icons — direct transfer, unchanged
- Shell load animation / page reveal CSS — remove or replace with simple CSS transition; display intent not argumentation
- MonthlyReportPage + MonthlyReportsListPage → two JSP files (monthly_report.jsp, monthly_reports_list.jsp)
- Mock data → new servlet + DTO fetching real data from DB

## Claim changes (confirmed with user)
- **CLAIM-1: Progressive disclosure state persists server-side** — Proto: sequential reveal is client-side only (resets on reload). Decision: persist review progress to DB; page load resumes where tutor left off — Confirmed: yes, 2026-07-02
- **CLAIM-2: Feedback ratings recorded to DB** — Proto: Helpful/Not Helpful/Inaccurate buttons advance-only (no data captured). Decision: each button press records the rating (helpful/not-helpful/inaccurate) for that insight + tutor to DB — Confirmed: yes, 2026-07-02
- **CLAIM-3: "View Recording" button removed** — Proto: button present on expanded dimension cards, links to '#'. Decision: remove entirely; can add later when recording infrastructure exists — Confirmed: yes, 2026-07-02

## Open questions
None — all claim changes confirmed. Ready for ari-port.
