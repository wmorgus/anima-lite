# Feature: My Classes
slug: lumilo-classes-my-classes
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: bridge-frontend/src/app/features/classes/my-classes.component.ts renamed/removed, or the Class GraphQL type changes

## Identity
Teacher's list of their classes. Domain-central: rolls up the `Class` entity (see material.md §7).

## Entry points
`bridge-frontend/src/app/features/classes/my-classes.component.ts`.

## Primary data structure
not traced — component confirmed, backing query/type not confirmed this pass (see `Class Detail` sibling feature for the confirmed `ClassDetail` type; `My Classes` likely lists a lighter-weight `AvailableClassData`/`ClassDetail` subset, but this was not read directly).

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
