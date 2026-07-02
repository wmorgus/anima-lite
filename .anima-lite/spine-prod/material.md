# Material: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash)

## Languages
- Java — Jakarta EE 6.0 servlet API, Tomcat 11.0.23
- JSP + JSTL — server-side rendering
- JavaScript — no transpile step; ES modules dominant for feature-level JS (30+ JSPs use type="module"); legacy shared utilities remain global-scope jQuery
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
- Entities: *Item.java + *.hbm.xml pairs in item/ (131 files, code-derived: find count)
- DTOs: *Dto.java assembled by *DtoHelper.java — DtoHelper.java ~132KB, AdminDtoHelper ~59KB
- Lesson content: JSON files in javascript/pl2/lessons/ (~178 files)

## Key entities (load-bearing)
PL2UserItem, AdvisorItem, PL2StudentItem, InstitutionItem,
SessionItem, TutorAiInsightItem, TutorAiInsightFeedbackItem

## State shape
- All user session state in HTTP session (key: cmu.edu.pl2.item.PL2UserItem)
- No client-side state management — page re-renders reset all state
- Multi-tenancy via InstitutionItem; advisor-student relationships explicit in DB

## Build artifact
- Exploded WAR via `ant deploy` / packaged WAR via `ant war.vm`
- External libs checked in to java/extlib/ — no Maven/Gradle dependency resolution
- Sass compiles to css-build/, copied to docroot/css/pl2/
