# Feature: Session Detail
slug: lumilo-sessions-session-detail
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `SessionSummary` type in sessionSummarySchema.graphql changes, or session-detail.component.ts renamed/removed

## Identity
Live/completed dashboard for one session — per-student status, detector events. Domain-central (the richest view of `SessionSummary`).

## Entry points
`bridge-frontend/src/app/features/sessions/session-detail.component.ts`.

## Primary data structure
`SessionSummary` (`sessionSummarySchema.graphql:104` per probe): `sessionMetadata` (`SessionSummaryMetadata`), `perStudentMetrics: [StudentMetrics!]` (attempt counts, success rate, `statusDurations`/`statusTransitions`, `workspaceDurations`/`Transitions`, `promotionCount`), `classWideMetrics`; also live `StudentStatusEvent`/`TimelineEntry` types surfacing detector states (idle/deep-dive/quick-dive/unproductive-struggle/late-start).

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
not traced.

## Port provenance
n/a until first port.
