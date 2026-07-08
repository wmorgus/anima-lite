# Feature: Redis-backed session enrichment
slug: rep-session-enrichment
repo(s): realtime-event-provider
stub: 2
source: ari-map-probe
prod-commit: adf0caf
goes-stale: RedisSessionService.java changes, StreamProcessorOrchestrator.java changes, or the session-context key/value format changes

## Identity
Attaches tenant/group/user identity context (established once by an `IdentityContextChangeMessage`) to every subsequent event in the same session, using Redis as the session-context store, so downstream consumers get a fully-identified record even though most message types don't carry identity fields themselves.

## Entry points
`StreamProcessorOrchestrator.processElement()` (a `KeyedBroadcastProcessFunction`, keyed by `sessionId`) — delegates to `MessageProcessorFactory`-selected processor (`IdentityContextChangeProcessor` writes context; `EnrichmentProcessor` reads it for the other 5 message types). File: `rep-flink/src/main/java/com/amazonaws/services/kinesisanalytics/functions/StreamProcessorOrchestrator.java`.

## Primary data structure
Redis session context, key format `key_[sessionId with special chars removed]`, value format `tenantId:::groupId:::userId`, TTL 43200s (12h) — per this repo's own CLAUDE.md; not independently re-derived from `RedisSessionService.java` source in this probe (README-stated, not code-confirmed at this depth).

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
