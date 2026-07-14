# Contract: fix metrics/summary.md's stale pre-rename spec path
Branch: main
Generated: 2026-07-14
Spine commit: 522e44b (self-spine, current)
Source of truth: n/a — single source, diagnosis.md
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
`summary.md`'s schema pointer should name the metrics-spec file's actual current location. No promise beyond "this pointer resolves to a real file" is at stake — there is no substrate/claim split to classify, since the entire content is one fact (a path string) that is either correct or dead.

## Substrate changes (free to translate)
n/a — no translatable medium here; the string itself is the whole of it.

## Claim changes (confirmed with user)
- Claim 1: pointer names `.claude/skills/ari-code-rhetoric/metrics-spec.md` — Decision: change-to-X (corrects dead path) — Confirmed: yes, 2026-07-14 (operator: "yeah sure run it thru").
  Schema deps: none.

## Open questions
None.

## Harness-change notes
n/a — this is debt-work, not harness-change; noted for completeness that no `Schema deps:`/playwright block applies here either, for the same reason PIN-38 already gave: mechanical, no argument to preserve.

## Disposition
First debt-work item to carry a `diagnosis.md` provenance line into a contract, closing PIN-39's goes-stale condition once the fix itself lands (below, applied directly — full ari-code-rhetoric plan/execute/validate/reconcile/harvest ceremony is disproportionate to a one-line path correction; PIN-38's own Contract field already called this "mechanical, no argument to preserve").
