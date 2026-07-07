# ari-intake — skill spec stub

Captured: 2026-07-07. Status: **named and scoped — not built.** Emerged from the ripple work-type (`ripple.md`) but cross-cutting: every work-type passes intake. Tracked as PIN-27.

---

## What it names

Intake is currently implicit pre-mapping inside ari-argue, which does double duty: it establishes what the intent *is* (reads the proto feature) and authorizes it (classifies substrate/claim). Port never exposed the seam because the prototype answers the first question — the feature's argument is sitting there in code. Ripple exposes it: with no source code, establishing the intent is real work that happens *before* classification can start.

**ari-intake:** sharpen the telos of the work item, and ensure everything being added is argued for — **by prototype** (the proto feature's code carries the argument) **or by language derived from context** (meeting outcomes, tickets, specs, the operator's own translation of a runaround email). Output: an argued intent artifact ari-argue can contract from.

## The cut between intake and argue

- **Intake answers:** where does this intent come from, and is every part of it argued for? Nothing enters the pipeline unargued — no invented behavior, no "while we're at it."
- **Argue answers:** may this intent change or institute promises? Classification and one-at-a-time ratification, unchanged.

Intake is upstream of argue for ALL work-types. Port's intake is near-trivial (the prototype is the argument — intake verifies it and sharpens telos); ripple's intake is authored (language → argued intent artifact); debt-work's intake is the diagnosis layer itself (divergence found and decomposed IS the argued intent for a fix). That last point suggests intake is where the four-primitive diagnosis (identity.md) eventually lives — diagnosis is intake for divergence-sourced work. Not yet ratified; noted as the natural home.

## Open questions (for shaping at stub:2)

1. Skill boundary: separate `/ari-intake` invocation vs. a named phase inside ari-argue. Leaning separate skill — different posture (gathering/sharpening vs. judging), different inputs, and diagnosis needs a home that isn't the authorization gate.
2. Output format: what the argued intent artifact looks like (per-claim provenance: `argued-by: prototype <path>` vs. `argued-by: language <source>`).
3. Telos-sharpening procedure: what "sharp enough" means — likely a gate (intent conflicts with target telos → GATE-TELOS fires here, earlier than it does today).
