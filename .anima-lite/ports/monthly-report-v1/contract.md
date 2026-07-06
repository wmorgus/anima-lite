# Contract: monthly-report → plus web-app
Branch: monthly-report
Port date: 2026-07-01
Proto source: plus-uno/playground/monthly-report/src/MonthlyReportContent.jsx
Prod target: tutor_review feature (tutor_review.jsp + tutor_review/*.js + Java layer)

---

## Claim changes (confirmed by user, 2026-07-01)

### Claim 1: Time Allocation section
**Proto argument**: Tutors see how they spent session time across 5 categories with a benchmark reference.
**Prod argument**: Same argument, same benchmark (40% Active Tutoring).
**Why it's a claim**: The benchmark figure ("40% Active Tutoring") is an editorial assertion, not substrate.
**Invariant**: Benchmark text must be rendered alongside the breakdown.
**Implementation**:
- Uncomment `TutorReviewDto.java`: timeAllocation field + getter/setter
- Uncomment `TutorReviewDtoHelper.java`: `getTimeAllocationDto()` call + methods; exception catch → safe defaults (0.0/0/null)
- Uncomment `applicationContext.xml`: HBM mapping (~line 166), service bean (~line 575), DAO factory entry (~line 707), DAO bean (~line 1064)
- Uncomment `tutor_review.jsp`: `#time-allocation-section` div
- Uncomment `main.js`: import + `renderTimeAllocationSection(data.timeAllocation)` call
- Add benchmark note to `time_allocation_section.js`: header row with "Benchmark: 40% Active Tutoring"

### Claim 2: isHighImprovement adaptive mode
**Proto argument**: When a tutor has many areas for growth, the page focuses attention on one "Start Here" insight — all others are locked — and shows an encouraging growth banner.
**Prod argument**: Same argument, same focus mechanism.
**Why it's a claim**: The lock-all-but-one pattern is an explicit editorial choice about how to present difficult feedback. Changing it would change the argument.
**Invariant**: In high improvement mode, every insight except the one marked `isStartHere=true` must be locked; training must filter to that insight's training only; training accordion must NOT auto-expand.
**Implementation**:
- `TutorReviewDto.java`: add `isHighImprovement` boolean field + getter/setter
- `TutorReviewDtoHelper.java`: set `isHighImprovement` (stub: false, real logic separate)
- `TutorReviewAiInsightDto.java` (or check existing): add `isStartHere` boolean field + getter/setter
- `ai_insights_section.js`: accept `isHighImprovement` param; render growth banner (Alert-style div) when true; lock all non-isStartHere insights in createInsightCard; pass isHighImprovement to training auto-expand logic
- Growth banner text: "This month has several areas for development. Remember, growth takes time and practice — let's focus on one skill at a time. Start with the insight marked 'Start Here' below."
- "Start Here" badge on the startHere insight card header

### Claim 3: isLowData empty state
**Proto argument**: When a tutor has fewer than 5 sessions, the page honestly states there isn't enough data for meaningful insights rather than showing empty or partial data.
**Prod argument**: Same argument.
**Why it's a claim**: The threshold (5 sessions) and the specific message are editorial choices.
**Invariant**: When `isLowData=true`, the growth insights section must show the empty state message; review progress bar must be hidden.
**Implementation**:
- `TutorReviewDto.java`: add `isLowData` boolean field + getter/setter
- `TutorReviewDtoHelper.java`: set `isLowData` (stub: false, real logic separate)
- `ai_insights_section.js`: check `isLowData`; when true render Alert-style empty state: "Limited data this month. We need at least 5 recorded sessions to generate personalized growth insights. Keep up the great work, and we'll have more detailed feedback for you next month!"; hide review progress bar
- `main.js`: pass `data.isLowData` to `renderAiInsightsSection`

### Claim 4: Feedback text minimum (10+ characters for not_helpful/inaccurate)
**Proto argument**: Negative feedback (not helpful or inaccurate) requires a minimum 10-character explanation — requiring it creates a friction gate that surfaces richer signal.
**Prod argument**: Same argument; same threshold; same character count display.
**Why it's a claim**: The 10-character threshold is an explicit design decision about what counts as usable feedback signal.
**Invariant**: When not_helpful or inaccurate is selected, the submit button must be disabled until feedbackText.length >= 10; character count must be displayed.
**Implementation**:
- `ai_insights_section.js`: modify `attachFeedbackHandlers` — for not_helpful/inaccurate, do NOT call `submitFeedback` immediately; instead show a text input below the buttons; disable submit until input.length >= 10; display character count (e.g. "3/10 characters minimum" when < 10, "12 characters" when >= 10); on submit → call `submitFeedback(insightId, rating, feedbackText, true)`
- For "helpful" → submit immediately (unchanged behavior)

### Claim 5: Training section in Bootstrap collapse (auto-expand after all reviewed, standard mode only)
**Proto argument**: Training recommendations are available but not forced on the tutor — they appear in a collapsed accordion that auto-expands only after all insights have been reviewed (in standard mode), rewarding completion with the next step.
**Prod argument**: Same argument; same trigger (all reviewed, standard mode only).
**Why it's a claim**: The auto-expand-after-all-reviewed behavior is an editorial choice about the learning flow — it enforces a sequence.
**Invariant**: Training section must be in a Bootstrap collapse; must auto-expand exactly when `reviewedCount === totalInsights && totalInsights > 0 && !isHighImprovement`; must NOT auto-expand in high improvement mode.
**Implementation**:
- `tutor_review.jsp`: add `#training-section` div + Bootstrap collapse structure
- New `training_section.js`: `renderTrainingSection(training, isHighImprovement)` — renders training cards; `expandTrainingAccordion()` — programmatically shows the Bootstrap collapse
- `TutorReviewDto.java`: add `recommendedTraining` list of `TutorReviewTrainingCardDto` (inner class or separate file with: trainingId, title, duration, category, lessonUrl)
- `TutorReviewDtoHelper.java`: populate stub training list
- `main.js`: import + call `renderTrainingSection(data.recommendedTraining, data.isHighImprovement)`
- `ai_insights_section.js`: on all-insights-reviewed (and !isHighImprovement) → call `expandTrainingAccordion()` from training_section.js

---

## Deferred

- **Goal progress table**: Not ported. goalProgress data and UI not added to prod.
- **Peer average time allocation**: Not in proto render path (data exists but not rendered) — not a port item.

---

## Not a claim change

- **AI attribution**: Prod reads "The growth insights are generated by AI, which may make mistakes!" (with AI icon). Proto reads "Powered by PLUS AI Coach." User confirmed in prior run: keep prod disclaimer. No code change.
- **Animation entrance sequences**: Substrate. CSS/JS animate → no animation on static page load. Argument unchanged.
- **React components → Bootstrap/jQuery**: Substrate. Translation, not claim change.
- **Client-side state → server-backed**: Substrate. Architecture difference; insight status comes from DTO/server.

---

## Playwright verification

login_url: http://localhost:8080/demo?pl2-demo-type=tutor&demo-category=toolkit
feature_url: http://localhost:8080/PLUS/TutorReview

checks:
  - claim: "Claim 1 — time allocation section"
    steps: "Observe the page after load"
    expect: "A section between 'Your Impact' and 'Growth Insights' renders — either the Highcharts stacked bar breakdown with 'Benchmark: 40% Active Tutoring' in the header, or the fallback 'No time allocation data available for this period.' Both are valid; absence of any #time-allocation-section content is a FAIL"

  - claim: "Claim 2 — isHighImprovement growth banner"
    steps: "Observe the Growth Insights section header area"
    expect: "When isHighImprovement=true on the DTO, a banner reading 'This month has several areas for development...' appears above the insight cards, and all insights except the one with isStartHere=true show as Locked. With stub data (isHighImprovement=false) this check is n/a — note as info blip"

  - claim: "Claim 3 — isLowData empty state"
    steps: "Observe the Growth Insights section"
    expect: "When isLowData=true, the section shows 'Limited data this month. We need at least 5 recorded sessions...' with no insight cards and no review progress bar. With stub data (isLowData=false) this check is n/a — note as info blip"

  - claim: "Claim 4 — feedback text minimum"
    steps: "Click the 'Not Helpful' button on the first insight card (Under Review)"
    expect: "A textarea appears labelled \"What's missing or off about this insight?\"; below it shows '0/10 characters minimum'; the Submit & Continue button is disabled. Type 5 characters and verify count updates to '5/10 characters minimum' and button remains disabled. Type 10+ characters and verify button becomes enabled."

  - claim: "Claim 5 — training accordion (collapsed by default)"
    steps: "Scroll to the bottom of the page and observe the Recommended Training section"
    expect: "A 'Recommended Training' header with a chevron is visible and the training cards are collapsed (not visible) by default. Click the header and verify training cards expand."

setup_notes: |
  Dev server: Tomcat 11 at localhost:8080
  Start sequence: docker start plus-mysql8 && JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home /opt/homebrew/opt/tomcat/libexec/bin/catalina.sh start
  Demo login creates a session as advisor_id=2 (Demo Tutor) with 2 stub AI insights for June 2026.
  isHighImprovement and isLowData are both false on stub data — Claims 2 and 3 visual checks are n/a unless DB is seeded with those flags set.
