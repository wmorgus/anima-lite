# Catch-Up: monthly-report port

## What this is

This PR ports the monthly-report feature from the plus-uno React prototype to the plus web-app production codebase. The feature is a structured monthly performance review page for PLUS tutors — showing impact stats, time allocation breakdown, and AI-generated growth insights with an interactive review flow. Five distinct claim changes were ported; each was confirmed by the product owner before implementation.

## Repo context

- **Proto** (plus-uno): Vite + React prototyping environment for the PLUS design system — exists to validate design hypotheses, not to ship production features. Code is disposable; design system conventions are not.
- **Prod** (plus web-app): Server-side Java web application (Spring/Hibernate/Tomcat 11). JSP + jQuery + Bootstrap. Session-authenticated, multi-tenant. Business logic goes through Service layer via ServiceFactory; no client-side framework.
- **Key translation constraint**: React component state (`useState`, `useEffect`, context) → server-side DTOs + jQuery DOM manipulation. Every piece of UI state that React held in memory now comes from a server round-trip. There is no client-side router, no component lifecycle — the page re-renders by re-fetching the JSON API and calling `renderPage(data)`.
- **Framework versions relevant to this PR**: Bootstrap **3/4** — `data-toggle`/`data-target` on the training collapse (`tutor_review.jsp:42`) is correct for this version. Bootstrap 5 would require `data-bs-toggle`/`data-bs-target`; do not flag `data-toggle` as wrong.
- **Diff base**: `29d41e50` (v11.3.0.4 for QA). `git diff 29d41e50..HEAD` shows all 5 claim commits on this branch.

## What changed and why

### Substrate (translate freely — no argument change)

- React JSX → JSP template + jQuery DOM manipulation — follows prod's server-rendered pattern
- Framer Motion entrance animations → removed — not available in prod stack; insight cards render on page load without animation; argument unchanged
- PLUS DS React components (Alert, Badge, Accordion, Progress) → Bootstrap equivalents (alert div, `plus-badge` class, Bootstrap collapse, inline progress fill) — follows prod's Bootstrap-based component pattern

### Claim changes (confirmed by user — argument is preserved)

**Claim 1 — Time Allocation section**
- Argument: Tutors see how they spent session time across 5 categories with a benchmark reference.
- Why it's a claim: The "40% Active Tutoring" benchmark figure is editorial — it asserts what good looks like. Changing it changes the argument the page makes to the tutor.
- Invariant: Benchmark text must render alongside the breakdown (`time_allocation_section.js:43`). Section must be present in the DOM (`tutor_review.jsp:36`). Fallback "No time allocation data available for this period." is valid when data is null.
- Old behavior: `#time-allocation-section` div was commented out in JSP. `renderTimeAllocationSection` import and call were commented out in `main.js`. `dto.setTimeAllocation(...)` was commented out in `TutorReviewDtoHelper.java`. Section simply did not appear on the page.
- Implementation:
  - `TutorReviewDto.java:31,59-60` — `timeAllocation` field + getter/setter uncommented
  - `TutorReviewDtoHelper.java:61` — `dto.setTimeAllocation(getTimeAllocationDto(...))` uncommented; full method block (was wrapped in `/* V1: ... */`) restored at lines 208–276
  - `applicationContext.xml:165` — `<value>edu/cmu/pl2/item/TutorTimeAllocation.hbm.xml</value>` uncommented (HBM mapping)
  - `applicationContext.xml:573` — `<bean id="tutorTimeAllocationService" ...>` uncommented
  - `applicationContext.xml:704` — `<entry key="edu.cmu.pl2.item.TutorTimeAllocationItem" value-ref="tutorTimeAllocationDao"/>` uncommented
  - `applicationContext.xml:1060` — `<bean id="tutorTimeAllocationDao" ...>` uncommented
  - `tutor_review.jsp:36` — `<div id="time-allocation-section">` uncommented
  - `main.js:6,131` — import + `renderTimeAllocationSection(data.timeAllocation)` call uncommented
  - `time_allocation_section.js:43` — "Benchmark: 40% Active Tutoring" added to header row (was "Total: 100%")

