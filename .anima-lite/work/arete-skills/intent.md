# Intent: arete work-type skills
Slug: arete-skills
Work-type: harness-change
Generated: 2026-07-14
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 522e44b

## Telos statement
Give the arete work-type (design closed 2026-07-14, `.anima-lite/reorient/arete.md` Part 2, rulings 1–11) real skills — `ari-arete`, `ari-arete-pan`, and an arete posture on `ari-argue-rhetoric`/`ari-code-rhetoric` — so founding a telos by language for a context-starved repo, and judging existing code against it, is a runnable mechanic rather than a design record.

Apex layer (RESOLUTION.md): clean. The arete pass is argument-driven throughout — the arete statement is drafted and ratified by iterative language, and every subsequent claim it authorizes still passes through argue-rhetoric's per-claim confirm. No conflict with "admits change only as argument."

Telos layer (spine telos.md §1/§2): clean. §1 already names ripple and debt-work as ratified-direction work-types added after port; arete is the same shape of addition, ratified in the 2026-07-14 design round. No §2 don't-contradict rule is touched. Note: telos.md §1's work-type roster (port/ripple/debt-work) is now stale relative to this addition — ordinary spine staleness, not a gate conflict; refresh at this workstream's code-rhetoric stage, same as prior harness-change items (PIN-40, PIN-41) refreshed the spine after landing.

## Sources
- `.anima-lite/reorient/arete.md` — Part 2, rulings 1–11 (2026-07-14 design round, operator Will)
- `.anima-lite/pins/PIN-42.md`, `.anima-lite/pins/PIN-43.md` — adjacent, explicitly out of scope for this item (flowcharts, terminology sweep)

## Claims

- **New skill `ari-arete`** — bare (asserts, doesn't argue). Holds: the seed-context gate (hard precondition, starting rule list of one — "must have an index file" — ratified to grow organically, not to be exhaustively specified by this item); the iterative draft-and-ratify pass producing a caveman-dense arete statement (agent reads seed context, asks clarifications, drafts v1, operator and agent iterate by language, operator ratifies, statement is committed); and cascade re-invocation per node (system-level statement first, then each derived component statement, top-down).
  argued-by: language `reorient/arete.md` rulings 1, 3, 10

- **New skill `ari-arete-pan`** — bare. Sorts an existing repo's code against an already-ratified arete statement into a three-way verdict — nugget (kept, still stated/confirmed via argue-rhetoric), ore (real pressure produced it, doesn't serve cleanly — pressure recorded as a note, claim rewritten), slag (no signal, discarded) — and holds its own batch-ratification gate over the full cut before any code moves, separate from argue-rhetoric's per-claim confirm. Independent entry point: precondition is "an arete statement exists for this repo," not "`ari-arete` just ran in this session" — it must be invokable standalone (periodic re-pan against an unchanged statement, or panning against a statement from an earlier/different session).
  argued-by: language `reorient/arete.md` rulings 4, 5, 7, 10, 11

- **The arete statement is a first-class artifact, not a variant of `intent.md`.** It generalizes the resolution concept (`RESOLUTION.md`/PIN-33): asserted-as-standard (a ratified value judgment, defended only by the operator's own conviction), not argued-for the way `intent.md` claims are. `ari-arete`'s output template must reflect this epistemic status explicitly, not borrow `intent.md`'s argued-by provenance shape.
  argued-by: language `reorient/arete.md` ruling 2

- **`ari-argue-rhetoric` and `ari-code-rhetoric` gain an arete posture**, not new skills — same pattern already used for ripple's and harness-change's own postures. The posture's defining feature: execution target is a new, empty repo built claim-by-claim (nuggets stated/confirmed as-is, ore rewritten from its recorded pressure-note), not an edit-in-place of the old repo. The old repo stays read-only/reference — its `ari-map` spine is the judgment's evidence, never a live target again.
  argued-by: language `reorient/arete.md` ruling 8

- **Cutover (deploy config, DNS/service pointers, downstream consumers, secrets, CI migration) is permanently excluded from every arete skill's scope** — not deferred, not a later phase of any of the skills above. None of the four artifacts built by this item (two skills, two postures) may include cutover mechanics.
  argued-by: language `reorient/arete.md` ruling 9

- **`ari-arete-pan`'s judgment is adjacent to `ari-diagnose` but must not be built as a mode of it.** `ari-diagnose`'s four primitives (spec/epistemic/world-drift/craft) all presuppose an existing telos the code drifted from; arete's target repo never had one. This is a category distinction the skill's own preconditions/orientations must state, not just an implementation detail.
  argued-by: language `reorient/arete.md` ruling 4

## Notes
Two items ruling 3 explicitly leaves unspecified and this workstream must not over-specify: (a) the seed-context best-practices rule list beyond the single index-file rule — `ari-arete`'s gate must be structured to hold a small starting list that grows, not a list dressed up to look complete; (b) the exact field/shape of the arete-statement artifact template — ruling 2 states its epistemic status (asserted, not argued) but the concrete markdown shape is this workstream's own design work, downstream of argue-rhetoric's classification, not a pre-given fact to carry in from `arete.md`.

PIN-42 (per-work-type flowcharts) and PIN-43 (resolution → arete-statement terminology sweep) are related but explicitly out of scope — arete.md's own "Next" section defers both until after these skills exist.
