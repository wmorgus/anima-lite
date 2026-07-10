# Intent: REP→lumilo-bridge direct Kinesis ingestion (drop lambda/GQL-mutation leg)
Slug: rep-lumilo-kinesis-direct
Work-type: ripple
Generated: 2026-07-08
Target spine: .anima-lite/spine-lumilo-bridge/telos.md, .anima-lite/spine-realtime-event-provider/telos.md
Target telos commit: lumilo-bridge e2b4831, realtime-event-provider adf0caf

## Telos statement
Replace realtime-event-provider's (REP) lambda-mediated GraphQL-mutation dispatch
to lumilo-bridge with lumilo-bridge consuming REP's output Kinesis stream directly,
removing the lambda hop while preserving equivalent MATHia event delivery to
lumilo-bridge. Scoped to the lumilo-bridge delivery leg only — REP's enrichment
pipeline (rep-flink/rep-simulator) and its lid-backend delivery leg are untouched.

Checked against both target spines, clean on both:
- **lumilo-bridge telos.md §1/§2**: matches directly — telos states "new ingestion
  work must land as a thin adapter that normalizes into `LumiloEvent` and calls
  the shared `commonIngestionService.ingest()`"; the adapter this change promotes
  to sole MATHia path (`mathiaKinesis.service.ts`) already does exactly this, and
  is already wired into startup per §2's own don't-contradict rule about new
  background consumers.
