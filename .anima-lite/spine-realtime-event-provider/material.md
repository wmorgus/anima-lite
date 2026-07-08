# Material: realtime-event-provider (realtime-event-provider)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Languages
- Java 11 (rep-flink; `maven.compiler.release=11`, `<java.version>1.11</java.version>` in pom.xml)
- Node.js — engine version not pinned in any package.json; Jenkins build agent requires `nodejs22` (`.jenkins/build.Jenkinsfile`); CLAUDE.md states "Node.js 14+" for local dev (README-stated, unconfirmed against a runtime pin)
- Bash (deploy.sh, local-test.sh, test-simulator.sh, diagnose-startup-failure.sh)
- Groovy (Jenkinsfiles)

## §2 Backend frameworks
- Apache Flink 1.20.0, running on AWS Kinesis Data Analytics (runtime `aws-kinesisanalytics-runtime` 1.2.0), `RuntimeEnvironment: FLINK-1_15` in infrastructure.yaml (version-mismatched against pom.xml's 1.20.0 — named finding, see formal.md §5)
- AWS Lambda (Node.js) for rep-delivery, rep-key-rotation, rep-simulator

## §3 Frontend libraries
None — this repo has no user-facing UI. All "features" (see feature ledger) are Lambda/stream endpoints.

## §4 Key dependencies
- `flink-connector-aws-kinesis-streams` 5.0.0-1.20 (Kinesis source/sink connector)
- `aws-java-sdk-bom` 1.12.788 (dependency-management import)
- Gson 2.13.1 (JSON parsing, rep-flink)
- Jedis 5.2.0 (Redis client, rep-flink session enrichment)
- Log4j 2.23.1 (rep-flink logging)
- `node-fetch` ^2.7.0 (rep-delivery HTTP/GraphQL calls)
- `jsonwebtoken` ^9.0.2 (rep-delivery JWT signing, rep-key-rotation JWT test-signing)
- `@aws-sdk/client-secrets-manager` ^3.450.0 (rep-delivery, reads signing key) / ^3.864.0 (rep-key-rotation — version skew between the two Lambdas' pinned SDK minor, named finding)
- `@aws-sdk/client-kinesis` ^3.450.0 (rep-delivery devDependency, local consumer) / ^3.864.0 (rep-simulator dependency) — same cross-Lambda version skew pattern
- Maven Shade Plugin 3.6.0 (rep-flink fat-jar build, main class `com.amazonaws.services.kinesisanalytics.RepMain`)
- Test-only: JUnit Jupiter 5.11.3, Mockito 5.18.0, Testcontainers 1.21.3, embedded-redis 1.4.3 (rep-flink); Jest ^29.7.0 (rep-key-rotation)

Version pin rule note: EOL/advisory status for any of the above was not checked — check upstream advisory feeds / npm audit / Maven Central at use time, not this file.

## §5 Data structures / schemas
- `EventMessage` (Java POJO, rep-flink) — the in-pipeline record: `messageType` (from input `@class`), `sessionId` (from `session_id`), `tenantId`/`groupId`/`userId` (raw, from `IdentityContextChangeMessage`), `enrichedTenantId`/`enrichedGroupId`/`enrichedUserId`/`eventClass` (populated during Redis enrichment), `originalJson` (full original payload retained for passthrough fields the POJO doesn't explicitly model).
- Output-stream wire format (JSON, written by `EventMessageSerializationSchema`): `{tenant_id, group_id, user_id, class, ...all other original fields except "@class"}`. This is the record shape any new direct Kinesis consumer (e.g. lumilo-bridge's planned service) must parse.
- Input-stream wire format (JSON, read by `EventMessageDeserializationSchema`): `@class` (message type discriminator), `session_id`, and — only for `IdentityContextChangeMessage` — `tenantId`, `groupId`, `userId` (camelCase; note the input uses camelCase `tenantId` while the output uses snake_case `tenant_id` — a field-name transform happens at the enrichment boundary, not just a passthrough).
- Environment routing config (JSON, `config/environments/{dev,staging,prod}.json`): `{environment, applications: {<appName>: {endpoint, validClassIds[], validTenantIds[]}}}`. Confirmed identical shape across dev.json and prod.json.
- `config/schema.json` (JSON Schema draft-07) additionally requires a top-level `streams: {ctp10StreamName, outputStreamName, simulatorStreamName}` object — **no environment file has this key** (confirmed by reading dev.json and prod.json in full); schema and actual config files have diverged.

## §6 State shape
- Session context lives in ElastiCache Redis (rep-flink only), keyed `key_[sessionId with special chars removed]`, value format `tenantId:::groupId:::userId`, TTL 43200s (12h) — per `RedisSessionService` per CLAUDE.md (README-stated; not independently re-derived from RedisSessionService.java source in this probe, flagged as unconfirmed-depth).
- Routing config for the Flink side (`RoutingConfig`, valid tenant/class ID lists) is broadcast state, refreshed on an interval by `RoutingConfigSource` and read by `StreamProcessorOrchestrator` via Flink's broadcast-state pattern (confirmed: `RoutingConfigSource`, `ROUTING_CONFIG_STATE_DESCRIPTOR` in StreamProcessorOrchestrator.java).
- Routing config for the Lambda side (`rep-delivery`) is a single JSON blob read once from the `APPLICATION_ROUTING_CONFIG` env var at cold start (`config/index.js` `Configuration.initialize()`), not the same mechanism as the Flink side's broadcast state — these are two independently-configured routing tables that happen to be sourced from the same environment JSON file by `deploy.sh`'s `extract_config_values`.
- JWT signing key state: RSA keypair in AWS Secrets Manager, rotated by `rep-key-rotation` via the standard AWSPENDING → AWSCURRENT rotation-lambda protocol; `rep-delivery`'s `jwtService.js` caches signed tokens per-audience in-process for 55 minutes.

## §7 Entity/field inventory

| entity | backing table | key fields | FKs | notes |
|---|---|---|---|---|
| EventMessage (in-pipeline) | n/a (Flink POJO, no DB) | messageType, sessionId, tenantId, groupId, userId, enrichedTenantId, enrichedGroupId, enrichedUserId, eventClass, originalJson | none (stream record, not relational) | see §5; `originalJson` is the escape hatch for fields not explicitly modeled |
| Output-stream record (JSON) | n/a (Kinesis record) | tenant_id, group_id, user_id, class, + passthrough original fields (session_id, message_id, server_time, assignmentId, etc. — not exhaustively enumerated, present per message type) | none | this is the seam a new lumilo-bridge Kinesis consumer would read |
| RoutingConfig (Flink broadcast state) | n/a (in-memory broadcast state) | validTenantIds[], validClassIds[] | none | confirmed via StreamProcessorOrchestrator log line; full class not read in this probe — `not traced` beyond these two fields |
| Environment application config entry | config/environments/*.json (file, not DB) | endpoint, validClassIds[], validTenantIds[] | none | keyed by application name (e.g. "lid-backend", "lumilo-bridge") |

## §8 Capabilities prod does NOT have

- rep-delivery does NOT do AND-matching on tenant+class despite CLAUDE.md's claim — it's OR (`validTenantIds.includes(tenantId) || validClassIds.includes(classId)` in `config/index.js` `getMatchingApplications`). A naive port assuming AND-matching (as documented) would silently over-deliver to applications that only match on one criterion.
- rep-delivery does NOT have a batch-processing path wired to its Kinesis trigger — `processAttemptsBatch`/`processSkillChangesBatch` and the batch GraphQL mutations exist in `index.js` and are exported, but `handler()` (the actual Lambda entry point) never calls them; only the per-record path (`routeDataToApplications` → `processAttempt`/`processSkillChange`/etc.) is wired. Grepped `handler` body — no call to either batch function.
- infrastructure.yaml does NOT define the actual `rep-delivery` Lambda that's deployed — its inline `RepDeliveryLambda` is a Python HTTP-webhook placeholder, not the real Node.js/GraphQL Lambda in `rep-delivery/`. Confirmed by reading both the CloudFormation inline `ZipFile` code and `rep-delivery/index.js` side by side.
- config/schema.json's required `streams` object does NOT exist in any environment config file — grepped dev.json and prod.json in full, zero occurrences of `"streams"`.

## §9 Domain vocabulary

- tenant = a school district (`tenant_id`/`tenantId`), the outer identity scope
- group / class = `group_id`/`groupId`/`classId` used interchangeably across layers; rep-delivery's CLAUDE.md and code both note "group_id maps to class_id in the new structure" — this is one noun with two names depending on which layer you're reading
- session = a tutoring session, keyed by `session_id`, the Flink `keyBy` partition key and the Redis session-context lookup key
- CTP10 = the production input stream family name (`ctp10-{env}-pipeline`) — the real upstream tutor-system feed, distinct from the simulator's synthetic feed
- REP = "Realtime Event Provider" — this repo's own name, used as a component-name prefix (`rep-flink`, `rep-delivery`, `rep-key-rotation`, `rep-simulator`)
- application (routing sense) = a downstream Carnegie Learning consumer of REP data (`lid-backend`, `lumilo-bridge`), each with its own GraphQL endpoint and valid tenant/class allow-lists — not to be confused with "the Flink application" (the Kinesis Data Analytics application itself), which is also called "application" in infrastructure.yaml. Same word, two referents, disambiguate by context.
