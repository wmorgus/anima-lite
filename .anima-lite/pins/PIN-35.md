### PIN-35 — backlog sharded: backlog.md becomes index, one file per pin
captured: 2026-07-07
stub: 2
status: done
home: anima-lite
goes-stale: superseded if the backlog returns to single-file layout or the index-line format changes
relates-to: .claude/skills/ari-backlog/SKILL.md (Layout, Pin format, fast lane, sweep steps 1/5, suspension step 2), PIN-31 finding (b) (same-file pin collision — structurally resolved for pin bodies by this change)

Operator direction (2026-07-07): the single-file backlog passed ~500 lines — past the Layout section's own ~300-line revisit threshold. Sharded: `backlog.md` is now an index carrying one searchable line per pin (status, stub, batch, semantic hook — enough of the pin's key nouns to be findable by search); each pin's full block lives in its own file at `pins/PIN-<n>.md`. Pin file is source of truth; index line is derived and must move with it. Side effect: PIN-31 finding (b)'s same-file collision class (two in-flight pins editing backlog.md) shrinks to index lines only — pin bodies can no longer collide.

---
Shaping fields.

**Scope:** In — migration of all 23 live pin blocks to `pins/PIN-<n>.md` (PIN-31/32 interleaving untangled); backlog.md rewritten as index (archived pins keep pointer lines); ari-backlog/SKILL.md updated (Inputs, Pin format + index-line spec, fast lane, sweep steps 1/5, suspension shared-file note, Layout); CLAUDE.md backlog reference. Out — archive format (done-<year>.md unchanged); index-generation automation; metrics changes.
**Batch:** unbatched
**Contract:** n/a — mechanical, no argument to preserve (pin format, lifecycle, and durability promises unchanged; storage layout only)
**Resolution:** done 2026-07-07 — shard executed same session as capture, operator-directed.
