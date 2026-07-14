# Execution Plan: arete work-type skills
Contract: .anima-lite/work/arete-skills/contract.md
Generated: 2026-07-14

## Claim changes
For each confirmed claim in the contract, in implementation order:

- **New skill `ari-arete`**: `.claude/skills/ari-arete/SKILL.md` (new file) — seed-context gate (hard precondition, one starting rule), draft→iterate→ratify statement-authoring process, cascade re-invocation per node. Frontmatter + full SKILL.md structure (Inputs/Preconditions/Active orientations/Process/Output/Escalation-Notes), matching the shape of `ari-diagnose/SKILL.md` and `ari-intake/SKILL.md` as the closest precedents (bare skill, asserts a fact/artifact rather than arguing a change).
- **New skill `ari-arete-pan`**: `.claude/skills/ari-arete-pan/SKILL.md` (new file) — nugget/ore/slag cut process, draft→iterate→ratify loop on the cut (amended ruling 5), batch-ratification gate, independent-entry-point precondition, explicit adjacency-not-mode statement re: `ari-diagnose`.
- **Arete statement artifact template**: designed inside `ari-arete/SKILL.md`'s own Output section (no separate spec file — same pattern as `ari-diagnose/SKILL.md` owning `diagnosis.md`'s template inline). States asserted-not-argued epistemic status explicitly, no `argued-by:` field.
- **Arete posture on `ari-argue-rhetoric`**: `.claude/skills/ari-argue-rhetoric/SKILL.md` — new `## Arete posture` section, placed after the existing "Harness-change classification" material inside the Process/Active-orientations area, following the same shape as the ripple and harness-change posture notes already in this file.
- **Arete posture on `ari-code-rhetoric`**: `.claude/skills/ari-code-rhetoric/SKILL.md` — new `## Arete posture` section, placed directly after the existing "Harness-change posture (PIN-41)" section, same shape (what's degraded / what isn't, relative to a normal port).
- **Cutover exclusion**: stated explicitly as a negative scope line inside `ari-arete`, `ari-arete-pan`, and both posture sections — not a separate file.
- **Adjacency-not-mode statement**: `ari-arete-pan/SKILL.md`'s own Active orientations section, in its own words (per contract: not satisfied by a bare cross-reference).

## Substrate translations
- `HARNESS.md` §1 (gate registry): add `GATE-SEED-CONTEXT` (ari-arete) and `GATE-ARETE-CUT` (ari-arete-pan) rows — metadata only, per HARNESS.md's own governing rule.
- `HARNESS.md` §2 (spec ownership map): add rows for the arete-statement artifact format (owner ari-arete) and the arete-cut artifact format (owner ari-arete-pan).
- `HARNESS.md` §4 (doc ownership map): update "Skill roster (6 skills)" → "(8 skills)".
- `CLAUDE.md` "## Skills" list: add two bullets (`ari-arete`, `ari-arete-pan`), same one-line style as the existing six.
- `README.md`: "## Six skills" → "## Eight skills", add two skill blurbs in the existing style. Mermaid diagram in README.md is explicitly NOT touched — PIN-42 already owns "each work-type gets its own flowchart"; folding an 8th/9th node into the existing dense diagram is exactly what that pin exists to prevent doing ad hoc.
- `.anima-lite/spine-anima-lite/telos.md` §1: add arete to the ratified-direction work-type list.
- `.anima-lite/spine-anima-lite/formal.md` §1/§3: "Six skills" → "Eight skills"; add per-skill stratum entries for `ari-arete`, `ari-arete-pan`; add posture-seam notes for the two edited skills.
- `.anima-lite/spine-anima-lite/material.md` §2, §3, §9: skill count in runtime note; deployment-target file list; work-types vocabulary line; gate-count line (9 required → 11 required).
- `.anima-lite/spine-anima-lite/efficient.md` §2: "six invocable skills" → "eight invocable skills."

## Order of operations
1. Write `ari-arete/SKILL.md` — no dependency on anything else new.
2. Write `ari-arete-pan/SKILL.md` — references `ari-arete`'s statement artifact by name; written second so the reference is concrete, not forward-looking.
3. Add arete posture to `ari-argue-rhetoric/SKILL.md` — references both new skills' hand-off shape.
4. Add arete posture to `ari-code-rhetoric/SKILL.md` — same reason.
5. `HARNESS.md` registry/spec-ownership/doc-ownership updates — done last among docs since it indexes facts fixed by steps 1-4.
6. `CLAUDE.md`, `README.md` — skill-roster surface, done after HARNESS.md so counts are consistent.
7. Spine refresh (`telos.md`, `formal.md`, `material.md`, `efficient.md`) — done last, as the observation of everything above having landed.

## Blockers
None. All six claims confirmed in `contract.md`; no schema dependency or playwright block applies (harness-change).
