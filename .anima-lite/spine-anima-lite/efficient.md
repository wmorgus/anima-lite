# Efficient: anima-lite (self)
(Reference depth — see telos.md for commit hash)

## §1 Invocation model
- User invokes via Claude Code slash commands (`/ari-map`, `/ari-argue`, `/ari-port`) or through the `ari-lite` agent
- Each invocation loads the SKILL.md file at runtime from disk — no compilation, no caching
- Changes to SKILL.md take effect immediately in the next invocation; running sessions see only the version loaded at session start

## §2 Change propagation
- Human edits SKILL.md → next Claude Code session loads updated skill → new behavior
- No CI/CD — no automated tests, no lint, no validation pipeline
- No mechanism to notify running sessions that the harness changed mid-session
- Deployment targets (Cursor, Windsurf, Copilot) require manual sync after SKILL.md changes — not automated

## §3 Versioning mechanism (and its gaps)
What exists:
- Git commits track all changes to SKILL.md files and committed artifacts
- `harness-v1` tag (commit `28d8464`) marks the first calibration baseline
- Spine telos.md files carry a `Commit:` hash pinning spine state to a specific repo HEAD
- Archive directory captures session artifacts at calibration snapshots

What is missing (the underspecified efficient cause):
- **No version field in SKILL.md** — a running session cannot determine what harness version it loaded
- **No harness version in contracts or blips** — artifacts from old harness versions are indistinguishable from current ones; a contract written under harness-v0 looks identical to one written under harness-v1
- **No mid-session change detection** — if SKILL.md is edited while a port is in progress, the running session has no signal
- **Git tag is not read by any skill** — `harness-v1` exists but nothing in the pipeline consults it
- **Deployment target drift undetectable** — Cursor/Windsurf/Copilot files carry no version; no diff is run at invocation time

## §4 Calibration process (current)
- Manual: run a test port, archive session artifacts under `.anima-lite/archive/calibration-<date>/`, tag the harness commit
- Diff next run's artifacts against archive to measure harness improvement
- No automated regression check — calibration is observer-dependent

## §5 Verifying a harness change works
1. Run a test port of a known feature through the updated harness
2. Compare artifacts against the archive baseline (contract, blips, catchup, plan)
3. Check spine for expected findings — the spine should surface what the test found, not what the prior run found
4. No automated pass/fail — judgment call on whether findings improved
