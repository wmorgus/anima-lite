# Blips: weekly-report
Branch: weekly-report
Generated: 2026-07-05

---

## Blip: SCSS lives in java/sass, not java/docroot/css-src
Severity: info
Location: /java/sass/monthly_report.scss — SCSS source directory is java/sass/, not java/docroot/css-src/ as the plan assumed
What happened: Plan named `java/docroot/css-src/weekly_report.scss` as the target path. Actual location for all SCSS is `java/sass/`. Created `java/sass/weekly_report.scss` instead.
Why: Following the discovered pattern from monthly_report.scss — substrate translation, file location is implementation detail.
Downstream consequence: JSP references compiled CSS at `/css/pl2/weekly_report.css` — Ant compiles from java/sass/ — same pattern as monthly_report.
Contracting failure?: n/a — plan gave a plausible guess; actual location required a quick find.

---

## Blip: web.xml is in java/docroot/conf-tomcat-11.0/, not java/WEB-INF/
Severity: info
Location: /java/docroot/conf-tomcat-11.0/web.xml — servlet registration file
What happened: Plan and prompt said `java/WEB-INF/web.xml`. Actual file is `java/docroot/conf-tomcat-11.0/web.xml`.
Why: Substrate — file location, same outcome.
Downstream consequence: WeeklyReportServlet registered in the correct file.
Contracting failure?: n/a — prompt gave a best-guess path; both are common Tomcat layouts.

---

## Blip: CLAIM-5 — View Recording button absent (recordingUrl not in DTO)
Severity: info
Location: weekly_report.js:buildCardBody — evidence quote rendered, no recording button
What happened: TutorAiInsightItem has no `recordingUrl` field. Contract says "conditionally hide if no URL." Since the field never exists, the condition is always false — button omitted entirely.
Why: Contract confirmed: "conditionally hidden if no recording URL is available in the DTO." The absence of the field means the condition is permanently false for now.
Downstream consequence: When/if `recordingUrl` is added to TutorAiInsightItem, a one-line addition to buildCardBody restores the button.
Contracting failure?: n/a — contract explicitly covered this case.

---

## Blip: CLAIM-7 — Get More Sessions CTA deferred (no scheduling destination in prod)
Severity: review-suggested
Location: weekly_report.jsp — no scheduling CTA section
What happened: Contract required ari-port to investigate whether a scheduling destination exists in prod. No scheduling servlet or endpoint was found that a "Get More Sessions" CTA could link to. Section omitted.
Why: Contract says "preserved by default, pending confirmation — investigate scheduling destination; if absent, log review-suggested blip and defer." Condition met.
Downstream consequence: Section absent from the port. Needs a prod scheduling URL before it can be wired in.
Contracting failure?: n/a — contract anticipated this outcome and prescribed the blip.

---

## Blip: CLAIM-1 pattern — REVIEWED cards non-interactive (substrate-treated)
Severity: info
Location: weekly_report.js:buildTimelineItem — REVIEWED cards have role=button but no feedback row
What happened: REVIEWED cards are rendered with the toggle-card click handler (so the user can re-read the insight) but the feedback buttons are not shown (status !== "under_review"). Server does not expose re-review from the UI.
Why: Contract says: "UI should reflect REVIEWED cards as non-interactive re: feedback submission. Whether the server allows status downgrade is an implementation detail — UI does not expose re-review."
Downstream consequence: Matches intent — REVIEWED cards are readable, not re-reviewable.
Contracting failure?: n/a — substrate-treated as specified.

---

## Blip: CLAIM-4 pattern — no optimistic UI advance (substrate-treated)
Severity: info
Location: weekly_report.js:submitFeedback — re-fetches server state after POST
What happened: Feedback submit POSTs, waits for response, then re-fetches full report data. No client-side optimistic advance. This matches monthly_report.js exactly.
Why: Contract recommends optimistic UI as an architecture decision but treats it as a substrate blip, not a confirmed claim. Following monthly_report.js precedent keeps the two features consistent.
Downstream consequence: Minor latency between feedback click and card advancing — acceptable for this tier.
Contracting failure?: n/a — substrate-treated as specified.

---

## Blip: claim logic committed with substrate (not held out separately)
Severity: info
Location: java/docroot/javascript/pl2/weekly_report.js — full detail page JS including feedback buttons and training lock
What happened: Plan staged claim-specific code (feedback buttons, training lock toggle, completion counts) for separate commits after the skeleton. In practice, the JS file is a single module — holding out CLAIM-2/3/8 logic would have required an inert skeleton with stubs, then a fill-in commit. Since the contract already confirmed all three claims, the full implementation was written in one pass and committed with the substrate. Claim commits below are confirmatory (no diff) — they mark the commit hash where each claim landed.
Why: All claims were pre-confirmed. Committing a broken skeleton then patching adds risk without benefit in this case.
Downstream consequence: Git log has three claim commits with no diff. The substrate commit c4725706 is where the claim code lives.
Contracting failure?: n/a — plan assumed staged skeleton; actual execution collapsed the gap cleanly.

---

## Blip: training-recommendations-stub — no data source connected
Severity: info
Location: weekly_report.js:renderTrainingPlaceholder — placeholder card rendered when training section unlocks
What happened: Training recommendations have no server-side data source. Placeholder card rendered ("Training recommendations coming soon") — identical to monthly_report.js pattern.
Why: Monthly report established this stub. No training data service exists to connect.
Downstream consequence: Training section unlocks correctly (CLAIM-3) but shows a stub card. Real recommendations require a future data sprint.
Contracting failure?: n/a — substrate-level stub, same as monthly report.

---

## Blip: CLAIM-7 resolved — scheduling CTA wired
Severity: info
Location: weekly_report.js (CTA render) + weekly_report.jsp (placeholder div)
What happened: "Get More Sessions" CTA links to /PLUS/TutorSchedule (TutorScheduleServlet Sign-Ups tab). Previously marked review-suggested/deferred; destination confirmed via codebase search.
Why: TutorScheduleServlet exists with a sign-ups tab for tutors to book additional sessions — exact destination the proto's CTA implied.
Downstream consequence: CLAIM-7 is now implemented. The motivational loop (review → reflect → schedule more) is complete.
Contracting failure?: Contract marked as "preserved by default, pending confirmation" — correct handling. No contracting failure.
