# Open questions — scaffold backbone contract (pin45-46-scaffold-backbone)

Source: `contract.md` (DRAFT), drafted by the argue-rhetoric subagent from `intent.md`'s 7 claims.
Answer inline under each question. Nothing in `contract.md` goes from DRAFT to FROZEN until
every claim below is confirmed and every open question is answered or explicitly deferred.

Per `spine-anima-lite/telos.md` §2: never bundle claim confirmations — each is its own decision,
even though they're listed together here for ease of answering.

---

## Claim confirmations (confirm, amend, or reject each)

**1. `scaffold.md` is a fifth upfront spine file.**
Tabular, markdown-native: one table per scenario, one row per `(scenario, path, step)`, three
columns (formal/material/efficient cell content). Happy path is the default table; other paths
get rows only where they diverge.

> Answer: yes

**2. Skeleton, not flesh — refresh, never accrete.**
`scaffold.md` follows the same comprehensive-by-intent, exactly-one-per-repo, refreshed-not-
accreted discipline as the other four spine files. The feature ledger stays the only accretive
artifact in this family.

> Answer: yes

**3. Always produced by `ari-map`, depth-gated not existence-gated.**
Every probe produces a `scaffold.md`, minimum stub:1 (scenarios named, cells unfilled). A
system-level arete founding pass must reach stub:2/3 (cells filled). Component-level depth is a
judgment call.

> Answer: good

**4. `ari-arete-pan`'s cut judges against the scaffold as evidence, not a second verdict axis.**
A unit tangled/unattributable in the scaffold is signal feeding the existing nugget/ore/slag call
— not an independent pass/fail dimension.

> Answer: yeah good

**5. `ledger-spec.md` gains a bidirectional rooting field (sharpened this round, see below), and
the ledger's home corrects from "the anima-lite root" to "the project's core repo."**
Rooting field: single-source entry gets `Scaffold coordinates: <scenario>/<path>/<step>[, ...]`
(present when the repo has a scaffold, absent — not "none" — when it doesn't); `ari-map` owns
writing this at probe time, not `ari-code-rhetoric`'s enrichment pass. Shared-origin (ripple)
entries get `Per-leg scaffold coordinates:` — one bullet per leg, since each leg has its own
repo-scoped scaffold. A filled scaffold cell gains the reverse pointer `Filled by:
features/<slug>.md`.
Ledger home: `ledger-spec.md` line 7's "the anima-lite root" is a tool-global bucket pooling every
project this tool has touched — corrected to "the project's core repo" (PIN-47 item 5, amended
this session: core-project-repo generalizes from arete-only to universal, with a single-codebase
collapse rule — one codebase's own `.anima-lite/` *is* the core repo, no redundant empty repo).
No behavior change for anima-lite's own self-harness-change work (already collapses); fixes
cross-project pooling for multi-repo projects.

> Answer: ownership + per-leg shape — yah good. ledger-home correction — yah good.

**6. Telos-growth propagates through the backbone via ripple's two-tier reopen, borrowed directly.**
Tier 1: every cascaded component statement and every scaffold scenario gets a mandatory
reconsideration pass on a ratified growth event, logged even when no-rework-needed. Tier 2: only
re-founding/re-walking where tier-1 judgment concludes the scenario actually depended on what
changed.

> Answer: yeah sure. 

**7. `scaffold.md`'s documentation must explicitly state its relationship to the four-cause frame
(not a fifth cause).**
Wherever `scaffold.md` is introduced, the doc must say plainly it's a coordinate backbone the
material/formal/efficient cells attach to per `(scenario, path, step)` — not a fifth Aristotelian
cause. Agent flagged this as borderline substrate/claim (see OQ7) rather than force-classifying.

> Answer: i meean not literally everywhere. just where it's important for a reader to understand anima-lite's operations

---

## Open questions

**OQ1 — Claim 3 scope-expansion cost.** Does "always produced, depth-gated" apply retroactively
(every existing `spine-<label>/` needs a `scaffold.md` backfilled at next refresh) or forward-only
(new probes from this point on)?

> Answer: backfill

**OQ2 — stub:0–3 field on the scaffold table itself.** `intent.md` names this "proposed, not yet
ratified" and defers it; `contract.md` keeps it deferred, not adopted as an 8th claim. Confirming
the deferral, or pulling it in now?

> Answer: discuss

**OQ3 — Claim 4: where does scaffold-derived evidence get recorded in `cut.md`?** Inside each ore
item's existing `Pressure:` field (informal, prose), or a new named field in `cut.md`'s own spec?

> Answer: discuss

**OQ4 — Claim 5: cardinality of `Filled by:`.** Can one scaffold cell's `Filled by:` name multiple
ledger slugs (several features converging on the same tangled step — exactly the case Claim 4
exists to surface), or is it constrained to one?

> Answer: discuss

**OQ5 — Claim 5: honesty vocabulary parity with `ledger-spec.md`'s "not traced" discipline.**
Should an *unfilled* cell (stub:1, not yet reached) read `not traced`, distinct from a
*divergent-path gap* (Claim 1's "empty column = a gap, not a missing row")? Two different kinds of
empty risk collapsing into the same blank cell if not distinguished.

> Answer: discuss, but leaning distinct

**OQ6 — Claim 6: what artifact receives the tier-1 reconsideration log?** Resolved as: deferred
to PIN-49. Ripple's ruling 4 doesn't name a dedicated artifact either — it logs inline into the
ordinary contract-amendment record. Discussion surfaced that a blip is already the harness's one
working instance of the coordinate+closed-taxonomy+triggered+append-only shape this needs, but
scoped to one workstream (file:line, not a repo-wide scaffold coordinate) — and that both the
sensor reading (PIN-48) and this tier-1 judgment are new *species* of that same genus, which
"blip" doesn't yet have a name for. Captured as PIN-49 rather than decided here. This contract
does not name a log artifact for Claim 6 — it records the tier-1 reconsideration *procedure* as
confirmed (mandatory pass, logged even when no-rework-needed), with the log's concrete home
explicitly pending PIN-49's rename/genus work.

> Answer: resolved via PIN-49 (see above)

**OQ7 — Claim 7's substrate-vs-claim register.** Contract leans claim for safety. Does a future
doc site that introduces `scaffold.md` without the four-cause disclaimer count as a doc-drift
finding (claim violation, HARNESS.md-style) or a lower-stakes wording gap (substrate slip,
fix-when-noticed)?

> Answer: discuss

**OQ8 — HARNESS.md §2 spec-ownership.** Agent recommends a new row + new sibling file
`ari-map/scaffold-spec.md` (tabular shape doesn't fit the existing prose-spine row — same
reasoning that gave the feature ledger its own file) rather than folding into "Spine file
formats." Confirm the new-row-and-file approach, or fold in instead?

> Answer: yeah i like the row and file approach.

**OQ9 — Group A/C sequencing, now that Claim 5 depends on PIN-47 item 5.** This contract borrows
PIN-47 item 5's ruling (amended this session, not yet independently run through its own
argue-rhetoric pass) rather than waiting for Group C's full build. Confirming that's the right
call — Group A proceeds on the ratified *rule*, Group C's own contract still formally classifies
and confirms it later, independently, when scheduled?

> Answer: discuss

---

## Not yet asked, but worth flagging while this doc is open

- Claim 7's documentation obligation (once confirmed) needs a concrete list of *where* — at
  minimum `PHILOSOPHY.md`, `spine-<label>/telos.md` §3's cause-files list, and whichever
  `HARNESS.md` §2 row houses this (OQ8). Confirm that list is complete once OQ8 is answered.
~~~ hold this open