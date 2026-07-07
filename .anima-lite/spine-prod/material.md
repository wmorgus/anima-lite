# Material: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash — HEAD: 29d41e50)

## §1 Languages
- Java (server) — plain bean-style entities, no Lombok/records
- JSP (views) — raw `<% %>` scriptlets, NOT JSTL (0 taglib directives repo-wide; see formal.md §3)
- JavaScript — predominantly global-scope jQuery; no transpile/bundle step
- SQL — MySQL 8; schema by hand-written versioned scripts in `java/sql/pl2/`
- (No `.scss` source present at dev HEAD — the sass build target exists but its source tree is empty here; see efficient.md §1)

## §2 Backend frameworks (code-derived: `java/extlib/` jars + applicationContext.xml)
- Spring 6.2.5 (core/beans/context/orm/jdbc/tx/web/webmvc/aop) — XML-wired, no `@Autowired`
- Hibernate ORM 6.6.25.Final — legacy `.hbm.xml` mappings, `hibernate.dialect=MySQL8Dialect`, `hbm2ddl.auto=validate` (no auto-DDL), batch_size=50
- Jakarta Servlet API 6.1.0; `web.xml` targets Servlet 6.0 / Jakarta EE 10 → Tomcat 11.0 runtime
- Log4j2 2.24.3; mysql-connector-j 8.4.0; org.json for JSON (no Jackson); opencsv 4.5; jakarta.mail 2.0.1; google-api-client 1.21.0; urlrewritefilter 5.1.3
- App internal version `11.3.0.4` (`java/build.xml` `plus.version`)

## §3 Frontend libraries (code-derived: `java/docroot/` file headers)
- Bootstrap 4.1.3 (`css/bootstrap/bootstrap.css`) — Bootstrap-4 syntax (`data-toggle`/`data-target`, NOT `data-bs-*`)
- jQuery 3.5.1 (`javascript/lib/jquery-3.5.1.js`); jQuery UI 3.3.1; DataTables 1.13.2
- jqWidgets — co-bundles a SECOND, older jQuery 1.11.1 (`javascript/jqwidgets/`) — two jQuery versions coexist (named finding)
- bootstrap-multiselect (version unknown — no banner)

## §4 Key dependencies
- Persistence: Hibernate + Spring ORM over MySQL 8. DTOs (`dto/`, 89) assembled by static `*DtoHelper` classes for JSP consumption.
- All external libs vendored as jars in `java/extlib/` — no Ivy/Maven/Gradle resolution.

## §5 Data structures / schemas
- 107 `.hbm.xml` legacy mappings co-located with each `*Item.java` in `item/`; loaded via `mappingResources` in applicationContext.xml.
- All entities extend abstract `Item` base (`item/Item.java`) supplying `objectEquals`/`objectHashCode`/`objectCompareTo`; every entity hand-implements `equals`/`hashCode`/`compareTo`.
- Join-table entities use composite keys via paired `*Id.java` classes + `<composite-id>` (e.g. `TutorSessionId`, `StudentSessionId`) — structurally distinct from simple-PK entities.

## §6 State shape
- Server-rendered request/session model, no SPA state. Login carried as `PL2UserItem` fetched per-request (`ServletHelper.getLoggedInUserItem`).
- Domain state lives entirely in MySQL via Hibernate; no cache layer, no in-memory store, no client-side state library. `web.xml` sets no `session-timeout` (container default).

---
(Sections below are lookup APPENDICES — exempt from the ~50-line narrative cap per ari-map SKILL.md.)

## §7 Entity/field inventory
One row per load-bearing entity in the tutoring/scheduling/enrollment/staffing/reflection/institution domain. Fields + table names are `.hbm.xml`-derived, not inferred.

