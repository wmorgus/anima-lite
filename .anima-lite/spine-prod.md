# Spine: plus web-app (prod)
Generated: 2026-06-30
Commit: 29d41e50
Confidence: high
Refresh trigger: any change to `java/source/edu/cmu/pl2/dto/TutorReview*.java`, `java/docroot/javascript/pl2/tutor_review/`, or `java/docroot/jsp_pl2/tutor_review.jsp`

## Material

- **Backend**: Java (Jakarta EE 6.0), Apache Tomcat 11.0, Apache Ant build system
- **Framework**: Spring (DI, declarative transactions, JPA), Hibernate ORM
- **Database**: MySQL 8
- **Templating**: JSP/JSTL (server-side rendering, no React/Vue)
- **Frontend JS**: jQuery 3.5.1 (dominant), ES modules for newer features (see Formal)
- **UI**: Bootstrap, jqWidgets (widget library)
- **Data viz**: Highcharts, Chart.js, Plotly
- **CSS**: Sass/SCSS compiled to CSS via Ant (`npx sass sass:css-build`)
- **Icons**: Font Awesome (referenced server-side in JSPs, same icons as proto)
- **No bundler**: JS files served directly, no webpack/Vite
- **DTOs relevant to port**: `TutorReviewDto`, `TutorReviewImpactDto`, `TutorReviewAiInsightDto`, `TutorReviewTimeAllocationDto` (disabled). These are the prod-side data carriers for the weekly report feature.

## Formal

**Pattern**: Layered servlet architecture. Servlet → Service → DAO → Item. 29 servlets extending `AbstractServlet`, all routed via `web.xml`. Service layer uses interface/impl split, Spring-managed. DAO layer uses Hibernate. Domain entities are `*Item` classes (230+) with `.hbm.xml` Hibernate mappings. DTOs (`*Dto`) bridge the persistence layer to the view.

**Dual interface**: Tutor/Advisor (`/PLUS`) and Student Portal (`/PLUSStudent`). Each has its own servlet hierarchy, JSP pages, and auth system.

**Typical change shape**: Add `*Item.java` + `.hbm.xml` → register in `applicationContext.xml` → add `*Dao` interface + `*DaoHibernate` → add `*Service` interface + `*ServiceImpl` → SQL migration → JSP + JS. This is a 7-step procedure documented in CLAUDE.md. No shortcut path.

**Inconsistencies (named findings):**

1. **ES module JS in a jQuery codebase** — the `tutor_review/` JS (`main.js`, `ai_insights_section.js`, etc.) uses ES module syntax (`import { ... } from "..."`) and `PlusInterface`/`PlusUtil` component abstractions. The rest of the JS codebase (e.g., `pl2Helper.js` at 82KB) is legacy jQuery plugins/globals. The tutor_review feature was built in a newer pattern; it is not representative of how other pages are built. Porting code that targets tutor_review JS should follow the ES module pattern, not the legacy jQuery pattern.

2. **Time allocation disabled in prod, present in proto** — `TutorReviewDto.java` has `TutorReviewTimeAllocationDto` commented out (`// V1: Time Allocation disabled`). The corresponding section in `tutor_review.jsp` is also commented out. The proto (`WeeklyReportContent.jsx`) has a full time allocation section. This is not a gap — it is a deliberate prod-side decision.

3. **Insight status is server-managed, not client-computed** — In prod, each `TutorReviewAiInsightDto` carries a `status` field ("LOCKED", "UNDER_REVIEW", "REVIEWED") that is set by the server and persisted in the DB. The progression is driven by AJAX calls (`submitFeedback` → `/PLUS/TutorReview` → re-fetch/re-render). In proto (`WeeklyReportPage.jsx`), the progression is purely client-side (`useState(0)` counter; state computed locally, not persisted). **This is a claim boundary** — see Final.

4. **No `weekLabel` / `weekNumber` concept in prod** — The proto uses "Week 18," "Week 17," etc. as display labels. Prod's `TutorReviewDto` uses `periodStart`/`periodEnd`/`periodType` ("monthly"/"weekly"/"custom"). The period selector is rendered in `#month-selector-container` by JS, not hardcoded. Week numbering is not a field in the DTO.

## Efficient

- **Build**: `ant deploy` (compile + CSS + deploy to local Tomcat), `ant war.vm` (WAR for production)
- **CI/CD**: GitHub Actions — `check-tables-pl2.yml` validates SQL schema on PRs to `dev` branch (Docker-based); no frontend or Java test automation
- **Branch strategy**: `dev` is main; feature branches → PR → `dev`
- **Testing**: No automated tests ("No automated tests are currently configured" per CLAUDE.md)
- **Deploy**: WAR file → Tomcat. Database migrations via SQL scripts in `sql/pl2/v9.x/alter/`
- **Local dev**: Docker compose available (`docker/plus-dev-compose.yml`); or direct Ant + local Tomcat
- **Version management**: `ant updateVersionInfo` propagates version to Java source, SQL, urlrewrite.xml

## Final

**Inferred telos**: A production tutoring management platform where evidence-based AI coaching helps tutors improve practice. The core promise: tutors receive structured, AI-generated feedback about their tutoring behavior, tied to real session evidence, which they review and rate to close the coaching loop.

The tutor_review feature (the port target) specifically promises: tutors can see AI-generated insights about their coaching constructs, review them sequentially (locked → under review → reviewed), rate them (helpful/not helpful/inaccurate), and that feedback persists and improves future recommendations.

**Evidence:**
- `TutorReviewAiInsightDto` has `userRating` and `userFeedbackText` — the feedback is stored, not just shown
- `submitFeedback` posts to `/PLUS/TutorReview` and re-fetches — persistence is a hard requirement, not a nice-to-have
- The "demo-only reset" button in `ai_insights_section.js` resets insight statuses for demo accounts — confirmation that status progression is meaningful state, not decoration
- `TutorReviewServlet.java` exists with its own routing — the feature has dedicated server-side handling

**Confidence:** high on overall telos; medium on specific AI insight generation pipeline (not traced — servlet and service implementation not read).

## Disclaimers
This spine points in a direction. It is not a guarantee. Treat any claim
here that materially affects a port decision as worth a quick verification
pass against the actual code, not as settled fact.
