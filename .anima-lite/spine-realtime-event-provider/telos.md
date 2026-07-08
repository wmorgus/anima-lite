# Telos: realtime-event-provider (realtime-event-provider)
Commit: adf0caf
Confidence: medium
Refresh trigger: any change to rep-flink/src/main/java/.../serialization/EventMessage*Schema.java (the output-stream record shape), rep-delivery/config/index.js (routing/matching logic), infrastructure.yaml, or the lambda-removal ripple landing (this spine was probed specifically to prep for it)

## §1 Purpose
This repo exists to take raw educational tutoring events (student attempts, skill changes, navigation/context changes) off two Kinesis input streams (`ctp10-{env}-pipeline` production feed, `rep-simulator-stream-{env}` test feed), enrich them with session identity (tenant/group/user) via Redis-backed session state, filter to valid/supported message types, and emit the enriched record onto one Kinesis output stream. A second stage currently consumes that output stream via a Lambda and re-dispatches each record as a GraphQL mutation to one or more downstream Carnegie Learning applications (lid-backend, lumilo-bridge), matched by tenant/class routing rules. New work either preserves the enrichment/filter contract on the Flink side or the routing/delivery contract on the Lambda side — it must not blur them, because they are about to become two independently-evolving surfaces (see §4).

## §2 Don't contradict
- Do not change the JSON field names written to the output stream (`tenant_id`, `group_id`, `user_id`, `class`, plus passthrough original fields) without updating every consumer of that stream — this shape is the seam a new external consumer (lumilo-bridge's planned direct Kinesis consumer) will be written against. `lives-in: rep-flink/src/main/java/com/amazonaws/services/kinesisanalytics/serialization/EventMessageSerializationSchema.java`
- Do not assume `rep-delivery`'s tenant/class matching is AND-logic — it is OR (`validTenantIds.includes(tenantId) || validClassIds.includes(classId)`), which contradicts this repo's own CLAUDE.md ("both tenant_id AND class_id match"). Any port of this routing rule must use the code-derived OR semantics, not the doc's stated AND semantics, until this is resolved. `lives-in: rep-delivery/config/index.js`
- Do not treat `infrastructure.yaml` as the source of truth for what's actually deployed — its inline `RepDeliveryLambda` code is a Python/urllib3 HTTP-webhook placeholder that does not match the real `rep-delivery/index.js` (Node.js, GraphQL, JWT-signed). The real deploy path is Jenkins (`.jenkins/build.Jenkinsfile` → `.jenkins/deploy.Jenkinsfile`) driving CloudFormation stacks loaded from an external "AWS infrastructure" repo (`cloudFormation.checkoutAwsInfrastructure()`, `baseDir: "lambdas/realtime-event-provider"`), not from this repo's `infrastructure.yaml`. `lives-in: infrastructure.yaml, .jenkins/deploy.Jenkinsfile, deploy.sh`
- Do not add a new Carnegie Learning application target without adding it to config/environments/{dev,staging,prod}.json AND confirming config/schema.json's "streams" requirement — the schema requires a top-level `streams` object but no environment file actually has one (schema is stale-or-aspirational; environment files never conformed). `lives-in: config/schema.json, config/environments/*.json`
- Do not have rep-flink or rep-simulator reach into GraphQL/HTTP delivery concerns, and do not have rep-delivery or rep-key-rotation reach into Kinesis enrichment/session concerns — the repo's four top-level dirs are intentionally single-purpose (see formal.md §2). `lives-in: rep-flink/, rep-delivery/, rep-key-rotation/, rep-simulator/`

## §3 Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## §4 Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
This probe was run in the specific context of an upcoming change: lumilo-bridge
will stop receiving data via rep-delivery's Lambda-mediated GraphQL mutation and
will instead consume this repo's output Kinesis stream directly. Findings bearing
on that change are surfaced above and in formal.md §4/§5 — the actual decision of
what changes is out of scope for this spine (that's ari-argue-rhetoric's job on a
future contract, not this map).
