# Feature ledger spec

Canonical spec for `.anima-lite/features/<slug>.md`. Referenced by ari-map (writes stubs) and ari-port (enriches to `stub:3`, Step 5). Edit here; both skills point to this file rather than restating the shape.

## Feature Ledger

Features live at `.anima-lite/features/<slug>.md` — at the anima-lite root, not under any repo spine. A cross-repo feature (a change spanning two webapps) has a natural home there; a single-repo feature declares its repo in the header. Spines do not contain features; spines reference them by slug.

The ledger is a different artifact from the spine. The spine answers "what is true repo-wide." The ledger answers "what is true about this one feature." The different-feature test is the boundary: an observation that passes the test lives in the spine; one that fails lives in the ledger.

Future mechanism (not required now): hash-controlled versioned copies per repo, so each port pins to the feature-doc version it used. Note the intent; do not build the versioning yet.

### Stub depth

ari-map creates a comprehensive feature map — every feature it can identify in the repo, stubbed as deep as it can decisively assert, no more. The failure mode is not the shallow stub. It is the dishonest stub: fields filled with assertions the agent cannot confirm. A shallow honest stub is a correct artifact; a deep dishonest one is a trap that reads as authority.

Stub levels (use these exact labels in the file header):
- `stub:0` — feature identified, existence confirmed, nothing else
- `stub:1` — entry point confirmed (URL mapping → servlet or equivalent)
- `stub:2` — entry point + primary data structure confirmed (DTO class + key fields)
- `stub:3` — full observable chain confirmed by ari-map probe, or enriched by ari-port

At `stub:3`, the `source:` field distinguishes probe-confirmed from port-distilled. A reader trusting a `stub:3` entry must check `source:` before treating it as probe-grade.

Every field not yet confirmed is written as `not traced` — never left blank. Blank reads as absence; `not traced` reads as unknown. The distinction is load-bearing.

### Feature ledger file template

`.anima-lite/features/<slug>.md`:

~~~markdown
# Feature: <feature name>
slug: <feature-slug>
repo(s): <repo slug, or comma-separated for cross-repo features>
stub: <0|1|2|3>
source: <ari-map-probe | ari-port-enriched | manual>
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
Everything below is enriched by ari-port after a port run.
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

### Field ownership

- **ari-map** populates at probe time: all header fields, Identity, Entry points, Primary data structure, and status markers (`not traced` on all unconfirmed fields)
- **ari-port** enriches after a port run: Full data flow, Client-side wiring, State machine, Feature gates, Seam-specific protocols, Known quirks, Port provenance — and updates `stub:`, `source:`, and `prod-commit:` to reflect the enrichment