| entity | backing table | key fields (name: type) | FKs (field → target) | notes |
|---|---|---|---|---|
| SessionItem | `session` | id: long; sessionName: string; sessionStart/sessionEnd: timestamp; sessionUrl: string; teacherName: string; period: string; cancelled: boolean; cancelledAt: timestamp; dateAdded: timestamp; attendanceTaken: boolean; attendanceNotes: string; hostKey: string; assignmentsGenerated: boolean | cancelledBy → AdvisorItem; institution → InstitutionItem; shift → ShiftItem; group → GroupItem | `getConsolidationKey()` = `group.name + start`, derived/non-persisted. **No capacity/subject field.** |
| TutorSessionItem | `tutor_session` | composite `TutorSessionId`(advisorId, sessionId); notifiedOfCancellation: boolean; tutorCancelled: boolean; dateAdded: timestamp; role: enum TutorSessionRole; isFillIn: boolean | advisor → AdvisorItem; session → SessionItem | "Tutor" = AdvisorItem; no separate TutorItem class. |
| StudentSessionItem | `student_session` | composite `StudentSessionId`(studentId, sessionId); dateAdded: timestamp | student → PL2StudentItem; session → SessionItem; addedAdvisor → AdvisorItem | **This join row IS "enrollment"** — a student in a specific session instance. |
| GroupItem | `institution_group` | id: long; name: string; lessons: string; inactiveFlag: boolean | institution → InstitutionItem; edTech → EdTechItem | `lessons` is free-text string, not a taxonomy FK (see §8.3). |
| ShiftItem | `shift` | id: long; teacherName: string; dayOfWeek: enum DayOfWeek; startTimeEst/endTimeEst: time; numTutorsNeeded: integer; numLeadTutorsNeeded: integer; isActive: boolean; created/updatedTime: timestamp | institution → InstitutionItem (not-null); createdBy/updatedBy → AdvisorItem; group → GroupItem | **Capacity lives here — tutor-staffing only** (§8.1). |
| InstitutionItem | `institution` | id: long; name/zip/city/state/country: string; kickoffJspfName: string; independent/inactiveFlag/noToolkit/accreditationEnabled: boolean; aliasId: long; lessons: string; lessonTimeGoal: int; languagePreference: string | (root — no up-FK) | Groups/shifts/students/advisors all FK down to this. |
| PL2StudentItem | `student` | id: long; anonId/salt: string; first/last/preferred + anon* names: string; schoolStudentId: string; birthDate: timestamp; grade: integer; ses/parentsEducationLevel/zip/gender/race: string; inactiveFlag: boolean; mathKnowledge/goals: string; tutoringType: string; proficiency: integer; canSetAchievementStrategy: boolean | institution → InstitutionItem; addedByAdvisor → AdvisorItem | Class is **`PL2StudentItem`** not `StudentItem` (naming trap). **No email field** (§8.2). |
| AdvisorItem | `advisor` | id: long; anon/salt/name fields: string; role: **string (freetext, not enum)**; inactiveFlag: boolean; isLeadTutor: boolean; clearanceStatus: string; isProspective: boolean; mentoring* fields; mathKnowledge/position: string; dateAdded: timestamp; signupConsentCompleted: boolean | institution → InstitutionItem | **One entity for advisor/tutor/admin**, disambiguated by `role` string + `isLeadTutor`. "Tutor*" classes are join/activity tables FK'd here. |
| ReflectionItem (base) | `reflection` | id: long; dateCreated/sessionDate: timestamp; reflectionText/goingWell/needsImprovement/noteToFutureSelf/objective: string; isBackground: boolean; actualFileName/filePath: string; rating: integer | student → PL2StudentItem; advisor → AdvisorItem; status → StudentStatusItem | Older/general reflection, distinct from the session-reflection cluster. |
| SessionReflectionItem | `session_reflection` | id: long; sdnhReasons/Explanation: string; sessionRating: int; session Pros/Cons/Notes/techDifficulties: string; selfRating: int; self Pros/Cons/Notes: string; missingStudents: string; formRating: int; formNotes/reflectionExperience: string; dateSubmitted/Modified: timestamp; recordingUploaded: boolean; videoName: string; status: enum ReflectionStatus | session → SessionItem (not-null); advisor → AdvisorItem (not-null) | Advisor-authored, one per session. |
| StudentReflectionItem | `student_reflection` | id: long; studentRating: integer; notes: string | sessionReflection → SessionReflectionItem (not-null); student → PL2StudentItem (not-null) | Per-student rating nested under a SessionReflection (1:many). |
| PL2MessageItem | `message` | id: long; messageText: string; actualFileName/filePath: string; dateSent/dateRead: timestamp | sender → PL2UserItem; receiver → PL2UserItem | In-app inbox (relevant to §8.2). |

