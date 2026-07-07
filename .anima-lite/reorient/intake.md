# ari-intake — skill spec stub

Captured: 2026-07-07. Status: **built 2026-07-07 — canonical spec is now `.claude/skills/ari-intake/SKILL.md`; this doc remains the design record.** Design ratified same day (Q1–3 below). Emerged from the ripple work-type (`ripple.md`) but cross-cutting: every work-type passes intake. Tracked as PIN-27.

---

## What it names

Intake is currently implicit pre-mapping inside ari-argue, which does double duty: it establishes what the intent *is* (reads the proto feature) and authorizes it (classifies substrate/claim). Port never exposed the seam because the prototype answers the first question — the feature's argument is sitting there in code. Ripple exposes it: with no source code, establishing the intent is real work that happens *before* classification can start.

**ari-intake:** sharpen the telos of the work item, and ensure everything being added is argued for — **by prototype** (the proto feature's code carries the argument) **or by language derived from context** (meeting outcomes, tickets, specs, the operator's own translation of a runaround email). Output: an argued intent artifact ari-argue can contract from.

## The cut between intake and argue

- **Intake answers:** where does this intent come from, and is every part of it argued for? Nothing enters the pipeline unargued — no invented behavior, no "while we're at it."
- **Argue answers:** may this intent change or institute promises? Classification and one-at-a-time ratification, unchanged.

Intake is upstream of argue for ALL work-types. Port's intake is near-trivial (the prototype is the argument — intake verifies it and sharpens telos); ripple's intake is authored (language → argued intent artifact); debt-work's intake is the diagnosis layer itself (divergence found and decomposed IS the argued intent for a fix). That last point suggests intake is where the four-primitive diagnosis (identity.md) eventually lives — diagnosis is intake for divergence-sourced work. Not yet ratified; noted as the natural home.

## Ratified decisions (2026-07-07, Q1–3 round)

1. **Separate skill.** `/ari-intake` is its own invocation, not a phase inside ari-argue. Settled structurally by the four-cause frame (`four-causes.md`): the final cause gets its own skill. Different posture (gathering/sharpening vs. judging), different inputs, and the diagnosis layer needs a future home that isn't the authorization gate. Skill roster goes 4→5.
2. **Argued-intent artifact at `work/<slug>/intent.md`.** Intake mints the slug — the workstream starts at intake, matching the workstream definition (intake→harvest). Fields: telos statement (checked against target spine `telos.md`), work-type, sources list, claims list with per-claim provenance lines — `argued-by: prototype <path>` or `argued-by: language <source>`. ari-argue contracts FROM it; nothing without an `argued-by:` line may enter the contract.
3. **GATE-TELOS: intake owns, argue keeps a backstop.** The gate moves early into intake — repo-telos meets change-telos there (four-causes.md arg 4), fires before any contracting. ari-argue keeps a cheap backstop: if contracting surfaces a claim that contradicts the intent artifact's telos, the gate re-fires. Belt and suspenders, per conservative default; the backstop does not fire unconditionally (gate-fatigue guard).
