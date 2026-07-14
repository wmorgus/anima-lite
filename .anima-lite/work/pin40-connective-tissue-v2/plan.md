# Execution Plan: connective tissue v2
Contract: .anima-lite/work/pin40-connective-tissue-v2/contract.md
Generated: 2026-07-14

## Claim changes

- **Claim 1+2 (cross-spine reference + unified promise graph)**: `.claude/skills/ari-map/SKILL.md` Output section (§2 Don't-contradict template, §5 Named findings template) — extend the existing `lives-in: <path[s]>` tag's neighborhood with a `relates-to: spine-<label>#<section> (<edge-kind>)` tag, reusing the backlog's already-ratified `relates-to:` vocabulary rather than inventing a new one. One graph: a promise's in-repo enforcement is `lives-in:`, its cross-spine relationship is `relates-to:` — same rule line, two tags, not two systems.
- **Claim 3 (edge-kind vocabulary)**: same template edit as above — `relates-to:` tags carry exactly one of `dependency` (A's promise is enforced by B's code) or `contract` (A's promise constrains what B may promise). Document the vocabulary and worked example against the real shelved case (`spine-lumilo-bridge`/`spine-realtime-event-provider`, read-only reference) in `.claude/skills/ari-map/SKILL.md`.
- **Claim 4+6 (three-tier external-reference + unspineable-as-fact)**: `.claude/skills/ari-map/SKILL.md` — new `§10 External references` template in `material.md`'s output block, three tiers (`spine-built`/`spine-buildable`/`unspineable`), `unspineable` entries carry `owner-of-record:` and `manual-recheck-date:` fields. Cross-reference PIN-21's §8 capabilities-NOT-present precedent so `unspineable` reads as the same class of stated structural absence, not a dangling tag.
- **Claim 5 (staleness folds into execution)**: `.claude/skills/ari-code-rhetoric/SKILL.md` Step 2 (Execute) — add a reverse-index check: when the execution subagent touches a path, check it against `lives-in:` targets across all ingested spines and log any implicated promise inline in that step's blip (`Severity: info`, new field `Spine promise touched:`), not as a separate script or pass. `PHILOSOPHY.md`'s "The spine self-corrects" §3 (Execution) updated to state this supersedes the standalone-script framing, not just still-defers it.

## Substrate translations
- `.anima-lite/reorient/spine-self-correction.md`: update item 4 (promise→promise graph, currently "deferred") and the Recommendation section (currently "Hold (4) entirely") to reflect that PIN-40 builds it now, against the real case named in its own Scope. Wording/placement only — no rule invented here that isn't already in the contract's claims.
- `HARNESS.md` §2 spec ownership map: add a row for the cross-spine/tier vocabulary, owned by `ari-map/SKILL.md` (Output section), consumed by `ari-code-rhetoric` (Claim 5's reverse-index check) and `ari-argue-rhetoric` (GATE-SCHEMA, per-leg schema check already existing).

## Order of operations
1. `ari-map/SKILL.md` template edits (Claims 1-4, 6) — this is the schema; everything else references it.
2. `reorient/spine-self-correction.md` update — depends on (1) existing so the design record can describe the built vocabulary accurately.
3. `PHILOSOPHY.md` "spine self-corrects" §3 update (Claim 5) — independent of (1)/(2), but sequenced after so the whole self-correction paragraph reads consistently in one pass.
4. `ari-code-rhetoric/SKILL.md` Step 2 reverse-index check (Claim 5) — depends on (1)'s `lives-in:`/`relates-to:` vocabulary existing to check against.
5. `HARNESS.md` spec-ownership row — last, references the finished vocabulary location.

## Blockers
None. This is a template/spec build (extending existing skill files), not a code change against a running feature — no dev server, no playwright, no external repo. The real shelved ripple case is read-only reference per the contract's Disposition; no write touches `work/rep-lumilo-kinesis-direct/`.
