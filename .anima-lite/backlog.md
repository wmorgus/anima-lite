# anima-lite backlog

Items queued for future work. Not yet formalized with contracts or spines.

---

## PIN-1 — Post-run-review: why did the execution plan fall short?

The weekly-report stress-test execution subagent returned empty claim commits — all claim logic landed in the substrate commit rather than being held out per-claim per the commit discipline spec. The plan was correct; the subagent didn't follow it. Questions to answer:
- Was the plan underspecified about when to separate claim logic from substrate scaffolding?
- Did the subagent misread the plan or override it with a judgment call?
- Does the substrate/claim commit boundary need to be enforced more explicitly (e.g., "do NOT write claim logic in substrate files — stub them, then fill in a separate commit")?
- Relates to: self-spine FINDING-2 (conservative default not always operationalized at skill level)

**When to address:** Next session before calibration run.

---

## PIN-2 — "Software as research programme" sensors

Anima-lite currently treats each run as an isolated event. It should accumulate measurements across runs. Before next calibration run, add:
- Failing review rate: how many validation FAIL results per N runs
- Blip severity distribution per run (review-suggested vs info vs CONTRACT-BREAK counts)
- Gate utilization: which required/optional gates fired, which were skipped
- Spine staleness rate: how often ari-map was triggered by staleness vs fresh map
- Contract amendment rate: how often CONTRACT-BREAK fired per N runs

Measurement artifacts should live in `.anima-lite/metrics/` and be committed. Each run produces a `run-<date>-<feature>.md` row. A `summary.md` aggregates.

**When to address:** Before next calibration run.

---

## PIN-3 — Per-run token analysis as instrumentation

Add token usage tracking to each run as part of research programme sensors (see PIN-2). Each calibration run should record:
- Total tokens consumed per pipeline phase (ari-map, ari-argue, ari-port steps 1–5)
- Token cost per subagent invocation
- Trend across calibration runs (are we getting better quality at similar token cost, or regressing?)

This surfaces the economic dimension of harness improvements: a better harness that costs 3× more tokens is a different tradeoff than one that costs the same.

Implementation: subagents return token counts in handoff; main agent logs to `.anima-lite/metrics/` alongside other sensors.

**When to address:** Alongside PIN-2 (sensors sprint), before next calibration run.

---

## Tabled from self-spine (formal.md §5)

- FINDING-3: lite face lost on direct skill invocation — likely by design, needs mechanism decision
- FINDING-5: deployment target sync (Cursor/Windsurf/Copilot) — needs concrete sync mechanism design
- Versioning fields in contracts/blips — low immediate impact, medium future impact

---

## PIN-4 — Agentic reasoning measurements from epistles 051 + 053

Epistle-051 (whole thing) + epistle-053 (phronesis, hamartia) contain frameworks for measuring agentic reasoning quality. Integrate into Anima-proper's measurement infrastructure:
- Phronesis (practical wisdom): is the agent making contextually appropriate judgment calls, not just rule-following?
- Hamartia (error pattern): what class of mistake is the agent making — hubris, ignorance, misjudgment of scope?
- These are qualitative measurement axes that complement quantitative sensor data (PIN-2/3)

**When to address:** Sensors sprint (alongside PIN-2/3), before next calibration run.
**Source:** `/Users/wmorgus/Desktop/anima/anima-corps/epistles/epistle-051.md`, `epistle-053.md`

---

## PIN-5 — Model-intensity compute-substrate axis instrumentation (epistle-040)

Epistle-040 describes a model-intensity / compute-substrate axis. Add this to the research programme sensor suite:
- Track which pipeline phases use which model tier (Opus vs Sonnet vs Haiku)
- Measure whether model choice correlates with output quality (blip rate, validation FAIL rate)
- The "compute-substrate axis" may inform harness decisions about where to spend model budget

**When to address:** Alongside PIN-3 (token analysis), sensors sprint.
**Source:** `/Users/wmorgus/Desktop/anima/anima-corps/epistles/epistle-040.md`

---

## Needs formalization

This backlog file itself is informal. Need: a lightweight process for moving items from here into contracts (ari-argue pass) and tracking their status. The absence of this process is the problem the self-spine named.
