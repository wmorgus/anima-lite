# Feature: User Management — Detail
slug: lumilo-user-management-detail
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `User`/`TeacherActionLog`/`GraphQLLog` types change, or user-detail.component.ts renamed/removed

## Identity
Single user's profile + activity. Domain-central.

## Entry points
`bridge-frontend/src/app/features/user-management/components/user-detail/user-detail.component.ts`.

## Primary data structure
`User` + nested `TeacherActionLog`/`GraphQLLog` (see `User Management — List` for `User` fields).

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
