## Blip: Claims 1/3 and 2/6 shared a commit each
Severity: info
Location: `.claude/skills/ari-arete/SKILL.md` (Claims 1+3), `.claude/skills/ari-arete-pan/SKILL.md` (Claims 2+6)
What happened: Contract Claim 3 (arete-statement artifact template) has no separable file existence apart from Claim 1's own skill file — it *is* that skill's Output section. Same relationship between Claim 6 (adjacency-not-mode statement) and Claim 2's skill file (Claim 6 is that skill's own Active orientations content). Committed each pair together rather than forcing an artificial split of one file's content across two commits.
Why: `ari-code-rhetoric/SKILL.md`'s own commit-discipline rule states "if a claim spans multiple files, they commit together — the claim is the unit, not the file" — the inverse case (two claims with no independent file existence, sharing one file) isn't explicitly covered, but the same principle (claim is the unit, not an artificial file-split) applies by extension.
Downstream consequence: A future reader diffing `git log` against the contract's claim list will find two commits, not six, for these four claims. This is by design, not a discipline lapse — noted here so it reads as a decision, not an oversight.
Contracting failure?: n/a — this is a structural fact about where the contract's claims live (co-located by definition), not something ari-argue-rhetoric could have contracted around differently.

## Blip: Opportunistic fix of pre-existing ari-diagnose doc-roster gaps
Severity: info
Location: `README.md` ("Nine skills" section, new `/ari-diagnose` blurb), `.anima-lite/spine-anima-lite/material.md` §2/§7/§9, `.anima-lite/spine-anima-lite/efficient.md` §2
What happened: While updating skill counts from six to reflect the two new arete skills, found that `ari-diagnose` (built earlier, PIN-39) had never been added to README.md's skill-blurb list, `material.md`'s runtime skill count, its §7 artifact-inventory table, or `efficient.md`'s key-targets list — all four already undercounted before this workstream touched them. Fixed all four in the same edit rather than landing a "seven, going on eight" count that would still be wrong.
Why: `HARNESS.md`'s own bidirectional-audit rule — "any skill that reads README.md/CLAUDE.md/HARNESS.md... and finds it disagrees with observed disk state fires a fast-lane backlog pin immediately... doc drift is a finding, not a distraction." Fixing a one-line count/list entry discovered mid-edit, in the same file already being touched for this contract's own claims, is cheaper and more honest than leaving a freshly-wrong number next to a freshly-right one.
Downstream consequence: Skill-roster counts (README, HARNESS.md §4, material.md, efficient.md) now agree at nine, consistently, rather than at eight-missing-one in some places and six-missing-three in others.
Contracting failure?: n/a — this predates the arete-skills contract entirely (ari-diagnose was built under a different contract, PIN-39) and wasn't something this contract could have named in advance; it surfaced only because these exact files were already open for the arete count update.

## Blip: CLAUDE.md's Skills-list intro sentence left untouched
Severity: info
Location: `CLAUDE.md:3` — "Porting features... is the work-type currently built"
What happened: Noticed this line is stale relative to the actual skill roster (port, harness-change, and now single-repo arete are all "built" to varying degrees; ripple and debt-work are "built partway" per the spine) but did not rewrite it.
Why: Out of scope for this contract's six claims — none of them touch this specific sentence, and it was already stale before this workstream started (independent of arete). Rewriting it correctly requires a judgment call about how to summarize five work-types' build status in one sentence, which is its own small piece of work, not a side effect of adding two skills.
Downstream consequence: The line remains misleading until addressed on its own.
Contracting failure?: n/a — pre-existing, out of this contract's scope.
Spine promise touched: none — no `lives-in:` tag names this line.
