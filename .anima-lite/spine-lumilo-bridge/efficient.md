# Efficient: lumilo-bridge (lumilo-bridge)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Build tooling
Backend: `tsc --build --verbose` (`graphql-server/package.json` `build` script); runtime is `ts-node index.ts` even for `start:prod` — build and start are decoupled (the compiled `dist/` output is not confirmed to be what actually runs in production; `entrypoint.sh` was not fully traced). Frontend: `ng build`, output path `../graphql-server/public/teacher` with base-href `/lumilo-bridge/teacher/` — confirmed by hashed JS chunk files already present under that path in the checked-out tree. Frontend tests run under Karma/Jasmine (`ng test`), separate from the backend's Jest suite.

## §2 Key targets
- `graphql-server`: `build`, `start`/`start:prod` (`ts-node index.ts`), `test` (`jest --runInBand --detectOpenHandles --forceExit`), `codegen` (GraphQL codegen), `seed:users`, `seed:test-class`.
- `bridge-frontend`: `ng build` (→ `graphql-server/public/teacher`), `ng test`, `ng serve`.
- `graphql-server/Dockerfile`: `node:alpine3.22` base, CodeArtifact npm registry auth, `npm ci --no-audit --strict-peer-deps`, conditional AWS RDS/DocumentDB TLS cert download (`DOWNLOAD_AWS_CERT`, defaults true — not confirmed whether `docker-compose.local.yml` overrides this for local dev), New Relic env vars baked in, listens on port 4000.

## §3 CI/CD
- `.jenkins/build.Jenkinsfile`: app name `lumilo-bridge`, version `1.3.x`; parallel stages for a Kaniko-based `docker-build` (deploys to a `Lumilo-Bridge-Deploy` target) and a skippable `sonarqube` stage; PR builds skip the "Deploy to QA" step.
- `.jenkins/sonarqube.Jenkinsfile` + `sonar-project.properties` (only `sonar.projectKey` set locally; quality-gate thresholds live server-side, not in-repo).
- `.github/workflows/codeql.yml`: triggers on push/PR to `main` plus manual dispatch, delegates to an org-shared workflow, `javascript-typescript` analysis with `build-mode: none` (source-only — may miss type-flow-dependent findings on a TS codebase).
- `.husky/pre-commit`: runs codegen + build (typecheck only — no lint, no test). `.husky/pre-push`: runs the full Jest suite + build. Regressions in logic (not just types) surface only at pre-push or CI, not at commit time. Hooks only gate `graphql-server/`; `bridge-frontend` has no husky gate at all.

## §4 Branching model
Current branch: `wip/common-ingestion-prep`. Sibling/prior branch referenced in an in-repo doc: `wip/prep-for-tutorshop` (`common-ingestion-format.md`'s stated branch, now stale relative to HEAD — see formal.md §5). No branch-protection or merge-policy config found in-repo (would live in CI/hosting platform config, out of scope for a file-based probe).

## §5 Deploy path
`docker-compose.yml` composes `graphql-server`, a `log-processor` service (port 5000, calls back into `graphql-server`'s `/graphql` — present in the compose topology but has no source directory in this repo's tracked files, likely a separately-built image), `redis`, and `mongodb`. `docker-compose.local.yml` mirrors this without `log-processor` and without CL-only secrets (`CLTOKEN_PASETO_KEY`, `CLTOKEN2`), using the public npm registry instead of CodeArtifact. `graphql-server/.env.example` already documents the Kinesis consumer's configuration surface — `KINESIS_STREAM_NAME`, `KINESIS_ITERATOR_TYPE`, `KINESIS_POLL_INTERVAL_MS` — commented out by default, alongside `TUTORSHOP_WS_URL`/`TUTORSHOP_WS_TOKEN` for the WebSocket path, `BYPASS_AUTH` (dev-only, but honored in any environment per formal.md §4), Google OAuth config, `JWT_PUBLIC_KEY`, and a CL-only PASETO/New Relic block. Jenkins → Kaniko-built image → `Lumilo-Bridge-Deploy` target is the actual deploy path; `infrastructure.yaml`-style declarative config was not found in this repo (unlike the sibling ingestion repo) — deploy target details live in the Jenkinsfile/deploy tooling, not a checked-in infra manifest here.
