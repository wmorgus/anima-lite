# Execution plan: recommend-sessions
Contract: ports/recommend-sessions/contract.md (Spine commit 9c02f5e8)
Prod base: anima-lite-recommend-sessions @ 29d41e50

## Blockers

1. **BLOCKER — "subject" is not modeled anywhere in the prod schema.** Grep across
   `item/`, `dto/`, and all `.hbm.xml` files confirms there is no subject/course
   field on `SessionItem`, `GroupItem`, `ShiftItem`, or `InstitutionItem`.
   `GroupItem.lessons` is a raw comma-separated lesson-id list, not a subject
   taxonomy, and no DtoHelper derives a subject label from it. CLAIM-2 (the rank
   rule) is written against "candidate set = open sessions in the student's
   subject + institution..." — that filter input does not exist in prod. This
   was not caught during ari-argue because the contract was written against the
   proto's mock dropdown (`Math` / `English` — hardcoded strings, not
   backed by prod data) without confirming the field existed prod-side.
   This is a genuine contract-vs-terrain mismatch, not a translation detail —
   per the ari-port halt policy, this must go back to ari-argue / the user
   before CLAIM-2 is implemented. Do NOT invent a subject proxy (e.g. reusing
   `GroupItem.lessons` as a stand-in) without confirmation; that would silently
   change what "subject match" means. Candidate resolution paths for the user
   to choose from (not decided here):
   - (a) Drop subject as a *filter/rank* input; keep it as a free-text or
     dropdown-only UI field used solely in the reason-text context, and rank
     purely on institution + free slots + soonest start (weakens CLAIM-2 as
     written — needs re-confirmation).
   - (b) Add a net-new subject field to `GroupItem` or `SessionItem` (schema
     change, larger scope than this port was framed as).
   - (c) Derive a coarse subject proxy from `GroupItem.lessons` via an existing
     lesson→subject lookup, if one exists elsewhere in the codebase (not found
     in this probe — would need a follow-up grep before trusting it).
   **This blocks CLAIM-2's commit only.** Everything else in the contract
   (CLAIM-1, 3, 4, 5, 6, 7, 8) is buildable against real prod data as probed
   below and is not blocked by this.

2. No other blockers found. Free-slot count, start time, institution, and
   already-enrolled-exclusion are all derivable from existing prod data (see
   Files touched §2 below). Persistence, gating, host placement, and field
   withholding all have confirmed prod patterns to mirror.

## Files touched (concrete)

