# Feature: Sessions List
slug: lumilo-sessions-list
repo(s): lumilo-bridge
stub: 2
source: ari-map-probe
prod-commit: e2b4831
goes-stale: sessionSummarySchema.graphql's `AllSessionsResponse`/`HistoricalSessionSummary` types change, or sessions-list.component.ts renamed/removed

## Identity
List of active/historical MATHia tutoring sessions. Domain-central (built on `SessionSummary`/session concept).

## Entry points
`bridge-frontend/src/app/features/sessions/sessions-list.component.ts`. Queries: `GetAllSessions`/`GetActiveSessions`/`GetFilteredSessions`.

## Primary data structure
`AllSessionsResponse`/`HistoricalSessionSummary` (`sessionSummarySchema.graphql:110` per probe): `sessionCode`, `classId`, `className`, `configName`, `teacherId`/`teacherName`, `sessionStartTime`/`sessionEndTime`, `studentCount`, `deviceCount`.

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
