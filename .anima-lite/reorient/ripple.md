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

## Proposed, not yet ratified

- **Break-reopens-all-legs:** CONTRACT-BREAK in any leg reopens ari-argue for every leg — a claim unimplementable in one target amends the shared contract, so all legs re-check even if already passed. The price of one-promise-N-bodies. Flagged for pressure-test before it becomes a gate rule.
- **Sequential-proto-first as default execution order** (cheap validation loop, matches plus-uno's purpose) with parallel legs allowed. Ordering is an execution policy, not a contract property.

## Machinery deltas (extensions, no rewrites)

- **ari-intake** (new, upstream — see `intake.md`): produces the argued intent artifact ripple starts from.
- **ari-argue:** intent-artifact input mode (no source feature). GATE-SCHEMA runs against every target repo. Contract gains per-target substrate-mapping sections; the claims section stays single — one promise, N renderings.
- **ari-port:** runs per leg against the shared contract; blips per leg; validation gains the cross-leg coherence check.
- **Preconditions:** comparison-count language (ratified, vocab decision 3b) extends — ripple is N spines, all targets, under a contract apex.
- **Feature ledger:** shared-origin entry type — a feature born in N repos, not ported into one.
