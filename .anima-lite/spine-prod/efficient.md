# Efficient: plus web-app (prod)
(Reference depth — see telos.md for entry point and commit hash — HEAD: 29d41e50)

## §1 Build tooling
- **Apache Ant** (`java/build.xml`, ~636 lines, `<project name="PLUS" default="runA">`). No Maven/Gradle/Ivy — every dependency is a vendored jar under `java/extlib/` (+ `hibernate/`, `spring/` subdirs) wired as literal `<pathelement>`s.
- **JDK 17 is a hard floor** (confirmed by bytecode, not inference): `build.xml` sets no `javac source/target/release`, so javac uses the ambient JDK — but `spring-core-6.2.5.jar` and `hibernate/jakarta.persistence-api-3.2.0.jar` on the compile classpath are class-file **major 61 (Java 17)**. Javac cannot even read a classpath jar newer than its own JDK, so JDK 11 fails `ant compile` on class-file version. (This is exactly the run4 compile blocker.)
- **SASS**: Dart Sass via `npx sass` (`compile-sass` target, build.xml:198) compiling `java/sass/*.scss` → `java/css-build`. NOTE: no `.scss` source is present at dev HEAD — the target exists, its source tree is effectively empty here (formal.md §3 Frontend).
- Ant itself: 1.9.14 (local dev, Homebrew) / 1.9.16 (Docker); Node 17.9.1.

## §2 Key targets (from build.xml)
- `compile` → `jar` (`plus.jar`) → `compile-sass` → `deploy` (jar+sass to local Tomcat)
- `deployAll` — prepareVersionProperties + deploy + config filter + updateTomcat (the one-shot "build + push to local Tomcat"; what the Docker images invoke)
- `war`/`war.vm` — build `ROOT.war` for release
- `test-compile`/`test`/`test-unit`/`test-integration` — JUnit; **NOT a dependency of `deployAll`** (opt-in)
- `lint-js` — ESLint via `npm run lint:quiet` (opt-in, not wired to CI)

## §3 CI/CD — SQL-only gate
Exactly two GitHub Actions workflows, and **neither compiles or tests Java**:
- `check-tables-pl2.yml` — on PR into `dev` touching `java/sql/pl2**`: spins a MySQL 8.0.43 container and validates that `create_tables_pl2.sql` + the versioned alter scripts apply cleanly. **The only automated gate in the repo.**
- `sql-notification.yml` — on merged PR touching `.sql`: posts a Slack notice. Not a gate.
- **Gap**: no CI runs `ant compile`/`test`/`war`, ESLint, or SASS. Any Java compile break, test failure, or lint failure ships to `dev` undetected. → **Validation of a port here is necessarily static-review-only for compile correctness** unless a JDK-17 local build is run.

## §4 Branching model
Base/integration branch is **`dev`** — **there is no `main`** (`git branch -a` → local: dev + feature/port branches; `origin/HEAD → origin/dev`). Remote carries 600+ ticket-per-branch feature branches (`Card-###`, `c###-…`, agent `claude/…`/`codex/…`) feeding `dev` via PR. `dev` is periodically version-stamped for QA — `git log dev` shows `v11.3.0.4 for QA` atop merged PRs, preceded by `v11.3.0.3 / .2 for QA` — i.e. a version-bump-per-QA-cycle cadence. No `main`/`release` branch observed to confirm the next hop to production.

## §5 Deploy path
Docker image wrapping the Ant pipeline: `docker/{plus,plus-dev,release}.dockerfile` build the app and `RUN ant clean.all clean.tomcat deployAll`, then serve Tomcat on 8080. `docker/docker-compose.yml` composes `webapp` + a `db-updater` (runs `docker/update-db/` over `java/sql`) + `llm`/`email` sidecars + MySQL. Schema changes ship as versioned alter scripts under `java/sql/pl2/v11.x/alter/`; `docker/check-tables/` (CI, §3) validates they apply. No CD automation pushing the image was found — the pipeline stops at "buildable image + validated SQL"; final production rollout isn't evidenced in this repo (gap).

## §5a Named findings / constraints
- **Docker base images are stale-contradictory**: all three Dockerfiles install **JDK 7u80** on `tomcat:7-jre7`, which cannot build the Java-17-bytecode Spring/Hibernate jars now on the compile classpath (§1). A separate unmerged branch `origin/docker-update-jdk-mysql-tomcat` attempts a bump (to JDK 11 / Tomcat 8.5 — still short of 17) — migration is in-flight and unreconciled. Do NOT treat the committed Dockerfile's JDK version as ground truth.
- `build.properties.nix` (local dev: Tomcat 11.0.8) is materially newer than what the committed Docker images build/run — reading it alone to answer "how does this deploy" misleads.
- `deployAll` does not depend on `test*`/`lint-js` — "build passed" and "tests passed" are independent, non-enforced claims.

## Verifying a change (practical)
1. Compile requires JDK 17+ (§1). Env without it → static review only.
2. No general automated test suite; CI checks only SQL alters. Browser test at `localhost:8080` after `ant deployAll` if a full JDK-17/Tomcat env is available.
3. Schema changes: add a versioned alter under `java/sql/pl2/v11.x/alter/` — CI will gate it.
