# Feature: Simulator event generation and ingestion
slug: rep-simulator-ingestion
repo(s): realtime-event-provider
stub: 2
source: ari-map-probe
prod-commit: adf0caf
goes-stale: rep-simulator/index.js or event-utils.js message-generation logic changes, or the simulator stream naming convention changes

## Identity
Generates synthetic educational event sequences (IdentityContextChange → follow-up events) and pushes them onto the `rep-simulator-stream-{env}` Kinesis stream, for testing the Flink pipeline without real tutor traffic.

## Entry points
Lambda: `rep-simulator/index.js` `exports.handler` — manually invoked (CLI/Console/programmatic), not on a schedule or event source mapping. CLI alternative: `rep-simulator/test-data-generator.js` (file/console/LocalStack-Kinesis output modes).

## Primary data structure
Generated event JSON, shape defined by `rep-simulator/event-templates/*.json` (identity-context-change, student-model-update, tutor-message, ct-context-change, ct-content-context-change, content-position) and produced by `event-utils.js`'s `generateEventSequence`. Sent via `PutRecordCommand` with `PartitionKey: event.session_id`.

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
Configurable via Lambda invocation payload: `config.numSessions` (default 3), `config.delayBetweenEvents` (default 100ms).

## Seam-specific protocols
Repo-wide seam protocols live in the spine (formal.md §4), not here. not traced.

## Known quirks
none.

## Port provenance
n/a until first port.
