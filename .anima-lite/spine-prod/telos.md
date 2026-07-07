# Telos: plus web-app (prod)
Commit: 29d41e50
Confidence: high
Refresh trigger: a new persistent entity is added (re-verify the 8-part wiring checklist still holds), applicationContext.xml bean-wiring structure changes, Spring/Hibernate/Servlet-API major version bumps, the build's JDK floor changes, or dev's `plus.version` advances materially past v11.3.0.x.

## §1 Purpose
Production tutoring-operations system of record for CMU PL2. It exists to reliably track and coordinate human tutoring delivery at institutions: the institution → group → shift → session hierarchy, tutor staffing/signups, student enrollment, call-offs, and post-session reflections. Everything is server-rendered and DB-backed (Hibernate/MySQL); there is no SPA or client-side state layer. New work either serves this operational-tracking purpose server-side or contradicts it.

## §2 Don't contradict
- **New persistent entities require the full 8-part wiring** (formal.md concrete example): `Item.java` + `.hbm.xml` + `applicationContext.xml` (dao bean + `daoMap` entry + service bean) + `Dao` interface + `DaoHibernate` impl + `Service` interface + `ServiceImpl` + `ServiceFactory` getter + a versioned SQL alter under `java/sql/pl2/v11.x/alter/`. Skipping any part ships a half-wired entity.
- **No annotation DI.** All dependency injection is Spring XML + setter injection, resolved at runtime via `ServiceFactory.DEFAULT` and `DaoFactory.getDao(XItem.class)`. Do not introduce `@Autowired` — it is used nowhere (0 hits repo-wide).
- **Schema changes ship as versioned SQL alter scripts** under `java/sql/pl2/v11.x/alter/`, never as live DDL or Hibernate auto-DDL. CI gates only that these alters apply cleanly (efficient.md §3).
- **Do not invent student-side data prod lacks.** No student-side session capacity, no `subject`/course taxonomy, and no out-of-band (email/SMS/push) student notification channel — students have no email field and only an in-app pull inbox. See material.md §8.
- **Do not assume a uniform AJAX envelope or JSTL views.** JSON response shape is per-endpoint (only 1/17 servlets use `{status}`); views are raw JSP scriptlets, not JSTL. See formal.md §3.

## §3 Cause files (reference depth)
- [material.md](material.md) — tech stack, entity/field inventory (§7), capabilities prod does NOT have (§8), domain vocabulary (§9)
- [formal.md](formal.md) — layered servlet→service→dao→item architecture, per-stratum patterns + seams, 8-part wiring trace
- [efficient.md](efficient.md) — Ant build, JDK-17 floor, SQL-only CI gate, dev branching, Docker/Tomcat deploy

## §4 Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
