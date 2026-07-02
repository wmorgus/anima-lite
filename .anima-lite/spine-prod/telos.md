# Telos: plus web-app (prod)
Commit: 29d41e50
Confidence: high
Refresh trigger: servlet URL mappings added/removed, applicationContext.xml restructured, Ant build targets change, Bootstrap/jQuery version upgraded

## Purpose
PLUS is a server-side Java web application that delivers tutoring, student management, and AI-assisted coach review to educators and institutions. It exists to provide a structured, multi-tenant educational workflow — session tracking, lesson assignment, progress monitoring — through a traditional request/response web architecture. New work either fits inside that layered, session-authenticated, server-rendered model or contradicts it.

## Don't contradict
- UI is JSP + jQuery + Bootstrap 4.1.3, not React/Vue — do not introduce a frontend framework or client-side router
- All business logic must go through the Service layer (via ServiceFactory); do not call DAOs directly from servlets or JSPs
- New entities require: *Item.java, *.hbm.xml mapping, applicationContext.xml registration, *Dao interface + *DaoHibernate impl, *Service interface + *ServiceImpl, and a SQL alter script
- Authentication is session-based; all protected endpoints extend AbstractServlet (9 confirmed) or use HttpServlet directly with session checks — verify which pattern applies before adding a new servlet
- Build and deploy via Ant; do not add Maven, Gradle, or npm build steps to the main compile path
- New feature JS uses ES module syntax (import/export) with type="module" script tags — do not write new global-scope jQuery scripts for feature-level code; legacy shared utilities (pl2Banners.js, pl2EffortGraph.js) remain global-scope but do not add to them

## Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
