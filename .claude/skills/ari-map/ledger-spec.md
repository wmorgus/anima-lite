# Feature ledger spec

Canonical spec for `.anima-lite/features/<slug>.md`. Referenced by ari-map (writes stubs) and ari-code-rhetoric (enriches to `stub:3`, Step 5). Edit here; both skills point to this file rather than restating the shape.

## Feature Ledger

Features live at `.anima-lite/features/<slug>.md` — at the anima-lite root, not under any repo spine. A cross-repo feature (a change spanning two webapps) has a natural home there; a single-repo feature declares its repo in the header. Spines do not contain features; spines reference them by slug.

The ledger is a different artifact from the spine. The spine answers "what is true repo-wide." The ledger answers "what is true about this one feature." The different-feature test is the boundary: an observation that passes the test lives in the spine; one that fails lives in the ledger.

Future mechanism (not required now): hash-controlled versioned copies per repo, so each port pins to the feature-doc version it used. Note the intent; do not build the versioning yet.

### Stub depth

ari-map creates a comprehensive feature map — every feature it can identify in the repo, stubbed as deep as it can decisively assert, no more. The failure mode is not the shallow stub. It is the dishonest stub: fields filled with assertions the agent cannot confirm. A shallow honest stub is a correct artifact; a deep dishonest one is a trap that reads as authority.