**Claim 2 — isHighImprovement adaptive mode**
- Argument: When a tutor has many areas for growth, the page focuses attention on one "Start Here" insight — all others are locked — and shows an encouraging growth banner.
- Why it's a claim: The lock-all-but-one pattern is an explicit editorial choice about presenting difficult feedback. Showing all insights as accessible would change what the page argues about how tutors should process hard feedback.
- Invariant: When `isHighImprovement=true`, growth banner must render above insight cards (`ai_insights_section.js:91`); every insight where `isStartHere=false` must be forced to locked state (`ai_insights_section.js:144`); training accordion must NOT auto-expand (`ai_insights_section.js:126` — `!isHighImprovement` gate).
- Old behavior: `renderAiInsightsSection` took 3 params `(insights, periodStart, periodEnd)`. No `isHighImprovement` param, no banner, no forced-lock logic. All insight cards rendered based solely on server-returned `status` field.
- Implementation:
  - `TutorReviewDto.java:34,62-63` — `isHighImprovement` boolean field + `isHighImprovement()` / `setHighImprovement()` (note: getter is `isHighImprovement()`, setter is `setHighImprovement()` — JavaBeans boolean convention)
  - `TutorReviewAiInsightDto.java:43,74-75` — `isStartHere` boolean field + `isStartHere()` / `setStartHere()`
  - `TutorReviewDtoHelper.java:62` — `dto.setHighImprovement(false)` stub; `TutorReviewDtoHelper.java:300` — `dto.setStartHere(false)` stub per insight
  - `ai_insights_section.js:35` — signature updated to `renderAiInsightsSection(insights, isHighImprovement, isLowData, periodStart, periodEnd)`
  - `ai_insights_section.js:91-97` — growth banner injected into container HTML when `isHighImprovement`
  - `ai_insights_section.js:144` — `const forcedLocked = isHighImprovement && !insight.isStartHere` — non-startHere insights get `effectiveStatus = "LOCKED"`
  - `main.js:133` — `renderAiInsightsSection(data.aiInsights, data.isHighImprovement, data.isLowData, ...)` — passes both new flags

**Claim 3 — isLowData empty state**
- Argument: When a tutor has fewer than 5 sessions, the page honestly states there isn't enough data rather than showing empty or partial insight cards.
- Why it's a claim: The 5-session threshold and specific message are editorial choices. "No insights" vs "limited data" are different arguments about what the product can and can't do.
- Invariant: When `isLowData=true`, the Alert-style empty state must render and the review progress bar must be hidden (`ai_insights_section.js:40-55` — early return before progress bar HTML is injected).
- Old behavior: Empty `insights` array showed the generic `<p class="body2-txt text-muted">No AI insights available for this period.</p>`. No distinct empty state, no message about session count, progress bar rendered unconditionally.
- Implementation:
  - `TutorReviewDto.java:37,65-66` — `isLowData` boolean field + `isLowData()` / `setLowData()`
  - `TutorReviewDtoHelper.java:63` — `dto.setLowData(false)` stub
  - `ai_insights_section.js:40-55` — `if (isLowData)` early return: renders Alert div with message, `return` before progress bar HTML block
  - `main.js:133` — `data.isLowData` passed to `renderAiInsightsSection` (same call as Claim 2)

