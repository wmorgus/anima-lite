# Feature: GraphQL mutation delivery to lid-backend
slug: rep-delivery-lid-backend
repo(s): realtime-event-provider
stub: 2
source: ari-map-probe
prod-commit: adf0caf
goes-stale: rep-delivery/index.js routing/transform functions change, config/environments/*.json lid-backend entry changes, or infrastructure.yaml's KinesisEventSourceMapping changes

## Identity
Consumes the output Kinesis stream via a Lambda event source mapping, matches records to the `lid-backend` application config, transforms Mathia-format events to GraphQL variables, and POSTs JWT-signed GraphQL mutations to `lid-backend`'s endpoint. Unaffected by the upcoming lumilo-bridge ripple — lid-backend keeps this delivery path.

## Entry points
Lambda `rep-delivery/index.js` `handler()`, triggered by `AWS::Lambda::EventSourceMapping` on the output stream (`infrastructure.yaml` `KinesisEventSourceMapping`, `BatchSize: 100`, `MaximumBatchingWindowInSeconds: 5`). Routing decided by `routeDataToApplications()` → `getMatchingApplications()` (`rep-delivery/config/index.js`) against the `lid-backend` entry in `config/environments/{env}.json`.

## Primary data structure
Per-message-type GraphQL mutation variables (`base` + type-specific fields), built by `transformAttemptData`/`transformSkillChangeData`/`transformContextChangeData`/`transformContentChangeData`/`transformPositionChangeData` in `rep-delivery/index.js`. Endpoint config: `{endpoint: "https://apps.carnegielearning.com/lid-backend/graphql", validClassIds[], validTenantIds[]}` (prod.json).

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
Matching is OR-logic (`validTenantIds.includes(tenantId) || validClassIds.includes(classId)`), not the AND-logic this repo's CLAUDE.md documents — see spine formal.md §5.

## Seam-specific protocols
See spine formal.md §4 "rep-delivery → downstream GraphQL apps." JWT audience = `lid-backend`.

## Known quirks
none beyond the OR/AND matching discrepancy already noted at spine level.

## Port provenance
n/a until first port.