Gaps: `GroupItem`/`InstitutionItem` share a `lessons: string` of unconfirmed semantic (free text vs. serialized) — consuming code not traced. `AdvisorItem.role` (string) vs `TutorSessionRole` (enum on TutorSessionItem) are two "role" concepts with colliding names.

## §8 Capabilities prod does NOT have
1. **Student-side session capacity / "open slots" — ABSENT (tutor-staffing capacity only).** `ShiftItem.numTutorsNeeded`/`numLeadTutorsNeeded` and `IndividualShiftDto` (`totalTutorsNeeded`, `tutorsSignedUp`, `isFull`) are all tutor-staffing. `grep -riE "maxStudent|capacity|studentCapacity|numStudentsNeeded"` over `item/`+hbm+`dto/` → zero student-capacity hits. A port assuming "session has max students" invents a field prod lacks.
2. **Out-of-band student notification — ABSENT (in-app pull inbox only).** `PL2MessageItem`/`PL2StudentMessageServlet` give students a readable in-app inbox, but `PL2StudentItem` has **no email field**, and every email/Slack send site targets advisors/tutors/admins only. No email/SMS/push to students is structurally possible without adding a contact field.
3. **`subject` / course-taxonomy on sessions or groups — ABSENT.** `grep -riE '"subject"|subject_id|courseTaxonomy|\bsubject\b'` over `item/*.java`+`*.hbm.xml` → zero hits. `GroupItem`/`InstitutionItem` carry a `lessons` free-text string instead; no subject enum/FK/table anywhere.

## §9 Domain vocabulary
- **session** = row in SessionItem — one scheduled tutoring meeting instance (has group, optional shift, optional cancellation).
- **shift** = row in ShiftItem — a recurring weekly slot (day/time + tutor-staffing target) under a group; sessions generate against shifts.
- **group** = row in GroupItem (`institution_group`) — a cohort/class within an institution, tied to one edTech.
- **institution** = row in InstitutionItem — a school/district; root of institution→group→shift/session→student/advisor.
- **student** = row in PL2StudentItem (class is `PL2StudentItem`, not `StudentItem`).
- **advisor / tutor** = row in AdvisorItem — one entity for advisor/tutor/admin, disambiguated by `role` string + `isLeadTutor`.
- **enrollment** = row in StudentSessionItem — a student in one session instance (composite studentId+sessionId).
- **capacity** = tutor-staffing only (ShiftItem.numTutorsNeeded); no student-capacity concept (§8.1).
- **reflection (general)** = row in ReflectionItem; **session reflection** = SessionReflectionItem (advisor's post-session form); **student reflection** = StudentReflectionItem (per-student rating under a session reflection).
- **message** = row in PL2MessageItem — in-app inbox message between two PL2UserItems.

Enums (`enums/`, 12 — closed code-derived value lists):
- **SessionStatus**: COMPLETED, CANCELLED, ACTIVE, URGENT, DEFAULT
- **TutorSessionRole**: LEAD, REGULAR (on TutorSessionItem.role — distinct from AdvisorItem.role string)
- **DayOfWeek**: MONDAY…SUNDAY
- **EdTechName**: MATHIA, EXACT_PATH, IMAGINE_MATH, ALEKS, DREAM_BOX, ESPARK, IREADY, IXL, DELTA_MATH, MOBY_MAX, KHAN_ACADEMY, NONE
- **ReflectionStatus**: IN_PROGRESS, SUBMITTED
- **CallOffApprovalType**: AUTO, MANUAL · **CallOffReason**: ILLNESS, FAMILY_EMERGENCY, JOB_CONFLICT, TRANSPORTATION_ISSUE, ACADEMIC_COMMITMENT, SIGNED_UP_BY_MISTAKE, OTHER · **CallOffStatus**: PENDING, APPROVED, REJECTED, WITHDRAWN · **CallOffType**: ONE_TIME, RECURRING
- **GoalCadence**: WEEKLY, BIWEEKLY, MONTHLY · **GoalCategory**: EFFORT, PROGRESS
- **StudentEngagementStatus**: FULL, PARTIAL, NONE
