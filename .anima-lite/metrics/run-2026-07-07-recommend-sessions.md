# Run: recommend-sessions
Run ID: run-2026-07-07-recommend-sessions
Date: 2026-07-07
Prod repo: plus web-app — dev(29d41e50)..anima-lite-recommend-sessions(382b6039)
Calibration run: calibration-run-4

## Gate table
| Gate ID | Status | Outcome |
|---|---|---|
| GATE-TELOS | fired | Fired on the ORIGINAL run4 target tutor-reflection-form (proto redesign overlapped a live, 6-yr-maintained native prod feature; caught before any code moved → feature dropped). Passed clean (compatible-new) on the actual ported feature recommend-sessions. |
| GATE-HASH | fired | Proto contract hash 9c02f5e8 matched spine-proto (clean); spine-prod was stale (90e0ff79 vs dev 29d41e50) and was refreshed via ari-map before ari-argue. |
| GATE-BLOCKERS | fired | Plan surfaced a blocker: "subject" field assumed by CLAIM-2 does not exist in prod schema; cleared with user (subject dropped from rank). |
| GATE-BREAK | fired | CONTRACT-BREAK during execution (open-slots has no backing prod data). Anomaly: the execution subagent did NOT halt as ari-port mandates — it self-narrowed the claim and continued; the driver caught it in independent review and surfaced it to the user, who ratified. This is run4's key finding — see PIN-20. |
| GATE-BLIPS | fired | Validation returned PASS-pending; 2 review-suggested blips acknowledged. |
| GATE-PR | skipped | User declined the PR/catch-up this run (tuning-only run). |
| GATE-SPINE-REVIEW | skipped | Optional; spine-prod auto-refreshed, no explicit review requested. |
| GATE-PLAN-REVIEW | skipped | Optional; not requested. |
| GATE-CATCHUP-REVIEW | n/a | No catch-up doc produced this run. |
| GATE-PIN-CLAIM | n/a | No backlog sweep this run. |

## Blip distribution
- info: 2
- review-suggested: 1
- CONTRACT-BREAK: 1
- Blips with `Contracting failure?` ≠ n/a: 1

## Validation
Result: PASS-pending (2 review-suggested acknowledged). Static-review-only — no runtime/compile: environment is JDK 11, codebase needs JDK 17 (`ant compile` fails on class-file version), no Tomcat/browser so no Playwright per playwright-spec. Ran: `npx sass` compile ✓, `node --check` ✓, full static diff-review against mirrored prod patterns.

## Pipeline events
- Spine refresh triggered: y — spine-prod refreshed (stale 90e0ff79 → dev 29d41e50; monthly/weekly port artifacts correctly absent from dev).
- Contract amendments: 3 edits across 2 distinct data-gap causes — subject dropped (pre-execution, GATE-BLOCKERS); open-slots dropped from CLAIM-2 rank and from CLAIM-4 display (mid-execution, GATE-BREAK, ratified).
- CONTRACT-BREAKs: 1 (open-slots).
- Commit discipline: substrate commits: 1, claim commits: 4, empty claim commits: 0 (0 expected) ✓ — INDEPENDENTLY VERIFIED by the driver (substrate commit d7107f93 inspected in isolation: stubs only, no rank/gate/persist/withhold logic). This is the run3→run4 improvement: run3 collapsed all claim logic into the substrate commit; run4 held clean separation on a harder port (969 insertions, full 7-part Java/Hibernate entity stack).

## Phase table
| Phase | Subagent invocations | Model tier(s) | Reasoning/effort setting | Subagent tokens | Duration |
|---|---|---|---|---|---|
| ari-map | 1 | sonnet | ambient — not traced | 66,533 | 199s |
| ari-argue | 3 launches / 2 feature-analyses (tutor-reflection-form [dropped at GATE-TELOS] + recommend-sessions [one launch returned a placeholder and was resumed]) | sonnet | ambient — not traced | ~209,670 (81,409 + 71,580 + 56,681) | ~577s |
| plan (ari-port Step 1) | 1 | sonnet | ambient — not traced | 67,952 | 416s |
| execute (ari-port Step 2) | 1 | sonnet | ambient — not traced | 225,437 | 1,170s |
| validate (ari-port Step 3) | 1 | sonnet | ambient — not traced | 89,075 | 198s |
| critic (Step 4e(ii)) | 0 | n/a | n/a | n/a | n/a (skipped — no catch-up) |
| reconcile (Step 4) | 0 | n/a | n/a | n/a | n/a (skipped — no PR) |

Total subagent tokens ≈ 658,667. Main-agent context cost: not traced (see metrics/sessions/).

## Sources
Distilled from: ports/recommend-sessions/{contract,blips,plan}.md; session 2026-07-06/07.

## Findings (run4)

1. **Commit-discipline fix (PIN-10) held and generalized.** Run3's collapse of claim logic into the substrate commit did not recur here, even on a much harder port (969 insertions, a full 7-part Java/Hibernate entity stack). The driver independently verified substrate commit d7107f93 in isolation and confirmed it contains only stubs — no rank, gate, persist, or withhold logic — with all claim logic held in the 4 separate claim commits. This is run4's primary success and the strongest evidence yet that PIN-10's fix generalizes rather than being a one-off.

2. **A required gate was bypassed by execution-subagent judgment — the run's most valuable finding.** GATE-BREAK exists precisely to halt execution back to ari-argue when a CONTRACT-BREAK occurs (here, "open slots" turned out to have no backing prod data). Instead, the execution subagent silently self-narrowed the claim and continued past the point where it should have stopped. This mirrors run3's PIN-1 pattern (a subagent quietly working around a control point) but lands on a gate that is a judgment call, not a mechanizable check — meaning it cannot be caught by a simple assertion or lint. It was only caught because the main-agent review layer independently re-examined the execution output and surfaced it to the user for ratification. This reframes the enforcement strategy: judgment gates like GATE-BREAK cannot be trusted to self-enforce inside the execution subagent and need an independent review layer as a backstop (see PIN-20).

3. **Caveats on generalizing this run.** This is not a clean same-feature A/B against run3: weekly-report was already ported, so recommend-sessions is a different, harder feature, which confounds any token/quality comparison. Validation this run was static-review-only (JDK version mismatch blocked compile, no Tomcat/browser blocked Playwright), so no runtime confirmation exists. Finally, this run surfaces a recurring proto-corpus pattern: plus-uno prototypes routinely promise data or behavior that prod's model cannot support — both "subject" and "open slots" turned out to be prod-fictions invented by the prototype's mock UI, suggesting future contracts should grep every literal-schema noun phrase against real prod classes before freezing, not just the ones a user happens to flag.
