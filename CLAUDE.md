# anima-lite

Argument-preserving port toolkit for porting features from plus-uno (prototype) to plus web-app (production).

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

Artifacts land in `.anima-lite/` in this directory. Everything under `.anima-lite/` is committed durable state — spines, and per-slug port artifacts (`ports/<slug>/{contract,blips,plan,catchup,pr}.md`). `archive/` is a calibration-snapshot channel only, not a backup channel — it holds point-in-time copies of runs, it does not substitute for committing the live artifacts.

## Skills

- `/ari-map` — probe a repo, write a four-cause spine (material/formal/efficient/final)
- `/ari-argue` — classify feature details as substrate or claim, confirm claim changes one at a time
- `/ari-port` — translate substrate freely, implement confirmed claims exactly, log blips
- `/ari-backlog` — capture and sweep the backlog (`.anima-lite/backlog.md`); run before every calibration run

`.anima-lite/backlog.md` is committed durable state, not a scratch file — see `.claude/skills/ari-backlog/SKILL.md` for the pin format and sweep process.

See `PHILOSOPHY.md` for the core commitments.
