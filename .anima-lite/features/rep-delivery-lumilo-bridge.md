# Feature: GraphQL mutation delivery to lumilo-bridge
slug: rep-delivery-lumilo-bridge
repo(s): realtime-event-provider
stub: 2
source: ari-map-probe
prod-commit: adf0caf
goes-stale: rep-delivery/index.js routing/transform functions change, config/environments/*.json lumilo-bridge entry changes, infrastructure.yaml's KinesisEventSourceMapping changes, or (most importantly) the ripple that removes this feature lands

## Identity
Consumes the output Kinesis stream via the same Lambda event source mapping as lid-backend, matches records to the `lumilo-bridge` application config, transforms Mathia-format events to GraphQL variables, and POSTs JWT-signed GraphQL mutations to `lumilo-bridge`'s endpoint. **This is the exact leg the upcoming ripple removes** — lumilo-bridge will instead consume the output Kinesis stream (`rep-output-stream-production`) directly via a new service on lumilo-bridge's side.

## Entry points
Same Lambda entry point as lid-backend: `rep-delivery/index.js` `handler()` → `routeDataToApplications()` → `getMatchingApplications()` matches the `lumilo-bridge` entry in `config/environments/{env}.json`. There is no separate entry point per downstream app — `lumilo-bridge` and `lid-backend` are both matched and dispatched inside the same `Promise.allSettled` fan-out per record, from the same Lambda invocation.

## Primary data structure
Same transform functions as lid-backend (shared code, not lumilo-specific): `transformAttemptData`/`transformSkillChangeData`/`transformContextChangeData`/`transformContentChangeData`/`transformPositionChangeData`. Endpoint config: `{endpoint: "https://apps.carnegielearning.com/lumilo-bridge/graphql", validClassIds: ["prod-class1","prod-class2"], validTenantIds: ["prod-tenant1","prod-tenant2"]}` (prod.json) — note lumilo-bridge's `validClassIds` list is a strict subset of lid-backend's (2 of 4 prod classes), so lumilo-bridge already receives a filtered subset of what lid-backend receives, even before the ripple.

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
Matching is OR-logic (`validTenantIds.includes(tenantId) || validClassIds.includes(classId)`), not AND as CLAUDE.md documents — see spine formal.md §5. This matters more for lumilo-bridge than lid-backend precisely because lumilo-bridge's allow-lists are narrower; OR-vs-AND changes who's in scope.

## Seam-specific protocols
See spine formal.md §4 "rep-delivery → downstream GraphQL apps." JWT audience = `lumilo-bridge`. When this feature is removed, `rep-key-rotation`'s rotation of the shared signing key becomes lumilo-bridge-irrelevant but not obsolete — the same key is still used for the `lid-backend` audience-scoped tokens, so `rep-key-rotation` itself is not a candidate for removal, only lumilo-bridge's audience claim usage of it.

## Known quirks
lumilo-bridge's `validClassIds` (2 classes) is a subset of lid-backend's (4 classes) in prod.json — confirmed by reading prod.json. A port/removal that assumes symmetric app configs would be wrong.

## Port provenance
n/a until first port.
