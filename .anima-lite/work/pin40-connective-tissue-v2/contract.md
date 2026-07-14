# Contract: PIN-40 — connective tissue v2
Branch: main
Generated: 2026-07-14
Spine commit: 522e44b (self-spine, current)
Source of truth: n/a — single source, converged operator design round + PIN-40.md capture
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
The harness is claiming: a promise recorded in one repo's spine can point at, depend on, or be constrained by a promise in another repo's spine — and where it can't (true vendor boundary), that absence is a stated structural fact, not silence. Staleness against these promises is caught as a side effect of normal `ari-code-rhetoric` execution, not a separate sweep. This is a harness-change contract; the "user" is the operator and future agents reading the spine-self-correction mechanism and `ari-code-rhetoric/SKILL.md`.

## Substrate changes (free to translate)
- Exact field names/YAML shape for edge-kind and tier tags, and where in `reorient/spine-self-correction.md` vs. a new doc the vocabulary lives — the rules are fixed by the claims below, prose/schema shape is not.
- Whether the reverse-index (Claim 5) is a literal in-memory structure, a generated file, or a query pattern over existing `lives-in:` tags — the requirement is that it exists and fires inline during execution, not its storage form.

## Claim changes (confirmed with user)
- Claim 1: cross-spine reference — a rule in spine A can point directly at a rule/finding in spine B (both already-ingested) — Decision: change-to-X — Confirmed: yes, 2026-07-14, converged in design round.
  Schema deps: none.
- Claim 2: promise→promise graph unified with Claim 1 (one graph), validated against the real shelved case (`spine-lumilo-bridge`/`spine-realtime-event-provider`) — Decision: change-to-X — Confirmed: yes, 2026-07-14.
  Schema deps: none.
- Claim 3: every cross-spine edge carries a kind — dependency or contract — Decision: change-to-X — Confirmed: yes, 2026-07-14, answers PIN-26's cross-leg coherence mechanization gap.
  Schema deps: none.
- Claim 4: three-tier external-reference classification (spine-built/spine-buildable/unspineable), `unspineable` carries owner-of-record + manual-recheck-date — Decision: change-to-X — Confirmed: yes, 2026-07-14, directly answers PIN-26's REP routing-config Open Question.
  Schema deps: none.
- Claim 5: staleness detection folds into `ari-code-rhetoric` execution as a reverse-index check against `lives-in:` targets, inline in the blip — supersedes (not just still-defers) PIN-37's standalone-script deferral — Decision: change-to-X — Confirmed: yes, 2026-07-14, operator correction on PIN-37's original deferred approach.
  Schema deps: none.
- Claim 6: `unspineable` reads as a stated structural fact on the spine (PIN-21 absence-representation precedent, applied cross-repo) — Decision: change-to-X — Confirmed: yes, 2026-07-14.
  Schema deps: none.

## Open questions
None — all six claims confirmed this session, per PIN-40.md's own capture (converged in conversation before this pass, this pass formalizes rather than re-litigates).

## Harness-change notes
No `Schema deps:`/playwright block applies to this contract (it's about the spine-self-correction mechanism and `ari-code-rhetoric`, not a feature). No GATE-SCHEMA fire. GATE-TELOS conditional backstop: not triggered — checked against RESOLUTION.md and spine-anima-lite/telos.md in intent.md, both clean.

## Disposition
Formalizes PIN-40's Contract field per PIN-32/36's rule (pin references this file, doesn't duplicate its text). Build target for Claims 1-3 is the real shelved ripple case (`work/rep-lumilo-kinesis-direct/`), read only as reference, per PIN-40's Scope — resuming that paused workstream itself stays out of scope and remains the operator's alone. Claim 5's build touches `ari-code-rhetoric/SKILL.md`, the same file PIN-41 just gave a real harness-change posture — this build should invoke that posture directly rather than improvise, first real proof-by-use of PIN-41.
