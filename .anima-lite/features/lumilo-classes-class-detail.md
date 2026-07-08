# Feature: Class Detail
slug: lumilo-classes-class-detail
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `ClassDetail` type in graphql-server/deviceInteractionSchema.graphql or schema.graphql changes, or class-detail.component.ts renamed/removed

## Identity
Single-class view — students, seat map, live status. Domain-central (built on `Class`).

## Entry points
`bridge-frontend/src/app/features/classes/class-detail.component.ts`.

## Primary data structure
`ClassDetail` (graphql-server schema, confirmed in `deviceInteractionSchema.graphql` and referenced at schema.graphql:302 per probe): `classId: ID!`, `className: String!`, `students: [StudentInfo!]!` (`studentId`, `name`), `activeAnchorId: ID`.

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
