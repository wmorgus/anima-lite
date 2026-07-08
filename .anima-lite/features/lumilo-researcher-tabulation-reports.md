# Feature: Tabulation Reports
slug: lumilo-researcher-tabulation-reports
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `TabulationReportClass` type in schema.graphql changes, or tabulation-reports.component.ts renamed/removed

## Identity
Aggregate research reports across classes/sessions. Not domain-central (a reporting surface over sessions/classes, not the noun itself).

## Entry points
`bridge-frontend/src/app/features/researcher/tabulation-reports/tabulation-reports.component.ts`.

## Primary data structure
`TabulationReportClass` (`schema.graphql:624` per probe) — existence confirmed, fields not enumerated this pass.

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
