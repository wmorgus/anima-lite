# Telos: plus web-app (prod)
Commit: c21f08b1
Confidence: high
Refresh trigger: servlet mappings added/removed, applicationContext.xml restructured, Ant build targets change, or Bootstrap/jQuery version upgraded

## Purpose
PLUS is a server-side Java web application that delivers tutoring, student management, and AI-assisted coach review to educators and institutions. It exists to provide a structured, multi-tenant educational workflow — session tracking, lesson assignment, progress monitoring — through a traditional request/response web architecture. New work either fits inside that layered, session-authenticated, server-rendered model or contradicts it.

## Don't contradict
- UI is JSP + jQuery + Bootstrap 4.1.3, not React/Vue — do not introduce a frontend framework or client-side router
- All business logic must go through the Service layer (via ServiceFactory); do not call DAOs directly from servlets or JSPs
- New entities require: *Item.java, *.hbm.xml mapping, applicationContext.xml registration, *Dao interface + *DaoHibernate impl, *Service interface + *ServiceImpl, and a SQL alter script
- Authentication is session-based; all protected endpoints extend AbstractServlet
- Build and deploy via Ant; do not add Maven, Gradle, or npm build steps to the main compile path
- New JS in tutor_review/ uses ES module syntax (import/export); JS elsewhere uses global jQuery scope — do not mix

## Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
