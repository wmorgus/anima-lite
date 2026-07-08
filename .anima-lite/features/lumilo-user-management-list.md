# Feature: User Management — List
slug: lumilo-user-management-list
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `User` type in userSchema.graphql changes, or user-list.component.ts renamed/removed

## Identity
Admin: list users, filter by role/school. Domain-central (`User` recurs across the RBAC/auth surface).

## Entry points
`bridge-frontend/src/app/features/user-management/components/user-list/user-list.component.ts`.

## Primary data structure
`User` (`userSchema.graphql`): `email`, `displayName`, `mathiaID`, `role: UserRoleType!`, `schoolId`, `isActive`, `logs: [TeacherActionLog!]`, `gqlLogs: [GraphQLLog!]`, `createdAt`, `updatedAt`.

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
