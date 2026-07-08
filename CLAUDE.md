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
/ari-intake feature: playground/weekly-report-demo (or whichever feature)
/ari-map    proto path: ../anima-core/plus-uno
/ari-map    prod path:  ../../other research dev/plus web-app
/ari-argue-rhetoric  feature: playground/weekly-report-demo (or whichever feature)
/ari-code-rhetoric
```

Questions about the system — not intents to change it — enter via `/ari-read` instead, not as part of this port sequence: it mints its own slug and writes `work/<slug>/judgment.md`. See `.claude/skills/ari-read/SKILL.md`.

Artifacts land in `.anima-lite/` in this directory. Everything under `.anima-lite/` is committed durable state — spines, and per-slug port artifacts (`work/<slug>/{intent,contract,blips,plan,catchup,pr}.md`). Spines are the product of this custody, not just precondition input consumed once per port — see `PHILOSOPHY.md`; continuous, incremental spine maintenance is ratified direction, not yet built. `archive/` is a calibration-snapshot channel only, not a backup channel — it holds point-in-time copies of runs, it does not substitute for committing the live artifacts.

## Skills

- `/ari-intake` — mint the workstream slug, sharpen the work item's telos, ensure every claim is argued for (by prototype or by language), write `work/<slug>/intent.md`
- `/ari-read` — the read-register doorway: a question about the system in, a telos-matched judgment out, presented for the operator's own reading. Mints its own slug, writes `work/<slug>/judgment.md`. Sibling to `/ari-intake`, not a step in the port sequence — see `.claude/skills/ari-read/SKILL.md`.
- `/ari-map` — probe a repo, write a four-cause spine (material/formal/efficient/final)
- `/ari-argue-rhetoric` — classify feature details as substrate or claim, confirm claim changes one at a time
- `/ari-code-rhetoric` — translate substrate freely, implement confirmed claims exactly, log blips
- `/ari-backlog` — capture and sweep the backlog (`.anima-lite/backlog.md` index + `.anima-lite/pins/PIN-<n>.md` per-pin files); run before every calibration run

The backlog is committed durable state, not scratch: `.anima-lite/backlog.md` is the searchable index (one line per pin), each pin's full block lives in `.anima-lite/pins/PIN-<n>.md` — see `.claude/skills/ari-backlog/SKILL.md` for the pin format, index-line format, and sweep process.

Canonical specs aren't limited to the six `SKILL.md` files above — three support files are canonical specs in their own right: `.claude/skills/ari-map/ledger-spec.md` (feature-ledger format), `.claude/skills/ari-argue-rhetoric/playwright-spec.md` (Playwright verification), and `.claude/skills/ari-code-rhetoric/metrics-spec.md` (metrics artifact shapes). See `HARNESS.md` §2 for the full spec-ownership map.

The metrics system under `.anima-lite/metrics/` (run rows, backlog-health rows, session-cost rows, `summary.md`) and the `SessionEnd` cost hook (`.claude/hooks/session-cost.py`) are already live — spec owned by `.claude/skills/ari-code-rhetoric/metrics-spec.md`.

See `HARNESS.md` for the gate registry, spec-ownership map, enforcement-level table, and doc-ownership map. This file (CLAUDE.md) is canonical for run procedure, commit policy, and target-repo paths; nothing else states those facts.

See `PHILOSOPHY.md` for the core commitments.
