# Ripple — work-type spec

Captured: 2026-07-07. Status: **ratified as first-class work-type — not built.** Extends the reorientation (`identity.md`); vocabulary per `vocab.md`. Tracked as PIN-26.

---

## Definition

A ripple institutes a new promise in N repos at once. Port preserves an existing promise across a boundary; ripple is the inverted direction of fit — there is no source code to read. The intent artifact (meeting outcome, spec, language derived from context) is the input, and **every claim is born, not inherited**. The contract is not "what survives translation" — it is the full claim specification, authored and ratified one claim at a time before any code exists.

The invariant generalizes without strain: no unratified claim enters *any* repo.

## Rulings (2026-07-07)

1. **First-class work-type.** NOT a composition of greenfield-in-proto + port. The composition derives the prod contract from proto's *code* rather than from ratified intent — proto idiom and shortcuts would bias what prod implements, exactly the contamination the contract exists to prevent. One contract is the apex; every leg binds to it. Proto validates the contract; it does not become it.
2. **Generalized to N execution legs.** Two-repo (proto+prod) is the first instance, not the definition. Geometry: target×N under a contract apex, versus port's source→target.
3. **Sibling divergence is the named threat; cross-leg coherence in validation is the answer.** Sibling divergence — N repos making *almost*-the-same promise (same feature name, subtly different validation, different visibility gate) — already looms silently in current multi-repo setups. It is nastiest at birth: no reference implementation to diff against, only the contract. The validation step gains a **cross-leg coherence check** (integration-testing posture): substrate may differ freely per leg (each follows its own spine's idiom); claims must be identical across all legs, walked against the shared contract.

## Rulings (2026-07-07, design round with PIN-26)

4. **Break reopens all legs for consideration, not automatically for execution.** CONTRACT-BREAK in any leg always reopens ari-argue-rhetoric *consideration* for every other leg: an explicit judgment is argued for whether the amendment touches that leg's already-honored claims. Execution (re-running ari-code-rhetoric) only reopens where that argument concludes the leg's telos is better honored by the amendment; otherwise the judgment is logged and closed, not silently skipped. This replaces blind full-rework and shallow auto-recheck alike — the judgment call itself is the record, and it's cheaper long-term than either extreme.
5. **Parallel-by-default execution across legs.** No privileged first leg — the shared contract is what guarantees cross-leg coherence, so there's no correctness reason to stage one leg before the others. Sequential (proto-first or any other order) is available as a judgment-based deviation when the operator has a specific reason, same posture as ruling 4 — not a fixed default. (Supersedes the sequential-proto-first proposal below, which assumed a proto/prod hierarchy that doesn't generalize to N legs.)
6. **Skill renames, folded into this build:** `ari-argue` → **ari-argue-rhetoric** (formal cause — makes the claim), `ari-port` → **ari-code-rhetoric** (efficient cause — makes it real). Intake and map stay bare: they surface facts (telos-sharpened, spine-read), no argument being made yet. Argue and port are where persuasion happens and then materializes — hence only those two carry "rhetoric." Rename touches: skill directories, CLAUDE.md run procedure + skill list, HARNESS.md spec-ownership map, PHILOSOPHY.md four-cause claim, README.md, ledger-spec.md ownership row, and every pin/backlog line naming the old skill IDs.

## Proposed, superseded above

- ~~Sequential-proto-first as default execution order~~ — superseded by ruling 5.

## Machinery deltas (extensions, no rewrites)

- **ari-intake** (new, upstream — see `intake.md`): produces the argued intent artifact ripple starts from.
- **ari-argue-rhetoric** (renamed from ari-argue): intent-artifact input mode (no source feature). GATE-SCHEMA runs against every target repo. Contract gains per-target substrate-mapping sections; the claims section stays single — one promise, N renderings.
- **ari-code-rhetoric** (renamed from ari-port): runs per leg against the shared contract, parallel by default (ruling 5); blips per leg; validation gains the cross-leg coherence check; CONTRACT-BREAK triggers the two-tier reopen (ruling 4).
- **Preconditions:** comparison-count language (ratified, vocab decision 3b) extends — ripple is N spines, all targets, under a contract apex.
- **Feature ledger:** shared-origin entry type — a feature born in N repos, not ported into one.
