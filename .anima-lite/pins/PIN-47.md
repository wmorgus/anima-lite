### PIN-47 — cascade registry (`~/.anima-lite`), core project repo, and living seed context
captured: 2026-07-14
stub: 1
status: open
home: anima-lite
goes-stale: not traced
relates-to: reorient/arete.md ruling 3 (cascade), ruling 12 (scaffold), PIN-45, PIN-46

Surfaced from a gap in the cascade design: ruling 3's system-level statement, and every component statement derived from it, need a durable home that isn't any one target codebase (the "system," e.g. a whole product spanning several repos, isn't itself a repo) and isn't fragile to any one anima-lite checkout's local filesystem path.

**Resolved this session:**

1. **Core project repo — no new artifact type.** The system-level arete pass runs *from* a dedicated repo holding no application code, just `.anima-lite/` — same shape anima-lite already uses on itself. Every cascade node's statement (`arete-statement.md`) and the scaffold (`scaffold.md`) live at this repo's own `.anima-lite/work/<slug>/`, same as any other workstream. This is the single source of truth for the whole cascade tree — component statements are authored here *before* their eventual new clean repos exist (ruling 8 — the new repo doesn't exist until code-rhetoric builds it), so there's nowhere else for them to live during founding anyway. Zero new machinery: this repo is just another `.anima-lite`-having repo, minus the sibling application code.

2. **Component repos cite, don't duplicate.** Once a component's new clean repo is built, its own `ARETE.md` (ruling 8's first commit) is a *citation* of the already-ratified statement — `{cascade-id, ratified-statement-hash}` — not a copy of the full text and not a raw local filesystem path into the core repo's checkout. A path breaks the moment the component repo is cloned elsewhere or the core repo's checkout moves; a cascade-id + hash resolves anywhere the registry (below) is present.

3. **`~/.anima-lite` — user-level, machine-durable registry.** A small markdown table (one row per cascade, same convention as `backlog.md`'s index lines — this harness's existing "git/markdown, no database" ethos, `material.md` §2) mapping cascade-id → core-repo location (git remote URL preferred over local path, for portability) → current ratified-statement hash. This is the first piece of state this harness has ever needed outside a single git-tracked repo — named explicitly as new territory, not an extension of an existing pattern.

4. **The core project repo also holds and custodies the raw seed context — added later same session (operator: "that's an arete-worthy task").** Not a one-time pile the operator assembles fresh before each founding pass — a living directory (the GATE-SEED-CONTEXT index file included) that persists in the core repo, gets updated as the project evolves, and is subject to the *same* spine self-correction discipline as everything else in this harness (`PHILOSOPHY.md`: detection → judgment → execution → exclusion) rather than a bespoke context-freshness mechanism invented for this case. Consequence: a material shift in the seed context is upstream of the statement it founded, so it's tier-1 reconsideration bait feeding PIN-46's growth-reopen mechanism one layer further back than "the statement itself changed" — a context change doesn't automatically invalidate the statement (detection ≠ verdict, as always), but it's exactly the kind of candidate that mechanism exists to surface rather than silently miss.

**Not yet designed:**
- The registry file's exact schema (columns beyond cascade-id/location/hash — does it need a `goes-stale`-style field, same as a backlog pin?).
- Who/what writes to `~/.anima-lite` and when — is this a manual operator step at founding time, or does `ari-arete` write it automatically as part of ratifying a system-level statement?
- The seed-context staleness mechanism's concrete shape — does it reuse `lives-in:`-style tags pointing at context documents, or need its own tracking field? (Likely inherits PIN-37/40's existing tag vocabulary rather than inventing a fourth tagging scheme — not yet confirmed.)
- Whether the core project repo itself ever gets its own arete pass (founding a telos for "what is this context-curation repo for") — noted as a clean recursive confirmation of the design's coherence, not proposed as real scope.
- HARNESS.md §2/§4 ownership: this is new enough (state outside any git repo) that it likely needs its own spec-ownership entry once built, not a restatement inside an existing skill file.

---
Shaping fields.

**Scope:** In — the core-project-repo pattern (reuses existing `.anima-lite/` shape, no new artifact type), the `ARETE.md` citation format (`{cascade-id, hash}`, not a path or a text copy), the `~/.anima-lite` registry's existence and rough shape, the living-seed-context framing and its tie into PIN-46's growth-reopen mechanism. Out — the registry's exact schema, the write-path (manual vs. automated), the seed-context staleness mechanism's concrete tagging, any HARNESS.md spec-ownership entry — all real build questions, not yet designed.
**Batch:** unbatched
**Contract:** n/a — ratified design direction, not yet contracted; a harness-change contract for this is real future work, likely bundled with or sequenced after PIN-45/46
**Resolution:** not traced
