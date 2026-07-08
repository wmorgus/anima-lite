# Feature: Class Config Detail
slug: lumilo-classes-config-detail
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `ClassConfig` type in graphql-server/deviceInteractionSchema.graphql changes, or class-config-detail.component.ts renamed/removed

## Identity
View of a saved seat-map configuration for a class. Domain-central (built on `Class`).

## Entry points
`bridge-frontend/src/app/features/classes/class-config-detail.component.ts`.

## Primary data structure
`ClassConfig` (`deviceInteractionSchema.graphql`, schema.graphql:314 per probe): `configName`, `anchorId`, `sourceTemplateId`, `studentCoordinates: [StudentCoordinates!]!` (`studentId`, `studentDisplayName`, `anchorPositions`).

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
