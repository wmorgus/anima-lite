# Feature: Experiment Telemetry
slug: lumilo-researcher-experiment-telemetry
repo(s): lumilo-bridge
stub: 0
source: ari-map-probe
prod-commit: e2b4831
goes-stale: experiment-telemetry.component.ts renamed/removed, or researcher.routes.ts's telemetry route changes

## Identity
Component exists but its route (`telemetry`) redirects to `sessions` per `researcher.routes.ts` — likely deprecated/in-transition, not a confirmed live feature distinct from Sessions.

## Entry points
`bridge-frontend/src/app/features/researcher/telemetry/experiment-telemetry.component.ts` — route redirects elsewhere per probe.

## Primary data structure
not traced.

---
Everything below is enriched by ari-code-rhetoric after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
not traced.

## Client-side wiring
not traced.

## State machine
not traced.

## Feature gates
not traced.

## Seam-specific protocols
not traced.

## Known quirks
Route redirects to `sessions` rather than rendering this component directly — likely an in-transition/deprecated surface, not a live distinct feature. A port should confirm liveness before treating this as active.

## Port provenance
n/a until first port.
