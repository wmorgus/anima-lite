# Efficient: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash — HEAD: 29d41e50)

## Build tooling (code-derived: build.xml + .github/workflows/)
- Apache Ant (java/build.xml) — primary build system; no Maven, Gradle, or npm pipeline
- External libs in java/extlib/ — checked in, no dependency resolution at build time
- `npx sass` — Sass compile step (not a bundler)

## Key Ant targets (code-derived: build.xml target enumeration)
- `ant compile` — compile Java sources only
- `ant deploy` — compile + Sass + deploy to local Tomcat (main dev loop)
- `ant deployAll` — deploy + configuration files (use after applicationContext.xml changes)
- `ant compile-sass` — Sass only
- `ant lint-js` — validates JavaScript with ESLint (present at 29d41e50; not previously recorded in the stale spine — confirm whether it runs in CI or is dev-invoked only)
- `ant war.vm` — package production WAR
- `ant release.plus` — WAR + SQL + lessons (full release artifact)
- `ant clean.db.pl2` — drop and recreate database tables

## Local dev prerequisites
- `java/build.properties` (copy from build.properties.sample): local.tomcat, local.docroot, base.files.dir
- `java/db.properties` (copy from db.properties.sample): MySQL credentials, pl2_db
- Java 17 required for Tomcat 11 (Tomcat 11.0.23 requires JDK 17+)
- Known blocker (still present at 29d41e50): `StudentsServlet.java` uses `case EdTechName.IXL:` syntax; verify Java 17 compatibility before relying on `ant deployAll` succeeding cleanly

## CI/CD (code-derived: .github/workflows/)
- Integration branch: `dev` (PRs target dev, not main) — the prod repo probed here is checked out at `29d41e50` on `anima-lite-tutor-reflection-form`, which equals the current `dev` tip
- GitHub Actions: `check-tables-pl2.yml` — triggers on PRs to `dev` that touch `java/sql/pl2**`
  - Runs `create_tables_pl2.sql` + recent alter scripts in Docker; schema validation only
  - Second workflow: `sql-notification.yml`
- No compile/deploy CI — schema validation only; all functional verification is manual
- `lint-js` Ant target exists but is not wired into either workflow file — ESLint is not currently CI-enforced

## Schema management (code-derived: java/sql/pl2/)
- Create: `java/sql/pl2/v9.x/create/create_tables_pl2.sql` (use latest v11.x for fresh installs)
- Migrations: `java/sql/pl2/v9.x/alter/` — hand-written, version-specific scripts
- Hibernate `hbm2ddl.auto=validate` — schema must match HBM mappings or startup fails

## Verifying a change
1. `ant deployAll` (for config changes) or `ant deploy` (Java + JS only)
2. Browser test at `http://localhost:8080`
3. Schema changes: run alter script manually before deploy
4. No automated test suite for the reflection area beyond `StudentReflectionDaoIntegrationTest.java` (java/test/); no automated test suite generally — manual + CI schema check on PR
