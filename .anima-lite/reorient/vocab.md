# Vocab review — identity reorientation (PIN-25 item a)

Scope: the term-by-term settlement identity.md's "Vocab review scope" table requires before any doc propagation. No file outside this doc is edited here. Method: occurrence inventory (grep, this repo, excluding `archive/` and `_run5_isolated/` as dead calibration snapshots unless noted) → tension analysis → recommendation, tagged SUBSTRATE-SHAPED (mechanical, no promise change) or CLAIM-SHAPED (changes what the harness promises its operator, needs Will's ratification).

Corpus-agnostic ruling in force: no corpus agent name (Pavel, Mnemosyne, Daedalus, Urania, Hephaestus, Clio) enters recommended vocabulary below. None were proposed; none appear.

---

## substrate

**Occurrence inventory.** 161 hits across 27 non-archive files. Two populations:
- **Load-bearing spec text** — PHILOSOPHY.md (defines the cut), README.md (restates it), CLAUDE.md (implicit), HARNESS.md (gate/enforcement rows reference it), all four `SKILL.md` files (ari-argue defines the classification, ari-port executes it, ari-map's formal.md is "the guide for idiom" substrate reads from, ari-backlog reuses it for pin classification), `.claude/agents/ari-lite.md`, both IDE mirrors (`.windsurf/rules/*.md`, `.github/copilot-instructions.md`).
- **Committed artifact instances** — every `contract.md`, `plan.md`, `blips.md` under `.anima-lite/ports/<slug>/` and `.anima-lite/_run5_isolated/ports/<slug>/` uses "substrate" as a section header and classification value (`## Substrate changes (free to translate)`, `Substrate — <spine citation>`). `spine-*/formal.md` and `spine-*/telos.md` files use it as the frame the whole cause file is organized around.

**Tension.** anima-corps logic.md §8.4 names "substrate debt" as code↔world drift — security landscape, dependency EOL, platform deprecation: the *because* is intact but the external world moved past the code. anima-lite's "substrate" is the near-opposite: the medium, free to change, precisely because it carries no promise. One is "this is stable and argument-preserving to touch," the other is "this has silently rotted relative to the world." Same word, opposite valence. identity.md's diagnosis-layer table already renames the corpus primitive "world-drift" for this reason (§8.4 footnote), leaving anima-lite's own substrate/claim cut untouched.

**Pressure-test of the provisional ruling.** The ruling is: keep anima-lite's substrate/claim, import the debt primitive as world-drift. Arguments for keeping:
- anima-lite's substrate/claim is the *authorization* cut — every contract, blip, and pin format is built on it. It is committed, versioned artifact vocabulary across every `ports/<slug>/contract.md` on disk. Renaming it is not a doc edit; it is a format migration across every historical artifact, or a permanent two-name split between old and new artifacts.
- anima-lite's usage predates and is unrelated to the corpus's; the collision is discovered, not designed. The corpus term is the newcomer to anima-lite's vocabulary (via the diagnosis-layer import), not vice versa — so the newcomer should be the one that adapts its name on entry, which is exactly what "world-drift" does.
- The two meanings don't actually compete for use in the same sentence once world-drift is named: anima-lite's substrate answers "is this a promise-change," the imported primitive answers "did the world move past this argument." Different question, and now different word.

Arguments against (pressure): a reader who knows the corpus (Will, and any future corpus-literate operator) will hit "substrate" in anima-lite's PHILOSOPHY.md and briefly load the wrong meaning before context corrects them. This is a real but one-time cost per new reader, not a running cost — once PHILOSOPHY.md's cut is read, "substrate" locks to anima-lite's sense for that reader within this repo. The corpus and anima-lite are read in different sessions by design (anima-lite is corpus-agnostic per ruling 1); the collision only bites a reader holding both vocabularies in working memory at once, which is Will reviewing this doc and rare otherwise.

**Recommendation.** Keep anima-lite's substrate/claim unchanged. Import the corpus's fourth primitive as **world-drift**, already done in identity.md's table — propagate that naming, don't re-open it. The ruling holds under pressure: the rename cost (every artifact format on disk) dominates the collision cost (a momentary misread by a bilingual reader), and the fix for the collision cost is a single clarifying line, not a rename.

**Tag: CLAIM-SHAPED** (the ruling itself — whether to keep or rename — is a decision about what anima-lite's core vocabulary means; already decided in identity.md's rulings, but restated here for ratification since it's the one true collision in the table). If ratified as stated, propagation itself (adding a one-line disambiguation note to PHILOSOPHY.md where the cut is defined, and using "world-drift" consistently in the new diagnosis-layer prose) is **SUBSTRATE-SHAPED** — mechanical, no change to what anima-lite promises.

**Rename cost if reversed (i.e. if Will instead wants anima-lite's substrate renamed):** every file in the load-bearing list above, plus a mechanical find-replace across all committed contracts/plans/blips/spines (12+ artifact files today, growing with every future port), plus both IDE mirrors. Old artifacts would either need retroactive rewrite (defeats "contract as inspectable receipt" — receipts shouldn't be edited after the fact) or the harness would carry two names for one concept across its history. Not recommended.

---

## port / ari-port / ports/<slug>/ layout / "port toolkit" self-description

**Occurrence inventory.** "port" (word-boundary) appears in 58 files; "ari-port" in 41 files; the `ports/<slug>/` directory pattern is real committed layout at `.anima-lite/ports/{main,recommend-sessions,weekly-report}/` (plus `_run5_isolated/ports/...`, a calibration snapshot). Self-description "port toolkit" / "Argument-preserving port toolkit" is the opening line of both README.md and CLAUDE.md, and `.github/copilot-instructions.md`.

**Tension.** identity.md ruling: "port becomes one work-type among several" — alongside intent-from-meeting, intent-from-moving-world (CVE/EOL/deprecation), intent-from-craft-ideal. The skill name `ari-port`, the artifact directory `ports/<slug>/`, and the repo tagline all name the narrower, superseded identity. A debt-diagnosis session ("fix this CVE") would currently have to write its artifacts into a directory literally called `ports/` and run a skill literally named `ari-port` to translate the confirmed claim into code — a work-type mismatch baked into the noun.

**Rename options and honest cost.**
1. **Keep `ari-port`/`ports/<slug>/` as-is; document port as one work-type among several.** Zero file-touch cost. Cost is conceptual friction: every non-port work item (CVE fix, craft cleanup) still lands in a directory called `ports/` and runs a skill called `ari-port`. Mirrors the same "term outgrew but still functions" situation as `spine` (below) — arguably fine if "port" is reinterpreted at the doc level as "the boundary-crossing execution step," analogous to how "argue" already means "classify and confirm," not literally "argue."
2. **Rename the skill and directory** (e.g. `ari-execute` / `execute/<slug>/`, or `ari-work`/`work/<slug>/`). Cost: skill directory rename (`.claude/skills/ari-port/` → new name, and its two support files `metrics-spec.md`, and cross-references to it in HARNESS.md §1–§4, README.md, CLAUDE.md, PHILOSOPHY.md is silent on it, both IDE mirrors, `.claude/agents/ari-lite.md`) — roughly 10 files with load-bearing cross-references, not counting the artifact layout. **Committed-artifact compatibility break**: every existing `.anima-lite/ports/<slug>/{contract,blips,plan,catchup,pr}.md` would need either a directory rename (mechanical, `git mv`, preserves history) or a permanent split between old `ports/` and new `<newname>/` trees. A directory rename is comparatively cheap because it's one `git mv` per slug, not a content rewrite — lower cost than the substrate rename above.
3. **Keep `ari-port` as the literal skill name (it does still port most of the time) but generalize the directory noun only** — e.g. keep `ari-port` skill, rename `ports/<slug>/` to `work/<slug>/` or `items/<slug>/`. Splits the skill-name question from the layout-noun question; lets the more entrenched piece (skill name, which is also the slash-command users type) stay stable while the newer, more mechanical piece (a directory string) generalizes. Cost: directory rename only, ~3 slugs today via `git mv`, plus every doc that states the layout path (HARNESS.md §4 table explicitly owns this fact — "Artifact layout `ports/<slug>/...`" — one edit point per the doc-ownership map, which is designed for exactly this kind of change).

**Recommendation.** Option 3. The skill name `ari-port` is a spoken/typed command (`/ari-port`) with real muscle-memory and cross-tool cost (IDE mirrors, agent definitions) disproportionate to the naming precision gained; keep it, and let "port" inside anima-lite mean "the execution step that moves confirmed intent into code," which is already almost how it is used (ari-port's own SKILL.md opens "Performs the code translation... Logs every meaningful translation decision" — generic enough). Generalize only the directory noun, since HARNESS.md §4 already centralizes that fact in exactly one place, making the edit cheap and low-risk. Candidate noun: `work/<slug>/` (matches "every work item is intent crossing a boundary," identity.md's own phrase) or `items/<slug>/`.

**Tag: CLAIM-SHAPED.** This changes what the harness's central noun means to an operator — whether "porting" is the literal job or the historical special case — and touches the doc-ownership map's canonical fact. Needs Will's ratification before any edit (see Decision 2 below).

---

## proto / prod spine labels

**Occurrence inventory.** "proto" in 45 files (207 raw hits), "prod" in 47 files (232 raw hits). Committed spine directories: `spine-proto/`, `spine-prod/` (the two-repo port pair) and `spine-anima-lite/` (already a precedent for a non-proto/prod label — ari-map's own SKILL.md explicitly says "any slug... `proto` and `prod` are conventional... arbitrary labels like `anima-lite` are valid"). ari-argue and ari-port SKILL.md files structurally assume exactly two spines (`spine-proto/`, `spine-prod/`) in their Inputs sections and precondition checks ("Both `spine-proto/` and `spine-prod/` directories exist...").

**Tension.** identity.md: "spine labels assume a two-repo pairing; debt work is single-repo." A CVE fix or craft cleanup operates on one repo with one spine — there is no "proto" to argue against, only the repo's own spine and the world (or the ideal of well-made code) as the second term of comparison. The *label scheme* (not the spine mechanism) is two-repo-shaped: ari-argue's precondition literally checks for two named directories.

**Generalization needed.** The mechanism already supports arbitrary labels (`spine-anima-lite/` proves it — anima-lite mapped itself under its own name, single-repo, no pairing). What's missing is *ari-argue's and ari-port's process logic*, which hardcodes "both spine-proto and spine-prod must exist" as a precondition rather than "the spine(s) relevant to this work item must exist." For single-repo debt work, the relevant spines are: the repo's own spine (playing the "prod" role — the thing being changed) and, when the divergence is spec/epistemic, whatever upstream artifact stands in for "proto" (a stale doc, an old ticket, nothing at all if the divergence is world-drift or craft, which compare the repo against the world or an ideal rather than against a second repo).

**Recommendation.** Don't rename the *labels* — `proto`/`prod` remain the right words for the two-repo port pairing, and the mechanism already supports arbitrary single labels for other cases. Generalize the *precondition language* in ari-argue/SKILL.md and ari-port/SKILL.md from "both spine-proto/ and spine-prod/ must exist" to something like "the spine(s) relevant to this work item's comparison must exist and be current — two for a port (proto/prod), one for single-repo debt work (the repo's own spine), zero additional spines for a pure world-drift check (the comparison is against the world, not another spine)." This is a precondition-text edit in two SKILL.md files plus their HARNESS.md gate-registry rows (GATE-HASH's trigger text names `spine-proto/telos.md` specifically), not a rename of any committed artifact — existing `spine-proto/`/`spine-prod/`/`spine-anima-lite/` directories need no changes.

**Tag: CLAIM-SHAPED.** Changes what ari-argue/ari-port promise to check before proceeding — a precondition is a gate, and gates are exactly the kind of thing this harness requires explicit ratification to alter (HARNESS.md §1's own discipline). See Decision 3.

---

## spine

**Occurrence inventory.** 274 raw hits across 26 non-archive files — the single most pervasive term in the harness. Committed directories `spine-proto/`, `spine-prod/`, `spine-anima-lite/`, each with `telos.md`/`material.md`/`formal.md`/`efficient.md`.

**What must change.** identity.md: "spine survives, promoted from precondition to product — docs must reflect the promotion." Currently every doc frames the spine as an input consumed once per port and then discarded in spirit (ari-map's own preconditions: "invoke when... `telos.md`'s Commit hash doesn't match HEAD" — refresh-on-demand). The promotion requires:
- README.md's Map section and "Why four causes?" section currently frame the spine purely as ari-argue/ari-port's input. Needs a line stating the spine is itself the durable asset, not just fuel for a port.
- HARNESS.md's bidirectional-audit rule (§ intro, already quoted in identity.md as "spine custody in embryo") needs promotion language — from "hygiene rule" framing to "this is spine maintenance, core function," per identity.md's own text.
- ari-map's SKILL.md preconditions section is written entirely in refresh-on-demand terms ("Invoke this skill when any of the following hold: ... does not match current HEAD..."). identity.md's ruling 3 (incremental spine maintenance, update-on-change, confirmed direction) is *new machinery this skill doesn't have yet* — not a wording fix. The vocab review's job stops at flagging this; building update-on-change maintenance is separate contracted work, not a doc-language change.

**Recommendation.** The word "spine" itself needs no change — it already reads correctly as "the four-cause map," and identity.md's promotion doesn't change what a spine *is*, only what it's *for* (product, not precondition). Doc-language edits needed: README.md, HARNESS.md's audit-rule framing, and CLAUDE.md's Artifacts section ("Everything under `.anima-lite/` is committed durable state — spines, and per-slug port artifacts" already gets this half right by listing spines as durable state alongside ports; it doesn't yet say spines are the *product*). The machinery gap (incremental maintenance) is out of scope for vocab review — flag as a backlog dependency, not a wording task.

**Tag: CLAIM-SHAPED** for the promotion framing itself (changes what the harness tells an operator the spine is for — precondition vs. product is a promise about priority and investment), **SUBSTRATE-SHAPED** for the mechanical edit once the framing decision is ratified (find the "precondition" framing sentences in README/HARNESS/CLAUDE and replace with "product" framing — no artifact format changes, no new machinery). See Decision 4.

---

## contract / blip / claim

**Occurrence inventory.** contract: 301 hits / 38 files. blip: 175 hits / 30 files. claim: 344 hits / 41 files. All three are the most load-bearing formats in the harness — contract is ari-argue's Output format, blip is ari-port's Output format (with mandatory `Why:`/`Contracting failure?:` fields), claim is the unit both are built around ("Claim changes (confirmed with user)" is a contract section header verbatim; blips carry `Contracting failure?:` referencing claims).

**Read under the wider identity.** All three still read correctly, with no strain found:
- **claim** — "the argument itself... what the user relies on" (PHILOSOPHY.md) generalizes cleanly to non-port work: a CVE fix's claim changes are exactly as real (does patching this dependency change what a user could previously rely on?) as a port's. No change needed.
- **contract** — "branch-scoped... every classification cites the spine section it rests on" generalizes without strain: a debt-diagnosis session still produces a frozen, cited decision record before code moves. The one place to watch (not a strain, a note): ari-argue's contract template's "## The argument" field currently reads "what is this feature claiming to the user" — under the wider identity this should silently generalize to "what is this *work item* claiming," since not every work item is a feature (a CVE fix has no user-facing "feature" but still has claims — e.g. "users can no longer submit the vulnerable form field unescaped" is a claim change even with no visible feature). This is a template wording tweak, not a structural change.
- **blip** — "logged whenever... something uncovered by the contract came up" is work-type-agnostic already; a blip during a craft-cleanup session works exactly the same way. No change needed.

**Recommendation.** No renames. One template wording note for ari-argue's contract Output section ("feature" → "work item" in the argument-statement field) to keep the template's own language from silently narrowing back to the old identity even after the surrounding docs are updated.

**Tag: SUBSTRATE-SHAPED.** These three words already mean what the wider identity needs them to mean; the one edit is a template-field label matching an already-ratified promotion, not a new promise.

---

## slop / divergence / janitor / added intent / added cruft

**Occurrence inventory.** All five are new — they exist only in identity.md itself (and backlog.md's PIN entries referencing it): slop (4 hits, 2 files), divergence (10 hits, 2 files), janitor (2 hits, 1 file), "added intent" (1 hit), "added cruft" (1 hit). None appear in any canonical doc (README/PHILOSOPHY/CLAUDE/HARNESS) or any skill file yet — they are pure talk-vocabulary from the reorientation conversation, not yet doc language anywhere.

**Which become canonical vs. stay presentation-layer.**
- **divergence** — this is the structural noun the whole identity shift rests on ("custodian of the alignment between what a codebase promises and what it actually is... detects divergence between promise and artifact"). It needs to be canonical doc language — it's the term PHILOSOPHY.md's expanded cut will be defined in terms of, playing the role "substrate/claim" currently plays alone. Recommend: canonical.
- **slop** — useful shorthand for one *instance* of divergence (fast-timescale, AI-authored) but the identity doc's own unifying claim is explicitly that slop and debt are "the same object" under one name (divergence). Keeping "slop" as a canonical doc noun re-introduces the two-word problem the unification was meant to dissolve — every canonical doc would need to say "slop-or-debt" or pick one. Recommend: presentation-layer only (fine in conversation, backlog pins, and rationale prose that explains the unification to a reader who arrived expecting "slop" or "debt" as separate concepts) — not a term any SKILL.md or gate name should be built on.
- **janitor** — vivid, memorable, and it's doing real work in identity.md's rhetoric ("the janitor doesn't care who left the mess"). But it names a *role* (an operator posture), not a structure the harness checks — it's closer to "the engineer is the claim court" (README/PHILOSOPHY's existing metaphor register) than to a term like "substrate" that a gate cites. Recommend: presentation-layer — keep it in narrative/rationale sections (README's "why" prose, PHILOSOPHY's commitments) as color, but don't build a skill name, gate ID, or artifact field around it.
- **added intent** — appears once, undefined beyond context (identity.md doesn't actually use this exact phrase — check: it's in the vocab-scope table itself as a term to review, not used elsewhere in the doc). This reads as a placeholder for "intent that got added beyond what was asked" — i.e., scope creep at the code level, already covered by ari-argue's existing "scope creep" routing at GATE-TELOS. Recommend: don't canonize a new term; if the concept needs a home, it already has one (scope creep, GATE-TELOS's existing vocabulary). Flag to Will: this term's referent may already be redundant with existing harness vocabulary — worth confirming it names something GATE-TELOS doesn't already cover before spending a canonical slot on it.
- **added cruft** — same situation as "added intent": one occurrence, in the scope table only, no defining use elsewhere in identity.md. Reads as a plain-language gloss for craft debt / accidental complexity (already the corpus's "craft" primitive, imported as-is per the diagnosis layer). Recommend: don't canonize; "craft" (imported unchanged from §8.6) already names this.

**Recommendation summary:** canonize **divergence** only. Keep slop and janitor as presentation-layer color (rationale prose, not skill/gate/field names). Do not canonize "added intent" or "added cruft" — both appear to be redundant glosses for concepts (scope creep, craft) the harness already names; confirm with Will whether either points at something genuinely uncovered before dropping them.

**Tag: CLAIM-SHAPED** for canonizing "divergence" (it becomes the noun PHILOSOPHY.md's core cut is redefined around — this is exactly the kind of promise-level vocabulary change the harness's own discipline requires surfacing one at a time). **SUBSTRATE-SHAPED, in fact a non-action,** for the rest (recommending they stay out of canonical docs is not a change to anything). See Decision 5.

---

## anima-lite / ari-* naming

**Brief take, lowest priority per identity.md's own ordering.** "anima-lite" still describes the thing reasonably — it's a lite, harness-only expression (ruling 1: "anima-lite is a harness-only expression... making no claim about the corpus's agent separation"), and "lite" already carries the right connotation of "no agent-role apparatus, markdown and skills only" independent of whether the scope is porting or custodianship. The `ari-*` skill-name prefix (ari-map, ari-argue, ari-port, ari-backlog) reads as an invented mnemonic, not tied to "port" specifically — no strain from the identity expansion. No rename recommended for either. This is not a decision that needs ratification; it's a non-finding.

**Tag: n/a — no change recommended, nothing to ratify.**

---

## Decisions needed

Numbered for Will to ratify one at a time. Each names the CLAIM-SHAPED question, the options, and the recommendation from above.

**RATIFIED 2026-07-07 (Will, one at a time via decision prompt): 1(a), 2(b), 3(b), 4(b), 5(a) — all recommendations accepted.** Vocabulary is settled; propagation (PIN-25 item b) is unblocked. Note for propagation sequencing: the `ports/` → `work/` git mv (decision 2) should not run while run5's staged renames are in flight — sequence it after run5 state is committed or resolved.

**Decision 1 — substrate/claim collision with corpus §8.4.**
Options: (a) keep anima-lite's substrate/claim as-is, import corpus's fourth primitive as "world-drift" [recommended — already stated in identity.md, this ratifies it against pressure-testing]; (b) rename anima-lite's substrate to something collision-free (cost: every committed contract/plan/blip/spine on disk, both IDE mirrors, all four skill files, PHILOSOPHY/README/CLAUDE/HARNESS).
Recommendation: (a).

**Decision 2 — port/ari-port/ports/<slug>/ generalization.**
Options: (a) keep both skill name and directory noun as-is, document "port" as one work-type among several at the doc level only, zero file touches; (b) rename only the directory noun (e.g. `ports/` → `work/`), keep `/ari-port` as the skill/command name [recommended]; (c) rename both skill and directory (highest cost — touches the slash-command surface, both IDE mirrors, and every cross-reference in HARNESS.md/README.md/CLAUDE.md).
Recommendation: (b).

**Decision 3 — proto/prod precondition generalization for single-repo debt work.**
Options: (a) leave ari-argue's/ari-port's "both spine-proto and spine-prod must exist" precondition untouched; single-repo debt work either fakes a second spine or the precondition text is simply wrong for that work-type and gets silently ignored [not recommended — silent precondition mismatch is exactly the failure mode this harness exists to prevent]; (b) generalize the precondition text to name the comparison-count per work-type (two spines for a port, one for single-repo debt work, zero additional for pure world-drift) [recommended] — edits ari-argue/SKILL.md, ari-port/SKILL.md, and HARNESS.md's GATE-HASH row; no committed-artifact renames.
Recommendation: (b).

**Decision 4 — spine's precondition-to-product promotion, doc language.**
Options: (a) don't touch existing "refresh-on-demand" framing in README/HARNESS/CLAUDE, let the promotion live only in identity.md until the incremental-maintenance machinery is actually built [defers the doc debt identity.md itself calls out]; (b) edit README's Map/four-causes framing, HARNESS's bidirectional-audit-rule intro, and CLAUDE's Artifacts section now, to state the spine is the product, while noting incremental maintenance as "direction, not yet built" [recommended] — pure wording, no new gates, no artifact-format change.
Recommendation: (b).

**Decision 5 — canonizing "divergence" as core vocabulary.**
Options: (a) canonize "divergence" in PHILOSOPHY.md as the noun the substrate/claim cut and the new diagnosis layer both serve [recommended]; (b) don't canonize any new term yet, keep "divergence"/"slop"/"janitor" as talk-vocabulary only until the diagnosis-layer machinery itself is built, and canonize together with that work.
Recommendation: (a) for "divergence" specifically — it is the connective tissue the whole reorientation prose depends on and costs nothing to state now (it's additive, not a rename of anything existing). "Slop"/"janitor" can wait regardless — no decision needed for those (see term section above, no canonization recommended either way).
