# Material: lumilo-bridge (lumilo-bridge)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Languages
TypeScript (Node) for `graphql-server/` — `typescript ^5.4.5`, `ts-node ^10.9.2` (`graphql-server/package.json`). No `engines` field and no `.nvmrc` in the repo (checked, zero hits); CLAUDE.md states "Node.js 18+" (README-stated, not lockfile-confirmed). TypeScript for `bridge-frontend/` (Angular). Small JS/TS ops-script toolkit under `scripts/` with its own `package.json` (not part of either app's build).

## §2 Backend frameworks
Apollo Server 4 (`@apollo/server ^4.12.0`) + Express, schema stitched from 12 `.graphql` files via `@graphql-tools/*` (`merge ^9.0.3`, `schema ^10.0.23`, `graphql-file-loader ^8.0.0`). Subscriptions over `graphql-ws ^6.0.4` + `ws ^8.18.1`, backed by `graphql-redis-subscriptions ^2.7.0` / `ioredis ^5.6.1`. ODM: `mongoose ^7.4.3` (driver `mongodb ^5.7.0`). AWS: `@aws-sdk/client-kinesis ^3.1057.0`. APM: `newrelic ^13.7.0`. Auth libs: `google-auth-library ^9.15.1`, `jsonwebtoken ^9.0.2`, optional internal `@carnegie-learning/auth-utils ^1.1.0` (optionalDependency — may not be installed in every checkout). Test stack: `jest ^29.7.0`, `ts-jest`, `mongodb-memory-server ^10.1.4`.

## §3 Frontend libraries
Angular 20 (`@angular/core ^20.3.15`, standalone components), `apollo-angular ^6.0.0` + `@apollo/client ^3.8.10`, `rxjs ~7.8.0`, `zone.js ~0.15.0`, `chart.js ^4.4.0`, `graphql ^16.11.0`. Test stack: Karma/Jasmine (`ng test`), not Jest.

## §4 Key dependencies
- **Named finding (version split):** `graphql-server`'s devDependencies pull `@apollo/client ^4.1.2` (v4) while `bridge-frontend` runs `@apollo/client ^3.8.10` (v3) paired with `apollo-angular ^6.0.0` — the server-side v4 is almost certainly test/codegen tooling only, not a shared runtime client; do not assume Apollo Client version parity between the two apps.
- **Named finding (version split):** the standalone `scripts/` toolkit pins `mongodb ^6.16.0`, one major ahead of `graphql-server`'s `mongodb ^5.7.0` — separate `node_modules` trees, no shared lockfile.
- All versions above are caret-ranged from `package.json`, not resolved exact pins from `package-lock.json` — re-derive exact pins from the lockfile if a port needs syntax-exact version behavior.
- A `log-processor` service exists in `docker-compose.yml` (port 5000, calls back into graphql-server's `/graphql`) that is composed alongside the app but has no source directory in this repo's tracked file tree — likely a separately-built image; flagged as present in the compose topology but not further probed here.

## §5 Data structures / schemas
Central internal envelope: `LumiloEvent` (`graphql-server/src/ingestion/types.ts`) — `source: 'MATHIA_GRAPHQL'|'MATHIA_KINESIS'|'TUTORSHOP'`, `classId`, `studentId`, `timestamp`, `sourceEventId` (dedup key), `eventType: 'ATTEMPT'|'SKILL_CHANGE'|'NAVIGATION'`, `payload: AttemptPayload|SkillChangePayload|NavigationPayload`. Every ingestion source adapter's job is to produce this shape before handing off to `commonIngestionService.ingest()`. GraphQL schema is split across 12 files (`baseSchema.graphql`, `adminSchema.graphql`, `deviceInteractionSchema.graphql`, `mathiaDataSchema.graphql`, `userSchema.graphql`, `schoolSchema.graphql`, `appStartConfigSchema.graphql`, `sessionSummarySchema.graphql`, `workspaceProgressSchema.graphql`, `anchorSchema.graphql`, `researcherSchema.graphql`, `classTemplateSchema.graphql`), merged via `mergeTypeDefs` in `index.ts`.

## §6 State shape
MongoDB (Mongoose) is system of record; Redis is cache + pub/sub + dedup + Kinesis-checkpoint store (`SHARD_ITERATOR_KEY`). 18 Mongoose models (`graphql-server/src/services/mongodb/models/index.ts`): Class, Student, User, StudentMathiaData, AppStartConfig, AppStartConfigArchive, SkillAttemptCount, SessionSummary, WorkspaceProgress, Anchor, ClassSession, StudentClassStatus, DetectorHistoryArchive, ClassTemplate, TeacherActionLog, GraphQLOperationLog, ClassActivityState, TabulationReport. Live per-student state lives on `Student.status`; a distinct nightly-tabulated `StudentClassStatus.recentHistoricStatus` is a separate, settled snapshot — the two must not be conflated.

## §7 Entity/field inventory

| entity | backing table | key fields | FKs | notes |
|---|---|---|---|---|
| Student | Student | `studentId` (unique, indexed), `displayName`, `status` (enum, 8 values), `deepDiveData.{recentActivityTimestamp, workspaceName, workspaceStartTime}`, `detectorHistory[]` (embedded `{statusName, timestamp, messageId}`) | `mathiaData` → StudentMathiaData | Central live-status entity; embeds detector-history subdocs rather than referencing them |
| Class | Class | `classId` (unique indexed), `schoolId` (indexed), `className`, `activeAnchorId`, `condition` (enum `'realtime'\|'historic'\|null`) | `students[]`→Student, `teachers[]`→User, `ghostStudents[]`→Student, `configs[].student`→Student | `configs[]` is an embedded array of named seating/coordinate configs |
| ClassSession | ClassSession | `classId` (plain string, not a ref), `startTimestamp`, `endTimestamp`, `enrolledRosterCount`, `peakActiveCount`, `isTabulated`, `isActive` | none | Partial unique index enforces at most one active session per class; represents a system-detected >50%-roster-active MATHia session window |
| StudentClassStatus | StudentClassStatus | `studentId`, `classId` (plain strings), `recentHistoricStatus` (same 8-value enum + null), `lastTabulatedAt` | `lastSessionId`→ClassSession | Nightly-tabulated, distinct from live `Student.status`; unique compound index `(studentId, classId)` |
| SessionSummary | SessionSummary | `sessionCode` (unique indexed), `classId`, `teacherId`, `sessionStartTime/EndTime`, `isActive`, `perStudentMetrics[]`, `classWideMetrics` | none (denormalized strings) | Lazily generated, fully-embedded materialized report; not incrementally referenced from other collections |
| StudentMathiaData | StudentMathiaData | `eventHistory[]`, `skillData[]`, `navigationHistory[]` (all embedded, tagged by `eventType`) | `student`→Student (required), `class`→Class (required) | Heaviest doc — raw per-student per-class MATHia event log |

## §8 Capabilities prod does NOT have

- Student-side capacity/workload does NOT exist — grepped `graphql-server/src` case-insensitively for "capacity", zero hits. Only status/detector state exists per student, no load/limit concept.
- A dedicated notification/alerting channel does NOT exist — grepped `graphql-server/src` case-insensitively for "notification", zero hits. Status changes surface only via GraphQL subscriptions + Redis pub/sub to already-connected clients (web UI, AR device); there is no email/push/SMS path.
- A single source of truth for the student-status vocabulary does NOT exist — the 8-value status enum is hand-duplicated verbatim in `student.model.ts`, `studentClassStatus.model.ts`, and `models/types.ts`, with no shared constant module backing all three.

## §9 Domain vocabulary

- `LumiloEvent` = the common internal envelope every ingestion source (MATHia GraphQL, MATHia Kinesis, TutorShop) normalizes into before detector processing (`graphql-server/src/ingestion/types.ts`).
- `status` (Student) = live, teacher-visible per-student state, one of `IDLE|CONTENT_HELP|UNPRODUCTIVE_STRUGGLE|SYSTEM_MISUSE|WORKING|DOING_WELL|OFFLINE|LATE_START`; produced by detectors.
- `recentHistoricStatus` (StudentClassStatus) = a distinct, nightly-tabulated "settled" status per student-per-class — not real-time, not the same field as `Student.status`.
- `ClassSession` = a system-detected session boundary (>50% roster active), not a user-initiated concept; has its own tabulation/archival lifecycle.
- Detector = a named algorithmic unit (idle, deepDive, quickDive, lateStart, unproductiveStruggle, simpleError) that watches the normalized event stream and emits status transitions.
- `condition` (Class) = `'realtime'|'historic'|null` — an experimental/research tag distinguishing live-monitored vs. replayed-historic classes, not a pedagogical concept.
- `TeacherActionLog.action` = teacher-side telemetry vocabulary (`PING, LOGIN, CLASS_SETUP_START/COMPLETE, TEACHER_APPROACH, TEACHER_DISENGAGE, TEACHER_LOCATION_TRACKING, ERROR_REPORT, GET_QUICK_DIVE, GET_DEEP_DIVE`) — `APPROACH`/`DISENGAGE` imply AR/physical-proximity tracking of the teacher relative to students.
- `User.role` = RBAC vocabulary: `system_admin | school_admin | teacher | researcher`.
- `AppStartConfig.phase`/`status` = AR/device app bootstrap lifecycle vocabulary: phase `teaching|setup`, status `active|expired` (archive adds `ended`).
