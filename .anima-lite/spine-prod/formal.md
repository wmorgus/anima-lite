# Formal: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash — HEAD: 29d41e50)

## §1 Layered architecture
Four-tier hand-rolled (pre-Spring-Boot) stack: **servlet → service → dao → item**. Servlets (`servlet/`, 45) handle HTTP + auth, call `service/` interfaces (204, interface+impl pairs) for business logic; services delegate to `dao/` interfaces (219, interface + `hibernate/` impl pairs); DAOs operate on `item/` Hibernate entities (131). `dto/` (89) is a presentation-shaping layer built by static `*DtoHelper` classes and consumed directly by JSPs — it sits alongside, not inside, the servlet→service→dao chain.

## §2 Module boundaries
Package root `edu.cmu.pl2` splits by architectural LAYER, not business domain (`item/`, `dto/`, `enums/`, `servlet/`, `service/`, `dao/`, + cross-cutting `helper/`, `util/`, `feed/`). A parallel **`student/` subpackage** (`student/dto`, `student/servlet`, `student/servlet/auth`) is a thin student-facing mirror — it has NO `student/service|dao|item`; student servlets reuse the top-level service/dao/item layers directly.

## §3 Dominant patterns — per stratum

### Backend
- **Servlet base class is split** (grep on top-level `servlet/*.java`): 22 `extends HttpServlet` directly, 7 `extends AbstractServlet` (which itself extends HttpServlet, centralizing login/session + Google-auth init). No dominant convention — the rest of the 45 live in subpackages/other bases.
- **ServiceFactory pattern**: `ServiceFactory.java` (abstract, one getter per service) + `ServiceFactoryImpl` (`ApplicationContextAware`, resolves each service lazily via `context.getBean("xService")`) + `ServiceFactoryInitializer` (a `ServletContextListener` that sets the static `ServiceFactory.DEFAULT`). Used in 114 files. **`@Autowired` = 0 repo-wide**; all DI is Spring XML (`applicationContext.xml`, 1073 lines) + setter injection.
- **Service→DAO indirection**: a service impl holds a `DaoFactory` (not its Dao) and resolves the specific DAO by item class at call time — `daoFactory.getDao(XItem.class)`, keyed off a Spring `<util:map>` (`daoMap` bean). One indirection beyond the ServiceFactory jump.
- **Hibernate**: DAOs extend `AbstractDaoHibernate` (`get`/`find`/`findAll`/`getSession`); hand-rolled HQL and native SQL are written ad hoc per DAO.
- `Seams:` servlet base class inconsistently applied (22 HttpServlet vs 7 AbstractServlet — the 22 duplicate auth/session boilerplate inline); dispatch style is also mixed — a `requestingMethod` query-param switch (26 servlets) coexists with plain doGet/doPost and servlet-path branching (EmailServlet mixes both). Read each servlet's routing individually.

### Frontend
- Views: JSP under `java/docroot/jsp_pl2` (126 `.jsp`/`.jspf`) + a parallel `jsp_pl2_student` tree.
- **JSTL effectively absent**: 0 taglib directives / `<c:*>` tags anywhere; 119/126 files use raw `<% %>` scriptlets. The convention is Java-in-JSP, not JSTL.
- **Chrome via static `.jspf` includes**: `pl2_content_start.jspf` pulls `pl2_head.jspf`, `topbar.jspf`, `sidebar_nav.jspf`, `maintenance_banner.jspf` via `<%@ include %>` (static, not `<jsp:include>`).
- **Bootstrap 4.1.3 + jQuery 3.5.1**: 34 JSPs use `class="btn`/`data-bs-*`; of 95 JS files, 65 use jQuery `$()`, 7 use `.ajax(`.
- `Seams:` AJAX transport mixed — mostly jQuery `.ajax()`, but `email.js` uses modern `fetch()` (isolated newer file, not a migration). No `.scss` source present at dev HEAD (styling = precompiled vendored CSS).

