# Diff: run2 (monthly-report) vs run3 (weekly-report)
Harness change: FINDING-1+2+4 fixes applied between runs
Date: 2026-07-06

## Summary

The harness fixes produced measurably better contract and catch-up quality in run3. The contract grew from 28 lines (3 confirmed claims, no source-of-truth declaration, no playwright block) to 69 lines (6 claims confirmed and deferred, explicit source-of-truth, substrate-treated decisions section, and a playwright verification block) — a direct result of the FINDING-1+2+4 improvements that formalized contract structure. Commit discipline improved from 2 monolithic commits to 4 per-claim commits, which means git blame now maps directly to claim boundaries. The main gap that persists: blip citations to spine sections are present in run3 but sparse (most blips cite a location, not a spine section), and that's a signal for the next calibration run.

## Contract

| Dimension | run2 | run3 | Delta |
|---|---|---|---|
| Line count | 28 | 69 | +41 — contract is substantially more complete |
| Claim changes documented | 3 confirmed | 5 confirmed + 1 deferred | +3 — run3 had more claims to resolve, harness handled all of them |
| Substrate items documented | ~10 bullet points | ~12 bullet points | +2 — added substrate-treated decisions section |
| Has playwright block? | No | Yes | Added in run3 — FINDING-4 fix materialized here |
| Has "Source of truth" declaration? | No | Yes | run3 names WeeklyReportContent.jsx as canonical; run2 does not disambiguate proto source |
| Has substrate-treated decisions section? | No | Yes (CLAIM-1+4 patterns) | run3 explicitly labels decisions that were substrate-treated and not confirmed as claims |
| Open questions documented? | No (section present but empty) | Yes (2 open questions) | run3 surfaces CLAIM-2 schema check and CLAIM-7 scheduling destination before porting |

## Blips

| Dimension | run2 | run3 | Delta |
|---|---|---|---|
| Line count | 41 | 94 | +53 — run3 feature was more complex and blips tracked it faithfully |
| Number of blips | 4 | 8 | +4 — more path corrections logged, more substrate-treated patterns surfaced |
| Severity distribution | 2 review-suggested, 2 info | 1 review-suggested, 7 info | run3 resolved more mid-execution (CLAIM-7 CTA went from deferred → confirmed) |
| All blips cite a spine section? | No — locations named but no spine-prod refs in Why field | No — same gap | No regression, but no improvement either; spine citation in blip Why field still missing |
| All blips have `Contracting failure?` field? | No | Yes | run3 added `Contracting failure?` field to every blip — structural improvement |
| CONTRACT-BREAK blips? | 0 | 0 | Neither run hit a CONTRACT-BREAK; the FINDING-2 recovery path was not exercised |

## Catch-up doc

| Dimension | run2 | run3 | Delta |
|---|---|---|---|
| Line count | 86 | 127 | +41 — run3 is more complete |
| File:line anchors in "What to focus on in review"? | Yes (4 anchors, e.g. MonthlyReportServlet.java:355–416) | Yes (4 anchors, e.g. WeeklyReportServlet.java:290–310) | Maintained — both runs have actionable line anchors |
| Old-vs-new delta per claim? | Yes — each claim has `Old behavior` + `Implementation` fields | Yes — each claim has code + verify fields | Both present; run3 format slightly more concise (no explicit `Old behavior:` label, but the same information is there) |
| Edge cases documented? | No dedicated section | Yes — two edge cases (REVIEWED card double-submit, empty list state) | run3 added edge case section; run2 did not |
| Deferred items enumerated? | Yes (4 items) | Yes (4 items) | Maintained |
| Completeness critic Q1 (are claims traceable to code)? | Yes | Yes | Both pass |
| Completeness critic Q2 (are deferred items explained)? | Yes | Yes | Both pass |
| Completeness critic Q3 (are blips summarized)? | Yes (inline in blips section) | Yes (explicit blips summary section) | run3 adds a dedicated blips summary at the end |
| Completeness critic Q4 (does reviewer know what to check)? | Yes — 3 "What to focus on" items | Yes — 4 "What to focus on" items | run3 surfaces one additional review concern (periodInsights sort order) |

