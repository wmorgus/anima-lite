## Blip: decodeRecord() rewritten as extensible per-class mapper (Claim C)
Severity: info
Location: `graphql-server/src/services/mathiaKinesisMapping.ts` (new file) —
holds the per-class registry; `mathiaKinesis.service.ts:decodeRecord()` now
delegates to it.
What happened: replaced the naive field check (`raw.classId/studentId/eventType/payload`,
which never existed on real REP records) with `mapMathiaRecord()`, a
`record.class` → mapper-function table. Field mapping for the 5 known Mathia
classes ported directly from realtime-event-provider's `rep-delivery/index.js`
transform functions (read as source of truth, not guessed).
Why: contract Claim C, `.anima-lite/work/rep-lumilo-kinesis-direct/contract.md`.
Downstream consequence: a new Mathia message class is a new registry entry in
`mathiaKinesisMapping.ts`, no REP-side or poll-loop change required — satisfies
the "minimal upstream filtering" claim added mid-argue.
Contracting failure?: n/a — this is exactly what the contract specified.

## Blip: ingest()'s NAVIGATION handling built (scope widened by operator, 2026-07-10)
Severity: review-suggested
Location: `graphql-server/src/services/commonIngestion.service.ts` — new
`handleNavigation()` private method, wired into `ingest()`'s `eventType ===
'NAVIGATION'` branch (previously an explicit no-op stub: "NAVIGATION events
from non-GraphQL sources: not yet implemented").
What happened: found, before writing any code, that even a correct Kinesis
mapper for the 3 navigation-type Mathia classes (CtContextChangeMessage,
CtContentContextChangeMessage, CtContentPositionMessage) would silently vanish
at `ingest()` — the NAVIGATION branch just logged and returned. Surfaced to
operator as a three-way choice (skip navigation for now / build ingest()
handling now / map all 5 and accept the drop); operator chose to build it now.
Implementation mirrors the existing GraphQL `addContextChange`/`addContentChange`/
`addPositionChange` resolvers' direct-Mongo write into
`StudentMathiaData.navigationHistory` — same schema, same shape
(`NavigationEventSchema`, `models/studentMathiaData.model.ts`) — just routed
through the shared `ingest()` pipeline instead of duplicated per-adapter code,
consistent with lumilo-bridge's own telos.md §2 don't-contradict rule.
Why: `spine-lumilo-bridge/telos.md` §2 ("every source adapter's only job is
validate/dedupe/map/call ingest()") — the existing GraphQL navigation
resolvers already violate this (direct Mongo write, bypassing ingest()); this
change does not fix those resolvers (out of scope, not asked), it only gives
the Kinesis adapter a working path that doesn't repeat that violation.
Downstream consequence: navigation events from Kinesis are now persisted
(pushed to `navigationHistory`) but dispatch no detectors — matches existing
behavior exactly (the GraphQL navigation resolvers don't dispatch detectors
either; nothing invented here). Flagging that `dataIngestion.ts`'s three
navigation resolvers could now be refactored to call `handleNavigation()`
too, killing the duplication — not done here, out of scope for this ripple.
Contracting failure?: yes — the contract's Claim C assumed `ingest()` was a
working shared pipeline for all payload types; it wasn't, for NAVIGATION. This
should have been checked by a probe of `ingest()`'s actual branches before the
contract froze, not caught mid-execution. Noting for future argue passes: when
a claim's contract cites a "shared downstream call," verify every branch that
call needs actually exists, not just the call site.

## Blip: KINESIS_STREAM_NAME is deploy-config, not a code change (Claim B)
Severity: info
Location: `.env.example` line 38 — documents the var name but with a
placeholder value (`lumilo-mathia-events`), not REP's real stream name
(`rep-delivery-input-stream-{env}` per `spine-realtime-event-provider/telos.md`
§2).
What happened: no code change made for Claim B — `mathiaKinesis.service.ts`
already reads `process.env.KINESIS_STREAM_NAME` at startup (confirmed,
`start()` method, unchanged). Activation is a deploy-time environment-variable
set, per environment, to REP's actual stream name — not a repo file edit.
Why: `.env.example`'s placeholder value would be wrong if copied literally;
flagging so whoever sets the real deploy value doesn't copy it verbatim.
Downstream consequence: this claim isn't "done" until someone sets the real
env var in each environment lumilo-bridge runs in. Tracked as a manual/deploy
action alongside this PR, not inside it.
Contracting failure?: n/a — contract already named this as deploy-config, not
code, in Claim B's per-target substrate mapping.

## Blip: @aws-sdk/client-kinesis declared but not installed
Severity: review-suggested
Location: `package.json:9` declares `"@aws-sdk/client-kinesis": "^3.1057.0"`;
`node_modules/@aws-sdk/client-kinesis` does not exist in this checkout.
What happened: `npx tsc --noEmit` on this repo fails with
`TS2307: Cannot find module '@aws-sdk/client-kinesis'` — pre-existing, not
introduced by this ripple's changes (the import predates this session, in
`mathiaKinesis.service.ts`'s original untested version). Left as-is; did not
run `npm install` against this real checkout without being asked.
Why: consistent with the operator's own characterization of this service as
"an untested first LLM pass" — it appears to have never been run against a
real `npm install` in this checkout.
Downstream consequence: this must be resolved (`npm install`, or equivalent in
whatever environment actually builds/deploys this branch) before Claim
B/C can be verified end-to-end, per the contract's sequencing note (Open
Questions §2) that recommends verifying lumilo-bridge before REP's routing
is removed.
Contracting failure?: n/a — genuinely unforeseeable from the contract; this
is an environment-setup gap, not an argument-level gap.
