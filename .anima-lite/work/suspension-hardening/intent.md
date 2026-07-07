# Intent: suspension-procedure hardening (PIN-31)
Slug: suspension-hardening
Work-type: harness-change *(enum gap — template offers port | ripple | debt-work; none fit a harness self-change. See Notes.)*
Generated: 2026-07-07
Target spine: .anima-lite/spine-anima-lite/telos.md
Target telos commit: 28d8464 *(stale vs. HEAD — known, tracked as PIN-23; see Notes)*

## Telos statement

Harden the workstream-suspension procedure so its promise — pausing a workstream is durable and reversible — survives the conditions the first dogfood actually hit: concurrent workstreams sharing a dirty tree and a shared backlog file. Checked against spine-anima-lite telos §1 Purpose and §2 Don't-contradict: clean — this strengthens the explicit-record discipline (§2 "never resolve uncertainty by guessing"); no conflict raised, GATE-TELOS did not fire.

## Sources

- `.anima-lite/backlog.md` PIN-31 body (captured 2026-07-07)
- `.anima-lite/backlog.md` PIN-29 Resolution — the three dogfood findings from run5's suspension (PIN-30, commits 7b19d56/9dc2e86)
- `.claude/skills/ari-backlog/SKILL.md` "Workstream suspension" section (the text being hardened)

## Claims

- Suspension commit scope is the suspended workstream's own files, not the whole tree. "Commit-everything policy applies with no exceptions" is re-scoped: everything *belonging to the suspended workstream* is committed; unrelated concurrent-workstream dirt is explicitly excluded and must NOT be swept into the suspension commit.
  argued-by: language PIN-29 Resolution finding (a) — agent hit the ambiguity live during run5 suspension and correctly took the narrow reading; codifying that reading
- When the pin-of-record edit collides file-locally with another in-flight pin's uncommitted edit in backlog.md, the procedure is a hunk-level split: stage only the suspension pin's hunks into the suspension commit, leave the other pin's edit in the tree.
  argued-by: language PIN-29 Resolution finding (b) — required a manual hunk split during the first dogfood; codifying the maneuver
- The `State:` shaping field has a specified format: `manifest <path>; suspension commit <hash>`.
  argued-by: language PIN-29 Resolution finding (c) — first-instance convention used on PIN-30, not yet codified

## Notes

- **Work-type enum gap (dogfood finding).** The intent.md template's work-type enum (port | ripple | debt-work) has no value for harness self-changes — the very first work item through intake doesn't fit the enum. Not fabricating a fit: recorded as `harness-change` and flagged for ari-intake/SKILL.md follow-up.
- **Debt-work honesty gate skirted, correctly.** This item resembles debt-work (spec diverged from what dogfood revealed) but the diagnosis is already human-made — the three findings ARE the argued intent, sourced above. No diagnosis-layer pass was fabricated; the gate's intent (no undiagnosed divergence dressed up as argued) is honored.
- **Target spine is stale** (Commit 28d8464 vs. current HEAD; content predates ari-backlog, PIN-23 tracks the re-probe). Its §1/§2 remain accurate for the telos check performed here; additionally the telos file's own refresh trigger ("new skill added, gate structure changes") has now fired twice today (ari-intake added, GATE-TELOS moved). Noted for PIN-23, not blocking intake.
- All three claims target one file: `.claude/skills/ari-backlog/SKILL.md` (owning spec for pin lifecycle + suspension procedure). Claim 3 also implies the pin-format template's field list mentions State: format where it's introduced.
