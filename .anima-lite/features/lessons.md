# Feature: Lessons
slug: lessons
repo(s): plus-web-app
stub: 1
source: ari-map-probe
prod-commit: 29d41e50
goes-stale: LessonServlet.java renamed, /PLUS/Lessons or /PLUS/Lesson URL mapping changed

## Identity
Tutor-facing lesson browsing and assignment interface; lesson content stored as JSON files.

## Entry points
/PLUS/Lessons, /PLUS/Lesson → LessonServlet.java → jsp_pl2/lessons.jsp, jsp_pl2/lesson.jsp
(confirmed: web.xml:420-425, LessonServlet.java exists, JSPs exist)

## Primary data structure
Lesson content: ~178 JSON files in javascript/pl2/lessons/ (code-derived: find count)

---
Everything below is enriched by ari-port after a port run.

## Full data flow
not traced

## Client-side wiring
javascript/pl2/lessons.js (type="module" — file uses import)

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
