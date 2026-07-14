# Contract: PIN-41 — give ari-code-rhetoric a harness-change posture
Branch: main
Generated: 2026-07-14
Spine commit: 522e44b (self-spine, current)
Source of truth: n/a — single source, this session's design round
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
The harness is claiming: a harness self-change gets the same execute/validate rigor a port gets (plan, contract-as-filter execution, blip logging, independent validation) — degraded only where port-specific machinery (proto/prod translation, playwright, cross-repo PR) genuinely doesn't apply, never degraded by silent omission. This is a harness-change contract; the "user" is the operator and future agents reading `ari-code-rhetoric/SKILL.md`.

## Substrate changes (free to translate)
- Exact wording/section placement of the new posture note within `ari-code-rhetoric/SKILL.md` (whether it's a new subsection under Preconditions, an inline parenthetical, or a dedicated "Harness-change posture" block like argue-rhetoric's) — the rules themselves are fixed by the claims below, prose shape is not.

## Claim changes (confirmed with user)
- Claim 1: Preconditions §1 names harness-change explicitly, single-repo/self-spine comparison, no proto/prod split required — Decision: change-to-X — Confirmed: yes, 2026-07-14.
  Schema deps: none.
- Claim 2: harness-change skips playwright (Step 3 D/E) and cross-leg coherence (Step 3 F) — Decision: change-to-X — Confirmed: yes, 2026-07-14, same reasoning as argue-rhetoric's existing carve-out.
  Schema deps: none.
- Claim 3: harness-change reconcile treats the harness repo as its own "prod" — no cross-repo PR, direct reviewed commit acceptable — Decision: change-to-X — Confirmed: yes, 2026-07-14, precedent already run informally on PIN-39.
  Schema deps: none.
- Claim 4: core loop (plan, clean-context execute, blips, independent validate A/B/C) is preserved, not skippable by omission — Decision: change-to-X (this is the load-bearing claim; 1-3 describe what's degraded, 4 states what is NOT) — Confirmed: yes, 2026-07-14, this is the operator's original prompt for the whole pin.
  Schema deps: none.

## Open questions
None — all four claims confirmed this session.

## Harness-change notes
No `Schema deps:`/playwright block applies to this contract itself (it's about the skill, not a feature). No GATE-SCHEMA fire. GATE-TELOS conditional backstop: not triggered.

## Disposition
Formalizes PIN-41's scope field. PIN-41.md's Contract field should reference this file per PIN-36's rule. This build runs through the still-gapped `ari-code-rhetoric` the same ad hoc way PIN-39's did (plan.md + independent clean-context validation, no proto/prod, no playwright, direct commit) — proof-by-use that claims 1-3 are the right shape, since this build IS an instance of them.
