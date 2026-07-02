# Feature: Tutor Schedule
slug: tutor-schedule
repo(s): plus-web-app
stub: 1
source: ari-map-probe
prod-commit: 29d41e50
goes-stale: TutorScheduleServlet.java renamed, /PLUS/TutorSchedule URL mapping changed

## Identity
Tutor-facing session scheduling interface for managing upcoming and past tutoring sessions.

## Entry points
/PLUS/TutorSchedule → TutorScheduleServlet.java → jsp_pl2/tutor_schedule.jsp
(confirmed: web.xml:383, servlet + JSP exist)

## Primary data structure
not traced

---
Everything below is enriched by ari-port after a port run.

## Full data flow
not traced

## Client-side wiring
javascript/pl2/schedule/ subdirectory — multiple ES module files (tutor_schedule.js, tutor_schedule_state.js, tutor_schedule_filters.js, etc.)

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
