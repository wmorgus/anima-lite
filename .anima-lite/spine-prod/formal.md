# Formal: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash)

## Layered architecture (actual, matches CLAUDE.md)
1. servlet/ — web layer, extends AbstractServlet; handles doGet/doPost, session check, forward to JSP
2. service/ + service/impl/ — business logic; interface + impl split; Spring-managed transactions
3. dao/ + dao/hibernate/ — data access; AbstractDao interface + *DaoHibernate implementations
4. item/ — Hibernate-mapped domain entities (*Item + *.hbm.xml pairs)
5. dto/ — data transfer objects assembled by large DtoHelper classes
6. helper/ — cross-cutting concerns (email, plot, servlet utilities, demo mode)

## Module boundaries
- edu.cmu.pl2.* — tutor/advisor interface (primary application)
- edu.cmu.pl2.student.* — student portal (separate servlet hierarchy, separate session)
- No shared DTOs between the two interfaces — each has its own *Dto tree

## Dominant patterns
- Factory access: ServiceFactory.get*Service(), DaoFactory.get*Dao() — no DI injection at call sites
- ThreadLocal for per-request user state (e.g., TutorReviewServlet.loggedInUserItem)
- Servlet dispatches to JSP via RequestDispatcher.forward()
- AJAX responses: servlets return JSON (JSONObject/JSONArray) directly to response writer
- JSP fragments (.jspf) for shared layout: pl2_head.jspf, topbar.jspf, sidebar_nav.jspf, pl2_content_start/end.jspf

## Shape of a typical feature change
Servlet receives request → calls ServiceFactory → Service calls DaoFactory → DAO queries Hibernate →
result assembled into DTO by DtoHelper → servlet sets DTO as request attribute → forwards to JSP →
JSP renders HTML + inline JS bootstrap → jQuery handles interactivity

## Tutor Review feature (as observed)
- TutorReviewServlet.java — extends AbstractServlet, routes GET/POST both to doPost
- TutorReviewDto.java — three-section wrapper (impact, time allocation [disabled V1], AI insights)
- tutor_review.jsp — JSP entry point at /jsp_pl2/tutor_review.jsp
- javascript/pl2/tutor_review/ — four JS modules: main.js, impact_section.js, time_allocation_section.js, ai_insights_section.js
- Time allocation section disabled at DTO level (commented out); JS file still present

## Named inconsistencies (findings)
- FINDING-1: TimeAllocation is commented out in TutorReviewDto (V1 scope reduction) but time_allocation_section.js still ships. ari-port must track whether the proto re-enables this or introduces new sections.
- FINDING-2: DtoHelper (132KB) and AdminDtoHelper (59KB) are monolithic — business logic has migrated into helper classes rather than staying in Service layer. New features should use *DtoHelper pattern to match, even though it violates strict layering.
- FINDING-3: No automated tests. Verification is manual (ant deploy, browser check). No test infrastructure to protect against regressions.