### Data flow
- browser → servlet (auth via `ServletHelper.getAuthenticatedUser`, then param- or method-dispatch) → `ServiceFactory.DEFAULT.getXService()` → service (resolves DAO via DaoFactory) → DAO (`AbstractDaoHibernate` + Hibernate Session) → `Item` → back up, either rendered to a `Dto` via a static `*DtoHelper` for JSP, or serialized to JSON for AJAX.
- AJAX helper: `helper/ServletHelper.java` — `writeJSON(resp, JSONObject|JSONArray)` and `writeJsonError(resp, msg)` → `{"status":"error","message":...}`.
- `Seams:` **the `{status}` envelope is NOT a project-wide contract** — of 17 servlets calling `writeJSON`, only ONE (`TutorReviewServlet`) sets a `status` key on success; `writeJsonError` supplies it only on the error path. Most build ad-hoc feature-specific JSON with no shared envelope. A port assuming uniform `{status, data}` is wrong for ~16/17 endpoints.

## §4 Seam protocols (CROSS-layer — distinct from the per-layer `Seams:` lines above)
- **Servlet → JS (AJAX)**: shape is per-endpoint, not standardized (see Data-flow seam). Read each servlet's JSON-building code; do not assume a shared envelope class.
- **JSP → browser (static assets)**: absolute paths off docroot (`/css/…`, `/javascript/pl2/…`); a `staticAssetVersion` is read from `version.properties` at context-init and stashed on the ServletContext for cache-busting. **Named gap**: whether/how that version is actually appended to asset URLs across all JSPs was not confirmed past `pl2_content_start.jspf` reading it into a scriptlet var.
- **Java → Hibernate (entity wiring)**: the 8-part checklist below.

## §5 Named findings
1. (code-derived) `@Autowired` = 0 repo-wide; all DI is Spring-XML + setters.
2. (code-derived) Servlet base class split 22 HttpServlet : 7 AbstractServlet — no dominant convention; don't assume a new servlet inherits AbstractServlet's auth helpers.
3. (code-derived) JSTL essentially unused despite JSP views — actual convention is raw scriptlets.
4. (code-derived) No `.scss` source at dev HEAD; styling is precompiled CSS + vendor bundles (Bootstrap, sb-admin-2, DataTables, FontAwesome, jqwidgets).
5. (code-derived) AJAX `{status}` envelope is a per-file idiom (1/17), not a platform contract.
6. (code-derived) `student/` is a thin servlet+dto mirror on the shared service/dao/item stack — no parallel vertical slice.
7. (code-derived) Services hold a `DaoFactory` and look up their DAO by `Item.class` via the `daoMap` `<util:map>` — an extra indirection beyond ServiceFactory; preserve or flatten it deliberately, don't assume it away.
8. (skeptical) `requestingMethod` dispatch (26 servlets) coexists with doGet/doPost and servlet-path branching — at least three overlapping routing shapes; read per servlet.
9. (skeptical) `staticAssetVersion` URL-append mechanism unconfirmed beyond one fragment reading the attribute.

## Concrete example — 8-part entity wiring traced (`StrategyOption`, cap-exempt reference)
1. `item/StrategyOptionItem.java` — POJO extends `Item` (`id`, `name`, `tagline`, `altTagline`, `imageFileName`, `description`).
2. `item/StrategyOption.hbm.xml` — `<class table="strategy_option">`, `<id column="strategy_option_id" generator="native"/>`, one `<property>` per field.
3. `java/docroot/conf-tomcat-11.0/applicationContext.xml` (1073 lines) — three registrations: dao bean (`strategyOptionDao` → `StrategyOptionDaoHibernate`), a `daoMap` `<util:map>` entry (`edu.cmu.pl2.item.StrategyOptionItem` → `strategyOptionDao`), and the service bean (`strategyOptionService` → `StrategyOptionServiceImpl`, `daoFactory` ref `plusDaoFactory`). The `plusServiceFactory` bean resolves services lazily by name — no per-service wiring needed there.
4. `dao/StrategyOptionDao.java` — interface extends `AbstractDao` + domain methods.
5. `dao/hibernate/StrategyOptionDaoHibernate.java` — impl extends `AbstractDaoHibernate implements StrategyOptionDao`; custom methods use HQL / `createNativeQuery`.
6. `service/StrategyOptionService.java` — interface.
7. `service/impl/StrategyOptionServiceImpl.java` — impl holds setter-injected `DaoFactory`, resolves `(StrategyOptionDao) daoFactory.getDao(StrategyOptionItem.class)` per call.
8. `service/ServiceFactory.java` (abstract `getStrategyOptionService()`) + `impl/ServiceFactoryImpl` (returns `context.getBean("strategyOptionService")`).
+ SQL: DDL/alters under `java/sql/pl2/v{N}.x/{create,alter,delete}/`. Migration filenames aren't derivable from the entity name — grep per entity.
