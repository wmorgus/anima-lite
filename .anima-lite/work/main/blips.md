# Blips: weekly-report-demo → plus web-app (run 3)
Branch: main
Port date: 2026-07-01
Contract: .anima-lite/contracts/main.md

---

## Blip: totalStudentLearningTime and conceptsMastered render as "--"
Severity: info
Location: TutorReviewDtoHelper.java:189-190, impact_section.js hero card
What happened: Hero card ported and visible. Two primary metrics display "--" — DTO fields exist but are hardcoded placeholders in DtoHelper.
Why: No service layer populates learning time or mastery data yet.
Downstream consequence: Hero card renders correct structure; primary numbers are dashes. All other impact data is real.
Contracting failure?: n/a — contract explicitly noted these are placeholders; data population is separate work.

---

## Blip: insight-card-header--clickable has no cursor CSS
Severity: info
Location: ai_insights_section.js, tutor_review.css
What happened: Reviewed card headers get class `insight-card-header--clickable` and `role="button"` but no `cursor: pointer` CSS exists for that class.
Why: New CSS class; no SCSS source edited in this port.
Downstream consequence: Toggle is functional; clickability affordance missing visually.
Contracting failure?: n/a — CSS affordance is substrate. Expand/collapse behavior (the claim) is implemented correctly.

---

## Session summary

Claim changes exercised: 3 of 4 (AI attribution kept as prod disclaimer — no code change required)
- Time allocation: PORTED — DTO, DtoHelper (with safe exception defaults), applicationContext.xml (4 blocks), JSP, main.js, time_allocation_section.js with benchmark note
- Expand/collapse one-at-a-time: PORTED — module-level expandedInsightId, auto-expand on UNDER_REVIEW, body wrapped in insight-card-body, reviewed card header toggles with sibling-collapse
- AI attribution: KEPT PROD DISCLAIMER — no change (confirmed)
- Impact hero card: PORTED — hero block above stat tiles with bolt icon, placeholder metrics, trophy callout

Blips by severity:
- info: 2
- review-suggested: 0
- CONTRACT-BREAK: 0
