# Feature: School Management — List
slug: lumilo-school-management-list
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `School` type in schoolSchema.graphql changes, or school-list.component.ts renamed/removed

## Identity
System-admin: list/manage schools/districts. Domain-central (`School` recurs across class/user records via `schoolId`).

## Entry points
`bridge-frontend/src/app/features/school-management/components/school-list/school-list.component.ts`.

## Primary data structure
`School` (`schoolSchema.graphql`): `schoolId`, `schoolName`, `district`, `isActive`, `createdAt`, `updatedAt`.

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
