# Blips: monthly-report → plus web-app
Branch: monthly-report
Port date: 2026-07-01
Contract: .anima-lite/contracts/monthly-report.md

---

## Blip: Java 17 enum syntax in StudentsServlet.java blocks ant build
Severity: info
Location: java/source/edu/cmu/pl2/servlet/StudentsServlet.java (and StudentEdTechGoalService.java)
What happened: `ant deployAll` fails compilation — `case EdTechName.IXL:` style is illegal in Java 17 (unqualified enum name required). These files are unrelated to the monthly-report port. Playwright validation was done by deploying JS/JSP files directly to webapps, bypassing the Java compile step. Server ran on old compiled classes.
Why: Java 17 requires `case IXL:` not `case EdTechName.IXL:`. This is a pre-existing issue in the repo, not introduced by this port.
Downstream consequence: The enum fix must be a separate PR before this port can be validated end-to-end with a full build. The new Java DTO fields (isHighImprovement, isLowData, recommendedTraining) were not exercised server-side in Playwright testing.
Contracting failure?: n/a — genuinely unforeseeable in ari-port context; the Java 17 issue predates this feature.

---

## Blip: New Java DTO fields not server-tested (server ran old compiled classes)
Severity: review-suggested
Location: java/source/edu/cmu/pl2/dto/TutorReviewDto.java, TutorReviewDtoHelper.java, TutorReviewAiInsightDto.java
What happened: Because ant deployAll failed (see previous blip), Playwright tests ran against old compiled classes. The server returned JSON without isHighImprovement, isLowData, or recommendedTraining fields. JS code handled undefined gracefully (treated as falsy/null). Playwright checks that depend on these fields (Claims 2 and 3) are marked n/a per contract (stub data = false anyway), but the end-to-end Java→JSON→JS path was not exercised.
Why: Enum syntax error in unrelated servlet blocked compilation.
Downstream consequence: Reviewer should verify the Java layer (DTO fields, getters/setters, DtoHelper stub logic) by inspection, and run a full build after the enum syntax PR merges.
Contracting failure?: Contract should note the Java 17 enum incompatibility as a known blocker — the enum fix is a prerequisite for a full build. Contracting failure?: partial — the enum issue was known from the previous run but not surfaced in this contract.

---

## Blip: isHighImprovement parameter accepted but vestigial in renderTrainingSection
Severity: info
Location: java/docroot/javascript/pl2/tutor_review/training_section.js
What happened: renderTrainingSection was originally designed to accept isHighImprovement as a second parameter. The final implementation does not use it — the parameter was removed from the function signature. The auto-expand guard lives in ai_insights_section.js (correct per contract).
Why: During implementation it became clear the training section itself doesn't need to know the mode — it just renders cards. The caller (ai_insights_section.js) handles the mode gate.
Downstream consequence: None. main.js no longer passes isHighImprovement to renderTrainingSection.
Contracting failure?: n/a — contract places auto-expand guard in ai_insights_section.js, correctly implemented.
