# Contract: recommend-sessions
Branch: anima-lite-recommend-sessions
Generated: 2026-07-07
Spine commit: 9c02f5e8
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue

## The argument
A tutor/supervisor, from the sessions dashboard, proactively steers a specific
student toward a specific already-scheduled session: pick a student + subject,
see a transparently-ranked list of open sessions that fit, and send the student
a personal, reasoned recommendation that is recorded server-side.

GATE-TELOS: PASSED as compatible-new. Fits prod's tutoring telos (session
tracking / lesson assignment / progress monitoring, server-rendered). Terrain
it plugs into: TutorScheduleServlet (/PLUS/TutorSchedule) as host, SessionItem /
TutorSessionItem / AvailableSignupsDto for candidate sessions. Strain noted and
resolved in CLAIM-2: prod has no session-recommendation mechanism; the port
defines an explicit, transparent rule rather than faking a needs-match.

## Substrate changes (free to translate)
- React JSX components → JSP + JSTL
- PLUS DS React components (Button, Table, Modal, NavTabs, Badge, Dropdown, Input,
  Toast, TopBar, StatCard) → Bootstrap 4.1.3 + JSP fragments
- useState (multi-step modal, selections, toast state) → server round-trips /
  request attributes / in-modal jQuery
- Inline styles + App.scss tokens → SCSS compiled via `npx sass` (reflection.scss pattern)
- backdrop-blur / success-check / hover transitions → CSS transitions + jQuery
- FontAwesome solid icons → FA Free (rename only)
- Success toast → prod AJAX success/error JSON pattern (ServletHelper.writeJSON;
  JS checks response.status === "error")
- Mock dropdown option lists → real reads (advisor's student roster, subjects,
  InstitutionItem schools)
- Breadcrumb / topbar / call-off alert-banner chrome → topbar.jspf (existing)

Host servlet: TutorScheduleServlet (/PLUS/TutorSchedule) — add the recommend
action here rather than a new dashboard.

## Claim changes (confirmed with user)
1. Scope — Decision: **port the reachable student-recommendation flow only**
   (RecommendModal). Drop the orphaned RecommendTutorsView / recruit-tutors path
   (imported but never rendered in proto). — Confirmed: yes, 2026-07-07.

2. Recommendation mechanism — Decision: **keep the "recommend" verb, backed by a
   transparent heuristic rank.** No ML, no "matched to their needs" data source
   implied. The rank rule is stated, not hidden. — Confirmed: yes (chose heuristic
   over honest-query-only and over full needs-based), 2026-07-07.
   **AMENDED 2026-07-07 (GATE-BLOCKERS, pre-execution):** prod has no `subject`
   field on SessionItem/GroupItem/ShiftItem/InstitutionItem — "subject" existed
   only in the proto's mock dropdown and backed nothing. Subject DROPPED from
   filter and rank. The proto's mock subject dropdown is removed.
   **AMENDED AGAIN 2026-07-07 (GATE-BREAK, mid-execution, ratified):** prod has no
   student-side "open slots" data either — every capacity concept in prod is
   *tutor-staffing* capacity, not student room. "Open slots" (a rank input here
   and a display field in CLAIM-4) has no backing. Open-slots DROPPED from the
   rank. **Final shipped rule:** candidate set = sessions in the student's
   **institution** the student is not already enrolled in; ranked by **soonest
   start**. Executor surfaced this as a CONTRACT-BREAK and narrowed rather than
   inventing a proxy; user ratified the narrowing 2026-07-07. Note: this leaves
   "recommend" as essentially "soonest upcoming institution sessions the student
   isn't in" — a product-thinness finding recorded for run4 review, not a defect.

3. User action on Confirm — Decision: **persist a recommendation record** (real
   server action, not console.log). Minimal fields. — Confirmed: yes (default
   accepted, not vetoed), 2026-07-07.

4. Session data shown — Decision: show session **title / time**. **Withhold Zoom
   link + passcode** — access-sensitive, not exposed in the recommend surface. —
   Confirmed: yes (default accepted), 2026-07-07.
   **AMENDED 2026-07-07 (GATE-BREAK, ratified):** "open slots" display DROPPED —
   no backing data in prod (see CLAIM-2 amendment). Shipped display = title + time
   only; Zoom link + passcode still withheld.

5. Persistence — Decision: **durable recommendation entity**, per prod's
   server-side telos — full 7-part wiring (Item + .hbm.xml + applicationContext.xml
   + Dao pair + Service pair + SQL alter). Minimal field set: student, session,
   recommending tutor, reason text, dateCreated. — Confirmed: yes (default
   accepted), 2026-07-07.

6. Notification — Decision: **record-only; no student-facing notification** this
   port (prod's student-facing notification channel is unconfirmed). The proto
   copy "will be shared with the student" is NOT honored as a live notification —
   log a blip so the gap is visible. — Confirmed: yes (default accepted), 2026-07-07.

7. Gating — Decision: **restrict to the tutor's own advisor-students and their
   institution's sessions** (multi-tenant + advisor-student relationship +
   session assignment scope). — Confirmed: yes (default accepted), 2026-07-07.

8. Surface scope — Decision: **recommend modal onto the existing TutorSchedule
   page only** — NOT the whole dashboard shell (fill-in / sign-ups / call-offs /
   reflections chrome stays out of scope). — Confirmed: yes, 2026-07-07.

## Open questions
(none blocking — all resolved above)
- Non-blocking: "Get More Sessions" CTA is absent at dev HEAD 29d41e50 (it lived
  on the weekly-report branch, not merged to dev). Entry point for this feature
  is the TutorSchedule page itself; if that CTA later merges to dev it becomes a
  natural secondary entry seam, but it is not required for this port.
