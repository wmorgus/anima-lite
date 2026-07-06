# Material: anima-lite (self)
(Reference depth — see telos.md for commit hash)

## §1 Language and format
- Markdown (.md) — all skill logic, artifact templates, gates, documentation; no code
- YAML frontmatter — skill metadata (`name`, `description`) in SKILL.md files

## §2 Runtime
- Claude Code skill runner — `/skill-name` invocation loads and executes SKILL.md in the active agent context
- Agent face: `ari-lite` (`.claude/agents/ari-lite.md`) — runs on Claude Opus; three orientations (ari/builder/lite) always active
- Skills invoke subagents via the Agent tool; subagents are ephemeral, isolated, no shared session context

## §3 Deployment targets (code-derived: file enumeration)
- Claude Code: `.claude/skills/` (SKILL.md files) + `.claude/agents/ari-lite.md`
- Cursor: `.cursor/rules/` (ari-map.mdc, ari-argue.mdc, ari-port.mdc, ari-lite.mdc)
- Windsurf: `.windsurf/rules/` (same four files, .md format)
- GitHub Copilot: `.github/copilot-instructions.md`
- No documented sync mechanism between sources and deployment targets — see formal.md §5 FINDING-5

## §4 Artifact data structures
Committed (shared, versioned):
- `spine-<label>/` — four .md files per repo; telos.md is hash-pinned
- `features/<slug>.md` — feature ledger, stub:0–3
- `archive/calibration-<date>/` — snapshot of session artifacts at calibration time

Gitignored (session-scoped, ephemeral):
- `contracts/<branch>.md` — frozen for session, branch-scoped
- `blips/<branch>.md` — translation log, branch-scoped
- `plans/<branch>.md` — execution plan
- `pr-<branch>.md`, `catchup-<branch>.md` — PR preparation artifacts

## §5 State shape
- Git is the only persistence mechanism — no database, no server, no build step
- Committed artifacts persist across sessions; gitignored artifacts do not
- `harness-v1` git tag marks the calibration baseline at commit `28d8464`
- No lock files, no dependency resolution, no compiled output
