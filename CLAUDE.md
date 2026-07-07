# anima-lite

anima-lite is the custodian of the alignment between what a codebase promises and what it actually is. Porting features from plus-uno (prototype) to plus web-app (production) is the work-type currently built — see `PHILOSOPHY.md` for the full identity.

Run Claude Code from this directory — the skills are in `.claude/skills/`.

## Target repos

| Role | Path |
|---|---|
| Proto | `../anima-core/plus-uno` |
| Prod | `../../other research dev/plus web-app` |

## Running a port

```
/ari-map    proto path: ../anima-core/plus-uno
/ari-map    prod path:  ../../other research dev/plus web-app
/ari-argue  feature: playground/weekly-report-demo (or whichever feature)
/ari-port
```

Artifacts land in `.anima-lite/` in this directory. Everything under `.anima-lite/` is committed durable state — spines, and per-slug port artifacts (`ports/<slug>/{contract,blips,plan,catchup,pr}.md`). Spines are the product of this custody, not just precondition input consumed once per port — see `PHILOSOPHY.md`; continuous, incremental spine maintenance is ratified direction, not yet built. `archive/` is a calibration-snapshot channel only, not a backup channel — it holds point-in-time copies of runs, it does not substitute for committing the live artifacts.

## Skills

- `/ari-map` — probe a repo, write a four-cause spine (material/formal/efficient/final)
- `/ari-argue` — classify feature details as substrate or claim, confirm claim changes one at a time
- `/ari-port` — translate substrate freely, implement confirmed claims exactly, log blips
- `/ari-backlog` — capture and sweep the backlog (`.anima-lite/backlog.md`); run before every calibration run

`.anima-lite/backlog.md` is committed durable state, not a scratch file — see `.claude/skills/ari-backlog/SKILL.md` for the pin format and sweep process.

Canonical specs aren't limited to the four `SKILL.md` files above — three support files are canonical specs in their own right: `.claude/skills/ari-map/ledger-spec.md` (feature-ledger format), `.claude/skills/ari-argue/playwright-spec.md` (Playwright verification), and `.claude/skills/ari-port/metrics-spec.md` (metrics artifact shapes). See `HARNESS.md` §2 for the full spec-ownership map.

The metrics system under `.anima-lite/metrics/` (run rows, backlog-health rows, session-cost rows, `summary.md`) and the `SessionEnd` cost hook (`.claude/hooks/session-cost.py`) are already live — spec owned by `.claude/skills/ari-port/metrics-spec.md`.

See `HARNESS.md` for the gate registry, spec-ownership map, enforcement-level table, and doc-ownership map. This file (CLAUDE.md) is canonical for run procedure, commit policy, and target-repo paths; nothing else states those facts.

See `PHILOSOPHY.md` for the core commitments.
