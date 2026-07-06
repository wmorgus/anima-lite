# Formal: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash)

## Layered architecture (code-derived: package enumeration + file counts)
1. servlet/ — *Servlet.java; handles doGet/doPost, session auth, forwards to JSP
2. service/ + service/impl/ — 204 files; Spring-managed transactions; interface+impl split
3. dao/ + dao/hibernate/ — 219 files; AbstractDao interface + *DaoHibernate implementations
4. item/ — 131 files; Hibernate-mapped domain entities (*Item.java + *.hbm.xml pairs)
5. dto/ — data transfer objects assembled by *DtoHelper classes
6. helper/ — cross-cutting concerns (email, plot, servlet utilities, demo mode)

## Module boundaries (code-derived: package enumeration)
- edu.cmu.pl2.* — tutor/advisor interface (primary application)
- edu.cmu.pl2.student.* — student portal; separate servlet hierarchy, separate session
- No shared DTOs between the two interfaces

## Servlet hierarchy (code-derived: grep-confirmed)
- 10 servlets extend AbstractServlet (session-user helper); 27 extend HttpServlet directly
- AbstractServlet subclasses: MonthlyReportServlet, TutorReviewServlet, ResearchDashboardServlet, StudentsServlet, auth servlets (Login/Logout/DemoLogin + student Login/Logout), AuthServlet
- Most tutor-side servlets (TrendsServlet, LessonServlet, AdminServlet, TutorScheduleServlet, etc.) extend HttpServlet directly and implement their own session checks
- FINDING-1 (code-derived): The prior spine's claim "all protected endpoints extend AbstractServlet" is not the actual pattern. The AbstractServlet count is now 10 (was 9). New advisor-side servlets (like MonthlyReportServlet) do extend AbstractServlet — this is the correct pattern for new advisor-side work. Verify base class before adding a new servlet.

## Servlet URL inventory (code-derived: web.xml)
Two URL patterns map to a single MonthlyReportServlet instance:
- `/PLUS/MonthlyReports` — list view (historical reports)
- `/PLUS/MonthlyReport`  — detail view (single month report)
Both patterns registered in web.xml alongside TutorReview, auth servlets, etc.

## Dominant patterns (code-derived: grep-confirmed)
- ServiceFactory used 117+ times across source layer; zero @Autowired/@Inject at call sites (code-derived)
- AJAX response: success = raw JSONObject/JSONArray via `ServletHelper.writeJSON(resp, json)`; error = `{"status":"error","message":"..."}` — no consistent success wrapper envelope
  - Exception: `submitInsightFeedback` returns `{"status":"ok","rating":"...","insightId":...,"statusChanged":...}` — success with an explicit `status` field. This is a per-method choice, not a new global pattern.
- JSP fragments (.jspf): pl2_head.jspf, topbar.jspf, pl2_content_start/end.jspf for shared layout
- ES modules: feature-level JS loaded as `type="module"` scripts; plus_components/ provides shared exports; schedule/ subdirectory uses export functions

## Shape of a typical feature change (code-derived: TutorReviewServlet traced)
Servlet receives POST → ServiceFactory.get*Service() → Service.get*() → DAO → Hibernate →
DtoHelper assembles DTO → servlet serializes to JSON → `ServletHelper.writeJSON()` → JS render fn updates DOM

## Seam protocols (code-derived)
- Servlet→JS: `application/json` content-type; success response = unwrapped DTO fields; error response = `{"status":"error","message":"<string>"}`. JS checks for `response.status === "error"` on AJAX callbacks.
- JSP→browser: static assets served via `/v/<staticVersion>/javascript/pl2/...` path (version-busting); type="module" scripts are async
- Servlet→JSP: attributes set via `req.setAttribute()` before `req.getRequestDispatcher().forward()`; JSP reads via `${requestScope.*}` or `<c:out>`
- Monthly-report JS routing: single `monthly_report.js` module serves both list and detail pages; branches on `window.location.pathname.includes("MonthlyReports")` in an IIFE at module load time

## Named findings
- FINDING-1 (code-derived): The AbstractServlet subclass count increased from 9 to 10 with the addition of MonthlyReportServlet. MonthlyReportServlet follows the correct pattern for new advisor-side servlets — extend AbstractServlet, use `ServletHelper.getAuthenticatedUser()` for auth, forward to JSP on page load and dispatch to private methods on AJAX calls.
- FINDING-2 (code-derived): DtoHelper.java (~132KB) and AdminDtoHelper.java (~59KB) are monolithic — business logic migrated into helper classes. New features should match the *DtoHelper pattern despite violating strict layering.
- FINDING-3 (code-derived): No automated compile/deploy CI — only schema validation on PR. All functional verification is manual (ant deploy + browser).
- FINDING-4 (code-derived): ES modules are the dominant pattern for feature-level JS (students.js, strategy.js, schedule/, tutor_review/, plus_components/, monthly_report.js all use import/export). Global jQuery scope remains only in legacy shared utilities (pl2Banners.js, pl2EffortGraph.js, pl2Feed.js). New feature JS should use ES module format.
- FINDING-5 (code-derived): Bootstrap 4.1.3 collapse requires `data-toggle`/`data-target`. Confirmed in bootstrap.js header. Do not use `data-bs-*` — Bootstrap 5 syntax.
- FINDING-6 (code-derived): MonthlyReportServlet handles two URL patterns in one class, branching on `req.getRequestURI().contains("MonthlyReports")`. This is a new pattern in the servlet layer — prior servlets are 1:1 URL-to-class. Acceptable for tightly coupled list/detail views; document if reused.

## Concrete example: new entity wiring (TutorAiInsightItem traced)
1. `item/TutorAiInsightItem.java` — entity POJO
2. `item/TutorAiInsightItem.hbm.xml` — Hibernate mapping
3. `applicationContext.xml` — bean registration
4. `dao/TutorAiInsightDao.java` + `dao/hibernate/TutorAiInsightDaoHibernate.java` — DAO pair
5. `service/TutorAiInsightService.java` + `service/impl/TutorAiInsightServiceImpl.java` — service pair
6. `helper/DtoHelper.java` — assembles into DTO fields used by servlets
