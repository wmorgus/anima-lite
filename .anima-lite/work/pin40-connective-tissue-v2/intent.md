# Intent: PIN-40 — connective tissue v2: cross-spine edges, external-reference tiers, folded-in staleness
Slug: pin40-connective-tissue-v2
Work-type: harness-change
Generated: 2026-07-14
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 522e44b (current)

## Telos statement
Extend PIN-37's `lives-in:` connective-tissue mechanism past its single-repo ceiling: let a spine rule point directly at a rule/finding in another repo's spine (not just describe the relationship in prose), give those cross-spine edges a kind (dependency vs. contract), classify external references into three tiers (spine-built/spine-buildable/unspineable) instead of one flat "outside" bucket, and fold staleness detection into `ari-code-rhetoric`'s normal execution as a reverse-index check rather than a standalone sweep script. Checked against RESOLUTION.md: clean — this deepens "software that admits change only as argument" by making the argument-graph itself cross repo boundaries instead of stopping at them; it doesn't change what any repo is for. Checked against spine-anima-lite/telos.md §1/§2: clean — no Don't-contradict rule touched; this is a direct extension of `reorient/spine-self-correction.md` (PIN-37), not a replacement.

## Sources
- `.anima-lite/pins/PIN-40.md` — captured scope, stub:1 at start of this pass, five converged extensions dated 2026-07-14
- `.anima-lite/pins/PIN-37.md` and `.anima-lite/reorient/spine-self-correction.md` — the `lives-in:` mechanism and self-correction framing this pin extends, not replaces; PIN-37 explicitly deferred both the staleness-check script and the promise graph
- `.anima-lite/pins/PIN-26.md` and `work/rep-lumilo-kinesis-direct/` — the shelved ripple run that surfaced both real gaps live: GATE-SCHEMA hit REP's env-injected routing config with no vocabulary sharper than "Open Question," and PIN-26's cross-leg coherence check had no mechanical way to run without re-reading contracts by hand
- `.anima-lite/pins/PIN-21.md` — spine-completeness precedent for absence-representation (capabilities-NOT-present), the same move this pin makes for `unspineable`
- Operator design round, this session, 2026-07-14 — the five extensions were converged in conversation before this pin was captured; this intent pass formalizes them, adds no new scope

## Claims
- Claim 1 — A rule in one repo's spine (`spine-<label>/`) can point directly at a rule/finding in another already-ingested repo's spine, not just describe the relationship in prose. This and Claim 2 share one graph structure, not two.
  argued-by: language <PIN-40.md item 1, converged 2026-07-14>
- Claim 2 — The promise-graph structure PIN-26 deferred is unified with Claim 1's cross-spine reference — one graph, built and validated against the real shelved case (`spine-lumilo-bridge` / `spine-realtime-event-provider`), not a synthetic example.
  argued-by: language <PIN-40.md item 2, citing PIN-26's deferred promise→promise graph>
- Claim 3 — Every cross-spine edge carries a kind: *dependency* (A's promise is enforced by B's code) or *contract* (A's promise constrains what B may promise). This is the vocabulary PIN-26's cross-leg coherence check needs to run mechanically instead of by re-reading contracts by hand.
  argued-by: language <PIN-40.md item 3, converged 2026-07-14>
- Claim 4 — External references classify into exactly three tiers: `spine-built` (pointer resolves into another repo's already-mapped spine), `spine-buildable` (names a real, accessible repo not yet mapped — a legitimate `/ari-map` backlog signal, not a dead end), `unspineable` (true third-party/vendor boundary, no source access ever — pointer terminates at a contract surface: API version, schema, endpoint). `unspineable` pointers carry an owner-of-record field and a manual-recheck-date field, since PIN-37's 3+-path smell threshold cannot apply where there are no paths to count.
  argued-by: language <PIN-40.md item 4, converged 2026-07-14, directly answering PIN-26's REP routing-config Open Question>
- Claim 5 — Staleness detection does not become a standalone sweep script (PIN-37's deferred item is now superseded, not merely still-deferred). Instead, when `ari-code-rhetoric` touches a path during normal execution, it checks that path against a reverse index of `lives-in:` targets and flags any promise touched, inline in the blip for that step — self-correction as a side effect of doing the work, per PHILOSOPHY.md's existing "the spine self-corrects" framing.
  argued-by: language <PIN-40.md item 5, operator correction on PIN-37's deferred approach, converged 2026-07-14>
- Claim 6 — `unspineable` reads on the spine as a stated structural fact (a permanently-opaque enforcement boundary), not a dangling tag a reader has to chase — same move as PIN-21's capabilities-NOT-present, applied to cross-repo absence instead of in-repo absence.
  argued-by: language <PIN-40.md item 6, citing PIN-21 precedent>

## Notes
Fifth harness-change to run real intake→argue (after PIN-26, PIN-39, PIN-41, and this one) — same posture: single-spine (this repo's own), `argued-by: language <source>` throughout, no prototype to read an argument off of. Design target for Claims 1-3 is the real shelved ripple case (`work/rep-lumilo-kinesis-direct/`), read only as reference — this pin's Scope explicitly excludes resuming that paused workstream. Once this contract freezes, the build (Claim 5 in particular touches `ari-code-rhetoric/SKILL.md` directly, the same file PIN-41 just gave a harness-change posture to) can run through the now-real posture instead of an ad hoc stand-in.
