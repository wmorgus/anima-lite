# Feature: Edit Seat Map
slug: lumilo-classes-edit-seat-map
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `ClassConfigInput`/`StudentCoordinateInput` in deviceInteractionSchema.graphql changes, or edit-seat-map.component.ts renamed/removed

## Identity
Edit/reposition students on a class's AR seat map. Domain-central (edits `ClassConfig`).

## Entry points
`bridge-frontend/src/app/features/classes/edit-seat-map.component.ts`.

## Primary data structure
Uses `ClassConfigInput`/`StudentCoordinateInput` (`deviceInteractionSchema.graphql:327-339` per probe) — mutation input shape confirmed to exist; full field enumeration not re-derived here (see `Class Config Detail` sibling for the read-side `ClassConfig` type).

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