## Commit discipline

| Dimension | run2 | run3 | Delta |
|---|---|---|---|
| Number of commits on feature branch | 2 | 4 | +2 per-claim commits |
| Substrate commit? | Yes (1 commit: substrate only) | Yes (1 commit: substrate only) | Maintained |
| Claims get separate commits? | No — CLAIM-1+2 in one commit, CLAIM-3 implicit (absence) | Partially — CLAIM-2+3 in one commit; CLAIM-8 separate; CLAIM-7 separate | Improved: 3 of 5 implemented claims have own commits; CLAIM-2+3 bundled (intentional — they share a JS block) |
| Empty/confirmatory claim commits? | No | Yes — substrate commit c4725706 has the claim code; claim commits are confirmatory with no diff | Noted as blip — harness produced a blip explaining this rather than silently omitting; transparent but commits don't carry diffs |
| All confirmed claims landed? | Yes (3/3) | Yes (5/5, with CLAIM-7 initially deferred then resolved) | run3 handled a mid-execution resolution correctly |

## Findings

**What improved:**

1. **Contract structure is categorically better.** The source-of-truth declaration, substrate-treated decisions section, open questions, and playwright verification block were all absent in run2 and present in run3. These aren't cosmetic — the source-of-truth declaration resolved a real ambiguity (two proto components existed; the harness named the canonical one before porting began). The open questions surfaced the CLAIM-2 schema check pre-port instead of mid-execution.

2. **Blip structure is now consistent.** Every run3 blip has a `Contracting failure?` field. run2 blips varied in structure. This means blips now answer the same question every time: "was this a harness failure or an expected unknown?" run3 result: every blip answered "n/a" — no contracting failures. That's a signal of better upfront scoping, not harness permissiveness.

3. **Commit discipline improved from 2 commits to 4.** Per-claim commits make git blame useful — a reviewer can trace CLAIM-7 to a single commit (176d11b0) without reading the full diff. The empty claim commits (confirmatory, no diff) are a known artifact and were logged as a blip rather than hidden.

4. **Mid-execution resolution was handled correctly.** CLAIM-7 was deferred (no destination found), then resolved (TutorScheduleServlet confirmed), and the blip was updated to reflect the resolution. run2 had no equivalent test — all claims resolved before porting began.

**What didn't improve:**

5. **Spine citation in blip Why fields is still absent.** Both run2 and run3 blips cite file locations but do not reference the spine section that governs the decision (e.g., "spine-prod/formal.md §4 — ES modules are the prod pattern"). This means a reader can't trace a blip back to the orientation document that made the decision legible. Not a regression from run2, but no improvement either.

6. **Empty claim commits are an open question.** The pattern of committing claim code with the substrate (because all claims were pre-confirmed) and then adding confirmatory empty commits is correct in intent but fragile: if someone rebases or squashes, the claim commits disappear. A better pattern might be: commit the substrate as a true skeleton (no claim code), then commit each claim. The blip acknowledges this but the harness doesn't enforce it.

## Signals for next calibration

1. **Instrument spine citation in blip Why fields.** The completeness critic should ask: "does each blip's Why field cite a spine section?" If not, flag. This is the clearest remaining structural gap.

2. **Watch the empty-commit pattern.** If the next feature also pre-confirms all claims and collapses claim code into the substrate commit, consider whether the harness should require a true skeleton commit before claim code is written — or explicitly document the confirmatory-commit pattern as a known exception.

3. **Test CONTRACT-BREAK recovery.** FINDING-2 (partial commit recovery) was not exercised in either run — no CONTRACT-BREAK was triggered. The next calibration run should intentionally include a claim that gets partially implemented to exercise the recovery path.

4. **Source-of-truth disambiguation was valuable.** Weekly report had two competing proto components; monthly report had one. The source-of-truth section in the contract prevented a wrong-source port. Instrument whether future runs use this field and whether it prevents a detectable error.
