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

Artifacts land in `.anima-lite/` in this directory. Spines are committed. Contracts and blips are gitignored (session artifacts).

## Skills

- `/ari-map` — probe a repo, write a four-cause spine (material/formal/efficient/final)
- `/ari-argue` — classify feature details as substrate or claim, confirm claim changes one at a time
- `/ari-port` — translate substrate freely, implement confirmed claims exactly, log blips

See `PHILOSOPHY.md` for the core commitments.
