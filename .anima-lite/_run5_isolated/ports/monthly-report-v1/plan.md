# Execution Plan: monthly-report → plus web-app
Branch: monthly-report
Contract: .anima-lite/contracts/monthly-report.md

---

## Step 1 — Java layer (Claim 1, 2, 3, 5)

### 1a. TutorReviewDto.java
- Uncomment `timeAllocation` field + getter/setter (Claim 1)
- Add `isHighImprovement` boolean + getter/setter (Claim 2)
- Add `isLowData` boolean + getter/setter (Claim 3)
- Add `recommendedTraining` List<TutorReviewTrainingCardDto> + getter/setter (Claim 5)
- Add static inner class `TutorReviewTrainingCardDto` with: trainingId, title, duration, category, lessonUrl (Claim 5)

### 1b. TutorReviewAiInsightDto.java
- Add `isStartHere` boolean + getter/setter (Claim 2: needed to mark the focus insight in high-improvement mode)

### 1c. TutorReviewDtoHelper.java
- Uncomment timeAllocation: call `getTimeAllocationDto()`, include try/catch with safe defaults (Claim 1)
- Set `dto.setIsHighImprovement(false)` — stub (Claim 2; real logic is backend concern, stub keeps schema consistent)
- Set `dto.setIsLowData(false)` — stub (Claim 3)
- Set stub `recommendedTraining` list with one training entry (Claim 5)

### 1d. applicationContext.xml
- Uncomment HBM mapping block (~line 166) for TutorReviewTimeAllocation (Claim 1)
- Uncomment service bean (~line 575) for TutorReviewTimeAllocationService (Claim 1)
- Uncomment DAO factory entry (~line 707) (Claim 1)
- Uncomment DAO bean (~line 1064) for TutorReviewTimeAllocationDaoHibernate (Claim 1)

---

## Step 2 — JSP (Claims 1, 5)

### 2a. tutor_review.jsp
- Uncomment `#time-allocation-section` div (Claim 1)
- Add `#training-section` div after ai-insights-section (Claim 5)

---

## Step 3 — JavaScript layer (Claims 1, 2, 3, 4, 5)

### 3a. time_allocation_section.js
- Add benchmark note to section header: `<span class="body3-txt text-muted">Benchmark: 40% Active Tutoring</span>` in a flex header row alongside the section title (Claim 1)

### 3b. New training_section.js
- `renderTrainingSection(training, isHighImprovement)`: renders training cards inside a Bootstrap collapse `#training-collapse`; renders nothing (empties container) if training is null/empty (Claim 5)
- `expandTrainingAccordion()`: programmatically calls Bootstrap `.collapse('show')` on `#training-collapse` (Claim 5)
- Training card structure: Bootstrap card layout with title, category badge, duration, "Start" link (substrate — adapts RecommendedLessons DS component to Bootstrap equivalent)

### 3c. ai_insights_section.js
- Change `renderAiInsightsSection(insights, periodStart, periodEnd)` signature → `renderAiInsightsSection(insights, isHighImprovement, isLowData, periodStart, periodEnd)` (Claims 2, 3)
- isLowData branch: render Alert-style div with empty-state message; hide review progress bar (Claim 3)
- isHighImprovement branch: render growth banner div above insight cards (Claim 2)
- Growth banner text: "This month has several areas for development. Remember, growth takes time and practice — let's focus on one skill at a time. Start with the insight marked 'Start Here' below."
- `createInsightCard`: when `isHighImprovement && !insight.isStartHere` → render as locked (Claim 2)
- When `insight.isStartHere` → add "Start Here" badge in card header (Claim 2)
- `attachFeedbackHandlers`: for not_helpful/inaccurate → do NOT submit immediately; instead show text input + character count + submit button disabled until length >= 10; on submit → call submitFeedback with text (Claim 4)
- On all-insights-reviewed callback (standard mode only): call `expandTrainingAccordion()` from training_section.js (Claim 5)

### 3d. main.js
- Import renderTimeAllocationSection from time_allocation_section.js (Claim 1)
- Import renderTrainingSection from training_section.js (Claim 5)
- `renderPage(data)`: call `renderTimeAllocationSection(data.timeAllocation)` (Claim 1)
- `renderPage(data)`: call `renderAiInsightsSection(data.aiInsights, data.isHighImprovement, data.isLowData, periodStart, periodEnd)` (Claims 2, 3)
- `renderPage(data)`: call `renderTrainingSection(data.recommendedTraining, data.isHighImprovement)` (Claim 5)

---

## Validation criteria (per contract)

1. Claim implementation: all 5 claims exercised, each invariant satisfied
2. Blip classification quality: n/a misclassification = FAIL; substrate-vs-claim calls correct
3. Blip severity routing: CONTRACT-BREAK only for invariant violations; review-suggested for quality concerns; info for expected gaps with no argument impact
