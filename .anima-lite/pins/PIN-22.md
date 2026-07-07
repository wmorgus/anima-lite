### PIN-22 — ari-argue pre-freeze schema-noun grep (contract-time backstop)
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once ari-argue greps claim-referenced domain nouns against real prod classes before freezing a contract, or once PIN-21's spine inventory proves sufficient on its own to make this redundant
relates-to: run-2026-07-07-recommend-sessions.md (findings §3, proto-fiction pattern), ports/recommend-sessions/blips.md (the CONTRACT-BREAK blip recommends exactly this), PIN-21 (the primary fix; this is its backstop), HARNESS.md §1 (candidate new gate), .claude/skills/ari-argue/SKILL.md

run4 finding not yet pinned: plus-uno prototypes routinely promise data/behavior prod's model cannot support. Both `subject` and `open-slots` were prod-fictions invented by the proto's mock UI — they backed nothing in prod, yet rode into the contract as claim inputs and detonated late (plan-time and mid-execution). The CONTRACT-BREAK blip and run4 findings §3 both recommend the same backstop: before freezing a contract, grep every schema-noun / literal-domain-noun in a claim's rule text against real prod classes (`item/`, `dto/`, `enums/`) — not just the nouns a user happens to flag. A noun that resolves to zero prod classes is a contract-time break, surfaced before freeze instead of after.

Relationship to PIN-21: PIN-21 (structured spine inventory) is the PRIMARY fix — if the spine carries the field inventory + negative-space, ari-argue can catch the mismatch by reading the spine. This grep is the BACKSTOP for when the spine is still incomplete (freshly probed, unusual noun, spine drift). Belt and suspenders on the same failure class.

---
Shaping fields.

**Scope:** In — an ari-argue step (before contract freeze) that greps each claim's declared schema dependencies against prod's `item/`/`dto/`/`enums/`; a zero-hit noun halts as a contract-time break for user resolution. **DECISION 2026-07-07: REQUIRED gate** (new GATE-* registry entry, halts like GATE-TELOS) — a claim built on a nonexistent field is exactly the break the pipeline exists to prevent, and catching it pre-freeze is strictly cheaper than at plan/execute (run4 paid the late price twice). Provisional ID: GATE-SCHEMA (finalize in HARNESS §1). **Noun-extraction approach (resolves the over-fire risk):** do NOT naively tokenize free-text rule prose — instead require each claim to DECLARE its schema dependencies explicitly (a per-claim `Schema deps:` field naming the prod entities/fields/enums the claim's rule relies on), and grep those. This makes the check precise, makes the claim's data assumptions visible in the contract, and shifts the extraction burden to contract-authoring where the knowledge is. Implies a contract-format change (new per-claim field) alongside the ari-argue step — stub advances to 2 with this resolved. Stub stays 1 only pending confirmation the contract-format change is in scope.
Out — the spine inventory itself (PIN-21); mechanizing this as a hook (it's grep, scriptable, but lives in the ari-argue skill flow, not a git hook).

**Batch:** spine-completeness
**Contract:** n/a — harness/process change, no user-facing argument to preserve
**Resolution:** in-progress — landed in ari-argue/SKILL.md on 2026-07-07 (sonnet subagent, driver-validated): per-claim `Schema deps:` field added to contract template; step 4c pre-freeze schema-dependency check (spine §7 inventory first, then grep prod `item/`/`dto/`/`enums/`); required GATE-SCHEMA callout mirroring GATE-TELOS. Driver wired the matching HARNESS.md §1 registry row, §3 enforcement row (hybrid mechanical/judgment), and metrics-spec.md gate-table row. Stub advanced 1→2: the contract-format change (explicit per-claim schema-dep declaration) was in scope and shipped, resolving the noun-extraction over-fire concern. Pin stays open pending run5 demonstrating GATE-SCHEMA halts on a real nonexistent-field dependency.
