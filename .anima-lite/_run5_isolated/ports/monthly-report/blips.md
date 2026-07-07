# Blips: Monthly Report port

## Blip: session-metrics-stub
Severity: review-suggested
Location: MonthlyReportServlet.java:193–196
What happened: `studentCount`, `learningTimeMin`, and `skillsMastered` are stubbed as -1 in the JSON response. The JS renders "—" for these fields in the UI.
Why: No confirmed single-pass aggregation service exists for student count per tutor per period, or for student learning time / skills mastered. TutorSessionService provides `findByAdvisorSortedBetweenDates` which yields session count, hours, and school count — those three are real data. The other three require additional queries against StudentSessionAssignment or skill mastery tables, which were not confirmed in the prod codebase during this probe.
Downstream consequence: Three metric cells in the Impact section display "—" rather than real numbers. The section still renders; it is not broken. Real values require a follow-up service method or HQL query.
Contracting failure?: Partially — the contract listed "session metrics (sessions, hours, students, schools) via TutorSessionService" as substrate but did not distinguish which aggregations exist vs. which would need new infrastructure. A more specific contract would have enumerated which metrics were confirmed vs. stubbed, placing the stub decision at ari-argue rather than mid-execution.

## Blip: training-recommendations-stub
Severity: review-suggested
Location: monthly_report.js:199–207 (renderTrainingPlaceholder)
What happened: Training recommendations section renders a placeholder card rather than real training data. No confirmed prod data source for per-tutor training recommendations tied to monthly insight results.
Why: Proto used hardcoded `RecommendedLessons` components with mock data. Prod has a lesson system (`LessonServlet`, lesson JSON files) but no service method confirmed that maps insight dimensions to specific lesson recommendations. Connecting this would require a new recommendation mapping layer.
Downstream consequence: Training section unlocks after all insights are reviewed (correct behavior per the gate claim), but displays placeholder content rather than real recommendations.
Contracting failure?: Yes — training recommendations are a distinct data problem from the progressive disclosure claim. The contract should have noted whether training recommendations would be real or stubbed, and confirmed that scope boundary with the user.

## Blip: time-allocation-section-omitted
Severity: info
Location: monthly_report.jsp, monthly_report.js
What happened: Time allocation section (progress bar breakdown of Active Tutoring / Goal Setting / etc.) is not rendered. JSP has no time-allocation-section element; JS has no time allocation logic.
Why: Proto's time allocation data is mock. No confirmed DB source for session activity breakdown (Active Tutoring / Goal Setting / Observing / etc.) was found in prod. Including it as a stub with fake percentages would mislead reviewers.
Downstream consequence: Monthly report detail page shows header + impact stats + growth insights + training. Time allocation section absent. Can be added when the data source (session activity tracking) is built.
Contracting failure?: n/a — genuinely unforeseeable; time allocation as a distinct DB concern wasn't surfaced during ari-argue.

## Blip: pl2userlogger-view-monthly-report-constant
Severity: info
Location: PL2UserLogger.java:404, 572
What happened: Added `VIEW_MONTHLY_REPORT = "View Monthly Report"` constant and registered it in `ACTIONS_USE_NEXT_TIME`. Standard pattern from `VIEW_TUTOR_REVIEW`.
Why: PL2UserLogger.log() requires the action string to be a registered constant. Modified PL2UserLogger.java to add the new constant — this is a shared utility file not specific to this feature.
Downstream consequence: Minimal. PL2UserLogger validates against the registered list; without registration the log call would fail at runtime. Standard extension of an existing registry.
Contracting failure?: n/a — standard prod convention for any new page-load event.

## Blip: es-module-import-plus-interface
Severity: info
Location: monthly_report.js:13
What happened: monthly_report.js imports `PlusInterface` from `./plus_components/general_interface.js` following the prod ES module pattern. Import is present but not currently invoked (structure mirrors tutor_review/main.js pattern for future use).
Why: Prod formal cause (FINDING-3, corrected): ES modules are the standard for feature-level JS. plus_components/ provides shared utilities. Import follows the established pattern even though PlusInterface is not called in V1.
Downstream consequence: Unused import. Can be removed if PlusInterface is never needed, or used to show error toasts, handle auth redirects, etc.
Contracting failure?: n/a — substrate translation judgment.