**Claim 4 — Feedback text minimum (10+ trimmed characters for not_helpful/inaccurate)**
- Argument: Negative feedback requires a minimum explanation — the friction gate surfaces richer signal than a one-click thumbs-down.
- Why it's a claim: The 10-character threshold is a deliberate design decision about what counts as usable feedback signal.
- Invariant: For `not_helpful` or `inaccurate`, submit must be disabled until `textarea.value.trim().length >= 10` (`ai_insights_section.js:385-391`). The submit handler also guards with `trim()` (`ai_insights_section.js:397`) — both checks use trim, preventing whitespace bypass. Character count must display.
- Old behavior: Clicking Not Helpful or Inaccurate immediately called `submitFeedback(insightId, rating, "", true)` — no text input, no gate, empty string submitted as feedbackText.
- Implementation:
  - `ai_insights_section.js:349-405` — entire `if (rating === "not_helpful" || rating === "inaccurate")` branch in `attachFeedbackHandlers`. Buttons are disabled/highlighted, then a `feedbackWrapper` div is appended to the feedback section containing: label, textarea, char count span, Submit & Continue button (starts disabled).
  - Input listener at `ai_insights_section.js:384-393`: uses `textarea.value.trim().length` (not raw length) to update counter and toggle button
  - Submit handler at `ai_insights_section.js:396-399`: `const text = textarea.value.trim(); if (text.length < 10) return;` — double guard

**Claim 5 — Training accordion (collapsed by default, auto-expands after all insights reviewed)**
- Argument: Training is available but not forced — it appears collapsed and auto-expands only after all insights are reviewed in standard mode, rewarding completion.
- Why it's a claim: The auto-expand trigger enforces a sequence: insights first, then training. Removing the gate changes the argument.
- Invariant: Section must be in a Bootstrap collapse (`tutor_review.jsp:44`, `id="training-collapse"`); must auto-expand exactly when `reviewedCount === totalInsights && totalInsights > 0 && !isHighImprovement` (`ai_insights_section.js:126`); must NOT auto-expand in high-improvement mode.
- Old behavior: Training section did not exist. `training_section.js` is a new file. No collapse, no auto-expand trigger anywhere in the codebase.
- Implementation:
  - `tutor_review.jsp:41-47` — Bootstrap collapse shell: `#training-section` wrapper, `#training-section-header` toggle div (`data-toggle="collapse" data-target="#training-collapse"`), `#training-collapse` collapse div, `#training-cards-container` inner div
  - `training_section.js` (new file) — `renderTrainingSection(training)`: populates `#training-section-header` with heading + chevron, binds Bootstrap collapse events to rotate chevron, renders training cards into `#training-cards-container`; `exportTrainingAccordion()`: calls `$(collapseEl).collapse("show")`
  - `TutorReviewDto.java:43,71-72` — `recommendedTraining` list field + getter/setter
  - `TutorReviewTrainingCardDto.java` (new file) — DTO with `trainingId`, `title`, `duration`, `category`, `lessonUrl`
  - `TutorReviewDtoHelper.java:65,325-350` — `dto.setRecommendedTraining(getStubTraining())` + `getStubTraining()` method returning 3 hardcoded cards
  - `main.js:8,132` — import `renderTrainingSection` + call `renderTrainingSection(data.recommendedTraining)`
  - `ai_insights_section.js:4,126-127` — import `expandTrainingAccordion`; call it when all-reviewed condition met

## Deferred

- **Goal progress table**: Not ported — outside scope of this feature contract
- **Peer average time allocation**: Not rendered in proto render path — not a port item

## Blips

**review-suggested: New Java DTO fields not server-tested end-to-end**

The Java 17 enum syntax in `StudentsServlet.java` (pre-existing, unrelated to this port) blocks `ant deployAll`. Playwright validation was run by deploying JS/JSP files directly to webapps; server ran old compiled classes. This means `isHighImprovement`, `isLowData`, and `recommendedTraining` were not returned in the JSON API during testing — JS handles `undefined` as falsy, so the page rendered correctly in default state, but the Java→JSON→JS path for non-default values was not exercised.

**Reviewer action required**: Verify by inspection:
- `TutorReviewDto.java:34,37,43` — fields declared
- `TutorReviewDto.java:62-66,71-72` — getters/setters correctly formed (booleans use `isX()`/`setX()`)
- `TutorReviewDtoHelper.java:62-65` — all 3 stubs set
- `TutorReviewDtoHelper.java:300` — `setStartHere(false)` set per insight

