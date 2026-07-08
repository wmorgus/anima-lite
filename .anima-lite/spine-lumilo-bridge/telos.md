# Telos: lumilo-bridge (lumilo-bridge)
Commit: e2b4831
Confidence: medium-high
Refresh trigger: any change to `graphql-server/src/services/commonIngestion.service.ts`'s `ingest()` pipeline, `graphql-server/src/ingestion/types.ts`'s `LumiloEvent` envelope, `graphql-server/src/services/mathiaKinesis.service.ts`, `graphql-server/index.ts`'s service-startup block, or the ripple that removes the MATHia-GraphQL-mutation ingestion leg and promotes Kinesis to the sole MATHia ingestion path

## §1 Purpose
Lumilo Bridge exists to turn raw MATHia (and soon TutorShop) student-tutoring events into a live, teacher-visible classroom status feed: it ingests attempt/skill-change/navigation events from one or more sources, normalizes them into a single internal envelope (`LumiloEvent`), runs status detectors (idle, deep-dive, quick-dive, unproductive-struggle, late-start, simple-error) over that stream, persists state to MongoDB, and pushes live updates to teachers (Angular web UI) and AR/Unity devices (via GraphQL subscriptions backed by Redis pub/sub). It also serves admin, researcher, and school/user-management surfaces on the same backend. New ingestion work must land as a thin adapter that normalizes into `LumiloEvent` and calls the shared `commonIngestionService.ingest()` — it must not duplicate detector logic, Mongo-write logic, or pub/sub logic per source.

## §2 Don't contradict
- Do not implement a new ingestion source's business logic (detector dispatch, Mongo persistence, cache invalidation, pub/sub publish) outside `commonIngestionService`. Every source adapter's only job is: validate, dedupe via Redis (`checkAndRegisterMessage`), map into a `LumiloEvent`, and call `commonIngestionService.ingest(event)`. `lives-in: graphql-server/src/services/commonIngestion.service.ts, graphql-server/src/ingestion/types.ts`
- Do not assume `commonIngestionService.ingest()` awaits detector results before returning — detector dispatch (`dispatchDetectors()`) is fire-and-forget; a caller (including a future Kinesis-only path) that needs detector-completion guarantees does not get them today. `lives-in: graphql-server/src/services/commonIngestion.service.ts`
- Do not assume idle detection runs through the same per-event pipeline as the other detectors — it runs on an independent 15-second poll loop (`startIdleDetectionSchedule`), decoupled from `dispatchDetectors()`. A source that stops sending live events does not silently lose idle detection, but idle detection does not silently benefit from a faster/streaming source either. `lives-in: graphql-server/src/services/idleDetection.service.ts`
- Do not add a new persistent background consumer (Kinesis, WebSocket, or otherwise) without wiring its start/stop into `index.ts`'s startup/shutdown sequence the way `mathiaKinesisService` and `tutorshopWsService` already are — both are started unconditionally at boot and stopped in the shared `serverCleanup.dispose()` path, each independently no-op-ing if its own env config (`KINESIS_STREAM_NAME`, `TUTORSHOP_WS_URL`) is absent. `lives-in: graphql-server/index.ts`
- Do not treat `common-ingestion-format.md` as current-state documentation — it is a design doc (branch `wip/prep-for-tutorshop`, predates this branch) that still lists the Kinesis checkpoint strategy as "TBD" and the GraphQL→common-format refactor as an open item; both are already implemented in code. Verify against `graphql-server/src/services/mathiaKinesis.service.ts` and `graphql-server/src/resolvers/dataIngestion.ts` before trusting the doc. `lives-in: common-ingestion-format.md, graphql-server/src/services/mathiaKinesis.service.ts`

## §3 Cause files (reference depth)
- [material.md](material.md) — tech stack and load-bearing dependencies
- [formal.md](formal.md) — architecture patterns; new code follows these conventions
- [efficient.md](efficient.md) — build/CI/deploy; how to verify a change works

## §4 Disclaimers
Telos is inferred, not declared. Treat any claim here that materially affects
a coding decision as worth a quick verification pass against the actual code.
This probe was run in the specific context of an upcoming change: lumilo-bridge
will stop receiving MATHia data via the sibling repo's Lambda-mediated GraphQL
mutation and will instead consume that pipeline's output Kinesis stream directly.
A live Kinesis consumer (`mathiaKinesis.service.ts`) already exists on this branch,
wired into server startup and gated only by an env var — see formal.md §4/§5 for
what it does and does not yet guarantee. Whether its assumed record shape matches
what the upstream producer actually emits is a cross-repo question this spine does
not answer — that's ari-argue-rhetoric's job on a future contract, not this map.
