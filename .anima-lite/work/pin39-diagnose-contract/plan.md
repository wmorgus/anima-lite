# Execution Plan: PIN-39 diagnosis-layer build
Contract: .anima-lite/work/pin39-diagnose-contract/contract.md
Generated: 2026-07-14
Posture: harness-change, single-repo (no spine-proto/spine-prod split — this repo's own spine; no playwright; no PR-to-external-repo — reconcile is an in-repo commit)

## Claim changes
- **Claim 1 (skill container)**: `.claude/skills/ari-diagnose/SKILL.md` (new) — new bare-named skill, upstream of `/ari-intake`, debt-work-only routing.
- **Claim 2 (artifact type)**: `.claude/skills/ari-diagnose/SKILL.md` (Output section) — `work/<slug>/diagnosis.md` template; `.claude/skills/ari-intake/SKILL.md` (Inputs, Per-work-type posture, Escalation) — consuming edge reads `diagnosis.md` as debt-work's source.
- **Claim 3 (scan order)**: `.claude/skills/ari-diagnose/SKILL.md` (Process step 3) — epistemic → spec → world-drift → craft, enforced sequencing with stated reasoning per primitive.
- **Claim 4 (entry modes)**: `.claude/skills/ari-diagnose/SKILL.md` (Preconditions, Process step 1) — two modes named explicitly (operator-nominated, `/ari-read` handoff), third mode (self-triggered) explicitly refused.
- **Claim 5 (evidence bar)**: `.claude/skills/ari-diagnose/SKILL.md` (Process step 4) — per-primitive citation standard, world-drift fixed by contract, spec/epistemic/craft specified here at build time.

## Substrate translations
- `HARNESS.md` §2 — new spec-ownership row for `diagnosis.md`, following the existing row format (judgment.md, intent.md) exactly.
- `CLAUDE.md` — new skill-list bullet, following existing bullet format exactly.

## Order of operations
1. Read `ari-intake/SKILL.md` and `ari-read/SKILL.md` to confirm exact handoff wording before writing the consuming edge — done before any file was written.
2. Write `ari-diagnose/SKILL.md` — no dependency, self-contained.
3. Edit `ari-intake/SKILL.md`'s three touch points (Inputs, Per-work-type posture, Escalation) — depends on step 2 existing so the cross-reference is accurate.
4. Edit `HARNESS.md` and `CLAUDE.md` — depends on step 2's final skill name/description.

## Blockers
None at plan-time — no external repo, no schema dependency, no spine staleness (self-spine current at 522e44b).
