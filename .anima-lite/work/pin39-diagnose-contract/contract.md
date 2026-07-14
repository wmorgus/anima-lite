# Contract: PIN-39 diagnosis-layer contract — /ari-diagnose scope
Branch: main
Generated: 2026-07-14
Spine commit: 522e44b (self-spine, current — see intent.md's Target telos commit note)
Source of truth: n/a — single source, this session's design round (see intent.md Sources)
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
The harness is claiming, to itself and to future readers of PIN-39/diagnosis-layer.md: debt-work's missing intake path is a scoped, ordered, two-entry-mode skill with its own artifact type — not an open question anymore. This is a harness-change contract — the "user" the argument is made to is the operator and future agents reading `/ari-diagnose`'s eventual SKILL.md, not an end feature-user.

## Substrate changes (free to translate)
- Wording/placement of the five ratified rulings within `reorient/diagnosis-layer.md` (section order, heading text) — semantic content is fixed, prose shape is not. Already written this way in the prior turn.
- The intent.md/contract.md file-naming pattern used for this harness-change itself (slug `pin39-diagnose-contract`) — cosmetic relative to what's argued for.
- The exact internal file/section layout `/ari-diagnose`'s eventual SKILL.md uses to present the four primitives — provided the scan order (claim 3) and entry modes (claim 4) are preserved as enforced behavior, not just documented intent.

## Claim changes (confirmed with user)
- Claim 1: `/ari-diagnose` as a new, separate, bare-named skill upstream of `/ari-intake`, debt-work-only routing — Decision: change-to-X (adds a new skill; port/ripple/harness-change routing is untouched) — Confirmed: yes, 2026-07-14.
  Schema deps: none (this claim is invocation-surface/routing structure, not data).
- Claim 2: `diagnosis.md` as a new committed artifact type at `work/<slug>/diagnosis.md`, read by `/ari-intake` as debt-work's source — Decision: change-to-X (new artifact type, parity with prototype's role for port) — Confirmed: yes, 2026-07-14. **Not yet executed** — this contract authorizes the artifact type and its consuming relationship to `/ari-intake`; the actual `/ari-diagnose` build (what writes `diagnosis.md`, and the `ari-intake/SKILL.md` edit removing its current honesty-gate refusal for debt-work) is PIN-39 build work, still pending.
  Schema deps: none (harness-change; no prod/proto schema applies).
- Claim 3: fixed scan order epistemic → spec → world-drift → craft, enforced sequencing not an unordered checklist — Decision: change-to-X (closes anima-corps `logic.md` §8.12's open orthogonal-vs-ordered question, for this diagnosis layer specifically) — Confirmed: yes, 2026-07-14, via structured choice.
  Schema deps: none.
- Claim 4: two entry modes in scope — (a) operator-nominated pointer, (b) `/ari-read` honoring-failure handoff; (c) self-triggered/unprompted spine scan explicitly out of scope, deferred to a future pin if picked up — Decision: change-to-X — Confirmed: yes, 2026-07-14 ("a and b are good").
  Schema deps: none.
- Claim 5: per-primitive evidence bar, no uniform citation rule; world-drift's bar (external checkable record) is the only one fixed by this contract, spec/epistemic bars deferred to build time — Decision: change-to-X — Confirmed: yes, 2026-07-14.
  Schema deps: none.

## Open questions
None — all five claims confirmed this session (four by direct operator statement, one — scan order — by structured choice), no ambiguity deferred. Spec/epistemic evidence-bar specifics (claim 5) are explicitly deferred to build time by the claim itself, not an unresolved contract-time question.

## Harness-change notes
No `Schema deps:` values beyond "none" apply — this contract concerns skill/artifact-type structure, not code with prod/proto data dependencies. No GATE-SCHEMA fire (nothing to resolve against a schema). No playwright verification block — port-specific, does not apply. GATE-TELOS conditional backstop: not triggered — no claim surfaced here contradicts `intent.md`'s recorded telos statement or `RESOLUTION.md`; debt-work is already a named, ratified-but-unbuilt part of anima-lite's own purpose statement (§1), so this contract extends existing purpose rather than introducing new purpose.

## Disposition
This contract formalizes the five rulings already recorded in `pins/PIN-39.md`'s Scope field and `reorient/diagnosis-layer.md`'s "Ratified decisions (2026-07-14)" section (written in the prior design round, before this intake/argue pass existed to formalize it). PIN-39.md's Contract field should be updated to reference this file rather than duplicate its text, per PIN-36's explicit rule (reference, not duplicate) and PIN-26's precedent. PIN-39 advances from stub:1 to stub:2 on this contract's freeze. Execution — building `/ari-diagnose` itself, the `diagnosis.md` template, wiring `/ari-intake`'s consuming side, and defining spec/epistemic evidence bars — remains future work; this contract covers only the five claims argued above.
