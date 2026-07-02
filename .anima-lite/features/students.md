# Feature: Students (Tutor Dashboard)
slug: students
repo(s): plus-web-app
stub: 1
source: ari-map-probe
prod-commit: 29d41e50
goes-stale: StudentsServlet.java renamed, /PLUS/Students URL mapping changed

## Identity
Tutor-facing dashboard listing assigned students with session status, progress metrics, and assignment controls.

## Entry points
/PLUS/Students → StudentsServlet.java → jsp_pl2/students.jsp
(confirmed: web.xml:311, servlet file exists, JSP file exists)

## Primary data structure
not traced

---
Everything below is enriched by ari-port after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
not traced

## Client-side wiring
students.js (type="module"); imports plus_components/ utilities, schedule/tutor_schedule_utils.js

## State machine
not traced or n/a

## Feature gates
not traced

## Seam-specific protocols
not traced

## Known quirks
not traced or none

## Port provenance
n/a until first port
