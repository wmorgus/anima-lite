# Contract: REP→lumilo-bridge direct Kinesis ingestion (drop lambda/GQL-mutation leg)
Branch: rep-lumilo-kinesis-direct
Generated: 2026-07-08
Spine commit: lumilo-bridge e2b4831, realtime-event-provider adf0caf
Source of truth: n/a — ripple, no prior implementation. Both legs' existing code
(mathiaKinesis.service.ts, rep-delivery/index.js's transform functions) was read
as classification evidence, not as a proto to translate from.
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
lumilo-bridge should receive MATHia classroom events by consuming
realtime-event-provider's (REP) output Kinesis stream directly — not through a
lambda-mediated GraphQL mutation hop — with no loss of message coverage: every
Mathia message type intended for lumilo-bridge should arrive, not just the
handful REP's lambda historically forwarded.

## Substrate changes (free to translate)
- Whether the Kinesis consumer polls via `GetRecordsCommand` in a loop
  (current `mathiaKinesis.service.ts` shape) vs. any other AWS SDK consumption
  pattern — lumilo-bridge formal.md §3 (Data flow) establishes shard-poll-loop
  as the existing pattern for this service; not load-bearing to the argument,
  free to keep or refactor.
- Redis-checkpoint key naming, poll-interval env var names, backoff timing —
  implementation detail, not part of what's promised.
- Internal file/function organization of the new mapping logic (single file vs.
  split per message class) — medium only.

## Claim changes (confirmed with user)

- **Claim A — REP stops delivering to lumilo-bridge via lambda/GraphQL.**
  Decision: change-to — remove lumilo-bridge as a routing target in REP's
  delivery leg. Confirmed: yes, 2026-07-08 (this is the ripple's core ask).
  Schema deps: REP's `APPLICATION_ROUTING_CONFIG` is not in either target
  repo — it's a CloudFormation parameter defined in a **third leg**, the
  company `aws-infrastructure` repo (checkout used:
  `/Users/wmorgus/Desktop/via-carnegie/aws-infrastructure`, currently on
  `wip/wmorgus/DEVOPS-10085-update-rep-routing-config` — already the live
  branch for exactly this kind of edit). Grep-confirmed (2026-07-10, no spine
  probe run — see note below) at:
  `lambdas/realtime-event-provider/profiles/rep-delivery/environments/{prod,staging,qa}/stack-config.yml`,
  each containing an `applications.lumilo-bridge` block with `endpoint`,
  `validClassIds`, `validTenantIds`. GATE-SCHEMA satisfied by direct
  confirmation in all three environments — no spine exists for
  `aws-infrastructure` and none is being probed for this ripple: the claim's
  rendering here is a bounded three-file JSON-block removal, not a code
  behavior change, so a full four-cause spine probe of a large multi-service
  infra monorepo is disproportionate to what this claim actually touches. This
  is a judgment call, not the ripple discipline's default — noted explicitly
  rather than silently skipped.
  **Per-target substrate mapping:**
  - **aws-infrastructure** (third leg, added 2026-07-10 — operator confirmed
    they can edit this repo directly): delete the `"lumilo-bridge": {...}`
    block from `applications` in all three `stack-config.yml` files
    (prod/staging/qa). Leave `lid-backend`'s entry untouched in every file —
    note prod's `lid-backend` entry also lists tenant `lumiloreseb1i32w`
    (shared with lumilo-bridge's own entry); that's lid-backend's own routing
    scope and is unaffected by removing lumilo-bridge's separate block.
  - realtime-event-provider: n/a for this claim's own code — `rep-delivery`
    reads whatever `APPLICATION_ROUTING_CONFIG` it's given; once
    aws-infrastructure's edit deploys, `getMatchingApplications` simply no
    longer has a lumilo-bridge entry to match against. OR-logic matching
    (`spine-realtime-event-provider/telos.md` §2) is not a residual risk here
    since the whole block is deleted, not partially edited.
  - lumilo-bridge: n/a — this claim has no rendering on lumilo-bridge's own
    code; it only stops inbound traffic from the old path.

- **Claim B — lumilo-bridge's MATHia ingestion becomes exclusively the direct
  Kinesis path.** Decision: change-to. Confirmed: yes, 2026-07-08.
  Schema deps: `LumiloEvent` (`graphql-server/src/ingestion/types.ts`) —
  confirmed exists: `{source, classId, studentId, timestamp, sourceEventId,
  eventType, payload}`. `commonIngestionService.ingest()` — confirmed exists
  (`graphql-server/src/services/commonIngestion.service.ts`).
  **Per-target substrate mapping:**
  - lumilo-bridge: set `KINESIS_STREAM_NAME` (and `AWS_REGION` if not already
    correct) in every environment lumilo-bridge runs in, to REP's actual output
    stream name (`rep-delivery-input-stream-{env}` per
    `spine-realtime-event-provider/telos.md` §2) — this activates the consumer
    already wired into `index.ts` startup (per `spine-lumilo-bridge/telos.md`
    §2's don't-contradict rule on background-consumer wiring). No new startup
    wiring needed; it's a config flip once Claim C lands.
  - realtime-event-provider: n/a — REP's output-stream production
    (rep-flink/EventMessageSerializationSchema.java) is untouched. lumilo-bridge
    becomes an additional, independent consumer of the same stream; this
    requires no REP-side change beyond Claim A.

- **Claim C — lumilo-bridge's Kinesis record mapper must actually decode REP's
  real record shape, and must not artificially limit message-type coverage to
  what REP's lambda historically forwarded.** This is the central finding of
  this argue pass, not anticipated at intake: `mathiaKinesis.service.ts`'s
  current `decodeRecord()` requires `raw.classId`, `raw.studentId`,
  `raw.eventType`, `raw.payload` — none of which exist on REP's actual
  output-stream records. Confirmed by reading both sides directly:
  - REP's actual record shape (confirmed in
    `rep-flink/.../EventMessageSerializationSchema.java` +
    `rep-delivery/index.js`'s five transform functions, which are the only
    place this mapping is currently implemented, anywhere): `{tenant_id,
    group_id, user_id, class, message_id, server_time, + Mathia-native
    passthrough fields specific to each `class` value}`.
  - `class` discriminates message type: `TutorMessage` (attempt),
    `StudentModelUpdateMessage` (skill change), `CtContextChangeMessage`,
    `CtContentContextChangeMessage`, `CtContentPositionMessage` (three
    navigation variants). REP's `rep-delivery/index.js` currently silently
    skips (`{skipped: true, reason: 'Unsupported message type'}`) any other
    `class` value.
  - As written, `decodeRecord()` fails its own required-field check on every
    real record and returns `null` — this leg has never actually been
    exercised against real REP data; the "existing service" is a stub, not a
    working adapter.

  Decision: **change-to.** Rewrite the mapping layer beneath `decodeRecord()`
  to: (1) discriminate on `record.class` via an extensible per-class handler
  registry (a class-name → mapper-function table), not a hardcoded switch
  capped at the 5 classes above — new Mathia message types must be addable by
  adding a table entry, without needing any REP-side change; (2) for each of
  the 5 currently-known classes, use REP's own `rep-delivery/index.js`
  transform functions as the field-mapping source of truth (`group_id`→
  `classId`, `user_id`→`studentId`, `message_id`→`sourceEventId`,
  `server_time`→ISO `timestamp`, and the per-class payload field mapping each
  transform function already performs — e.g. `assignmentId`→`workspaceId`,
  `evaluation`/`tutorOutcome`→`outcome`, `nodePath`→`goalnodeId`, etc. for
  attempts; `skillStatuses[].{id,newPknown,prevPknown}`→`skillData[].{skillId,
  newPknown,prevPknown}` for skill changes; the three Ct*Message field sets for
  navigation); (3) for a `class` value with no registered handler, log it
  visibly and drop the record — do not error the poll loop — but this is a
  named extension point, not a silent permanent skip, so adding coverage later
  is a table entry, not an architecture change.
  Confirmed: yes, 2026-07-08, including the extensibility requirement
  ("minimal upstream filtering so lumilo bridge gets all raw data intended for
  it" — operator framing).
  Schema deps: `AttemptPayload`, `SkillChangePayload`, `NavigationPayload`
  (`graphql-server/src/ingestion/types.ts`) — all three confirmed to exist with
  the field shapes the mapping must populate.
  **Per-target substrate mapping:**
  - lumilo-bridge: rewrite lands entirely in
    `graphql-server/src/services/mathiaKinesis.service.ts` (or a new sibling
    module it delegates to, e.g. `mathiaKinesisMapping.ts`) — `formal.md` §3
    (Data flow) names `commonIngestionService.ingest()` as the shared
    downstream call every adapter converges on; this claim only changes what
    happens before that call, consistent with the spine's own don't-contradict
    rule against duplicating ingest-side logic per source.
  - realtime-event-provider: n/a for the mapping rewrite itself — REP's five
    transform functions in `rep-delivery/index.js` are read here as reference
    logic to port, not modified. **However**, note for Open Questions: once
    lumilo-bridge reads Kinesis directly, REP's own message-class skip logic
    (`rep-delivery`'s "Unsupported message type" branch) no longer constrains
    lumilo-bridge at all — lumilo-bridge bypasses `rep-delivery` entirely by
    construction of Claim B. "Minimal upstream filtering" is therefore already
    structurally achieved by this ripple's own shape; the remaining work to
    honor the operator's intent is entirely on lumilo-bridge's side (the
    extensible registry in this claim), not a REP-side loosening.

- **Claim D — `commonIngestionService.ingest()` must persist NAVIGATION events,
  not silently no-op them.** Surfaced during execution, not anticipated at
  argue-time: `ingest()` had an explicit stub for `eventType === 'NAVIGATION'`
  (`// NAVIGATION events from non-GraphQL sources: not yet implemented`) that
  logged and returned. A correct Claim C mapper for the 3 navigation-type
  Mathia classes would decode fine and then be dropped there. Presented to
  operator as a three-way choice; operator chose to build the handling now.
  Decision: change-to. Confirmed: yes, 2026-07-10.
  Schema deps: `StudentMathiaData.navigationHistory` /
  `NavigationEventSchema` (`graphql-server/src/services/mongodb/models/studentMathiaData.model.ts`)
  — confirmed exists, required `eventType` enum
  `['ContextChange','ContentChange','PositionChange']`.
  **Per-target substrate mapping:**
  - lumilo-bridge: new `handleNavigation()` private method on
    `CommonIngestionService`, wired into `ingest()`'s NAVIGATION branch.
    Mirrors the existing GraphQL `addContextChange`/`addContentChange`/
    `addPositionChange` resolvers' direct-Mongo write into
    `navigationHistory` (same schema, same shape) rather than inventing a new
    persistence shape — the only change is that this is now the shared path,
    not duplicated per-adapter. Does not dispatch any detectors for
    navigation events, matching the existing GraphQL resolvers' behavior
    exactly (no detector dispatch invented where none existed).
  - realtime-event-provider: n/a.

## Cross-leg coherence check (ripple)
Claims A, B, and C together describe one promise — "lumilo-bridge receives
MATHia events via direct Kinesis consumption, with no coverage regression
versus the old lambda path, and room to grow beyond it" — rendered across two
legs with no shared code. No claim is stated differently per leg; only the
substrate mapping differs, as expected. Sequencing risk identified and
resolved below (see Open Questions / execution order).

## Open questions
1. ~~REP's real routing config is not in this repo~~ — **resolved 2026-07-10**.
   Located in the third leg, `aws-infrastructure`
   (`lambdas/realtime-event-provider/profiles/rep-delivery/environments/{prod,staging,qa}/stack-config.yml`).
   Operator confirmed direct edit access. `/ari-code-rhetoric` should treat
   this as a real third target for Claim A, alongside lumilo-bridge (Claims
   B/C) — not a manual-ops carve-out.
   Operator also confirmed (2026-07-10): lumilo-bridge's existing
   `mathiaKinesis.service.ts` was an untested first LLM pass — explicit
   green light to overwrite/extend it as Claim C requires, not just patch
   around it.
2. **Execution sequencing (not a claim — an execution-order note, per PIN-26
   ruling 5's "sequential only as an explicit judgment-based deviation").**
   Recommend: land and verify Claim C (mapping fix) and Claim B (env var /
   activation) on lumilo-bridge FIRST, confirm real REP records decode and
   ingest correctly end-to-end in a non-prod environment, THEN execute Claim A
   (remove the lambda routing entry). Reason: if Claim A executes before C is
   verified working, there is a window where lumilo-bridge receives MATHia
   data via neither path. This is the one deviation from parallel-by-default
   this contract identifies; it does not require re-opening intake (PIN-26
   ruling 4 — ordering is an execution judgment, not a contract amendment).
3. Whether `commonIngestionService.runPlatformDetectors()` — called by
   `mathiaKinesis.service.ts`'s `processBatch()` before `ingest()`, unlike the
   GraphQL adapter's resolvers, which don't call it — is itself correct or a
   pre-existing asymmetry unrelated to this ripple. Flagged, not resolved: this
   predates the ripple and `spine-lumilo-bridge/formal.md` §5 already names it
   as a finding. Out of scope here; noted so ari-code-rhetoric doesn't assume
   it's part of this contract's ask.

## Playwright verification
n/a — this is backend infra (Kinesis consumer + lambda routing config), no
browser-reachable UI surface to verify. Verification is functional: confirm
real REP Kinesis records decode without error and land in MongoDB /
detector-visible state via `commonIngestionService.ingest()`, in a non-prod
environment, before Claim A executes (see Open Questions #2).
