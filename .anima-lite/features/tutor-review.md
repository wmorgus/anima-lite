# Feature: Tutor Review (AI Coach Review)
slug: tutor-review
repo(s): plus-web-app
stub: 1
source: ari-map-probe
prod-commit: 29d41e50
goes-stale: TutorReviewServlet.java renamed, /PLUS/TutorReview URL mapping changed, TutorAiInsightItem schema change

## Identity
Tutor-facing AI-assisted review of coaching sessions with impact metrics and AI-generated insights for self-reflection.

## Entry points
/PLUS/TutorReview → TutorReviewServlet.java → jsp_pl2/tutor_review.jsp
(confirmed: web.xml:449, TutorReviewServlet.java exists, tutor_review.jsp exists)

## Primary data structure
not traced

---
Everything below is enriched by ari-port after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
not traced

## Client-side wiring
javascript/pl2/tutor_review/ (main.js, impact_section.js, ai_insights_section.js, time_allocation_section.js) — all ES modules

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
