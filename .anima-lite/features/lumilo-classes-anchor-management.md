# Feature: Anchor Management
slug: lumilo-classes-anchor-management
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `Anchor` type in schema.graphql, graphql-server/src/resolvers/anchor.ts, or anchor-management.component.ts/anchor.service.ts changes

## Identity
Upload/manage AR spatial-anchor files (Unity/AR tracking) per school and assign to classes. Not domain-central (infrastructure for AR tracking, not a recurring core noun like session/class/student).

## Entry points
`bridge-frontend/src/app/features/classes/anchor-management.component.ts`, `bridge-frontend/src/app/core/anchor.service.ts`, `bridge-frontend/src/app/graphql/queries/anchors.graphql`. Backend resolver: `graphql-server/src/resolvers/anchor.ts` (queries `GetAnchorIds`/`GetAnchor`).

## Primary data structure
`Anchor` (schema.graphql:218 per probe): `anchorId`, `schoolId`, `label`, `fileSize`, `uploadedBy`, `uploadedAt`, `assignedClasses`.

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
