# Intent: scaffold backbone — fifth spine file + ledger-rooting + telos-growth reopen
Slug: pin45-46-scaffold-backbone
Work-type: harness-change
Generated: 2026-07-14
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 89cf4c3

## Telos statement
Give arete's founding pass (and, depth-gated, every ordinary `ari-map` probe) a first-class,
addressable artifact for how a repo's process actually moves — not just the final-cause telos
sentence — so a repo can be aligned to its telos and still be legible or illegible as a process.
Checked against RESOLUTION.md: clean, no conflict — this is custodial spine-completeness work,
squarely inside "custodian of the alignment between what a codebase promises and what it actually
is." Checked against spine-anima-lite/telos.md §1: clean — arete is named there as "ratified
direction, built partway"; this closes part of that gap. §2 don't-contradict rules: no conflict
(doesn't touch GATE-HASH, claim-confirmation discipline, conservative default, or mode honesty).
Apex layer: RESOLUTION.md present, checked, clean.

## Sources
- `.anima-lite/reorient/arete.md` ruling 12 (scaffold ruling, 2026-07-14)
- `.anima-lite/pins/PIN-45.md` — arete's scaffold: shape, home, relationship to the cut
- `.anima-lite/pins/PIN-46.md` — the coordinate backbone ("spine under the spine")
- operator ratification, design round 2026-07-14 (both pins' bodies record the resolved design
  directly; no separate meeting/ticket exists)

## Claims
- **`scaffold.md` is a fifth upfront spine file**, sibling to telos/material/formal/efficient —
  markdown-native, one table per scenario, one row per `(scenario, path, step)`, three columns
  (formal/material/efficient cell content per row). Happy path is the default table; other paths
  get rows only where they diverge from it (a gap is an empty column entry, not a missing row).
  **Cell honesty, two distinct kinds of empty:** an unreached cell (not yet probed to that depth)
  reads `not traced`, parity with the ledger's own not-traced discipline; a divergent-path gap
  (the row exists because a path diverges, but this specific cause doesn't differ from the happy
  path at this step) stays the existing blank-empty-column convention. These must not collapse
  into the same blank — one means "unknown," the other means "confirmed, no divergence here."
  **Per-scenario `stub:0–3` field, pulled in from deferred to confirmed this round** — reuses the
  feature-ledger's own stub vocabulary. Not optional: Claim 3 below already talks in `stub:1` /
  `stub:2/3` terms to describe scaffold depth, which only means something if this field exists —
  keeping it deferred while Claim 3 assumes it would leave Claim 3 unimplementable as written.
  argued-by: language reorient/arete.md ruling 12; PIN-46.md Fork 1/Fork 2/"stub extension
  proposed" (pulled in, not deferred, per this round's OQ2 resolution)
- **Skeleton, not flesh — refresh, never accrete.** `scaffold.md` follows the same
  comprehensive-by-intent, exactly-one-per-repo, refreshed-not-accreted discipline as the other
  four spine files (PHILOSOPHY.md's spine self-correction rule). The feature ledger stays the one
  accretive artifact in this family.
  argued-by: language PIN-46.md "The skeleton/ledger distinction"
- **Always produced by `ari-map`, depth-gated not existence-gated.** Every probe already runs an
  unconditional "comprehensive feature map" step (entry-point tracing + grouping by function);
  that walk is most of what a scaffold needs. An ordinary port may stop at a shallow scaffold
  (stub:1 — scenarios named, cells unfilled); a system-level arete founding pass must reach
  stub:2/3 (cells filled) because it has no other legible source to found the telos against.
  Component-level depth is a judgment call based on whether that component has internal process
  complexity worth mapping. **This makes the scaffold a co-requirement with the feature ledger,
  not a lesser or optional sibling of it** — the ledger is already unconditional today (`ari-map`
  writes a stub for every feature found, every probe, no gate, per `ledger-spec.md`'s Stub depth
  section); this claim gives the scaffold the same always-produced/depth-gated shape, on the same
  probe pass, deliberately modeled on the ledger's own existing discipline rather than inventing a
  weaker standard for the newer artifact.
  argued-by: language PIN-45.md "Artifact home" bullet; reorient/arete.md ruling 12;
  ledger-spec.md "Stub depth" (parallel precedent)
- **`ari-arete-pan`'s cut judges against the scaffold as evidence, not a second verdict axis.** A
  unit can serve the telos but sit at a tangled, unattributable spot in the scaffold — that's
  signal feeding the same nugget/ore/slag call the telos check alone would miss. Recorded as a new
  named field in `cut.md`, `Scaffold signal: <coordinate> — <tag>`, not folded into the existing
  free-prose `Pressure:` field — this is closed-taxonomy-shaped (a coordinate plus a short tag),
  and mixing it into prose loses the thing that makes it checkable later, same reasoning as the
  sensor/blip discussion this round.
  argued-by: language PIN-45.md; reorient/arete.md ruling 12; operator design round 2026-07-14
- **`ledger-spec.md` gains a bidirectional rooting field, populated by `ari-map` at probe time,
  with a per-leg shape for shared-origin entries.** A single-source ledger entry gains
  `Scaffold coordinates: <scenario>/<path>/<step>[, ...]` — present when the repo has a scaffold,
  absent (not "none") when it doesn't, same graceful-degradation posture as the playwright block
  or `Schema deps:`. A filled scaffold cell gains the reverse pointer, `Filled by:
  features/<slug>.md`, so either artifact is walkable from the other. Ownership: `ari-map`
  populates `Scaffold coordinates:` at probe time (same pass that traces entry points and builds
  the scaffold in the first place — PIN-45's "always produced" argument applies here directly),
  not deferred to `ari-code-rhetoric`'s enrichment pass. For a `shared-origin` (ripple) entry,
  this is `Per-leg scaffold coordinates:` — one bullet per leg, following the existing
  `Per-leg entry points`/`Per-leg primary data structure` convention (`ledger-spec.md` lines
  103-111) — because each leg has its own repo-scoped scaffold; a single flat field can't resolve
  which leg's scaffold a cross-repo entry's coordinate belongs to. **Cardinality, both fields
  allow multiple:** `Scaffold coordinates:` already allows multiple via `[, ...]`; `Filled by:`
  is symmetric — one scaffold cell may name multiple ledger slugs (several features converging on
  the same tangled step is exactly the tangled-attribution signal the cut's `Scaffold signal:`
  field above is built to surface).
  argued-by: language PIN-46.md "Ledger-rooting field — resolved"; operator design round
  2026-07-14 (ledger-spec discussion, this contracting session)
- **The feature ledger's home corrects from "the anima-lite root" to "the project's core repo"
  (PIN-47 item 5, amended this session).** `ledger-spec.md` line 7 currently states features live
  "at the anima-lite root, not under any repo spine" — a singular location pooling every project
  this tool has ever touched. This corrects to: the ledger lives at the project's core repo
  (PIN-47's core-project-repo pattern, now generalized off arete-only to universal, with a
  single-codebase collapse rule — a project with one codebase has no separate empty-of-app-code
  repo; that codebase's own `.anima-lite/` *is* the core repo). For anima-lite's own self-
  harness-change work (this workstream included), this resolves to the same physical location as
  today — single-codebase, already collapses, no behavior change. It only changes behavior for a
  multi-repo project (a ripple's legs, an eventual arete cascade), whose ledger entries stop
  pooling into an unrelated shared bucket and instead live at that project's own core repo.
  argued-by: language PIN-47.md item 5 (amended 2026-07-14); operator design round 2026-07-14
- **Telos-growth propagates through the backbone via ripple's two-tier reopen, borrowed
  directly.** On a ratified system-level arete-statement growth event: tier 1 — every cascaded
  component statement and every scaffold scenario gets a mandatory reconsideration pass ("does
  this still follow from the new parent?"), judgment logged even when the answer is
  no-rework-needed. Tier 2 — only re-founding/re-walking where that judgment concludes the
  scenario/statement actually depended on what changed.
  argued-by: language PIN-46.md "Telos-growth propagation"; reorient/ripple.md ruling 4
  (borrowed mechanism)

- **`scaffold.md`'s documentation must explicitly state its relationship to the four-cause
  frame — it is not a fifth cause — at every canonical/spec-defining site, not every mention.**
  telos/material/formal/efficient map onto final/material/formal/efficient cause;
  `scaffold.md` doesn't correspond to a fifth Aristotelian cause — it's a coordinate backbone
  that the material/formal/efficient *cells* attach to, per `(scenario, path, step)`. Required at:
  `PHILOSOPHY.md` (wherever the four-cause frame is stated), `spine-<label>/telos.md` §3's
  cause-files list (wherever `scaffold.md` is first named), the new `HARNESS.md` §2 spec-ownership
  row (OQ8), and `ari-map/SKILL.md`'s Output section / the new `scaffold-spec.md` itself. Not
  required at every incidental mention — pins, contracts, and casual references (including this
  one) don't need to repeat the disclaimer each time. A reader who's absorbed "four causes" as the
  harness's organizing frame should not have to infer the fifth file's status from the schema at
  the sites that define the concept — everywhere else, it's just a name.
  argued-by: language operator, this round (2026-07-14) — documentation-legibility requirement,
  narrowed to canonical sites

## Notes
- **Tier-1 reconsideration log artifact (Claim 6/OQ6): deferred to PIN-49, not decided here.**
  Discussion surfaced that a blip is already the harness's coordinate+closed-taxonomy+
  triggered+append-only primitive, scoped to one workstream — and that the sensor reading
  (PIN-48) and this tier-1 judgment are new species of that same genus, which needs its own name
  before either gets a concrete log format. This contract confirms the tier-1 *procedure* only;
  the log's home is explicitly open pending PIN-49.
- **Real gap, explicitly out of this contract's scope:** the telos-derivation edge kind that would
  make tier-1 reconsideration computable (which cells/statements derive from which parent-telos
  clause). PIN-46 names this unbuilt and undesigned. Tier-1's mandatory-reconsideration-pass
  *procedure* is in scope; the tooling that would make it automatic instead of manual is not.
- **Spec-ownership:** this work introduces a new canonical shape doc (`scaffold.md`'s schema) —
  argue-rhetoric should determine whether this needs its own `HARNESS.md` §2 spec-ownership row or
  folds into `ari-map/SKILL.md`'s existing Output section ownership. Not pre-decided here.
- PIN-45's own further-open item — a cross-repo pointer home for a component's statement pointing
  up to its system-level parent (a `~/.anima-lite`-style registry) — is PIN-47's scope, not this
  contract's.
- Sequencing: this contract's coordinate scheme is PIN-48's (sensor) hard dependency — PIN-48
  should not be intake'd until this lands.
- **Sequencing correction (this round):** Group A (this contract) and Group C (PIN-47) were
  flagged parallel-safe/independent when the batch was first split. That no longer holds exactly —
  the corrected ledger-home claim above depends on PIN-47's core-project-repo collapse rule
  (item 5) being ratified, even though PIN-47's full build (registry schema, write-path,
  `ARETE.md` citation format) can still land after this contract. What's needed from Group C
  before this contract can freeze is the *rule*, not the full implementation.
