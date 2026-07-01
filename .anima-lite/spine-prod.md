# Spine: plus web-app (prod)
Generated: 2026-07-01
Commit: 29d41e50
Confidence: high
Refresh trigger: New servlet added, new item/DAO/service registered in applicationContext.xml, or schema version bumps past v9.x

## Material

**Language/Runtime:** Java (Jakarta EE 6.0) on Apache Tomcat 11.0. No modern JVM framework (no Spring Boot, no Quarkus). Spring is used only as an IoC container and transaction manager — not as an MVC framework.

**Build:** Apache Ant (`build.xml`). No Maven/Gradle. Version locked at 9.3.0.1 in `build.xml` line 17.

**ORM:** Hibernate with Spring JPA. Entity mappings are XML (`*.hbm.xml` files co-located with item classes). Validation mode is `validate` — no auto-DDL. All mappings and DAOs registered explicitly in `applicationContext.xml`.

**Database:** MySQL 8. JNDI datasource (`java:comp/env/jdbc/Pl2DS`). Schema in `java/sql/pl2/v9.x/`. Migrations are manual alter scripts; no Flyway/Liquibase.

**Frontend:** JSP + jQuery 3.5.1. No bundler, no transpiler. Sass compiled to CSS via `npx sass`. Third-party UI: jqWidgets, Bootstrap, Chart.js, Plotly, Highcharts.

**Key domain entities (230+ Item classes):** `PL2UserItem`, `PL2StudentItem`, `AdvisorItem`, `InstitutionItem`, `ModuleItem`, `LessonAssignedItem`, `SessionItem`, `TutorTimeAllocationItem`, `TutorAiInsightItem`.

**State shape:** Session-based auth (no JWT). User stored in HTTP session as `PL2UserItem`. Separate sessions for tutor and student interfaces.

## Formal

**Dominant pattern:** Classic Java EE layered architecture — Servlet → Service → DAO → Hibernate Entity. Every layer has an interface and an implementation. Spring wires them via `applicationContext.xml`; service methods are annotated with AOP transaction advice (read-only for `get*/find*/is*/has*`, write for `save*/delete*/update*/create*`).

**Module boundaries:**
- `servlet/` — 29 servlets, each handling a named feature surface. `AbstractServlet` is the auth/session gate for all tutor-side routes.
- `service/` + `service/impl/` — business logic, all Spring-managed.
- `dao/` + `dao/hibernate/` — `AbstractDao` interface; Hibernate impls.
- `item/` — 230+ domain entities with XML HBM mappings.
- `dto/` — data transfer objects; two large helpers (`DtoHelper` 132KB, `AdminDtoHelper` 59KB) aggregate response construction. This layer does significant work; it is not a thin pass-through.
- `student/` — parallel package (student/servlet/, student/dto/, student/helper/) for the student portal. Shares item/DAO layer but has its own servlet hierarchy.

**Dual-interface system:** Two fully separate user interfaces sharing the same DB. Tutor/advisor interface at `/PLUS` (PL2Servlet). Student portal at `/PLUSStudent` (PL2StudentServlet). Each has its own JSP tree (`jsp_pl2/` vs `jsp_pl2_student/`), auth, and navigation.

**Frontend pattern:** Feature-per-file JS (home.js, students.js, tutor_schedule.js, etc.). Flat global scope — no module system. `pl2Helper.js` (82KB) is a shared utility glob. Sass compiled separately; assets served statically.

**Inconsistency — the DTO helpers:** The stated layering puts business logic in Service. In practice, `DtoHelper` and `TutorReviewDtoHelper` contain substantial aggregation and formatting logic. The boundary between Service and DTO is blurry; adding a new view feature requires touching both.