For domain-central features — those built on entities that recur across the repo (sessions, students, institutions, and similar) — ari-map should reach `stub:2` at probe time, not stop at `stub:1`. Field-depth deferred to ari-code-rhetoric's enrichment pass (`stub:3`) arrives after ari-argue-rhetoric has already frozen the contract; a claim built on a nonexistent field detonates late instead of getting caught at contract-time. `stub:2` at map-time puts the field-level truth in front of ari-argue-rhetoric while there's still time to act on it. This is required only where the probe can actually confirm the fields — the honest-stub rule is not relaxed by this: a dishonest `stub:2` (fields the probe didn't confirm) is worse than an honest `stub:1`. For features not built on a recurring entity, `stub:1` remains a fine stopping point at map-time.

Stub levels (use these exact labels in the file header):
- `stub:0` — feature identified, existence confirmed, nothing else
- `stub:1` — entry point confirmed (URL mapping → servlet or equivalent)
- `stub:2` — entry point + primary data structure confirmed (DTO class + key fields)
- `stub:3` — full observable chain confirmed by ari-map probe, or enriched by ari-code-rhetoric

At `stub:3`, the `source:` field distinguishes probe-confirmed from port-distilled. A reader trusting a `stub:3` entry must check `source:` before treating it as probe-grade.

Every field not yet confirmed is written as `not traced` — never left blank. Blank reads as absence; `not traced` reads as unknown. The distinction is load-bearing.

### Feature ledger file template

`.anima-lite/features/<slug>.md`:

~~~markdown
# Feature: <feature name>
slug: <feature-slug>
repo(s): <repo slug, or comma-separated for cross-repo features>
stub: <0|1|2|3>
source: <ari-map-probe | ari-code-rhetoric-enriched | manual>
prod-commit: <short hash at time of population>
goes-stale: <one line — what would invalidate this, e.g. "DTO schema change, servlet rename">

## Identity
<one sentence — what this feature does for the user. not traced if unconfirmed.>

## Entry points
<URL mapping → servlet/controller → template path; confirmed from routing config.
 not traced if unconfirmed.>

## Primary data structure
<DTO or equivalent class + key fields observed. not traced if unconfirmed.>

---
Everything below is enriched by ari-code-rhetoric after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
<entry → service → data layer → entity chain, with class names. not traced.>

## Client-side wiring
<JS/TS files involved, render function names, data binding pattern. not traced.>

## State machine
<if a multi-step user flow: states and transitions. not traced or n/a.>

## Feature gates
<flags, conditions, admin-only guards — anything that conditions availability.
 not traced or none.>

## Seam-specific protocols
<communication patterns unique to this feature's boundaries. Repo-wide seam
 protocols live in the spine, not here. not traced.>

## Known quirks
<observations that surprised — not general patterns. Each entry names the
 contract or blip it was distilled from. not traced or none.>

## Port provenance
<contract slug + prod commit hash this enrichment was distilled from. n/a until
 first port.>
~~~

### Shared-origin entries (ripple)

A feature born in N repos simultaneously — a ripple — is not "ported into" one repo from another; there is no source leg and no destination leg, only legs, all instituting the same promise from a single contract apex (`reorient/ripple.md` ruling 1). This entry type generalizes the ledger's default single-source-repo shape to that case, so the ledger doesn't misrepresent a shared-origin feature as if it had originated in one leg and traveled to the others.

**Header field.** `origin: <ported | shared-origin>`. `ported` is the default for every existing feature (single source, translated elsewhere, or single-repo) and is assumed when the field is absent — this keeps every pre-ripple ledger entry valid without a backfill pass. `shared-origin` marks a ripple-born feature.

**What changes in the body.** `repo(s):` lists every leg (not a source/destination pair). Any body section whose fact could plausibly differ by substrate splits into one bullet per leg, following the contract's own per-target substrate-mapping discipline (`ari-argue-rhetoric/SKILL.md` Output section) — one promise, N renderings. `Identity` stays single, exactly like the contract's `## Claim changes` section stays single: it is the one promise, not N descriptions of it.

~~~markdown
# Feature: <feature name>
slug: <feature-slug>
repo(s): <leg-a-slug>, <leg-b-slug>, <leg-n-slug>
origin: shared-origin
stub: <0|1|2|3>
source: <ari-code-rhetoric-enriched | manual>
prod-commit: n/a — see Per-leg commits below
goes-stale: <one line — what would invalidate this across ANY leg>

## Identity
<one sentence — the one promise every leg institutes. not traced if unconfirmed.>

## Per-leg entry points
- <leg-a-slug>: <URL mapping → servlet/controller → template path, or leg-equivalent>
- <leg-b-slug>: <leg-equivalent>
- <leg-n-slug>: <leg-equivalent>

## Per-leg primary data structure
- <leg-a-slug>: <DTO/entity/equivalent class + key fields observed>
- <leg-b-slug>: <leg-equivalent>
- <leg-n-slug>: <leg-equivalent>

---
Everything below is enriched by ari-code-rhetoric as each leg's execution completes.
At stub:0–2, all fields below are `not traced`.

## Per-leg data flow
- <leg-a-slug>: <entry → service → data layer → entity chain, with class names. not traced.>
- <leg-b-slug>: <leg-equivalent>

## Per-leg client-side wiring
- <leg-a-slug>: <JS/TS files, render function names, data binding pattern, or leg-equivalent. not traced.>
- <leg-b-slug>: <leg-equivalent>

## State machine
<if a multi-step user flow: states and transitions, named as one promise. Note per-leg
 only if the transitions genuinely differ by substrate; otherwise this stays single like
 Identity. not traced or n/a.>

## Per-leg feature gates
- <leg-a-slug>: <flags, conditions, admin-only guards. not traced or none.>
- <leg-b-slug>: <leg-equivalent>

## Seam-specific protocols
<communication patterns unique to this feature's boundaries, per leg where they differ.
 Repo-wide seam protocols live in the spine, not here. not traced.>

## Known quirks
<observations that surprised — not general patterns. Each entry names both the blip it
 was distilled from AND which leg(s) it applies to — a quirk found in one leg's
 rendering is never assumed to hold for the others. not traced or none.>

## Per-leg commits
<shared contract slug + one prod-commit hash per leg. n/a until the ripple's legs
 execute.>
~~~

### Field ownership

- **ari-map** populates at probe time: all header fields, Identity, Entry points, Primary data structure, and status markers (`not traced` on all unconfirmed fields). For domain-central features, `Primary data structure` is expected to be populated (confirmed key fields, not `not traced`) — that's what `stub:2` at map-time means; ari-map does not get to defer this field to ari-code-rhetoric just because it's more convenient to confirm later. This applies to `origin: ported` entries only — ari-map probes existing code, and a shared-origin feature has no existing code to probe before its legs execute.
- **ari-code-rhetoric** enriches after a port run: Full data flow, Client-side wiring, State machine, Feature gates, Seam-specific protocols, Known quirks, Port provenance — and updates `stub:`, `source:`, and `prod-commit:` to reflect the enrichment. For non-domain-central features left at `stub:1` by ari-map, ari-code-rhetoric's enrichment pass is still the first point `Primary data structure` gets confirmed — the split narrows, it doesn't disappear. For a `shared-origin` entry, ari-code-rhetoric originates the entry itself (there is no ari-map stub to enrich) as each leg completes execution, populating that leg's bullet in every per-leg section; the entry reaches full `stub:3` coverage only once every leg named in the contract apex has executed and contributed its bullet.
