# Feature: Student Portal
slug: student-portal
repo(s): plus-web-app
stub: 1
source: ari-map-probe
prod-commit: 29d41e50
goes-stale: PL2StudentServlet.java renamed, /PLUSStudent URL mapping changed, jsp_pl2_student/ restructured

## Identity
Student-facing interface for viewing assignments, resources, and session progress — separate from the tutor interface.

## Entry points
/PLUSStudent → PL2StudentServlet.java → jsp_pl2_student/pl2_student.jsp
(confirmed: web.xml:399, servlet file exists, JSP directory jsp_pl2_student/ exists with 11 files)

## Primary data structure
not traced

---
Everything below is enriched by ari-port after a port run.

## Full data flow
not traced

## Client-side wiring
not traced

## State machine
not traced or n/a

## Feature gates
Separate session and auth hierarchy from tutor side (PL2StudentLoginServlet extends AbstractServlet)

## Seam-specific protocols
not traced

## Known quirks
not traced or none

## Port provenance
n/a until first port
