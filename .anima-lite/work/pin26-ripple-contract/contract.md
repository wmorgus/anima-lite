# Contract: PIN-26 ripple contract — rulings + skill renames
Branch: main
Generated: 2026-07-07
Spine commit: 28d8464 (self-spine, known stale per PIN-23 — see intent.md's Target telos commit note)
Source of truth: n/a — single source, this session's design round (see intent.md Sources)
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric (name pending this contract's own claim 3)

## The argument
The harness is claiming, to itself and to future readers of PIN-26/ripple.md: ripple's break-handling and leg-ordering rules are settled (not still-proposed), and the skills that make and materialize arguments are named consistently with that role. This is a harness-change contract — the "user" the argument is made to is the operator and future agents reading these skills, not an end feature-user.

## Substrate changes (free to translate)
- Wording/placement of the ratified rulings within `reorient/ripple.md` (numbered-list format, which section header) — the semantic content is what's fixed, not the prose shape. Already written this way in the prior turn; no further translation needed.
- The intent.md/contract.md file-naming pattern used for this harness-change itself (slug choice, section order) — cosmetic relative to what's being argued for.

## Claim changes (confirmed with user)
- Claim 1: two-tier CONTRACT-BREAK reopen (consideration always, execution only if argued to better honor telos) — Decision: change-to-X (replaces the flat "reopens ari-argue for every leg" text in ripple.md's original ruling draft) — Confirmed: yes, 2026-07-07, verbatim quoted in intent.md.
- Claim 2: parallel-by-default leg execution, sequential as judgment-based deviation — Decision: change-to-X (supersedes the sequential-proto-first proposal) — Confirmed: yes, 2026-07-07.
- Claim 3: `ari-argue`→`ari-argue-rhetoric`, `ari-port`→`ari-code-rhetoric` — Decision: change-to-X (renames two live, already-built, already-referenced skills) — Confirmed: yes, 2026-07-07. **Not yet executed** — this contract authorizes the rename; the actual file/directory moves and reference sweep (skill dirs, CLAUDE.md, HARNESS.md, README.md, PHILOSOPHY.md, ledger-spec.md, all pin/backlog lines) are PIN-26 build work, still pending. Until executed, both old and new names may appear in the repo (old = live skill, new = ratified future name) — do not treat a stray old-name reference found before the rename lands as a bug.

## Open questions
None — all three claims confirmed this session, no ambiguity deferred.

## Harness-change notes
No `Schema deps:` or playwright verification block applies (port-specific machinery; see `.claude/skills/ari-argue/SKILL.md`'s harness-change classification note). No GATE-SCHEMA fire. GATE-TELOS conditional backstop: not triggered — no claim surfaced here contradicts `intent.md`'s recorded telos statement or `RESOLUTION.md`.

## Disposition
This contract formalizes decisions already recorded in `pins/PIN-26.md`'s Contract field and `reorient/ripple.md`'s rulings 4-6 (written in the prior turn, before this intake/argue pass existed as a path). PIN-26.md's Contract field should be updated to reference this file rather than duplicate its text, per existing backlog practice (reference, not duplicate). Execution of claim 3 (the actual renames) and the rest of PIN-26's build scope (ari-argue-rhetoric intent-artifact mode, ari-code-rhetoric per-leg execution, ledger shared-origin entry) remains future work — this contract covers only the three claims argued above.
