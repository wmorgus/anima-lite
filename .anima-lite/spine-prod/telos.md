# Telos: plus web-app (prod)
Commit: 29d41e50
Confidence: high
Refresh trigger: servlet URL mappings added/removed, applicationContext.xml restructured, Ant build targets change, Bootstrap/jQuery version upgraded, or reflection subsystem (Reflection/SessionReflection/StudentReflection) schema/servlet changes

## Purpose
PLUS is a server-side Java web application that delivers tutoring, student management, and AI-assisted coach review to educators and institutions. It exists to provide a structured, multi-tenant educational workflow — session tracking, lesson assignment, progress monitoring, and post-session mentor/tutor reflection capture — through a traditional request/response web architecture. New work either fits inside that layered, session-authenticated, server-rendered model or contradicts it.

## Don't contradict
- UI is JSP + jQuery + Bootstrap 4.1.3, not React/Vue — do not introduce a frontend framework or client-side router
- All business logic must go through the Service layer (via ServiceFactory); do not call DAOs directly from servlets or JSPs
- New entities require: *Item.java, *.hbm.xml mapping, applicationContext.xml registration, *Dao interface + *DaoHibernate impl, *Service interface + *ServiceImpl, and a SQL alter script
- Authentication is session-based; AbstractServlet is the base class for 10 confirmed servlets, but it is NOT a hard rule — most servlets, including the reflection subsystem's own ReflectionServlet, extend HttpServlet directly with their own session checks (see formal.md FINDING-1)
- Build and deploy via Ant; do not add Maven, Gradle, or npm build steps to the main compile path
- New feature JS uses ES module syntax (import/export) with type="module" script tags — do not write new global-scope jQuery scripts for feature-level code; legacy shared utilities (pl2Banners.js, pl2EffortGraph.js) remain global-scope but do not add to them
- A native "Tutor Reflection Form" subsystem already exists (ReflectionServlet, SessionReflectionItem/StudentReflectionItem, reflection.jsp/js/scss) and has been actively developed since 2020 through at least April 2026 (commit 462dfa96, "Card2225: Tutor Reflection Form Editing") — any tutor-reflection-form work must be checked against this subsystem before assuming new code is needed

## Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.

## Refresh diff (vs commit 90e0ff79, 2026-07-06)
- **Monthly-report port artifacts are gone at 29d41e50, confirmed absent.** No `MonthlyReportServlet` (java or class), no `weekly_report` servlet mapping, and no `MonthlyReports`/`MonthlyReport` URL patterns anywhere in `web.xml` (grep across the whole tree, case-insensitive, returns nothing). These lived on a port branch layered onto 90e0ff79, not on `dev`. The prior spine's servlet-hierarchy claims ("10 extend AbstractServlet... MonthlyReportServlet"), the two-URL-pattern servlet finding (FINDING-6), and the monthly-report seam-protocol note are all dropped from this refresh.
- **TutorAiInsightItem/Service/Dao are NOT part of the dropped port work — they are native to `dev`.** They are wired through `TutorReviewServlet` (`/PLUS/TutorReview`), registered in `applicationContext.xml`, and trace to commit `73c87e9b` ("Add Tutor AI Coach Review page (V1: Impact + Growth Insights)"). The old spine's material.md listed them as load-bearing entities without tying them to MonthlyReportServlet; that entry was correct and is retained here, just re-attributed to the Coach Review feature rather than monthly reporting.
- **AbstractServlet count reverts to 9** (was reported as 10 in the stale spine, inflated by the now-absent MonthlyReportServlet). Re-confirmed by grep at HEAD 29d41e50.
- **New finding, not present in old spine:** the native reflection subsystem (ReflectionServlet, SessionReflectionItem, StudentReflectionItem) is a long-lived, actively-committed feature (2020–2026) that is architecturally and nominally close to the incoming `tutor-reflection-form` port. It was out of scope for the prior spine's probe. It is the single most important new fact for the upcoming port and is detailed in material.md §5/§6 and formal.md §3/§5.
- No other architectural drift detected: layering (servlet/service/dao/item/dto/helper), ServiceFactory usage, Ant build targets, and Bootstrap 4.1.3/jQuery 3.5.1 versions are unchanged from the prior spine.
