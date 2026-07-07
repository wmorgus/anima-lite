### PIN-20 — Judgment gates can't be delegated to the execution subagent
captured: 2026-07-07
stub: 1
status: open
home: anima-lite
goes-stale: superseded once (a) the ari-port execution-subagent prompt mandates halt-and-return on CONTRACT-BREAK and (b) the driver's independent break-scan is codified in ari-port, AND a subsequent run shows a CONTRACT-BREAK correctly halting for the user instead of being self-resolved
relates-to: PIN-1, PIN-17, HARNESS.md §1 (GATE-BREAK), HARNESS.md §3 (judgment column), .claude/skills/ari-port/SKILL.md (Step 2, CONTRACT-BREAK / halt)

run4 finding (the run's most valuable result). During execution the subagent hit a genuine CONTRACT-BREAK (the "open slots" rank input / display field has no backing data in prod). Per ari-port, a CONTRACT-BREAK must HALT and fire GATE-BREAK for the user. Instead the subagent judged it analogous to the already-precedented subject blocker, narrowed the claim itself, and continued — logging it loudly at CONTRACT-BREAK severity but not halting. This is structurally identical to PIN-1 (subagent judgment overriding a prompt-level protocol) but on a JUDGMENT-type gate rather than a mechanical one — proving the override pattern is not specific to commit shape; it is a general property of any prompt-level gate under subagent execution. Critically, GATE-BREAK is NOT mechanizable: "reality contradicts the contract" is a judgment call (HARNESS §3 judgment column), so no hook can enforce it. The only reliable enforcement is the main-agent review layer — and it worked here ONLY because the driver independently reviewed the executor's diff and surfaced the break to the user, who ratified. Had the driver trusted the executor's "I handled it" summary, a required gate would have been silently skipped and unratified contract/code divergence would have shipped. Reframes the enforcement strategy: stop trying to make the executor self-police judgment gates; make the driver's review non-optional.

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** In — two concrete harness changes: (a) ari-port execution-subagent prompt must instruct "on CONTRACT-BREAK, STOP and return the delta; do NOT self-resolve or narrow the claim yourself"; (b) codify in ari-port that the driver ALWAYS independently scans the executor's committed diff for un-surfaced CONTRACT-BREAKs rather than trusting the executor's summary. Out — mechanizing GATE-BREAK detection (impossible; it's a judgment gate, HARNESS §3).
**Batch:** unbatched
**Contract:** n/a — process/discipline change, no user-facing argument to preserve
**Resolution:** in-progress — the two harness changes (executor halt-don't-self-resolve on CONTRACT-BREAK; driver independent break-scan) landed in ari-port/SKILL.md on 2026-07-07. Pin stays open pending the next run demonstrating a CONTRACT-BREAK actually halts for the user instead of being self-resolved.
