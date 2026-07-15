### PIN-45 — arete's scaffold (ruling 12): shape, home, relationship to the cut
captured: 2026-07-14
stub: 2
status: scheduled
home: anima-lite
goes-stale: not traced
relates-to: reorient/arete.md ruling 12, PIN-46

**Renamed from "movement map" to "scaffold" 2026-07-14, same session** (operator: "scaffold" is the better name — everywhere else in this pin and PIN-46, read "movement map"/`movement.md` as the pre-rename term for the same thing).

A `lite`-agent study of `anima-core/plus-uno`'s `uno-blueprint` (Supabase-backed service blueprint — every process fact addressable at `phase → service_scenario → path → step → layer → cell`, single-source/queried-live, tool-coupled read layer, paired-write anti-drift with its PRD, vocabulary-fenced) surfaced a gap in arete's founding pass: it currently produces only the telos statement (final cause), with no first-class artifact for the *formal* cause — how the repo's process actually moves. Ruling 12 (`reorient/arete.md`) folds the direction in.

Follow-on discussion (2026-07-14, same session) resolved most of the design questions this pin originally posed:
- Codebase analogue of `layer`/`step`/`cell`: `layer` = execution boundary (module/service/subsystem), `step` = sequence position within a named scenario (a use-case), `scenario`/`path` = the use-case and its happy/error/edge branches — carries over cleanly.
- `ari-arete-pan`'s cut does judge against the scaffold, feeding the same nugget/ore/slag verdict as additional evidence (a unit can serve the telos but sit at a tangled, unattributable spot in the scaffold — real signal for "ore" the telos check alone would miss), not a second judgment axis.
- Required at system-level founding passes; component-level is a judgment call based on whether that component has internal process complexity worth mapping.
- Artifact home: **generalized past arete-exclusive, then corrected from optional to depth-gated (2026-07-14, later same session).** Checked against `ari-map/SKILL.md` directly: every probe already does a "Comprehensive feature map" step (trace entry points, group by user-facing function) and writes a feature-ledger stub for every feature found — unconditionally, not gated to any work-type. That walk is already most of what a scaffold needs (entry-point tracing + grouping by function ≈ identifying scenarios); sequencing steps and coordinatizing by boundary/layer is marginal work on the same pass, not a second cold probe. So the scaffold is not "optional for ports, mandatory for arete" — it's **always produced by `ari-map`, same session as the feature map; what differs is depth, not existence.** An ordinary port can tolerate a shallow scaffold (stub:1, scenarios named, cells unfilled) because the prototype's own legible intent backstops any gaps. Arete cannot — it has nothing else to found the telos against — so arete's actual contribution to ruling 12 is requiring the scaffold reach real depth (stub:2/3) at system level, same shape as domain-central features already getting pushed to stub:2 at map-time instead of stopping at stub:1. This is also where PIN-37/40's connective tissue (`lives-in:` tags, `relates-to:` edges) gets a proper coordinate home instead of staying loose prose in `formal.md`.
- **What this leaves as the actual differentiator of an "arete codebase":** not the scaffold's mere presence (every `ari-map`'d repo gets one now) but the *teleological relationship* — whether the repo's telos was founded by language (arete) or read off existing code (every other work-type), and, for a component within a larger cascaded system, whether it carries a pointer up to the system-level statement it derives from. That pointer's home is an open question, not yet this pin's or PIN-46's — see the new discussion thread on a system-wide (`~/.anima-lite`?) registry for cascade roots that aren't themselves any one codebase.
- **Skeleton, not flesh.** The scaffold sits with `telos`/`material`/`formal`/`efficient` as one of five upfront, comprehensive-by-intent, non-accretive spine files (refreshed, not accreted) — distinct from the feature ledger, the one artifact in this family that genuinely grows in count, one entry per landed feature, tied to actual events. Full distinction, and the ledger-rooting field this implies, now owned by PIN-46 (below) since it's really about the ledger spec, not arete-specific.

**Spun out to PIN-46:** the further generalization — one shared coordinate backbone (scenario × path × step) under *all three* non-final causes, not three independent grids (material-lineage, scaffold, efficient-invocation) that could drift out of step with each other — plus the backbone's concrete schema, its relationship to the feature ledger, and how a telos-growth event propagates through it. This pin (PIN-45) now stays scoped to arete's own requirement and use of whatever PIN-46 designs; PIN-46 owns the backbone's actual shape.

---
Shaping fields — not traced.

**Scope:** In — arete's requirement (always-produced, depth-gated), the cut-vs-scaffold evidence relationship. Out — the backbone's own schema (PIN-46).
**Batch:** scaffold-backbone (Group A, with PIN-46)
**Contract:** `work/pin45-46-scaffold-backbone/contract.md` — FROZEN 2026-07-14, ready for `ari-code-rhetoric` (one carve-out: Claim 6's log artifact deferred to PIN-49)
**Resolution:** not traced
