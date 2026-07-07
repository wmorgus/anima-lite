# Material: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash — HEAD: 29d41e50)

## Languages
- Java — Jakarta EE 6.0 servlet API, Tomcat 11.0.23
- JSP + JSTL — server-side rendering
- JavaScript — no transpile step; ES modules dominant for feature-level JS; legacy shared utilities remain global-scope jQuery
- Sass/SCSS — compiled via `npx sass`, not a bundler
- SQL — MySQL 8, schema managed by hand-written scripts in java/sql/pl2/

## Backend frameworks (code-derived: applicationContext.xml + extlib/)
- Apache Tomcat 11.0.23 — servlet container
- Hibernate ORM + Spring JPA — entity persistence; hbm2ddl.auto=validate (no auto-DDL)
- Spring AOP — declarative transaction management only
- Log4j2 — logging
- org.json (JSONObject/JSONArray) — JSON serialization; no Jackson

## Frontend libraries (code-derived: pl2_head.jspf script/link tags + file headers)
- jQuery 3.5.1 — DOM and AJAX (confirmed: `/javascript/lib/jquery-3.5.1.js` header)
- Bootstrap 4.1.3 — layout + collapse/modal components (confirmed: bootstrap.js header)
  - Data attributes: `data-toggle`/`data-target` (Bootstrap 4 syntax, NOT `data-bs-*`)
- Highcharts — data visualization (confirmed: javascript/pl2/highcharts/)
- DataTables — tabular display (confirmed: javascript/pl2/DataTables/)
- jqWidgets — grid widgets (confirmed: extlib/jqwidgets/)
- Chart.js, Plotly — secondary visualization

## Data structures
- Entities: *Item.java + *.hbm.xml pairs in item/ (code-derived: find count)
- DTOs: *Dto.java assembled by *DtoHelper.java — DtoHelper.java ~132KB, AdminDtoHelper ~59KB
- Lesson content: JSON files in javascript/pl2/lessons/

## Key entities (load-bearing)
PL2UserItem, AdvisorItem (= tutor/mentor; confirmed via reflection.jsp `tutorId` param → `getAdvisorService().get()`), PL2StudentItem, InstitutionItem, SessionItem, TutorSessionItem, TutorAiInsightItem, TutorAiInsightFeedbackItem

## Native reflection subsystem — data model (code-derived, terrain for the tutor-reflection-form port)
Two related but distinct reflection entities exist:
- **SessionReflectionItem** (`item/SessionReflection.hbm.xml`) — the mentor/tutor's per-session self-reflection form. Fields: `advisor` (FK AdvisorItem), `session` (FK SessionItem), `sdnhReasons`/`sdnhExplanation` (session-did-not-happen), `sessionRating`/`sessionPros`/`sessionCons`, `techDifficulties`, `sessionNotes`, `selfRating`/`selfPros`/`selfCons`/`selfNotes` (tutor's self-assessment), `missingStudents`, `formRating`/`formNotes`/`reflectionExperience` (meta-feedback on the form itself), `recordingUploaded`/`videoName`, `status` (ReflectionStatus enum), `dateSubmitted`/`dateModified`.
- **StudentReflectionItem** (`item/StudentReflection.hbm.xml`) — a per-student child row of a SessionReflectionItem. Fields: `sessionReflection` (FK), `student` (FK PL2StudentItem), `studentRating`, `notes`. One SessionReflectionItem has many StudentReflectionItems (one per student in the session).
- **ReflectionItem** (older/parallel model, `item/Reflection.hbm.xml`) — still live, used by `MentorReflectionPost` (activity feed) and read by AdminServlet/StudentDashboardServlet/ResearchDashboardServlet. Fields: `student`, `advisor`, `status`, `dateCreated`, `sessionDate`, `reflectionText`, `goingWell`, `needsImprovement`, `noteToFutureSelf`, `objective`, `isBackground`, `actualFileName`/`filePath`, `rating`. This is a simpler, feed/dashboard-facing reflection record, distinct from the SessionReflection/StudentReflection pair that ReflectionServlet's save path writes to.
- **ReflectionStrategyMapItem** — join entity mapping reflections to coaching strategies (composite key `ReflectionStrategyMapId`).
- Git history confirms active, sustained development of this exact feature under the name "Tutor Reflection Form": commit `462dfa96` "Card2225: Tutor Reflection Form Editing" (recent), plus a long commit chain back through 2020 (file uploads, zip support, Slack escalation workflow, ajax error handling, dirty-page handling).

## State shape
- All user session state in HTTP session (key: cmu.edu.pl2.item.PL2UserItem)
- No client-side state management — page re-renders reset all state
- Multi-tenancy via InstitutionItem; advisor-student relationships explicit in DB
- Reflection status persisted server-side on SessionReflectionItem.status (ReflectionStatus enum) and ReflectionItem.status; not initialized client-side

## Build artifact
- Exploded WAR via `ant deploy` / packaged WAR via `ant war.vm`
- External libs checked in to java/extlib/ — no Maven/Gradle dependency resolution
- Sass compiles to css-build/, copied to docroot/css/pl2/ (reflection.scss → reflection.css confirmed present in css-build/)
