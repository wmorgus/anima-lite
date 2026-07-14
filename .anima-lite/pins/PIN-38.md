### PIN-38 — metrics/summary.md header points at pre-rename metrics-spec.md path
captured: 2026-07-09
stub: 2
status: done
home: anima-lite
goes-stale: superseded once summary.md's header line points at the current `.claude/skills/ari-code-rhetoric/metrics-spec.md` path
relates-to: PIN-26 (the ari-port→ari-code-rhetoric rename sweep that missed this spot), .anima-lite/metrics/summary.md, .claude/skills/ari-code-rhetoric/metrics-spec.md

Surfaced during the README audit (2026-07-09) and confirmed at this sweep: `.anima-lite/metrics/summary.md` line 3 reads "Schema for every artifact under `.anima-lite/metrics/`: `.claude/skills/ari-port/metrics-spec.md`." That path is dead — `ari-port` was renamed to `ari-code-rhetoric` under PIN-26 (2026-07-07), and the file lives at `.claude/skills/ari-code-rhetoric/metrics-spec.md`. The 2026-07-06 backlog-health row (predates the rename, correctly) also cites the old path in its own header prose, but that file is an archived-in-place dated snapshot, not a live pointer — leave it as historically accurate. summary.md is different: it's a live, standing document, and its stale pointer is exactly the residue PIN-26's own rename sweep says it deliberately swept ("full forward-facing reference sweep across CLAUDE.md/HARNESS.md/README.md/PHILOSOPHY.md/.windsurf/.github") but evidently missed `.anima-lite/metrics/summary.md`.

---
Shaping fields.

**Scope:** In — one-line path fix in summary.md's header. Out — auditing the rest of the metrics/ tree or archived snapshots for the same pre-rename path string (those are dated records, not live pointers; not in scope unless a future sweep finds a live pointer among them).
**Batch:** unbatched
**Contract:** n/a — mechanical, no argument to preserve. Formalized anyway as the first real `/ari-diagnose` → `/ari-intake` → `/ari-argue-rhetoric` dogfood run: `work/summary-md-stale-metrics-path/{diagnosis,intent,contract}.md`.
**Resolution:** fixed 2026-07-14 — `summary.md` line 3 now points at `.claude/skills/ari-code-rhetoric/metrics-spec.md`.
