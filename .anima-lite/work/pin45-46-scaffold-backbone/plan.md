# Execution Plan: scaffold backbone (PIN-45/46)
Contract: .anima-lite/work/pin45-46-scaffold-backbone/contract.md (FROZEN)
Generated: 2026-07-14

## Claim changes
In implementation order — each claim below maps to its own commit, substrate scaffolding first:

- **Substrate/scaffolding**: create `.claude/skills/ari-map/scaffold-spec.md` shell (new canonical
  sub-spec, per confirmed HARNESS.md §2 recommendation) — stubbed structure only, filled in by
  Claim 1's commit.
- **Claim 1** (`scaffold.md` is a fifth spine file, schema, cell honesty, stub:0–3 field): write
  `ari-map/scaffold-spec.md` in full — schema (one table per scenario, one row per
  `(scenario,path,step)`, three formal/material/efficient columns, happy-path-default table),
  `not traced` vs. blank-gap honesty distinction, per-scenario `stub:0–3` field reusing the
  ledger's vocabulary.
- **Claim 2** (skeleton, not flesh): fold into `scaffold-spec.md`'s own opening + a one-line
  addition to `PHILOSOPHY.md`'s spine self-correction section naming `scaffold.md` alongside the
  other four refresh-not-accrete files.
- **Claim 3** (always-produced by `ari-map`, depth-gated, retroactive backfill) + **Claim 7**
  (four-cause disclaimer, canonical sites): amend `ari-map/SKILL.md`'s Output section to require
  producing `scaffold.md` every probe (min stub:1), arete-mandatory stub:2/3 at system level; note
  retroactive backfill obligation for existing spines. Add the four-cause disclaimer at this site
  (one of the four canonical sites) and at `PHILOSOPHY.md` and `spine-anima-lite/telos.md` §3.
- **Claim 4** (`ari-arete-pan` cut evidence, `Scaffold signal:` field): amend
  `ari-arete-pan/SKILL.md`'s Output section (`cut.md` template) to add the field.
- **Claim 5** (ledger rooting field, per-leg shape, ari-map ownership, ledger-home correction):
  amend `ari-map/ledger-spec.md` — both templates gain `Scaffold coordinates:`/
  `Per-leg scaffold coordinates:` and `Filled by:` (multiple allowed); Field ownership section
  reassigned to `ari-map` at probe time; opening paragraph's "the anima-lite root" corrected to
  "the project's core repo," citing PIN-47 item 5.
- **Claim 6** (telos-growth two-tier reopen, procedure only): amend `spine-anima-lite/formal.md`'s
  `ari-arete` stratum to document the tier-1/tier-2 procedure in prose. No log artifact — carved
  out to PIN-49 per contract.
- **HARNESS.md §2**: add the new "Scaffold artifact spec" row (owner `ari-map`, canonical file
  `ari-map/scaffold-spec.md`, read by `ari-arete`/`ari-arete-pan`/`ari-argue-rhetoric`). Fourth
  canonical four-cause-disclaimer site.
- **Dogfood backfill (Claim 3's retroactivity, scoped)**: produce `spine-anima-lite/scaffold.md`
  itself at `stub:1` — anima-lite's own self-spine is the most relevant, lowest-risk backfill
  target and proves the schema against a real case. The other four existing spine directories
  (`spine-lumilo-bridge`, `spine-prod`, `spine-proto`, `spine-realtime-event-provider`) are
  **not** backfilled in this pass — logged as a blip (conservative default: retroactive obligation
  confirmed, but backfilling four more spines is real probe work belonging to those repos' next
  `ari-map` refresh, not manufactured here against stale context).

## Substrate translations
None — harness-change, no proto/prod pair; every file touched is this repo's own skill/spec/spine
material, translated per the confirmed claims above, not against an external substrate pattern.

## Order of operations
1. `ari-map/scaffold-spec.md` (new file) — Claims 1, 2, 7 (one disclaimer site)
2. `ari-map/SKILL.md` — Claims 3, 7 (second disclaimer site)
3. `ari-arete-pan/SKILL.md` — Claim 4
4. `ari-map/ledger-spec.md` — Claim 5
5. `spine-anima-lite/formal.md` — Claim 6 (procedure only)
6. `PHILOSOPHY.md` — Claim 2, 7 (third disclaimer site)
7. `spine-anima-lite/telos.md` §3 — Claim 7 (fourth disclaimer site, cause-files list)
8. `HARNESS.md` §2 — new row
9. `spine-anima-lite/scaffold.md` (new file) — dogfood backfill, stub:1
10. Feature-ledger harvest: no new feature here (harness-change), skip.

## Blockers
None. Contract is FROZEN with no open Open Questions blocking implementation; Claim 6's carve-out
is a scope boundary, not a blocker.
