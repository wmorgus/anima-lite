# Formal: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash)

## Layered architecture (code-derived: package enumeration + file counts)
1. servlet/ — 37 files; extends AbstractServlet; handles doGet/doPost, session auth, forwards to JSP
2. service/ + service/impl/ — 100 interface files; Spring-managed transactions; interface+impl split
3. dao/ + dao/hibernate/ — 219 files; AbstractDao interface + *DaoHibernate implementations
4. item/ — 131 files; Hibernate-mapped domain entities (*Item.java + *.hbm.xml pairs)
5. dto/ — data transfer objects assembled by *DtoHelper classes
6. helper/ — cross-cutting concerns (email, plot, servlet utilities, demo mode)

## Module boundaries (code-derived: package enumeration)
- edu.cmu.pl2.* — tutor/advisor interface (primary application)
- edu.cmu.pl2.student.* — student portal; separate servlet hierarchy, separate session
- No shared DTOs between the two interfaces

## Dominant patterns (code-derived: grep-confirmed)
- All 7 tutor-side servlets extend AbstractServlet (grep: `extends AbstractServlet` → 7 hits) (code-derived)
- ServiceFactory used 484 times across servlet layer; zero `@Autowired`/`@Inject` at call sites (code-derived)
- AJAX responses: servlets write JSON directly to response writer via JSONObject/JSONArray
- JSP fragments (.jspf): pl2_head.jspf, topbar.jspf, pl2_content_start/end.jspf for shared layout
- ThreadLocal for per-request user state in servlets

## Shape of a typical feature change (code-derived: TutorReviewServlet traced)
Servlet receives POST → ServiceFactory.get*Service() → Service.get*() → DAO → Hibernate →
DtoHelper assembles DTO → servlet serializes to JSON → JS renderPage(data) updates DOM

## Named findings
- FINDING-1 (code-derived): DtoHelper.java (~132KB) and AdminDtoHelper.java (~59KB) are monolithic — business logic has migrated into helper classes rather than staying in Service layer. New features should match this *DtoHelper pattern even though it violates strict layering.
- FINDING-2 (code-derived): No automated compile/deploy CI — only schema validation on PR. All functional verification is manual (ant deploy + browser). No test infrastructure to catch regressions.
- FINDING-3 (code-derived): ES modules used in tutor_review/ only (import/export syntax); all other JS is global-scope jQuery. Mixed module strategy — new JS for tutor_review features must use ES module format; JS elsewhere must not.
- FINDING-4 (README-stated, partially code-derived): Bootstrap 4.1.3 collapse requires `data-toggle`/`data-target`. Confirmed in bootstrap.js header; confirmed in tutor_review.jsp:42. Do not use `data-bs-*` — that is Bootstrap 5 syntax.