| Path | Change | Claim |
|---|---|---|
| `java/docroot/jsp_pl2/tutor_schedule.jsp` | Add "+ Recommend Session" button + recommend-modal JSP fragment (multi-step: criteria select → results → confirm) | substrate (CLAIM-8: hosted here, not a new dashboard) |
| `java/docroot/javascript/pl2/schedule/tutor_schedule_recommend.js` (new file, following the existing `tutor_schedule_<topic>.js` split convention alongside `tutor_schedule_fill_ins.js`, `tutor_schedule_signups.js`, etc.) | New ES-module-pattern JS: modal step state, AJAX calls to the new servlet action(s), renders results list, submits confirm | substrate (scaffolding) + CLAIM-4 (field render/withhold) layered in separately |
| `java/sass/tutor_schedule.scss` (or a new `_recommend_modal.scss` partial imported from it, mirroring the `reflection.scss` pattern named in the contract) | Modal layout, step transitions | substrate |
| `java/source/edu/cmu/pl2/servlet/TutorScheduleServlet.java` | New `requestingMethod` branches: `getRecommendCandidates` (CLAIM-2 query + CLAIM-7 gating), `confirmRecommendation` (CLAIM-3/5 persistence) | substrate (branch scaffolding, empty/stub bodies) → filled in by CLAIM-2/7/3+5 commits |
| `java/source/edu/cmu/pl2/item/SessionRecommendationItem.java` (new) | Entity: `student` (FK PL2StudentItem), `session` (FK SessionItem), `advisor` (FK AdvisorItem, the recommending tutor), `reason` (text), `dateCreated` | CLAIM-3+5 |
| `java/source/edu/cmu/pl2/item/SessionRecommendation.hbm.xml` (new) | Hibernate mapping for the above, modeled on `item/TutorAiInsight.hbm.xml` | CLAIM-3+5 |
| `java/docroot/conf-tomcat-11.0/applicationContext.xml` | Add hbm mapping entry (mirror line ~167 pattern), DAO bean + DAO map entry (mirror lines ~708, ~1067-1069), service bean (mirror lines ~578-580) | CLAIM-3+5 |
| `java/source/edu/cmu/pl2/dao/SessionRecommendationDao.java` + `dao/hibernate/SessionRecommendationDaoHibernate.java` (new) | DAO pair, mirrors `dao/TutorAiInsightDao.java` + `dao/hibernate/TutorAiInsightDaoHibernate.java` | CLAIM-3+5 |
| `java/source/edu/cmu/pl2/service/SessionRecommendationService.java` + `service/impl/SessionRecommendationServiceImpl.java` (new) | Service pair, mirrors `service/TutorAiInsightService.java` + `service/impl/TutorAiInsightServiceImpl.java` | CLAIM-3+5 |
| `java/source/edu/cmu/pl2/service/ServiceFactory.java` (abstract getter, mirror line 201) + `service/ServiceFactoryImpl.java` (impl, mirror lines 503-505) | Register `getSessionRecommendationService()` | CLAIM-3+5 |
| `java/sql/pl2/v4.x/alter/YYYYMMDD_card<ticket-number>.sql` (new — actual naming convention confirmed as `YYYYMMDD_card<number>.sql`, no hyphen before the number, e.g. real examples: `20260324_card2225.sql`, `20260511_card2338.sql`) | `CREATE TABLE session_recommendation (...)` | CLAIM-3+5 |
| `dto/SessionDtoHelper.java` (existing — confirmed real name, contract's "TutorSessionDtoHelper" guess was close but not exact) | Extend or add a method assembling the recommend-candidates JSON (title/time/open-slots/subject-if-resolved; explicitly omit Zoom link + passcode fields that exist elsewhere in the session DTO) | CLAIM-4 |
| `java/source/edu/cmu/pl2/servlet/TutorScheduleServlet.java` (same file as above, later hunk) | Wire `AdvisorStudentMapService.findByAdvisor(advisor)` scoping + institution-match check into `getRecommendCandidates` | CLAIM-7 |
| `.anima-lite/ports/recommend-sessions/blips.md` | Record CLAIM-6 (no student-facing notification wired — record-only) as a blip; no prod code | CLAIM-6 (no code) |

CLAIM-1 (scope exclusion — drop `RecommendTutorsView.jsx`) requires no prod file
at all; it is enforced by simply never translating that proto file.

## Commit sequence (COMMIT DISCIPLINE — critical)

**Commit 1 — substrate.** No claim behavior: no rank rule, no gating rule, no
field withholding, no persistence.
- Message: `port(recommend-sessions): substrate — modal scaffolding + servlet action skeleton`
- Files: `tutor_schedule.jsp` (button + modal fragment shell, all three steps
  rendered as empty/placeholder containers), `tutor_schedule_recommend.js` (step
  navigation only — next/back/close; AJAX calls stubbed to hit the new
  `requestingMethod` values but the servlet side returns a hardcoded/empty
  candidate list), `tutor_schedule.scss`/new partial (visual styling only),
  `TutorScheduleServlet.java` — add the two new `requestingMethod` branches
  (`getRecommendCandidates`, `confirmRecommendation`) as empty/pass-through
  stubs (e.g. return `[]` / a "not implemented" JSON) so the wiring compiles
  and the modal is reachable end-to-end with no real behavior yet.
- Explicitly embodies CLAIM-8 (hosted on TutorSchedule, not a new dashboard)
  as a structural fact, but introduces no decision logic — placement isn't a
  behavior, it's where the file lives.

**Commit 2 — CLAIM-2 (ranking logic). BLOCKED — see Blockers §1.**
Do not write this commit until the subject-filter question above is resolved.
Once resolved:
- Message: `port(recommend-sessions): CLAIM-2 — heuristic session ranking`
- Files: `TutorScheduleServlet.java` (`getRecommendCandidates` body — real
  query: open sessions in student's institution [+ subject, if resolved] with
  free slots > 0, excluding sessions where `StudentSessionService.findBySession`
  already contains the student; sort by soonest `sessionStart`, then most open
  slots, then subject match if applicable), any new query method added to
  `SessionDtoHelper.java` or `TutorSessionService`.
- Claim behavior introduced: the transparent heuristic rank rule itself —
  this is the one place "matched to their needs" logic lives, and it must
  stay legible/inspectable per the contract's transparency requirement.

**Commit 3 — CLAIM-7 (gating).**
- Message: `port(recommend-sessions): CLAIM-7 — scope recommend to advisor's own students/institution`
- Files: `TutorScheduleServlet.java` (`getRecommendCandidates` — add
  `AdvisorStudentMapService.findByAdvisor(advisor)` check that the selected
  student belongs to the requesting tutor, and an institution-match check
  mirroring the pattern at lines ~611/649/724-726 of the same file); apply the
  same check inside `confirmRecommendation` before persisting.
- Claim behavior introduced: multi-tenant / advisor-student scope enforcement.
  Kept separate from CLAIM-2 because it is an authorization decision, not a
  ranking decision — the two must be independently auditable/revertable.

**Commit 4 — CLAIM-3+5 (persistence entity + confirm action).**
- Message: `port(recommend-sessions): CLAIM-3+5 — persist recommendation record`
- Files: `SessionRecommendationItem.java`, `SessionRecommendation.hbm.xml`,
  `applicationContext.xml` hunks, `SessionRecommendationDao.java` +
  `SessionRecommendationDaoHibernate.java`, `SessionRecommendationService.java`
  + `SessionRecommendationServiceImpl.java`, `ServiceFactory.java` +
  `ServiceFactoryImpl.java` getters, new SQL alter script, and
  `TutorScheduleServlet.java`'s `confirmRecommendation` body wired to call
  `ServiceFactory.getSessionRecommendationService().save(...)` with student,
  session, advisor (recommending tutor), reason text, dateCreated.
- Claim behavior introduced: the decision to persist a durable server-side
  record (vs. console.log/no-op) and its minimal field set.

**Commit 5 — CLAIM-4 (field display/withholding).**
- Message: `port(recommend-sessions): CLAIM-4 — show session summary fields, withhold Zoom access fields`
- Files: `SessionDtoHelper.java` (candidate-session JSON assembly — include
  title/time/open-slots/subject-if-resolved; explicitly exclude Zoom link +
  passcode fields), `tutor_schedule_recommend.js` (results-list rendering —
  only render the permitted fields).
- Claim behavior introduced: the field-withholding decision. Kept as its own
  commit (not folded into substrate rendering) because it is a deliberate
  access-sensitivity decision, not incidental UI scaffolding — an auditor
  should be able to see exactly which commit chose to hide Zoom credentials.

**CLAIM-6 — no prod commit.** Record-only behavior; there is no
notification code to withhold because none is being written. Log the gap as a
blip in `.anima-lite/ports/recommend-sessions/blips.md` (the proto's "will be
shared with the student" copy is not honored as a live notification this
port). If any commit's JS/JSP copy needs to avoid implying real-time student
notification (e.g. confirm-step microcopy), fold that copy fix into Commit 4
(it is presentation of the persistence action, not new behavior) and call it
out in that commit's description — do not create a 6th commit for a copy tweak.

**CLAIM-1 — no prod commit.** Enforced by omission: `RecommendTutorsView.jsx`
and its recruit-tutors path are never translated. Nothing to commit.

Total: **1 substrate commit + 4 claim commits** (CLAIM-2, CLAIM-7, CLAIM-3+5,
CLAIM-4), with CLAIM-2 blocked pending the subject-field resolution above.
CLAIM-1 and CLAIM-6 are accounted for with zero commits, as the contract's own
mapping implies ("largely substrate"/"no code" for placement and
no-notification — here genuinely zero, not folded into another commit).

## Step-by-step execution

1. Resolve Blocker §1 (subject field) with the user before starting Commit 2.
   All other steps can proceed in order regardless.
2. **Commit 1**: Add the "+ Recommend Session" button and three-step modal
   fragment to `tutor_schedule.jsp` (mirror the existing modal patterns already
   present in that JSP, e.g. the fill-in modal). Create
   `tutor_schedule_recommend.js` with step-navigation state only (no AJAX
   payload logic beyond hitting stub endpoints). Add the two new
   `requestingMethod` branches to `TutorScheduleServlet.java`'s `doPost` chain
   (around the existing `if/else if` block at lines 179-217) as stubs. Add
   SCSS. Verify the modal opens/closes/steps through with placeholder data.
3. **Commit 2** (post-blocker-resolution): Implement `getRecommendCandidates`
   query logic per the resolved rank rule. Use `SessionItem`/`TutorSessionItem`/
   `StudentSessionItem` and `SessionDtoHelper` patterns already probed.
4. **Commit 3**: Layer `AdvisorStudentMapService.findByAdvisor` + institution
   check into the same method (and into `confirmRecommendation`), following
   the institution-mismatch warn-log pattern already used elsewhere in
   `TutorScheduleServlet.java`.
5. **Commit 4**: Build the 7-part `SessionRecommendationItem` stack exactly
   mirroring `TutorAiInsightItem`'s 7 files/registrations (see Files touched
   table for each exact mirrored location). Wire `confirmRecommendation` to
   call the new service's save method with the minimal field set.
