# metrics-spec.md — canonical spec for all metrics artifacts

Owner: ari-port. Readers: ari-backlog (backlog-health row), SessionEnd hook (session-cost row), calibration diffs. This file is the single source of truth for the shape of every metrics artifact under `.anima-lite/metrics/`. Skills and hooks that write or read metrics cite this file rather than restating the schema.

**Honest-stub rule (governs all metrics artifacts):** record only what was actually observed. Where a value cannot be observed, write `not traced` — never leave the field blank, and never estimate or guess a plausible-looking number. A guessed number is worse than an absent one: it looks like data.

---

## Run row

Path: `.anima-lite/metrics/run-<date>-<slug>.md`

Written by: the main pipeline agent (not a subagent), at ari-port Step 5.5 — see `.claude/skills/ari-port/SKILL.md`.

```markdown
# Run: <feature-slug>
Run ID: run-<date>-<slug>
Date: <date>
Prod repo: <repo name> — <base-branch>..<head-branch/commit>
Calibration run: <run number, e.g. "calibration-run-4"> | production run

## Gate table
| Gate ID | Status | Outcome |
|---|---|---|
| GATE-TELOS | fired\|skipped\|n/a | <one line> |
| GATE-SCHEMA | fired\|skipped\|n/a | <one line> |
| GATE-HASH | fired\|skipped\|n/a | <one line> |
| GATE-BLOCKERS | fired\|skipped\|n/a | <one line> |
| GATE-BREAK | fired\|skipped\|n/a | <one line> |
| GATE-BLIPS | fired\|skipped\|n/a | <one line> |
| GATE-PR | fired\|skipped\|n/a | <one line> |
| GATE-SPINE-REVIEW | fired\|skipped\|n/a | <one line> |
| GATE-PLAN-REVIEW | fired\|skipped\|n/a | <one line> |
| GATE-CATCHUP-REVIEW | fired\|skipped\|n/a | <one line> |
| GATE-PIN-CLAIM | fired\|skipped\|n/a | <one line> |

Every registry ID from `HARNESS.md` Section 1 gets a row, no omissions. `n/a` = the trigger condition never arose this run (e.g. no CONTRACT-BREAK occurred, so GATE-BREAK is n/a, not skipped). `skipped` = the gate's trigger condition arose and it was an optional gate the user explicitly declined. A required gate is never `skipped` — if its trigger fired, it either `fired` or the run halted.

## Blip distribution
- info: <count>
- review-suggested: <count>
- CONTRACT-BREAK: <count>
- Blips with `Contracting failure?` ≠ n/a: <count>

## Validation
Result: PASS | PASS-pending (<n> review-suggested acknowledged) | FAIL (<n> loop(s))

## Pipeline events
- Spine refresh triggered: y/n — <which label, e.g. "spine-prod refreshed">
- Contract amendments: <count>
- CONTRACT-BREAKs: <count>
- Commit discipline: substrate commits: <count>, claim commits: <count>, empty claim commits: <count> (0 expected)

## Phase table
| Phase | Subagent invocations | Model tier(s) | Reasoning/effort setting | Subagent tokens | Duration |
|---|---|---|---|---|---|
| ari-map | <n> | <tier per invocation> | <thinking/effort setting per invocation, or "ambient — not traced"> | <from task-result usage, or "not traced"> | <or "not traced"> |
| ari-argue | <n> | ... | ... | ... | ... |
| plan (ari-port Step 1) | <n> | ... | ... | ... | ... |
| execute (ari-port Step 2) | <n> | ... | ... | ... | ... |
| validate (ari-port Step 3) | <n> | ... | ... | ... | ... |
| critic (ari-port Step 4e(ii)) | <n> | ... | ... | ... | ... |
| reconcile (ari-port Step 4) | <n> | ... | ... | ... | ... |

**Reasoning/effort column:** thinking is a model-intensity variable (research question (c)), recorded here — not enforced by any gate. The harness does not mandate a thinking budget; it leaves that to the ambient model/ecosystem and records what was observed. Where the setting is ambient and not readable per-invocation, write `ambient — not traced` (honest-stub rule). This column exists so calibration diffs can hold thinking constant across an A/B (or deliberately vary it) rather than confounding it silently.

Main-agent context cost: not traced (see metrics/sessions/) — never estimated.

## Sources
Distilled from: <work/<slug>/{contract,blips,plan,catchup}.md paths>, session <date/id if known>
```

---

## Backlog-health row

Path: `.anima-lite/metrics/backlog-health-<date>.md`

Written by: ari-backlog, at sweep time (slow-lane sweep step 7 — see `.claude/skills/ari-backlog/SKILL.md`).

```markdown
# Backlog health: <date>

## Open pin count by stub level
- stub:0 — <count>
- stub:1 — <count>
- stub:2 — <count>

## Count by status
- open: <count>
- scheduled: <count>
- in-progress: <count>
- done: <count>
- superseded: <count>
- elsewhere: <count>

## Age of oldest open pin
<pin ID> — captured <date> — <n> days old

## Capture-to-done latency (pins closed since last sweep)
| Pin | Captured | Resolution commit date | Latency |
|---|---|---|---|
| PIN-<n> | <date> | <date> | <n> days |

(From `captured:` field vs. the git commit date that added the `Resolution:` line. If no pins closed since last sweep, state that explicitly.)

## Un-exported elsewhere count
<count> — pins with `status: elsewhere` and no export confirmation (per ari-backlog's cross-repo handling rule).
```

---

## Session-cost row

Path: `.anima-lite/metrics/sessions/<date>-<session>.md`

Written by: the SessionEnd hook (`.claude/hooks/session-cost.py`) — mechanically, not by an agent. This is the only mechanically-written metrics artifact; it complements run rows by capturing main-agent cost, which agents cannot self-measure (a session cannot introspect its own total token usage from inside the conversation).

```markdown
# Session cost: <date> <session-id-prefix>
Session ID: <full session id>
Date: <date>

## Tokens by model
| Model | Input | Output | Cache read | Cache creation |
|---|---|---|---|---|
| <model> | <n> | <n> | <n> | <n> |

## Message count
<n> assistant messages
```

---

## summary.md

Path: `.anima-lite/metrics/summary.md`

Standing header naming the research questions this data serves:
- (a) **Harness cost-benefit threshold** — at what feature complexity does the ceremony (spine + contract + plan + validation + reconcile) pay for itself, versus a lighter-weight approach costing less for the same quality?
- (b) **Quality-vs-token trend** across calibration runs — is the harness getting better outcomes (fewer FAILs, fewer review-suggested blips) at similar or falling token cost, or is quality improvement being bought with token inflation?
- (c) **Model-intensity correlation** — does model tier per phase correlate with blip rate or validation failure rate? Does a cheaper model in a given phase produce measurably worse outcomes, or is tier choice currently arbitrary relative to outcome?

One table, one line per run row, appended when a run row is written:

| Run ID | Gates fired | Blips (info/review/BREAK) | Validation | Total subagent tokens |
|---|---|---|---|---|
| run-<date>-<slug> | <n> | <n>/<n>/<n> | PASS\|PASS-pending\|FAIL | <n or "not traced"> |

**Anti-paperwork rule:** a metrics artifact nobody reads in the next calibration diff is a candidate for deletion. This data exists to answer the three questions named above, not to accumulate. If a field in this spec goes unread across several calibration diffs, that is grounds to drop it from the spec — raise it at the next ari-backlog sweep rather than letting it silently persist.
