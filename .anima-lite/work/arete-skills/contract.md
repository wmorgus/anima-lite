# Contract: arete work-type skills
Branch: arete-skills
Generated: 2026-07-14
Spine commit: 522e44b
Source of truth: n/a — harness-change, single source (`.anima-lite/reorient/arete.md` Part 2, rulings 1-11); no competing candidate design exists
Status: FROZEN FOR SESSION — do not modify without re-running ari-argue-rhetoric

## The argument
The harness gains a fifth work-type: founding a telos by iterative language for a repo that never had one on record, then judging existing code against it and rebuilding into a clean new repo — rather than reading a telos off code that already exists, the way every other work-type does.

## Substrate changes (free to translate)
- Exact prose/section wording, internal heading structure, and file-internal naming inside the two new `SKILL.md` files and the two posture additions — Harness-change classification: doc wording that doesn't change the invocation surface or a gate's rule is substrate, per `ari-argue-rhetoric/SKILL.md`'s Harness-change classification section. No spine section covers file-internal wording; classification is by that section's own stated rule.
- Which existing `SKILL.md` (`ari-diagnose`, `ari-intake`, `ari-read`) is cited as the structural precedent for a given piece of `ari-arete`/`ari-arete-pan` prose (e.g. borrowing `ari-read`'s "independent entry point" framing for ruling 11) — free choice of precedent, doesn't change what's promised.
- The concrete markdown field/shape of the arete-statement artifact template (explicitly left open by ruling 3/intent.md's Notes) — free to design, since ruling 2 fixes only its epistemic status (asserted, not argued), not its shape.
- The concrete starting seed-context best-practices rule beyond "must have an index file" is already fixed at exactly one rule by ruling 3 — no further rules are added here; this is substrate only in the sense that the exact prose stating that one rule is free to write, not that the list is free to grow during this workstream.

## Claim changes (confirmed with user)

- **New skill `ari-arete`** — Decision: build a bare (asserts, doesn't argue) skill holding: (a) a hard-precondition seed-context gate, starting rule list of exactly one item ("must have an index file"), explicitly not exhaustive; (b) an iterative draft-and-ratify process producing a caveman-dense arete statement — agent reads seed context, asks clarifications, drafts v1, operator/agent iterate by language, operator ratifies, statement commits; (c) cascade re-invocation per node — system-level statement authored first, then re-invoked per derived component, top-down. — Confirmed: yes, 2026-07-14
  Harness-change classification: Claim — new invocation surface (`/ari-arete`) and a new gate (seed-context precondition); per `ari-argue-rhetoric/SKILL.md`'s Harness-change classification section, a new gate rule is definitionally a claim, not substrate.

- **New skill `ari-arete-pan`** — Decision: build a bare skill that sorts an existing repo's code against an already-ratified arete statement into nugget (kept, still stated/confirmed via argue-rhetoric)/ore (real pressure recorded as a note, claim rewritten)/slag (discarded, no signal); holds its own batch-ratification gate over the full cut before any code moves, separate from argue-rhetoric's per-claim confirm; is an independent entry point whose precondition is "an arete statement exists for this repo," not "`ari-arete` just ran." — Confirmed: yes, 2026-07-14
  Harness-change classification: Claim — new invocation surface (`/ari-arete-pan`) and a new gate (batch-ratification before execution); same rule as above.

- **`ari-arete-pan`'s cut goes through an explicit draft→iterate→ratify loop before the batch gate fires** — Decision: the skill produces a draft cut (every item assigned nugget/ore/slag, ore carrying its pressure-note), presents it in full to the operator, and allows iteration — reassigning an item between buckets, sharpening an ore pressure-note — before the batch-ratification gate (above) fires on the stabilized result. The gate is not the operator's first exposure to the cut. This mirrors `ari-arete`'s own draft→iterate→ratify pattern for the statement itself (ruling 3) and does not reopen ruling 5's batch-not-per-item argument — it is still one gate, ratifying the whole cut once, only preceded by revision instead of arriving cold. — Confirmed: yes, 2026-07-14 (surfaced mid-session, amending ruling 5)
  Harness-change classification: Claim — changes the gate's own procedure (what must happen before it is allowed to fire), the same class of thing as the new-gate claims above.

- **The arete statement is a first-class artifact, not a variant of `intent.md`** — Decision: `ari-arete`'s output template states its epistemic status explicitly (asserted-as-standard, defended only by the operator's own conviction) and does not borrow `intent.md`'s `argued-by:` provenance shape, even though it is a sibling artifact in the sense of being first-class and committed. — Confirmed: yes, 2026-07-14
  Harness-change classification: Claim — this changes what the harness promises about how this artifact's authority is challenged (never by "show your source," only by re-opening the founding pass); an artifact-authority distinction, not wording.

- **Arete posture on `ari-argue-rhetoric` and `ari-code-rhetoric`** — Decision: add a posture section to each (same pattern as the existing ripple and harness-change posture sections already in both files) whose defining rule is: execution target is a new, empty repo built claim-by-claim — nuggets stated/confirmed as-is with no code change, ore rewritten from its recorded pressure-note — and the old repo is never a live edit target again, read only as `ari-map` evidence for the judgment. — Confirmed: yes, 2026-07-14
  Harness-change classification: Claim — changes what these two skills are allowed to target (a repo that does not yet contain the code being written, inverted from port's "translate into existing prod code" default) and what "old repo" means procedurally (read-only after judgment, never re-entered).

- **Cutover is permanently out of scope for every artifact built by this workstream** — Decision: none of `ari-arete`, `ari-arete-pan`, or the two posture additions may include deploy config, DNS/service-pointer changes, downstream-consumer migration, secrets, or CI migration steps, at any process step, in any version. — Confirmed: yes, 2026-07-14
  Harness-change classification: Claim — this is a scope boundary on what the work-type is allowed to do, the exact class of thing the Harness-change classification section names as claim-shaped ("a change to what a work-type is allowed to do or must check").

- **`ari-arete-pan`'s judgment is adjacent to `ari-diagnose` but not a mode of it** — Decision: `ari-arete-pan`'s own Active orientations (or equivalent section) must state the category distinction explicitly and in its own words — `ari-diagnose`'s four primitives (spec/epistemic/world-drift/craft) all presuppose an existing telos the code drifted from; arete's target code never had one to drift from. This is not satisfied by a cross-reference alone; the distinction must be load-bearing prose in the new skill, the same way `ari-read`'s Escalation/Notes states its own mirror relationship to `ari-intake` in its own words rather than only pointing at the other file. — Confirmed: yes, 2026-07-14
  Harness-change classification: Claim — this determines whether a future reader of the harness could mistake `ari-arete-pan` for a fifth `ari-diagnose` primitive; a category boundary the skill roster depends on being legible, not a wording choice.

## Open questions
None. All six claims confirmed as scoped in this session, matching `reorient/arete.md` rulings 1-11 exactly — no delta between the design record and this contract.

## Proto visual reference
n/a — harness-change, no running feature to navigate to.

## Playwright verification
n/a — harness-change posture (per `ari-argue-rhetoric/SKILL.md` Harness-change classification: "No Schema deps/playwright block applies... omit those sections rather than fabricating entries").
