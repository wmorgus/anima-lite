# Formal: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash — HEAD: 29d41e50)

## Layered architecture (code-derived: package enumeration + file counts)
1. servlet/ — *Servlet.java; handles doGet/doPost, session auth, forwards to JSP
2. service/ + service/impl/ — Spring-managed transactions; interface+impl split
3. dao/ + dao/hibernate/ — AbstractDao interface + *DaoHibernate implementations
4. item/ — Hibernate-mapped domain entities (*Item.java + *.hbm.xml pairs)
5. dto/ — data transfer objects assembled by *DtoHelper classes
6. helper/ — cross-cutting concerns (email, plot, servlet utilities, demo mode, Slack webhooks)

## Module boundaries (code-derived: package enumeration)
- edu.cmu.pl2.* — tutor/advisor interface (primary application)
- edu.cmu.pl2.student.* — student portal; separate servlet hierarchy, separate session
- No shared DTOs between the two interfaces

## Servlet hierarchy (code-derived: grep-confirmed at 29d41e50)
- 9 servlets extend AbstractServlet (session-user helper); the rest extend HttpServlet directly and implement their own session checks
- FINDING-1 (code-derived): AbstractServlet is not a hard boundary rule. `ReflectionServlet` — the native reflection-form servlet, and the one most relevant to the upcoming port — extends `HttpServlet` directly (`public class ReflectionServlet extends HttpServlet`), not AbstractServlet. Do not assume a new reflection-adjacent servlet must extend AbstractServlet; follow ReflectionServlet's own base class if extending that subsystem.

## Servlet URL inventory — reflection subsystem (code-derived: web.xml)
- `/PLUS/Reflection` → `ReflectionServlet` — single URL pattern, action-dispatched internally (not split into separate list/detail servlets)

## Dominant patterns (code-derived: grep-confirmed)
- ServiceFactory used pervasively across the source layer; zero @Autowired/@Inject at call sites
- AJAX response: success = raw JSONObject/JSONArray via `ServletHelper.writeJSON(resp, json)`; error = `{"status":"error","message":"..."}`. ReflectionServlet follows this exactly — multiple call sites build `AbstractServlet.json("status", "error", "message", ...)` and pass to `ServletHelper.writeJSON`.
- JSP fragments (.jspf): pl2_head.jspf, topbar.jspf, pl2_content_start/end.jspf for shared layout; reflection subsystem contributes its own fragments: `post/mentor_reflection_post.jspf` (activity-feed card) and `student_dashboard/weekly_reflections.jspf` (student-dashboard summary of a mentor's weekly reflections)
- ES modules: feature-level JS loaded as `type="module"` scripts; `reflection.js` is a plain (non-module) script served alongside `reflection.jsp` — confirm module vs global-scope status before treating it as a template for new JS

## Shape of a typical feature change (code-derived: ReflectionServlet traced)
Servlet action param dispatches to a private method (e.g. `saveOrUpdateReflection`) → ServiceFactory.get*Service() → Service → DAO → Hibernate →
entity persisted/read → DtoHelper (where used) assembles DTO → servlet serializes to JSON via `ServletHelper.writeJSON()` → `reflection.js` updates DOM

## Seam protocols (code-derived)
- Servlet→JS: `application/json` content-type; success response = unwrapped DTO/JSON fields; error response = `{"status":"error","message":"<string>"}`. JS checks `response.status === "error"` on AJAX callbacks.
- JSP→browser: static assets served via `/v/<staticVersion>/javascript/pl2/...` path (version-busting)
- Servlet→JSP: attributes set via `req.setAttribute()` before `req.getRequestDispatcher().forward()`; JSP reads via `${requestScope.*}` or `<c:out>`
- ReflectionServlet handles file uploads via `jakarta.servlet.http.Part` (multipart), including zip-file extraction (`extractZipFile`) — a seam not present in most other servlets; relevant if the ported feature includes attachments

## Named findings
- FINDING-1 (code-derived): see Servlet hierarchy above — ReflectionServlet extends HttpServlet, not AbstractServlet; the "advisor-side servlets extend AbstractServlet" convention from the prior spine does not hold for the reflection subsystem.
- FINDING-2 (code-derived): DtoHelper.java and AdminDtoHelper.java are monolithic — business logic migrated into helper classes. New features should match the *DtoHelper pattern despite violating strict layering.
- FINDING-3 (code-derived): No automated compile/deploy CI — only schema validation on PR. All functional verification is manual (ant deploy + browser).
- FINDING-4 (code-derived): ES modules are the dominant pattern for feature-level JS in most newer features, but `reflection.js` itself does not use `type="module"` — an inconsistency between the stated dominant pattern and the actual reflection subsystem. Verify module-vs-global scope per file before assuming the ES-module convention applies inside the reflection feature.
- FINDING-5 (code-derived): Bootstrap 4.1.3 collapse requires `data-toggle`/`data-target`. Do not use `data-bs-*` — Bootstrap 5 syntax.
- FINDING-6 (code-derived): The reflection subsystem carries two parallel-but-distinct data models — `ReflectionItem` (older, feed/dashboard-facing) and `SessionReflectionItem`/`StudentReflectionItem` (current, written by ReflectionServlet's save path, actively developed through 2026). A port touching "reflections" must confirm which model it targets; they are not interchangeable and are not kept in sync automatically.

## Concrete example: new entity wiring (TutorAiInsightItem traced)
1. `item/TutorAiInsightItem.java` — entity POJO
2. `item/TutorAiInsight.hbm.xml` — Hibernate mapping
3. `applicationContext.xml` — bean registration (dao + service beans + hbm mapping list)
4. `dao/TutorAiInsightDao.java` + `dao/hibernate/TutorAiInsightDaoHibernate.java` — DAO pair
5. `service/TutorAiInsightService.java` + `service/impl/TutorAiInsightServiceImpl.java` — service pair
6. `helper/DtoHelper.java` — assembles into DTO fields used by servlets (here, `TutorReviewServlet`)
