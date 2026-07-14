# Efficient: anima-lite (self)
(Reference depth — see telos.md for entry point and commit hash)

## §1 Build tooling
None. No compiler, bundler, or build step of any kind — `SKILL.md` files are read directly by the Claude Code skill runner at invocation time (code-derived: file enumeration finds no build config anywhere in the repo).

## §2 Key targets
- `/ari-intake`, `/ari-map`, `/ari-argue-rhetoric`, `/ari-code-rhetoric`, `/ari-backlog`, `/ari-read`, `/ari-diagnose`, `/ari-arete`, `/ari-arete-pan` — the nine invocable skills (slash commands map 1:1 to `.claude/skills/<name>/SKILL.md`)
- The `ari-lite` agent (`.claude/agents/ari-lite.md`) — an alternate invocation surface wrapping the three port-relevant skills (map/argue/port) in one agent face; the only place the three-faces model is currently enforced (formal.md §5, FINDING-3)

## §3 CI/CD
None — confirmed by enumeration: no `.github/workflows/`, no `*.yml`/`*.yaml` files anywhere in the repo. The one automated mechanism that exists is the `SessionEnd` hook (`.claude/hooks/session-cost.py`, registered in `.claude/settings.json`), which writes a session-cost row on session end — this is cost capture, not validation, and HARNESS.md §3 tags it as the only `mechanical (IMPLEMENTED)` row in an otherwise all-`judgment`-or-`unbuilt` enforcement table.

## §4 Branching model
Single branch in this repo (`main`; no other local or remote branches exist at probe time) — the branching discipline this harness enforces applies to the *target* repos a port touches, not to anima-lite itself. Ari-code-rhetoric requires a feature branch per workstream slug in the target repo (never commits land on `main`/`dev`/`develop`/etc.), and contracts/plans/blips are branch-scoped by that slug so concurrent ports off the same prototype don't collide. `harness-v1` is a git tag on this repo at commit `28d8464` (pre-dates the current HEAD by many commits); nothing in the pipeline reads or consults this tag — it is inert history, not a live version marker (material.md §6).

## §5 Deploy path
There is no deployment in the application sense — "shipping" a harness change means committing updated `SKILL.md`/support files to `main`; the next invocation of that skill loads the new text with no caching or compilation step. Verifying a harness change works is entirely manual and observer-dependent:
1. Run a real workstream (port, ripple, debt-work, or harness-change) through the updated skill(s).
2. Compare the resulting artifacts (`intent.md`/`contract.md`/`plan.md`/`blips.md`/`catchup.md`/ledger entries) against a prior baseline or against the skill's own stated Output format.
3. Check whether the run's gate table (`metrics/run-<date>-<slug>.md`, per `metrics-spec.md`) actually exercised the gates the change was meant to affect — every HARNESS.md §1 gate ID gets a row whether it fired or not, so a change intended to affect a gate that shows "did not fire" is a signal, not a pass.
4. No automated pass/fail exists anywhere in this loop — judgment call on whether the run's artifacts show the intended improvement, same as before this probe (`git log` on `.anima-lite/metrics/` and `.anima-lite/archive/` is the only historical trail).

Calibration is the closest thing to a regression suite: `archive/calibration-<date>/` captures point-in-time snapshots of session artifacts (explicitly not a live-state substitute, per README.md "Artifacts"), and `ari-backlog`'s sweep is a mandatory precondition before every calibration run — but the comparison itself (did this run's artifacts improve on the archived baseline) is read by a human, not scored by a script.
