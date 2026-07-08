# Contract: spine connective tissue — `lives-in:` tags + self-correction procedure
Branch: main
Generated: 2026-07-08
Spine commit: 522e44b (self-spine)
Source of truth: n/a — single source, `reorient/spine-self-correction.md` (agent-authored, operator-ratified with one correction)
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
The harness is claiming: every promise a spine states can be mechanically traced to the file(s) that embody it, and the procedure for keeping that promise-map current — detect via diff, judge whether it's actually stale, re-probe, keep the correction narrative out of the artifact — is written down once, not reinvented per pin.

## Substrate changes (free to translate)
- Exact wording of the `lives-in:` field name and its placement (end-of-line tag vs. its own indented line under a rule) — the semantic content (a file pointer exists per rule) is the claim, not the syntax.
- Where in PHILOSOPHY.md the new procedure paragraph sits relative to the five-field tiling paragraph — adjacency matters for readability, not for the argument.

## Claim changes (confirmed with user)
- Claim 1: `lives-in:` tags on §2 rules and named findings — Decision: change-to-X (new field, `ari-map/SKILL.md` Output section) — Confirmed: yes, 2026-07-08.
- Claim 2: multi-path tolerance + 3-path smell threshold — Decision: change-to-X — Confirmed: yes, 2026-07-08. **Not yet exercised** — no spine has been re-probed under this rule yet; the threshold is untested against a real case, same epistemic status as any judgment-tagged gate before its first fire.
- Claim 3: spine self-correction procedure named in PHILOSOPHY.md — Decision: change-to-X (new paragraph) — Confirmed: yes, 2026-07-08. Supersedes the `Pending triggers:` field proposal discussed earlier this session — that proposal is not built, replaced before it shipped.
- Claim 4: staleness-check script and promise→promise graph explicitly deferred — Decision: preserve (do not build) — Confirmed: yes, 2026-07-08.

## Open questions
None — all four claims confirmed this session, no ambiguity deferred.

## Harness-change notes
No `Schema deps:` or playwright verification block applies (per `ari-argue-rhetoric/SKILL.md`'s harness-change classification note). No GATE-SCHEMA fire. GATE-TELOS conditional backstop: not triggered.

## Disposition
This contract authorizes the `ari-map/SKILL.md` Output-section edit (claims 1-2) and the `PHILOSOPHY.md` procedure paragraph (claim 3). PIN-25's item (c) is spun out to its own pin (PIN-37) per existing practice (PIN-26 was spun the same way from PIN-25). Claim 4's deferrals are recorded, not built — a future pin should re-open them only against a real case (a hand-audited spine for the staleness script; a real N-leg ripple for the graph), not speculatively.
