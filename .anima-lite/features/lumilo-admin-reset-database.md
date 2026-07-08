# Feature: Reset Database
slug: lumilo-admin-reset-database
repo(s): lumilo-bridge
stub: 0
source: ari-map-probe
prod-commit: e2b4831
goes-stale: reset-database.component.ts renamed/removed, or adminGuard changes

## Identity
Admin destructive action — wipe/reset DB state, guarded by an admin route guard. not traced beyond existence.

## Entry points
`bridge-frontend/src/app/features/admin/reset-database.component.ts` (guarded by `adminGuard`).

## Primary data structure
not traced.

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
Guarded by `adminGuard` (route-level) — not traced further.

## Seam-specific protocols
not traced.

## Known quirks
not traced.

## Port provenance
n/a until first port.
