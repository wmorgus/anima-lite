# Feature: Researcher Dashboard
slug: lumilo-researcher-dashboard
repo(s): lumilo-bridge
stub: 0
source: ari-map-probe
prod-commit: e2b4831
goes-stale: researcher-dashboard.component.ts is removed or wired into researcher.routes.ts (which would resolve the orphan status noted below)

## Identity
Component exists on disk but appears **not routed** in `app.routes.ts`/`researcher.routes.ts` — likely legacy/superseded by `researcher-overview`. Named finding: possible orphaned entry point, not a confirmed live feature.

## Entry points
`bridge-frontend/src/app/features/researcher/researcher-dashboard.component.ts` — file exists; route wiring not confirmed (probe found no route referencing it).

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
not traced.

## Seam-specific protocols
not traced.

## Known quirks
Possibly orphaned — component file exists without a confirmed route reference. A port that assumes every component file is a live, routed feature would be wrong here.

## Port provenance
n/a until first port.
