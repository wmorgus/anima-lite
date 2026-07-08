# Feature: User Guide (multi-section)
slug: lumilo-user-guide
repo(s): lumilo-bridge
stub: 0
source: ari-map-probe
prod-commit: e2b4831
goes-stale: user-guide.component.ts or its sections renamed/removed

## Identity
In-app static help/onboarding documentation, no auth guard. not traced beyond existence.

## Entry points
`bridge-frontend/src/app/features/user-guide/user-guide.component.ts` + sections: welcome, room-setup, class-seatmaps, daily-use, teaching, troubleshooting.

## Primary data structure
not traced (static content, likely no backing GraphQL type).

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
No auth guard confirmed (accessible without login, per probe).

## Seam-specific protocols
not traced.

## Known quirks
not traced.

## Port provenance
n/a until first port.
