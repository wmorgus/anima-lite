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
        AM1["enumerate repo"]
        AM2(["⟳ probe:material"])
        AM3(["⟳ probe:formal"])
        AM4(["⟳ probe:efficient"])
        AM5["synthesize → spine + feature stubs"]
        AM1 --> AM2 & AM3 & AM4 --> AM5
    end

    AM5 --> OPT1{{"◎ spine review"}}
    OPT1 --> ARIARGUE

    subgraph ARIARGUE["ari-argue"]
        AA(["⟳ argue subagent\nspines + proto source\n→ classify substrate / claim\n→ confirm each claim with user\n→ write contract"])
        TELOS{{"⛔ telos conflict?"}}
        AA --> TELOS
    end

    TELOS -- none --> HASHCHECK
    TELOS -- conflict --> USER

    HASHCHECK{{"⛔ spine hash mismatch?"}}
    HASHCHECK -- ok --> ARIPORT
    HASHCHECK -- mismatch → re-map --> ARIMAP

    subgraph ARIPORT["ari-port  ·  main agent"]
        AP1["Step 1 — plan.md"]
        BLOCKER{{"⛔ plan blockers?"}}
        OPT2{{"◎ plan review"}}
        AP2(["⟳ Step 2 — execution agent\nimplement · commit per claim · write blips"])
        BREAK{{"⛔ CONTRACT-BREAK?"}}
        AP3(["⟳ Step 3 — validation agent\n→ PASS / FAIL / PASS pending review"])
        BLIPS{{"⛔ review-suggested blips?"}}
        AP4["Step 4 — reconcile · PR draft"]
        AP5["Step 4e — catch-up doc"]
        AP6(["⟳ post-4e — completeness critic\nreads doc cold → gaps"])
        OPT3{{"◎ catch-up review"}}
        AP7["patch · present for PR approval"]
        AP8["Step 5 — harvest ledger"]

        AP1 --> BLOCKER
        BLOCKER -- clear --> OPT2 --> AP2
        BLOCKER -- blocked --> USER
        AP2 --> BREAK
        BREAK -- no break --> AP3
        BREAK -- break → re-argue --> ARIARGUE
        AP3 -- FAIL --> AP2
        AP3 -- PASS --> BLIPS
        BLIPS -- acknowledged --> AP4
        AP4 --> AP5 --> AP6 --> OPT3 --> AP7 --> AP8
    end

    AP7 --> PRGATE{{"⛔ PR creation"}}
    PRGATE -- approved --> GH(["👤 gh pr create"])
    PRGATE & GH --> AP8

    classDef sub   fill:#e8f4f8,stroke:#4a9aba,color:#1a3a4a
    classDef main  fill:#fff,stroke:#888,color:#222
    classDef user  fill:#f5f0ff,stroke:#8b6bbf,color:#3a1a6a
    classDef req   fill:#fdecea,stroke:#c0392b,color:#7b1a13
    classDef opt   fill:#fef9e7,stroke:#d4ac0d,color:#6b4c00

    class AM2,AM3,AM4,AA,AP2,AP3,AP6 sub
    class AM1,AM5,AP1,AP4,AP5,AP7,AP8 main
    class USER,GH user
    class TELOS,HASHCHECK,BLOCKER,BREAK,BLIPS,PRGATE req
    class OPT1,OPT2,OPT3 opt
```

| Shape | Meaning |
|---|---|
| White rectangle | Main agent step |
| Blue rounded | Subagent (clean context, isolated) |
| Red diamond `⛔` | Required human gate — pipeline halts |
| Yellow diamond `◎` | Optional human gate — user can inspect or skip |
| Purple | User action |

**Required gates (6):** telos conflict · spine hash mismatch · plan blockers · CONTRACT-BREAK · review-suggested blips · PR creation

**Optional gates (3):** spine review (first-time repos) · plan review · catch-up doc review

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
