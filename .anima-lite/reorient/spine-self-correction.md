# Spine connective-tissue audit

**Date:** 2026-07-08. Agent-authored proposal, operator-ratified same day, folded into PIN-37 (spun from PIN-25 item (c), incremental spine maintenance). Relocated here from repo root — this is now the design record `ari-map/SKILL.md`'s `lives-in:` addition and the spine self-correction procedure in `PHILOSOPHY.md` are built from.
**Scope:** the spine artifact system produced by `ari-map` (`.anima-lite/spine-<label>/telos.md` + material/formal/efficient cause files), and its consumers (`ari-argue-rhetoric`, `ari-code-rhetoric`).

**Correction (2026-07-08, operator round):** §"The gap" below overclaims that PIN-26 (ripple) is "stuck" without this. It isn't — PIN-26's actual machinery (per-leg execution, cross-leg coherence check, GATE-SCHEMA per target) is built and functional independent of `lives-in:` tags; it's open only pending a real ripple run to prove it. What `lives-in:` adds is a different, real capability — mechanically knowing which spine promises a code change implicates — not unblocking something already broken. Everything else in this audit stands as proposed and was ratified as-is.

## Current state

The spine is markdown, not code — schema lives as prose in `ari-map/SKILL.md` and `ledger-spec.md`. A spine node carries:

- `telos.md`: `Commit:` (repo-wide git hash, whole-spine freshness marker), `Confidence:`, `Refresh trigger:`, §1 Purpose, §2 Don't contradict (the actual promises, as an imperative rule list), §3 Cause files, §4 Disclaimers.
- Cause files (material/formal/efficient): entity/field inventory tables, capabilities-NOT-had lists, domain vocabulary, named findings tagged `(code-derived)` or `(README-stated)`.
- Feature ledger entries (sibling system): `slug`, `repo(s)`, `stub:0-3`, `source:`, `prod-commit:`, `goes-stale:`, `origin: ported|shared-origin`.

Provenance exists, but only one layer up: `argued-by: prototype <path>` appears on individual claims inside `work/<slug>/intent.md` (the intake artifact), not in the spine itself. `material.md` §7 has class/table names, which is partial connective tissue for entities — but §2's promises, and the cause files' named findings, carry no pointer to the file(s) that embody them.

## The gap

A spine can state "must reject unauthenticated writes to the ledger" and never say where that's enforced. Consequence: when code changes, there's no mechanical way to tell which promises are now stale — someone has to re-read the cause files and reconstruct the mapping by hand. This is also why PIN-26 (ripple) is stuck: ripple needs "this file changed → these promises are implicated," and today that arrow doesn't exist anywhere in the artifact.

Two things are conflated in the original framing worth separating:
- **connective tissue** — a pointer from promise to file/symbol. Structural, cheap, stable.
- **muscle** — the actual code/snippet. Not worth storing; it's exactly the kind of code-derived material this system already treats as liquid by default. Caching it just creates a second staleness surface.

## Extensibility read

The system is well-shaped for this addition specifically *because* it already has a provenance convention (`argued-by:`) and already tags findings by origin (`code-derived` / `README-stated`). Adding `lives-in:` is consistent with existing vocabulary, not a new concept. Risk is low: it's an annotation on existing rule lines, not a new file, section, or cross-artifact schema.

Where it doesn't extend cleanly: nothing in the current spine format tracks *edges between promises* (only promise→file, which is what's proposed). If ripple eventually needs promise→promise reasoning ("this rule's rationale depends on that one"), that's a materially bigger addition — a real graph, not a tag — and shouldn't be pulled in prematurely. No N-leg feature has been ported through the shared-origin machinery yet, so designing that graph now would be speculative.

## Prospective useful features, roughly ordered by leverage

1. **`lives-in:` tags on §2 rules and named findings** — the fix for the gap above. One instruction addition to `ari-map/SKILL.md`'s output spec. Unblocks mechanical ripple detection (diff touches file X → grep spine for `lives-in: X`) without new machinery.
2. **Staleness check as a byproduct** — once `lives-in:` exists, a cheap script can diff `git log` against tagged files since `Commit:` and flag which §2 rules are due for re-audit. This falls out of (1) almost for free; worth sequencing right after.
3. **Multi-path tolerance with a smell threshold** — allow `lives-in:` to list multiple files per rule (a promise enforced at N call sites), but flag 3+ during `ari-map` authoring as a signal the rule may be too coarse and should split. Prevents silent sprawl without forcing premature decomposition.
4. **Promise→promise graph (built, PIN-40, 2026-07-14)** — no longer deferred. Built as a cross-spine extension of the existing tag vocabulary rather than a separate graph structure: `ari-map/SKILL.md`'s Output section (§2 don't-contradict rules, §5 named findings) now carries an optional `relates-to: spine-<label>#<section> (<edge-kind>)` tag alongside `lives-in:` — one graph, two tags (in-repo enforcement vs. cross-spine relationship), edge-kind exactly `dependency` or `contract`. Validated (read-only) against the real shelved case named in this doc's own scope (`spine-lumilo-bridge`/`spine-realtime-event-provider`). The same build also folded staleness *detection* into `ari-code-rhetoric`'s own execution (Step 2 reverse-index check against `lives-in:` targets, logged inline as a blip) rather than leaving it a standalone script — see `PHILOSOPHY.md`'s "spine self-corrects" §3 and `ari-code-rhetoric/SKILL.md` Step 2. Full contract: `.anima-lite/work/pin40-connective-tissue-v2/contract.md`.

## Recommendation

Ship (1) and (3) together as a single compact instruction change to `ari-map`. Hold (2) until (1) is live and at least one spine has been re-audited by hand, so the staleness heuristic is checked against a real case before automating it. **(4) is no longer held** — PIN-40 built it 2026-07-14 (see item 4 above); the vocabulary lives in `ari-map/SKILL.md`'s Output section.
