# Execution Plan: weekly-report-demo
Contract: .anima-lite/contracts/main.md
Generated: 2026-07-01

## Claim changes

1. **Time allocation section** (Java + JSP + JS, 6 touch points)
   - `TutorReviewDto.java` — uncomment `timeAllocation` field + getter/setter
   - `TutorReviewDtoHelper.java` — uncomment import, method call in getTutorReviewDto, getTimeAllocationDto method, generateTimeAllocationSuggestion method; fix exception catch to set safe defaults
   - `applicationContext.xml` — uncomment 4 blocks: HBM mapping (line ~166), service bean (line ~575), DAO factory entry (line ~707), DAO bean (line ~1064)
   - `tutor_review.jsp` — uncomment `#time-allocation-section` div
   - `main.js` — uncomment import + renderTimeAllocationSection call
   - `time_allocation_section.js` — add benchmark note to section header

2. **Expand/collapse interaction model** (1 JS file)
   - `ai_insights_section.js` — add module-level `expandedInsightId`, auto-set on render, wrap card body in `.insight-card-body` div, `d-none` when not expanded, click handler on reviewed card headers with sibling-collapse

3. **AI attribution** — no change (keep prod disclaimer, confirmed)

4. **Impact hero card** (1 JS file)
   - `impact_section.js` — add hero card block above stat tiles: bolt icon, "Monthly Impact on Students", two placeholder metrics, trophy+dynamicInsight callout; remove insight callout from flat card section

## Substrate translations

- `impact_section.js` stat tile section — stays, just moves below hero card
- No other substrate changes require file edits (existing prod code already covers other substrate items)

## Order of operations

1. Java layer first (TutorReviewDto → DtoHelper → applicationContext.xml) — change together; each depends on the previous being correct
2. JSP + main.js — uncomment section div and JS call; depends on Java layer being wired
3. time_allocation_section.js — add benchmark note; independent of other changes
4. impact_section.js — hero card restructure; independent of time allocation changes
5. ai_insights_section.js — expand/collapse; most complex JS change, do last so other simpler changes are already verified

## Blockers

None identified. All infrastructure exists (dormant). All service/DAO/item classes for time allocation are present and already wired — just commented out.
