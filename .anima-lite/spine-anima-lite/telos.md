# Telos: anima-lite (self)
Commit: 28d8464
Confidence: high
Refresh trigger: PHILOSOPHY.md changes, new skill added, subagent pattern changes, gate structure changes

## §1 Purpose
anima-lite exists to ensure argument survives substrate translation. When a feature moves from prototype to production, the substrate — framework, library, architecture — can change freely. The argument the feature makes to its user cannot change without explicit human confirmation. A port that changes the promise silently is worse than a failed port: it feels complete.

## §2 Don't contradict
- Never run ari-port without a current, hash-matched spine and confirmed contract — the precondition gate is the entire point of the pipeline, not overhead before the real work
- Never bundle claim confirmations — each is a discrete human decision; bundling converts explicit confirmation into implicit batch approval
- Never resolve uncertainty by guessing — preserve by default, log as blip, escalate; the conservative default is a mechanism, not a suggestion
- Never change an argument without the user noticing — silent argument change is the failure mode the whole system exists to prevent
- Never let the spine go stale silently — a hash mismatch is a signal, not an inconvenience

## §3 Cause files (reference depth)
- [material.md](material.md) — runtime, artifact types, state shape
- [formal.md](formal.md) — pipeline structure, subagent pattern, gates, named tensions
- [efficient.md](efficient.md) — versioning mechanism and its gaps (the user-identified underspecified cause)

## §4 Disclaimers
This is a self-spine — anima-lite mapping itself using its own methodology. The observer and the observed are the same system. Treat findings that touch the probe methodology itself with extra scrutiny: the probe cannot easily surface its own blind spots.
