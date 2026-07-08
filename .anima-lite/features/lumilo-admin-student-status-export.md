# Feature: Student Status Export
slug: lumilo-admin-student-status-export
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `StudentStatusHistoryExport` type in schema.graphql changes, or student-status-export.component.ts renamed/removed, or its route/ownership split changes

## Identity
Export historical per-student detector-status timelines (CSV likely). Not domain-central.

## Entry points
`bridge-frontend/src/app/features/admin/student-status-export.component.ts` — note: the route lives under `/researcher/export` per `app.routes.ts` while the component file itself lives under `features/admin/`, a split-ownership named finding (see formal cause of the feature-map probe; not yet promoted into formal.md as it's feature-specific, not repo-wide).

## Primary data structure
`StudentStatusHistoryExport` (`schema.graphql:146` per probe): `classId`, `studentId`, `displayName`, `historyEntries: [DetectorHistoryEntryExport!]`.

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
Route (`/researcher/export`) and component location (`features/admin/`) disagree — a naive port that assumes route path implies feature-area ownership would misfile this feature.

## Port provenance
n/a until first port.
