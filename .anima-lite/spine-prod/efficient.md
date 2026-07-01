# Efficient: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash)

## Build tooling
- Apache Ant (java/build.xml) — primary build system
- No Maven, no Gradle, no npm build pipeline (npx sass is a compile step, not a bundler)
- External libs: java/extlib/ — checked in, no dependency resolution at build time

## Key Ant targets
- ant compile — compile Java sources only
- ant deploy — compile + Sass + deploy to local Tomcat (main dev loop)
- ant deployAll — deploy + configuration files
- ant compile-sass — Sass only
- ant clean — clean build artifacts
- ant war.vm — package production WAR
- ant release.plus — WAR + SQL + lessons (full release artifact)
- ant updateVersionInfo — stamp version into source + SQL + urlrewrite.xml
- ant clean.db.pl2 — drop and recreate database tables (requires db.properties)

## Local dev prerequisites
- java/build.properties (copy from build.properties.sample): local.tomcat, local.docroot, base.files.dir, plus.admin
- java/db.properties (copy from db.properties.sample): MySQL credentials, pl2_db
- Local Tomcat installation (path set in build.properties)

## Docker path
- docker/docker-compose.yml — full stack (Tomcat + MySQL + LLM + email)
- docker/plus-dev-compose.yml — faster dev containers
- Box CLI required to download build dependencies before Docker build
- Database reset: remove plus_plus-mysql-volume

## CI/CD
- GitHub Actions: .github/workflows/check-tables-pl2.yml
  - Trigger: PRs to dev branch
  - Action: runs create_tables_pl2.sql, checks recent alter scripts
  - Uses docker/check-tables/ compose
- No compile/deploy CI — schema validation only
- Main integration branch: dev (not main)

## Schema management
- Location: java/sql/pl2/v9.x/
- Create: create/create_tables_pl2.sql
- Drop: delete/drop_tables_pl2.sql
- Migrations: alter/ directory, version-specific scripts
- Hibernate validation mode = validate — schema must match mappings or startup fails

## Verifying a change
1. ant deploy (or ant deployAll for config changes)
2. Browser test against local Tomcat (http://localhost:8080)
3. For schema changes: run alter script manually, then ant deploy
4. No automated test suite — all verification is manual + CI schema check on PR
