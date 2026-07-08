# Feature: MATHia Sessions (list)
slug: lumilo-admin-mathia-sessions
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `ClassWithMathiaSessions` type in schema.graphql changes, or mathia-sessions.component.ts renamed/removed

## Identity
System-admin view of raw ingested MATHia session/event data (ingestion debugging). Not domain-central (a debugging surface over ingestion, not a user-facing session concept itself).

## Entry points
`bridge-frontend/src/app/features/admin/mathia-sessions.component.ts`.

## Primary data structure
`ClassWithMathiaSessions` (`schema.graphql:522` per probe) — existence confirmed, fields not enumerated this pass.

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
