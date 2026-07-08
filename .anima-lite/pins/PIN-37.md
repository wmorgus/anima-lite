### PIN-37 — spine connective tissue: `lives-in:` tags + self-correction procedure
captured: 2026-07-08
stub: 2
status: done
home: anima-lite
goes-stale: superseded once a real spine re-probe has exercised the `lives-in:` tag and multi-path smell threshold against a live case (still untested — see Resolution)
relates-to: PIN-25 (spun from item (c), incremental spine maintenance), PIN-23 (the re-probe this closes the loop on), PIN-26 (a secondary beneficiary, not the blocker the source audit initially overclaimed), `.anima-lite/reorient/spine-self-correction.md` (design record), `work/pin37-spine-connective-tissue/{intent,contract}.md` (formal harness-change contract)

Agent-authored audit (`reorient/spine-self-correction.md`), operator-ratified 2026-07-08 with one correction: the spine can state a promise ("must reject unauthenticated writes") with no pointer to what enforces it, so a code change gives no mechanical signal about which promises are now stale — someone has to re-read the cause files by hand (PIN-23 was exactly this, done manually). Fix: a `lives-in: <path[s]>` tag on every spine rule and named finding — connective tissue (a pointer), never muscle (cached code) — extending the existing `argued-by:`/`(code-derived)` provenance vocabulary rather than inventing new concepts. This also replaces an earlier, weaker proposal from the same design round (a `Pending triggers:` field for debouncing staleness) before it was ever built.

---
Shaping fields.

**Scope:** In — (a) `lives-in:` tag on `ari-map/SKILL.md`'s telos.md §2 rules and formal.md §5 named findings, with a 3+-path smell-threshold flag during authoring; (b) name the spine self-correction procedure (detection/judgment/execution/exclusion) in `PHILOSOPHY.md`, tied to the existing belief/record split rather than stated as a new rule. Out — a staleness-check script (deferred until (a) ships and one spine is hand-re-audited against it); a promise→promise graph for PIN-26 (deferred until a real N-leg ripple exists to design against); relocating or fixing `.cursor/rules/*.mdc` (separate, deeper drift, tracked by PIN-7/PIN-18).
**Batch:** spine-completeness
**Contract:** harness-change, run through the real intake→argue path (second instance after PIN-26, per PIN-32/PIN-36's fix) — `work/pin37-spine-connective-tissue/{intent,contract}.md`. Four claims: `lives-in:` tags (1), multi-path smell threshold (2), the named self-correction procedure (3, supersedes `Pending triggers:`), explicit deferral of the staleness script and promise graph (4).
**Resolution:** done 2026-07-08. `ari-map/SKILL.md` Output section: `lives-in:` added to the telos.md §2 template and to formal.md §5's provenance-rule paragraph, with the 3+-path smell-threshold instruction and an explicit pointer-not-cache statement. `PHILOSOPHY.md` gained "The spine self-corrects (PIN-37)" paragraph, next to the five-field tiling, naming all four procedure parts and citing the belief/record split rather than restating it. Neither the staleness script nor the promise→promise graph was built — both explicitly deferred per contract claim 4. Untested: no spine has been re-probed under the new `lives-in:` rule yet, so the smell threshold and the mechanical-diff detection loop are unverified against a real case — same epistemic status as any freshly-written judgment-tagged instruction before its first live fire.