6. **Commit 5**: Restrict the JSON fields returned by `SessionDtoHelper`'s new
   candidate-assembly method to title/time/open-slots(+subject), and update
   the JS renderer to match. Confirm no Zoom link/passcode field is present in
   the response payload at any point (not just hidden client-side — do not
   send it to the browser at all).
7. Log the CLAIM-6 blip in `.anima-lite/ports/recommend-sessions/blips.md`.

## Verification approach

No automated test suite covers this area (prod's own efficient.md: "No
automated test suite for the reflection area... no automated test suite
generally — manual + CI schema check on PR"), and this environment has no
running Tomcat/MySQL instance wired up for `ant deploy` + browser verification.
Honest verification plan given that constraint:

- **Compile check**: `ant compile` (java/build.xml target) can be run in this
  environment if a JDK 17 toolchain is available; use it after each commit to
  catch type/wiring errors in the new Java files before moving to the next
  commit. This does not prove behavior, only that the code compiles.
- **Sass check**: `ant compile-sass` (or the raw `npx sass` invocation from
  build.xml line ~198) can be run standalone to confirm the new SCSS partial
  compiles without a full deploy.
- **Schema check**: the new SQL alter script should be run manually against a
  local/test MySQL instance if one is available, or at minimum reviewed for
  syntax against the confirmed alter-script naming/content convention
  (`20260324_card2225.sql` etc.) — this repo's CI (`check-tables-pl2.yml`)
  is the real gate and will run when the branch is pushed.
- **No claim of a browser-verified test pass.** If no local Tomcat/MySQL is
  available in this environment, final verification is by diff review against
  this plan and the contract, plus the compile/sass checks above — say so
  explicitly in the PR rather than asserting a manual browser test that did
  not happen.
