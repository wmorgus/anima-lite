# Feature: User Activity Logs
slug: lumilo-user-management-activity-logs
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `TeacherActionLog`/`GraphQLLog` types change, or user-activity-logs.component.ts renamed/removed

## Identity
Per-user audit-log viewer. Domain-central (nested under `User`).

## Entry points
`bridge-frontend/src/app/features/user-management/components/user-activity-logs/user-activity-logs.component.ts`.

## Primary data structure
`TeacherActionLog`/`GraphQLLog`, nested under `User` — not independently enumerated this pass.

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
