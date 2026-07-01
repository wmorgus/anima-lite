# Material: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash)

## Languages
- Java (primary backend) — Jakarta EE 6.0 servlet API, running on Tomcat 11.0
- JSP + JSTL (server-side rendering)
- JavaScript (jQuery 3.5.1, no transpile step)
- Sass/SCSS (compiled to CSS via npx sass, not a bundler)
- SQL (MySQL 8, schema managed by hand-written scripts)

## Backend frameworks and libraries
- Apache Tomcat 11.0 — servlet container
- Hibernate (ORM) with Spring JPA — entity persistence; validation mode = validate (no auto-DDL)
- Spring AOP — declarative transaction management
- Log4j2 — logging
- org.json (JSONObject/JSONArray) — JSON serialization in servlets (no Jackson)

## Frontend libraries
- jQuery 3.5.1 — DOM and AJAX
- jqWidgets — grid and UI widget library
- Bootstrap — layout
- Chart.js, Plotly, Highcharts — data visualization
- DataTables — tabular display

## Data structures
- Entities: *Item classes with Hibernate HBM XML mappings
- DTOs: *Dto classes, assembled by *DtoHelper classes (DtoHelper 132KB, AdminDtoHelper 59KB)
- Lesson content: JSON files (178 files in javascript/pl2/lessons/)

## Key entities (load-bearing)
PL2UserItem, PL2StudentItem, AdvisorItem, InstitutionItem, ModuleItem,
LessonAssignedItem, SessionItem, ResourceItem, TutorAiInsightItem,
TutorAiInsightFeedbackItem

## State shape
- All user state in HTTP session (key: cmu.edu.pl2.item.PL2UserItem)
- No client-side state management — page reloads reset state
- Multi-tenancy via InstitutionItem; advisor-student relationships explicit in DB

## Build artifact
- Deployed as exploded WAR (ant deploy) or packaged WAR (ant war.vm)
- Sass compiles to css-build/, then copied to docroot/css/pl2/
- External libs in java/extlib/ (no Maven/Gradle dependency resolution)
