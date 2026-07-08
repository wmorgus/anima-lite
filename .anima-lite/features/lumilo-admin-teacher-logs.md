# Feature: Teacher Logs
slug: lumilo-admin-teacher-logs
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `TeacherActionLogExport` type in schema.graphql changes, or teacher-logs.component.ts renamed/removed

## Identity
View teacher action-log audit trail. Not domain-central.

## Entry points
`bridge-frontend/src/app/features/admin/teacher-logs.component.ts`.

## Primary data structure
`TeacherActionLogExport` (`schema.graphql:153` per probe): `userId`, `displayName`, `role`, `action`, `timestamp`, `metadata`, `sessionCode`.

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
