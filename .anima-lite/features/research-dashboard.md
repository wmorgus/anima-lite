# Feature: Research Dashboard
slug: research-dashboard
repo(s): plus-web-app
stub: 1
source: ari-map-probe
prod-commit: 29d41e50
goes-stale: ResearchDashboardServlet.java renamed, /PLUS/ResearchDashboard URL mapping changed

## Identity
Research/admin-facing data export and analysis dashboard (CMU-internal research tooling).

## Entry points
/PLUS/ResearchDashboard → ResearchDashboardServlet.java (extends AbstractServlet) → jsp_pl2/research_dashboard.jsp
(confirmed: web.xml:430, servlet extends AbstractServlet confirmed)

## Primary data structure
not traced

---
Everything below is enriched by ari-port after a port run.

## Full data flow
not traced

## Client-side wiring
javascript/pl2/research.js (confirmed: file uses import)

## State machine
n/a

## Feature gates
not traced

## Seam-specific protocols
not traced

## Known quirks
not traced or none

## Port provenance
n/a until first port
