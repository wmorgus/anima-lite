# HARNESS.md — gate registry, spec ownership, enforcement levels

**Governing rule: operative text lives in the skill files where it fires; HARNESS.md holds metadata — inventory, ownership, enforcement level. Never duplicate behavioral prose here.** If a gate's body text or a spec's shape needs to change, edit it at the skill file (or support file) that owns it, then update this index if the ID, owner, or trigger changed. This file never becomes the second place a reader has to check to know what a gate does. This applies to human-facing docs too, not just skill specs — README.md, CLAUDE.md, and PHILOSOPHY.md each own facts nobody else restates; see §4.

**Bidirectional audit for docs — spine custody, not just hygiene.** Any skill or agent that reads README.md, CLAUDE.md, or HARNESS.md in the course of work and finds it disagrees with observed disk state fires a fast-lane backlog pin immediately — zero ceremony, per ari-backlog stub:0. This is not a cleanliness rule bolted onto the pipeline: every doc read is an audit *because* the spine — and these docs with it — is the product this harness custodians, not a disposable precondition consumed once per port (see `PHILOSOPHY.md`). Doc drift is a finding, not a distraction from the task at hand.

---

## Section 1 — Gate registry

Every required and optional gate currently defined across the four skill files, plus the one precondition that behaves as a gate without a callout box (GATE-HASH).

| ID | Name | Required/Optional | Owning skill | Trigger | Cleared by |
|---|---|---|---|---|---|
| GATE-TELOS | Telos conflict | Required | ari-argue | Feature's argument conflicts with the prod telos or don't-contradict rules (step 1) | User acknowledges the conflict, names it telos-error or scope-creep, and explicitly authorizes continuing |
| GATE-SCHEMA | Schema dependency | Required | ari-argue | A claim's declared `Schema deps:` resolves to zero prod classes/fields, checked before the contract is frozen (step 4c) | User resolves — drops the claim, amends it, or confirms the field exists under another name |
| GATE-HASH | Spine-hash mismatch | Required (inline precondition, no callout box) | ari-port | The contract's `Spine commit:` hash doesn't match the current `Commit:` of the spine(s) relevant to this work item's comparison — two for a port (`spine-proto/telos.md`), one for single-repo debt work (the repo's own spine), zero additional for a pure world-drift check (precondition 3) | User confirms the contract still holds, or a quick re-pass through ari-argue is run |
| GATE-BLOCKERS | Plan blockers | Required | ari-port | Execution plan's `## Blockers` section is non-empty (Step 1) | Every listed blocker is explicitly cleared with the user before the execution subagent is spawned |
| GATE-BREAK | CONTRACT-BREAK | Required | ari-port | Execution subagent returns `contract_break: true` — contract actively contradicted by the real code (Step 2) | Ari-argue re-run completes and produces an amendment covering the uncovered case |
| GATE-BLIPS | Review-suggested blips | Required | ari-port | Validation agent returns PASS (pending review) — one or more `review-suggested` blips outstanding (Step 3) | User acknowledges each review-suggested blip individually |
| GATE-PR | PR creation | Required | ari-port | Reconcile step reaches the point of running `gh pr create` (Step 4f) | User gives explicit confirmation on the PR description and staged diff summary |
| GATE-SPINE-REVIEW | Spine review | Optional | ari-map | Spine files finished writing, before ari-argue runs | User reviews or explicitly skips |
| GATE-PLAN-REVIEW | Plan review | Optional | ari-port | Execution plan blockers cleared (or none existed), before execution begins (Step 1) | User reviews or explicitly skips |
| GATE-CATCHUP-REVIEW | Catch-up doc review | Optional | ari-port | Completeness-critic patches applied to the catch-up doc, before PR creation (Step 4e(ii)) | User reviews or explicitly skips |
| GATE-PIN-CLAIM | Claim-shaped pin | Optional | ari-backlog | A pin's Contract is classified claim-shaped during the slow-lane sweep (step 4) | User reviews the contract paragraph or explicitly skips |

**On GATE-HASH's inline form:** it is not written as a `> **⛔ REQUIRED GATE**` callout in ari-port's SKILL.md — it is stated as precondition 3's paragraph ("If mismatched... don't auto-fail or proceed silently... ask the user whether the contract still holds"). It is included here because it functions identically to a required gate: it halts the pipeline pending explicit user resolution. Skill authors should treat any precondition phrased this way as gate-registry material even without the callout formatting.

---

## Section 2 — Spec ownership map

| Spec | Canonical location | Owner skill | Who else reads it |
|---|---|---|---|
| Feature-ledger spec | `.claude/skills/ari-map/ledger-spec.md` | ari-map | ari-port (Step 5, harvest) |
| Playwright verification spec | `.claude/skills/ari-argue/playwright-spec.md` | ari-argue | ari-port (Step 3, validation D/E) |
| Contract format | `.claude/skills/ari-argue/SKILL.md` (Output section) | ari-argue | ari-port (Inputs, all steps) |
| Blip format | `.claude/skills/ari-port/SKILL.md` (Output section) | ari-port | ari-argue (none — blips are downstream of it), validation agent |
| Pin format | `.claude/skills/ari-backlog/SKILL.md` (Pin format section) | ari-backlog | none — self-contained |
| Gate registry | `HARNESS.md` (this file, Section 1) | HARNESS.md | ari-map, ari-argue, ari-port, ari-backlog (all cite gate IDs inline) |
| Spine file formats | `.claude/skills/ari-map/SKILL.md` (Output section) | ari-map | ari-argue (Inputs), ari-port (Inputs) |
| Metrics artifact spec (run row, backlog-health row, session-cost row, summary.md) | `.claude/skills/ari-port/metrics-spec.md` | ari-port | ari-backlog (backlog-health row), SessionEnd hook (session-cost row), calibration diffs |

