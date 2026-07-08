# Feature: Enriched-event output stream production
slug: rep-output-stream-production
repo(s): realtime-event-provider
stub: 2
source: ari-map-probe
prod-commit: adf0caf
goes-stale: EventMessageSerializationSchema.java changes, StreamFactory.createSinkDeliveryStream changes, or the output stream name/ARN convention changes

## Identity
Writes the enriched, filtered event record to the `rep-delivery-input-stream-{env}` Kinesis stream — this is the single seam where the ingest/enrich pipeline (rep-flink) hands off to whatever consumes the data next. Load-bearing for the upcoming ripple: this feature is UNCHANGED by removing the Lambda-mediated GraphQL dispatch, since it has no knowledge of its consumer.

## Entry points
`RepMain.main()` → `StreamFactory.createSinkDeliveryStream(deliveryStreamARNString)`, `deliveryStreamARN` from Flink application properties. File: `rep-flink/src/main/java/com/amazonaws/services/kinesisanalytics/RepMain.java`, `rep-flink/src/main/java/com/amazonaws/services/kinesisanalytics/utils/StreamFactory.java`.

## Primary data structure
Output JSON record via `EventMessageSerializationSchema`: `{tenant_id, group_id, user_id, class, ...passthrough original fields except "@class"}`. This is the exact shape a new direct Kinesis consumer (e.g. lumilo-bridge's planned service, per the ripple this repo was probed for) must parse. Partition key = `String.valueOf(element.hashCode())` (not session-based — named for future callers: this stream is not partitioned by session, ordering-per-session is not guaranteed at the shard level).

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
See spine formal.md §4 "Flink → output Kinesis stream" — this feature's entire content is that seam.

## Known quirks
Partition key is `element.hashCode()`, not `sessionId` — confirmed in `StreamFactory.createSinkDeliveryStream`. A new consumer relying on per-shard session ordering would be wrong to assume it.

## Port provenance
n/a until first port.