Full end-to-end build + test is possible after the Java 17 enum PR merges (see separate PR for `StudentsServlet.java` + `StudentEdTechGoalService.java`).

## What to focus on in review

1. **Java DTO getter/setter naming** (`TutorReviewDto.java:62-66`) — Java boolean convention: getter is `isHighImprovement()`, setter is `setHighImprovement()` (not `setIsHighImprovement()`). JSON serialization depends on this. If wrong, Jackson won't serialize the field and JS receives `undefined`.

2. **Feedback whitespace bypass — both trim checks** (`ai_insights_section.js:385,397`) — input listener at :385 uses `textarea.value.trim().length`; submit handler at :397 uses `textarea.value.trim()`. Both must use `.trim()`. A raw `.length` on either one allows 10 spaces to enable or submit. Previously this was a CONTRACT-BREAK that required an explicit harness rule.

3. **Training auto-expand gate — all three conditions** (`ai_insights_section.js:126`) — condition is `reviewedCount === totalInsights && totalInsights > 0 && !isHighImprovement`. Missing `!isHighImprovement` violates Claim 2's invariant (accordion would auto-expand in high-improvement mode). Missing `totalInsights > 0` would fire on empty insight arrays.

4. **applicationContext.xml — all 4 uncomments** — verify all four are present (a partial uncomment causes Spring context load failure at startup, not a compile error):
   - `:165` HBM mapping `TutorTimeAllocation.hbm.xml`
   - `:573` bean `tutorTimeAllocationService`
   - `:704` DAO factory entry `TutorTimeAllocationItem`
   - `:1060` bean `tutorTimeAllocationDao`

## How to verify

**Dev server** (requires Java 17 enum PR to merge for full build):
```
docker start plus-mysql8
JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home \
  /opt/homebrew/opt/tomcat/libexec/bin/catalina.sh start
```
Login (bypasses Google OAuth): `http://localhost:8080/demo?pl2-demo-type=tutor&demo-category=toolkit`
Feature: `http://localhost:8080/PLUS/TutorReview`

**Claim 1 — Time allocation section**
Load the page. Between "Your Impact" and "Growth Insights", either: (a) Highcharts stacked bar chart with header showing "Benchmark: 40% Active Tutoring", or (b) fallback text "No time allocation data available for this period." Both pass. Absence of any visible content in `#time-allocation-section` = FAIL.

**Claim 2 — isHighImprovement** (not verifiable with stub data — `isHighImprovement=false` hardcoded)
To exercise: seed `isHighImprovement=true` on the DTO via a DB flag or temporary DtoHelper change. Expect: orange/green Alert banner appears above insight cards; all insights except the one with `isStartHere=true` show as "Locked"; training accordion does NOT auto-expand after reviewing the startHere insight.

**Claim 3 — isLowData** (not verifiable with stub data — `isLowData=false` hardcoded)
To exercise: set `isLowData=true` in DtoHelper temporarily. Expect: Growth Insights section shows "Limited data this month. We need at least 5 recorded sessions..." alert; no insight cards; no review progress bar.

**Claim 4 — Feedback text minimum**
Click "Not Helpful" on the first Under Review insight card. Verify:
1. Textarea appears with label "What's missing or off about this insight?"
2. Below textarea: "0/10 characters minimum"; Submit & Continue button disabled
3. Type "hello" (5 chars): counter shows "5/10 characters minimum"; button still disabled
4. Type 5 more chars (total 10+): counter switches to "10 characters" (or N characters); button enables
5. Clear the textarea: button must re-disable

**Claim 5 — Training accordion**
On page load: scroll to bottom — "Recommended Training" heading visible with chevron; no training cards visible (collapsed). Click the heading: training cards expand (3 cards: "Mastering Response to Help Requests", "Reacting to Errors", "Prompting Students to Explain"). Accordion does NOT auto-expand on load or before all insights are reviewed.
