### PIN-19 — Thinking as recorded variable, not enforced gate
captured: 2026-07-06
stub: 0
status: done
home: anima-lite
goes-stale: superseded if a run shows ambient thinking produces measurably worse classification, which would reopen the enforce-vs-record decision
relates-to: HARNESS.md §3 (mechanical-vs-judgment axis), metrics-spec.md phase table, PIN-5 (model-intensity axis), summary.md research question (c)

Decision (2026-07-06, pre-run4): do NOT enforce a thinking budget on port subagents. Rationale: (1) fails the mechanical test — presence of thinking blocks is a hollow proxy for good thinking, same class as the judgment-tagged rows in HARNESS §3; (2) the harness doesn't cleanly own the lever — Agent-tool/Task subagents inherit ambient session reasoning config, no per-call effort knob in this path; (3) enforcing a fixed budget bets against the ecosystem trend toward adaptive self-managed thinking. Instead: thinking is a model-intensity variable, recorded in the run-row phase table's new Reasoning/effort column and correlated via research question (c). Resolution landed: metrics-spec.md phase table gained the Reasoning/effort column. run4 records its own thinking baseline so the run3/run4 A/B isn't silently confounded.

**Resolution:** metrics-spec.md phase-table Reasoning/effort column added (2026-07-06). Enforcement deliberately declined; recording adopted. run4 will populate the baseline. run4 baseline populated: all 6 subagent phases (ari-map, ari-argue×2, plan, execute, validate) ran on sonnet at ambient reasoning — no per-call effort override was set — recorded as "ambient — not traced" in the phase table of run-2026-07-07-recommend-sessions.md. This is the baseline future runs diff against.
