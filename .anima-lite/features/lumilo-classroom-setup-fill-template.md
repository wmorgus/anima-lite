# Feature: Fill Template
slug: lumilo-classroom-setup-fill-template
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `ClassConfigInput` changes, or fill-template.component.ts renamed/removed

## Identity
Apply a template + assign students to desks, creating a new class config. Not domain-central (produces a `ClassConfig`, see `Class Config Detail` feature).

## Entry points
`bridge-frontend/src/app/features/classroom-setup/fill-template.component.ts`.

## Primary data structure
Produces a `ClassConfig` via `ClassConfigInput` (see `Edit Seat Map`/`Class Config Detail` siblings).

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
