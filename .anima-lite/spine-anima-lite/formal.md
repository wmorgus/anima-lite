# Formal: anima-lite (self)
(Reference depth — see telos.md for commit hash)

## §1 Pipeline structure
Three sequential skills, each gated on the prior:
```
ari-map → ari-argue → ari-port
```
Each SKILL.md organized as: Inputs → Preconditions → Active orientations → Process (numbered steps) → Output → Escalation/Notes

Artifact flow: spine (committed, hash-pinned) → contract (gitignored, branch-scoped, frozen once port begins) → blips (gitignored) → archive (committed at calibration)

## §2 Subagent pattern (as of harness-v1, commit 28d8464)
- **ari-map**: main agent enumerates repo; spawns 3 parallel probe subagents (material/formal/efficient) on large repos (>500 files); synthesizes into four spine files; creates feature ledger stubs
- **ari-argue**: entirely a subagent spawned by main — full classification loop + user interaction in isolated context; returns contract path + telos conflict flag
- **ari-port**: main agent; spawns execution subagent (clean context, implements contract); spawns validation subagent (adversarial); spawns completeness critic (reads catch-up doc cold)

## §3 Human gate pattern
Required (pipeline halts): telos conflict · spine hash mismatch · plan blockers · CONTRACT-BREAK · review-suggested blips · PR creation (6 total)
Optional (user can inspect or skip): spine review · plan review · catch-up doc review (3 total)

## §4 Dominant patterns
- Conservative default: when uncertain, preserve the original claim and log a blip — stated in PHILOSOPHY.md and ari-lite.md but not operationalized as a SKILL.md decision instruction (see FINDING-2)
- Section numbers: spine files use §N headers to make findings citable by downstream skills
- Skeptical reads: each probe subagent has a secondary adversarial output alongside primary findings
- Citation discipline: substrate translations and blips cite the spine §-section grounding them

## §5 Named findings
- FINDING-1 (code-derived): label system in SKILL.md preconditions only recognizes `proto` and `prod` — the `anima-lite` label used in this self-spine is formally unsupported, creating a gap between the documented labels and what the system needs to map itself
- FINDING-2 (code-derived): conservative default is stated in PHILOSOPHY.md and ari-lite.md but absent from SKILL.md files — a session using skills directly without the ari-lite agent face has no conservative default instruction; the philosophy is unoperationalized at the skill level
- FINDING-3 (code-derived): lite face authority is documented in ari-lite.md but not referenced in any SKILL.md — the three-face orientation (ari/builder/lite) is only active when ari-lite agent is invoked; direct skill invocation loses the lite face entirely
- FINDING-4 (code-derived): CONTRACT-BREAK recovery path is underspecified — SKILL.md says halt and re-run ari-argue, but does not address whether partial execution commits should be reverted, preserved, or cherry-picked before the re-run
- FINDING-5 (code-derived): deployment targets (Cursor .mdc files, Windsurf .md files, Copilot instructions) have no documented sync mechanism with the SKILL.md sources — they can silently drift; no version field in any deployment target file
