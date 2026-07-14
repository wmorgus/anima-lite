# Telos: anima-lite (self)
Commit: 89cf4c3
Confidence: high
Refresh trigger: RESOLUTION.md or PHILOSOPHY.md changes, a skill added/removed/renamed, HARNESS.md §1 gate registry changes, or the work/ artifact layout changes

## §1 Purpose
anima-lite is the custodian of the alignment between what a codebase promises and what it actually is (`RESOLUTION.md`). It treats code as a structure of promises to a user, not a description of a system, and exists to stop divergence between promise and artifact — whether introduced in seconds (slop) or accrued over years (debt) — from landing unratified. Porting a feature from prototype to production is the first work-type this custody takes and the only one fully built end to end; ripple (instituting a promise in N repos at once), debt-work (fixing a diagnosed divergence), and arete (founding a telos by language for a repo with none on record, then judging existing code against it) are ratified direction, built partway.

## §2 Don't contradict
- Never run ari-code-rhetoric without a current, hash-matched spine and a frozen contract with no open Open Questions — GATE-HASH and the contract-status precondition are the entire point, not overhead before the real work
- Never bundle claim confirmations — each is a discrete human decision (README.md "The key distinction"; PHILOSOPHY.md "The cut")
- Never resolve uncertainty by guessing — preserve by default, log as a blip, escalate; the conservative default is a mechanism, not a suggestion (PHILOSOPHY.md "Conservative default")
- Never let a work item enter unregistered or unargued — an intent to change routes through `/ari-intake`, a question routes through `/ari-read`; nothing enters through an undeclared default (PHILOSOPHY.md "Mode honesty")
- Never quietly edit `RESOLUTION.md` to match code or a work item that drifted — a resolution-layer conflict is adjudicated as drift (fix the work item) or growth (a separate, explicitly-ratified workstream), never smoothed over (PHILOSOPHY.md "The resolution")

## §3 Cause files (reference depth)
- [material.md](material.md) — artifact/spec inventory, deliberate non-capabilities, harness vocabulary
- [formal.md](formal.md) — per-skill strata, seam protocols, named findings
- [efficient.md](efficient.md) — invocation model, change propagation, calibration/metrics

## §4 Disclaimers
This is a self-spine — anima-lite mapping itself using its own methodology. The observer and the observed are the same system; findings that touch the probe methodology itself (ari-map/SKILL.md, this spine's own template) warrant extra scrutiny, since the probe cannot easily surface its own blind spots. Where this repo's judgment calls (e.g. what counts as "entity" or "final cause" for a markdown harness rather than an app) required adaptation from ari-map's prod-shaped template, the adaptation is named explicitly in material.md/formal.md rather than silently substituted.
