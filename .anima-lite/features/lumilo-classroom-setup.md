# Feature: Classroom Setup (template list)
slug: lumilo-classroom-setup
repo(s): lumilo-bridge
stub: 1
source: ari-map-probe
prod-commit: e2b4831
goes-stale: `ClassTemplate` type in classTemplateSchema.graphql changes, or classroom-setup.component.ts renamed/removed

## Identity
Browse reusable classroom seating templates. Not domain-central (a setup utility, not a recurring core noun).

## Entry points
`bridge-frontend/src/app/features/classroom-setup/classroom-setup.component.ts`.

## Primary data structure
`ClassTemplate` (`classTemplateSchema.graphql`): `templateId`, `schoolId`, `label`, `anchorId`, `deskPositions: [DeskPosition!]` (`x`, `y`, `z`), `createdBy`, `createdAt`.

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