**Tutor Review feature set (relevant sub-module):** Full stack exists — `TutorReviewServlet`, `TutorReviewDto/TutorReviewDtoHelper/TutorReviewImpactDto/TutorReviewTimeAllocationDto/TutorReviewAiInsightDto`, `tutor_review.jsp`, `javascript/pl2/tutor_review/` (main.js, impact_section.js, time_allocation_section.js, ai_insights_section.js). AI Insight items (`TutorAiInsightItem`) are persisted domain objects — this is not a thin display layer.

**Tutor Coach sub-module:** `tutor_coach.jsp`, `javascript/pl2/tutor_coach/` (main.js, tutor_coach_charts.js, tutor_coach_tables.js, util.js). Separate from TutorReview.

**Multi-tenancy:** Institution → Advisor → Student hierarchy. Role-based access. Institution admin pages in `jsp_pl2/institution_admin/` (22 files) and `javascript/pl2/admin/`.

**EdTech platform integrations:** Mathia, ALEKS, ExactPath, DreamBox, iReady, IXL, Khan Academy, eSpark, Imagine Math, MobyMax — each has dedicated goal/usage items, import servlets, and admin JSP fragments. These are structural seams, not minor integrations.

## Efficient

**Build pipeline:** `ant deploy` → compile Java, create JAR, compile Sass, deploy to local Tomcat. `ant war.vm` → production WAR. `ant release.plus` → WAR + SQL + lessons package.

**CI:** GitHub Actions. Two workflows: `check-tables-pl2.yml` validates SQL schema changes on PRs to `dev` branch (spins Docker, runs `create_tables_pl2.sql`, checks recent alter scripts). `sql-notification.yml` (notification only — not traced further). No automated test workflow; CLAUDE.md states "No automated tests are currently configured."

**Branch strategy:** `dev` is the integration branch. PRs go to `dev`. No main/release branch structure described.

**Docker:** Full docker-compose for local dev and CI. Images: `plus`, `plus-llm`, `plus-email`, `update-plus-database`. Dev containers available for faster test cycles. Box CLI used to download build dependencies.

**Deployment:** WAR deployed to Tomcat. Configuration via JNDI (datasource), `applicationContext.xml` (Spring beans), `web.xml` (servlet mappings), `urlrewrite.xml` (versioned asset routing). Schema changes are manual: write an alter script, run it, version with `ant updateVersionInfo`.

**No automated tests:** This is not a gap in the CLAUDE.md description — it is the actual state. The CI checks SQL schema validity only; no unit or integration tests exist.

## Final

**Inferred telos:** PLUS is an institutional tutoring management platform. Its job is to help educators (tutors/advisors) track, analyze, and act on student learning progress across multiple external EdTech platforms. The student portal is secondary — a lightweight student-facing surface. The core value is in the tutor/advisor interface: session tracking, lesson assignment, performance review (TutorReview, TutorCoach), and aggregated reporting across EdTech goal data.

The TutorReview feature (with AI insights as persisted domain objects) suggests the platform is actively moving toward automated performance analysis — not just reporting what happened, but generating structured assessments that a tutor/advisor can act on.

**Evidence traced from:**
- Route map: 8 named tutor/advisor routes vs. 3 student routes.
- Defensive code concentration: the DTO helpers are large and complex precisely around performance data aggregation (TutorReviewDtoHelper, TutorPerformanceDtoHelper).
- Entity investment: `TutorAiInsightItem` and `TutorTimeAllocationItem` are persisted entities, not transient display constructs — the system treats AI-generated insights as first-class data.
- EdTech integration breadth (10 platforms): the system's identity is as an aggregator across tools, not as a standalone curriculum engine.
- Test absence: the authors feared database schema breakage most (the only CI check). Application logic correctness is not currently gated.

**Confidence:** High for the tutor-management telos; medium for the AI-insight trajectory (the entities exist and are wired, but actual LLM integration depth was not traced).

## Disclaimers
This spine points in a direction. It is not a guarantee. Treat any claim
here that materially affects a port decision as worth a quick verification
pass against the actual code, not as settled fact.
