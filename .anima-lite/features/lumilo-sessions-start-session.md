# Feature: Start Session
slug: lumilo-sessions-start-session
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `CreateAppStartConfig` mutation changes, or start-session.component.ts renamed/removed (also the app's default landing route)

## Identity
Begin a live monitored classroom session — also the app's default landing route. Domain-central (initiates the session concept).

## Entry points
`bridge-frontend/src/app/features/sessions/start-session.component.ts`.

## Primary data structure
Uses mutation `CreateAppStartConfig` — confirmed to exist; full field list not re-derived this pass (see `appStartConfig.model.ts` in material.md §7 candidates for the backing Mongo model, not yet added to the entity inventory table).

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