---

## Section 3 — Enforcement levels

Tags each harness discipline as `mechanical` (checkable by a hook or script, in principle) or `judgment` (prompt-only, no reliable mechanical check). This is a prioritized list for future hook work, not an implementation.

| Discipline | Owning skill | Level | Notes |
|---|---|---|---|
| Commit-shape discipline (substrate commits contain no claim logic) | ari-port | **mechanical** | **First hook candidate.** Structurally checkable: diff the substrate commit against a claim-logic pattern named in the contract. PIN-1's run3 failure (claim logic landed in the substrate commit) is direct evidence a prompt-only instruction was insufficient on its own. |
| Blip Why-citation presence | ari-port | **mechanical** | Checkable as a field-presence + pattern rule: the `Why:` field must be non-empty and contain either a `§` marker or the literal phrase "no spine section applies." |
| Contract hash-pinning | ari-argue / ari-port | **mechanical** | `Spine commit:` in the contract vs. `Commit:` in `spine-proto/telos.md` is a string comparison — GATE-HASH is already the halt condition; a hook could run this comparison automatically instead of relying on the agent to check it. |
| Stub-depth field honesty | ari-map | judgment | Whether a `stub:N` claim is actually confirmed in code (vs. asserted) requires reading the code, not just checking that the field is present. No mechanical proxy without re-running the probe. |
| Substrate/claim classification | ari-argue | judgment | Whether a detail is substrate or claim is the core epistemic judgment the harness exists to protect — there is no pattern-match substitute for "would a user notice a different promise." |
| Schema-dependency existence check (GATE-SCHEMA: each claim's declared `Schema deps:` resolves against prod `item/`/`dto/`/`enums/`) | ari-argue | **mechanical (resolve-check) / judgment (declaration completeness)** | The resolve-check is a string-existence grep — scriptable as a hook that reads a contract's `Schema deps:` lines and greps each against prod schema dirs, failing on zero hits. What is NOT mechanizable: whether the claim author *declared* every real dependency (an undeclared dep can't be checked). So the gate is a hybrid — mechanical on what's declared, judgment on completeness of the declaration. Hook candidate for the declared half. |
| Conservative default | ari-port / ari-backlog | judgment | Recognizing an uncovered case and choosing to preserve rather than guess is a judgment call in the moment; a hook can't detect an omission it doesn't know to look for. |
| Spine probe depth | ari-map | judgment | Whether the probe was deep enough (2+ representative files per pattern claim, grep-confirmed versions, etc.) is a completeness judgment, not a structural check. |
| Session-cost capture (main-agent token totals by model, per session) | ari-port (metrics-spec.md owns the shape) | **mechanical (IMPLEMENTED — `.claude/hooks/session-cost.py`)** | The first mechanical hook actually built, not just tagged as a candidate. A `SessionEnd` hook parses the session transcript and writes `.anima-lite/metrics/sessions/<date>-<session>.md`, distinct from the discipline hooks above (commit-shape, blip-citation, hash-pinning) which remain tagged-but-unbuilt. |
| Doc-drift check (README/CLAUDE.md layout-path strings match real `ports/<slug>/` pattern on disk; committed deployment configs match fresh generator output) | none (cross-cutting, human-facing docs) | **mechanical, UNBUILT** | Intended home is ari-backlog's slow-lane sweep (periodic), not a per-session hook: (a) checks that layout-path strings in README.md/CLAUDE.md match the real `ports/<slug>/{contract,blips,plan,catchup,pr}.md` pattern on disk; (b) checks committed deployment configs against fresh generator output — the generator itself is a separate pinned task, pending (see backlog PIN for deployment-config generator). Same status as the commit-shape/blip-citation/hash-pinning candidate rows above — not implemented. |

Hook implementation = future pin, except session-cost capture (above), which is implemented. Nothing else in this section is built; the remaining rows only tag candidates so future hook work has a prioritized starting list instead of starting from scratch.

---

## Section 4 — Human-facing doc ownership map

Metadata only, same discipline as Sections 1–3: each fact below has exactly one canonical home. Everyone else points to that home rather than restating the fact. If you find a doc carrying a second copy of a fact listed here, that's doc drift — see the bidirectional-audit rule above.

| Fact | Canonical home | What others do |
|---|---|---|
| Artifact layout `ports/<slug>/{contract,blips,plan,catchup,pr}.md` | Skill files (spine/contract/blip formats), indexed by HARNESS.md §2 | README.md points to HARNESS.md §2 instead of drawing the tree. **Rename pending:** the directory noun `ports/<slug>/` is ratified to become `work/<slug>/` (skill name `ari-port` stays as-is) — sequenced after run5's staged git state resolves. Disk is `ports/<slug>/` today; every doc stays accurate to that until the `git mv` lands. |
| Skill roster (4 skills) | README.md (narrative one-liners) + CLAUDE.md (command list) | Everyone else links to `.claude/skills/<name>/SKILL.md` rather than restating what a skill does |
| Gate registry (count + IDs) | HARNESS.md §1 | README.md states no count — points to "see HARNESS.md §1" |
| Gitignore/commit policy | CLAUDE.md + `.gitignore` itself | Nothing else states this fact |
| Target-repo paths | CLAUDE.md | Nothing else states paths |
| Run procedure/workflow narrative | README.md (prose + mermaid) | CLAUDE.md keeps a condensed command subset only |
| Four-causes lens | PHILOSOPHY.md (canonical narrative) | README.md and any deployment-config docs point to PHILOSOPHY.md rather than carrying independent condensed copies. Exception: ari-map/SKILL.md's copy is operative (it fires there) and is exempt from this rule. |