- **realtime-event-provider telos.md §1/§2**: matches directly — telos explicitly
  names the Flink-enrichment surface and the Lambda-delivery surface as "about to
  become two independently-evolving surfaces," anticipating exactly this ripple.
  This work item touches only the delivery/routing surface (removing one consumer
  from `rep-delivery`'s routing config), not the enrichment surface or the output
  stream's record shape.

**Apex layer (RESOLUTION.md): absent for both legs.** Neither lumilo-bridge nor
realtime-event-provider is an anima-lite-tracked repo with a RESOLUTION.md — both
are external real-world production repos. No apex check performed; this absence
does not block the gate per GATE-TELOS's own rule.

GATE-TELOS: clean, no conflict, both layers.

## Sources
- Operator description, 2026-07-08 (this workstream's originating instruction):
  "change the infra to instead of having REP send gql mutations thru a lambda,
  have lumilo-bridge consume the kinesis stream directly using a new service"
  — note: "new service" in the operator's framing turned out, on probe, to
  already exist as `mathiaKinesis.service.ts` on lumilo-bridge's
  `wip/common-ingestion-prep` branch; see Notes.
- `.anima-lite/spine-realtime-event-provider/telos.md` §1/§2 and formal.md §4/§5
  (probed 2026-07-08) — output-stream record shape, rep-delivery routing logic,
  rep-key-rotation's shared use by lid-backend.
- `.anima-lite/spine-lumilo-bridge/telos.md` §1/§2 and formal.md §4/§5 (probed
  2026-07-08) — existing `mathiaKinesis.service.ts` consumer, its startup wiring,
  the common-ingestion-format.md doc/code mismatch.

## Claims
- Remove lumilo-bridge as a routing target in REP's `rep-delivery` GQL-mutation
  dispatch (`rep-delivery/config/index.js` and its per-environment tenant/class
  allow-lists) — REP stops sending lumilo-bridge any GraphQL mutations once the
  direct-Kinesis path is live.
  argued-by: language operator description, 2026-07-08
- lumilo-bridge's MATHia ingestion path becomes: consume REP's output Kinesis
  stream directly via `mathiaKinesis.service.ts`, replacing the lambda-mediated
  GraphQL-mutation path as the live source for MATHia events.
  argued-by: language operator description, 2026-07-08
- REP's Flink enrichment pipeline, its output-stream record shape/schema, and its
  lid-backend delivery leg (`rep-delivery` routing to lid-backend, `rep-key-rotation`)
  are out of scope and must not change as part of this ripple — lid-backend
  continues to receive its GraphQL mutations exactly as before.
  argued-by: language spine finding, spine-realtime-event-provider/telos.md §1
  ("two independently-evolving surfaces") + §2 (rep-key-rotation shared-use finding),
  probed 2026-07-08
- rep-simulator (REP's test-feed producer) is unaffected — it feeds the same
  enrichment pipeline and output stream, which this ripple does not alter.
  argued-by: language spine finding, spine-realtime-event-provider/telos.md §1

## Claims (added during argue pass, 2026-07-08)
- lumilo-bridge's Kinesis mapping layer (replacing/extending `decodeRecord()`)
  must be built as an extensible per-message-class mapper, not artificially
  limited to whatever message classes REP's `rep-delivery` historically
  supported (`TutorMessage`, `StudentModelUpdateMessage`,
  `CtContextChangeMessage`, `CtContentContextChangeMessage`,
  `CtContentPositionMessage`) — new Mathia message types must be addable on
  lumilo-bridge's side without requiring a REP-side change. Operator framing:
  "minimal upstream filtering so that lumilo bridge gets all raw data intended
  for it."
  argued-by: language operator description, 2026-07-08 (clarifying round, during
  ari-argue-rhetoric, in response to the decodeRecord-scope confirmation question)

## Claims (added during execution, 2026-07-10)
- `commonIngestionService.ingest()` must actually persist NAVIGATION-type
  events (the 3 Ct*Message classes), not silently no-op them. Discovered
  during execution: even a correct Kinesis mapper would decode these
  correctly and then vanish at `ingest()`'s explicit "not yet implemented"
  NAVIGATION stub. Operator chose to build this now rather than defer it or
  ship a mapper that feeds a known dead end.
  argued-by: language operator description, 2026-07-10 (three-way choice
  presented mid-execution: skip navigation types / build ingest() handling
  now / map all 5 and accept the silent drop — operator chose to build it)

## Notes
**Central open technical question, deferred to `/ari-argue-rhetoric` for
classification, not resolved here per intake's scope fence:** whether
lumilo-bridge's `mathiaKinesis.service.ts` `decodeRecord()` — which expects an
already-`LumiloEvent`-like JSON shape — actually matches what REP's
`EventMessageSerializationSchema.java` writes to the output stream (per REP's
own spine: `{tenant_id, group_id, user_id, class, + passthrough original
fields}`). Both spines flagged this as cross-repo and explicitly left it
unresolved (see each telos.md §4 disclaimer). This is the single highest-risk
unknown in this ripple and argue must classify it before any contract can freeze:
if the shapes already match, the "new service" claim above is closer to a
substrate no-op (the adapter is done, only routing config changes); if they
don't match, `mathiaKinesis.service.ts`'s `decodeRecord()` needs a claim-level
change to actually consume REP's real record shape.

**Scope note on "new service" framing.** The operator's original framing was
"consume the kinesis stream directly using a new service." The probe surfaced
that this service is not new — `mathiaKinesis.service.ts` already exists, is
already wired into lumilo-bridge's startup, and is already gated by
`KINESIS_STREAM_NAME` (currently presumably unset in the environments this
lambda-GQL leg is live in). This does not contradict the operator's intent — it
changes what "doing" the change means: this ripple is closer to "confirm the
adapter that exists is correct, then flip the switch and remove the old leg"
than "build a consumer from scratch." Flagging so argue and any downstream
execution don't duplicate work that's already built.

**Routing-logic caveat carried forward for execution.** REP's `rep-delivery`
matching logic is OR (`validTenantIds.includes(tenantId) || validClassIds.includes(classId)`),
not the AND its own CLAUDE.md claims. Whoever edits the routing config to drop
lumilo-bridge must reason about actual OR semantics — a naive edit assuming AND
could leave lumilo-bridge partially still receiving mutations for classes that
match by class-id alone even after its tenant entries are removed.

**Third leg surfaced during argue, 2026-07-10.** REP's `APPLICATION_ROUTING_CONFIG`
(Claim A's schema dependency) is not in either original leg — it's a
CloudFormation parameter in the company `aws-infrastructure` repo
(`/Users/wmorgus/Desktop/via-carnegie/aws-infrastructure`,
`lambdas/realtime-event-provider/profiles/rep-delivery/environments/{prod,staging,qa}/stack-config.yml`).
Operator confirmed (language, 2026-07-10) direct edit access to this repo, and
separately confirmed lumilo-bridge's existing `mathiaKinesis.service.ts` was an
untested first LLM pass — explicit go-ahead to overwrite/extend it per Claim
C. No spine was probed for aws-infrastructure; see `contract.md`'s Claim A for
the judgment call on why (bounded config-block removal, not a code-behavior
change).

**Execution posture (per PIN-26 rulings, not re-argued here):** parallel-by-default
across both legs (ruling 5) — no privileged first leg unless argue surfaces a
specific reason to sequence them (e.g. if the shape-mismatch question above
resolves such that lumilo-bridge's adapter needs a claim-level fix, that fix
should land and be verified before REP's routing-removal claim executes, to
avoid a window where lumilo-bridge receives neither the lambda mutations nor
correctly-shaped Kinesis events). Two-tier break-reopen (ruling 4) applies if
either leg's contract amends downstream once execution starts.
