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

### Resolved
- FINDING-1 (code-derived): label system in SKILL.md preconditions only recognized `proto` and `prod` — **FIXED**: ari-map Inputs now accepts arbitrary labels; `proto`/`prod` documented as conventional, not required.
- FINDING-2 (code-derived): conservative default absent from SKILL.md as a top-level orientation — **FIXED**: added as explicit Active Orientation in ari-port SKILL.md; no longer requires ari-lite agent face to be active.
- FINDING-4 (code-derived): CONTRACT-BREAK recovery path for partial commits unspecified — **FIXED**: ari-port SKILL.md now specifies preserve-and-amend over revert-and-redo.

### Tabled (backlog formalization needed — track separately)
- FINDING-3 (code-derived): lite face authority only active via ari-lite agent invocation; direct skill invocation loses it. Likely by design — tabled pending decision on whether skills should self-declare face requirements.
- FINDING-5 (code-derived): deployment targets (Cursor/Windsurf/Copilot) have no sync mechanism with SKILL.md sources. Tabled — needs a concrete sync mechanism design before it can be addressed.
- Versioning fields (efficient cause gap): no version field in SKILL.md files, contracts, or blips. Tabled — low immediate impact, medium future impact as harness versions accumulate.

Note: backlog formalization for tabled items is itself a gap — there is no `.anima-lite/backlog.md` or equivalent. These items are tracked here by name only.
