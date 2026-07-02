# anima-lite

Argument-preserving feature port toolkit for Claude Code.

Ports a feature from a prototype repo to a production repo while preserving what the feature *argues* — not just what it does. Code is a structure of promises to a user. Translation has to preserve the promises, not just the mechanics.

See `PHILOSOPHY.md` for the core commitments.

---

## The key distinction

**Substrate** — the medium. Library swap, rename, file restructure, styling system. None of these change what the software promises. Translate freely.

**Claim** — the argument itself. Dropping a confirmation step, relaxing a validation, changing reversible to permanent, removing a gate. These change what the user relies on. Always confirmed explicitly, one at a time, never bundled.

When unsure: ask whether a user who understood the feature's promise would notice a difference in the promise. If yes — claim.

---

## Three skills

**`/ari-map`** — probe a repo and write a four-cause spine (material, formal, efficient, final). Run once for each repo in the port pair. Must be current before anything else runs.

**`/ari-argue`** — read both spines plus the feature, identify what it's arguing, classify every implementation detail as substrate or claim, and confirm claim changes with the user one at a time. Produces a branch-scoped contract.

**`/ari-port`** — four steps: plan → execute → validate → reconcile (+ harvest). Translates substrate freely, implements confirmed claims exactly, logs everything else as a blip. Halts back to ari-argue if the contract is actively contradicted by the real code.

---

## Execution flow

```mermaid
flowchart TD
    USER(["👤 User"]) --> ARIMAP

    subgraph ARIMAP["ari-map  ·  main agent"]
        AM1["probe: enumerate + read repo"]
        AM2(["⟳ probe:material"])
        AM3(["⟳ probe:formal"])
        AM4(["⟳ probe:efficient"])
        AM5["synthesize → write spine-label/\n+ feature ledger stubs"]

        AM1 --> AM2 & AM3 & AM4
        AM2 & AM3 & AM4 --> AM5
    end

    ARIMAP --> ARIARGUE

    subgraph ARIARGUE["ari-argue  ·  main agent"]
        AA1["read both spines + proto feature"]
        AA2{"claim change?"}
        AA3["confirm with user\n(one at a time)"]
        AA4["write contract"]

        AA1 --> AA2
        AA2 -- yes --> AA3 --> AA2
        AA2 -- all confirmed --> AA4
    end

    ARIARGUE --> ARIPORT

    subgraph ARIPORT["ari-port  ·  main agent"]
        AP1["Step 1 — write plan.md"]
        AP2(["⟳ Step 2 — execution agent\ncontract + spines + plan + proto source\n→ implement · commit per claim · write blips\n→ return: commits + blips + CONTRACT-BREAK?"])
        AP3(["⟳ Step 3 — validation agent\ncontract + blips + changed files\n→ PASS / FAIL / PASS pending review"])
        AP4["Step 4 — reconcile\nclean tree · draft PR description"]
        AP5["Step 4e — write catch-up doc"]
        AP6(["⟳ post-4e — completeness critic\nreads catch-up doc cold\n→ gaps that block a reviewer"])
        AP7["patch catch-up doc · present for approval"]
        AP8["Step 5 — harvest feature ledger → stub:3"]

        AP1 --> AP2 --> AP3
        AP3 -- FAIL --> AP2
        AP3 -- PASS --> AP4 --> AP5 --> AP6 --> AP7 --> AP8
    end

    AP7 --> USERAPPROVE(["👤 User approves\n→ gh pr create"])

    classDef sub fill:#e8f4f8,stroke:#4a9aba,color:#1a3a4a
    classDef main fill:#fff,stroke:#888,color:#222
    classDef user fill:#f5f0ff,stroke:#8b6bbf,color:#3a1a6a

    class AM2,AM3,AM4,AP2,AP3,AP6 sub
    class AM1,AM5,AA1,AA2,AA3,AA4,AP1,AP4,AP5,AP7,AP8 main
    class USER,USERAPPROVE user
```

**White** = main agent (carries full session context). **Blue** = subagent (clean context, isolated). **Purple** = user interaction.

Subagents are used where isolation is load-bearing (validator cannot share the execution agent's framing) or where work is genuinely parallel with no dependency chain (probe causes are independent).

---

## Artifacts

```
.anima-lite/
  spine-proto/              # four-cause spine of the prototype repo
    telos.md                # coding-agent entry point; commit-pinned
    material.md             # tech stack + dependencies
    formal.md               # architecture patterns + seam protocols
    efficient.md            # build/CI/deploy
  spine-prod/               # four-cause spine of the production repo
    (same structure)
  features/                 # feature ledger — stubs created by ari-map, enriched by ari-port
    <slug>.md               # stub:0–3; not traced on unconfirmed fields
  contracts/<branch>.md     # feature contract; frozen for session; branch-scoped
  plans/<branch>.md         # execution plan; written before any code moves
  blips/<branch>.md         # translation log with contracting-failure self-audit
  pr-<branch>.md            # PR description draft
  catchup-<branch>.md       # catch-up briefing for reviewer or review agent
```

Spines and feature ledger are committed — shared repo-level state. Contracts, blips, plans, PR drafts, and catch-up docs are gitignored — session artifacts.

Spine refresh collisions across branches surface as merge conflicts. That's intentional: two diverging mental models of the same repo should conflict explicitly.

---

## Running a port

```
/ari-map    path: ../proto-repo,          label: proto
/ari-map    path: ../../prod-repo,        label: prod
/ari-argue  feature: path/to/feature/dir
/ari-port
```

Invoke from the anima-lite root. Both target repos must be on disk. Spines must be current (commit hash in `telos.md` matches HEAD of the target repo) before ari-argue runs.
