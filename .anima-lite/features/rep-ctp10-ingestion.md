# Feature: CTP10 production event ingestion
slug: rep-ctp10-ingestion
repo(s): realtime-event-provider
stub: 2
source: ari-map-probe
prod-commit: adf0caf
goes-stale: EventMessage.java field changes, EventMessageDeserializationSchema.java changes, or the CTP10 stream ARN/naming convention changes

## Identity
Consumes the real Carnegie Learning tutor-system event feed (`ctp10-{env}-pipeline` Kinesis stream) as one of two input streams to the Flink enrichment/filter pipeline.

## Entry points
`RepMain.main()` → `StreamFactory.createStreamSource(env, ctpStreamARNString)`, where `ctpStreamARNString` comes from Flink application property `ctpStreamARN` (via `ConfigurationService.getApplicationProperties()`). File: `rep-flink/src/main/java/com/amazonaws/services/kinesisanalytics/RepMain.java`, `rep-flink/src/main/java/com/amazonaws/services/kinesisanalytics/utils/StreamFactory.java`.

## Primary data structure
`EventMessage` (POJO): `messageType`, `sessionId`, `tenantId`, `groupId`, `userId`, `enrichedTenantId`, `enrichedGroupId`, `enrichedUserId`, `eventClass`, `originalJson`. Populated by `EventMessageDeserializationSchema` from input JSON's `@class`, `session_id`, and (IdentityContextChangeMessage only) `tenantId`/`groupId`/`userId`.

---
Everything below is enriched by ari-code-rhetoric after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
not traced.

## Client-side wiring
n/a — no client.

## State machine
not traced.

## Feature gates
not traced.

## Seam-specific protocols
Repo-wide seam protocols live in the spine (formal.md §4), not here. not traced.

## Known quirks
none.

## Port provenance
n/a until first port.
