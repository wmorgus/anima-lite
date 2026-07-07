# Playwright verification spec

Canonical spec for the `## Playwright verification` block written into contracts by ari-argue, and read by ari-port's validation step (Step 3, checks D and E). Edit here; both skills point to this file rather than restating the shape.

## Block schema

Written into the contract file, after `## Proto visual reference`:

```markdown
## Playwright verification
login_url: <proto or prod login URL>
feature_url: <URL for this feature in the target environment>
checks:
  - claim: "<Claim N — name>"
    steps: "<human-readable interaction steps>"
    expect: "<specific content elements that must be present — title, badge, button label, count, etc.>"
```

Concrete example (as it appears in a real contract):

```markdown
## Playwright verification
login_url: http://localhost:8080/demo?pl2-demo-type=tutor&demo-category=toolkit
feature_url: http://localhost:8080/PLUS/TutorReview
checks:
  - claim: "Claim 4 — feedback text minimum"
    steps: "Click 'Not Helpful' button on the first insight card"
    expect: "Textarea appears with character count label showing '0/10 characters minimum'; Submit button is disabled"
  - claim: "Claim 5 — training accordion"
    steps: "Click 'Recommended Training' accordion header"
    expect: "Training cards expand and are visible"
```

Each check names the claim, the interaction steps (human-readable, the Playwright agent interprets them), and the expected outcome. If an expected outcome is not met, that is a CONTRACT-BREAK for the named claim.

## Rules for the `expect` field

- Name the specific UI elements that must be present — title, duration, badge, action button, character count, whatever the proto shows for that claim.
- Bare existence checks ("the section is visible") are not sufficient for content-bearing sections. The expect clause must be specific enough to catch content quality failures.
- If the port explicitly stubs content (a review-suggested blip exists for that section), the expect clause must describe what the stub renders — not what a full implementation would render. This documents the known limitation rather than failing on it. Example: if the blip says "training recommendations stub," the expect clause says "section renders one card with text 'Training recommendations coming soon'" — not "4 training cards with title, badge, and Start button."
- Every confirmed claim that has a visible UI behavior must have at least one check. Claims with no visible UI behavior (e.g. pure server-side logic) may be omitted from the playwright block with a comment explaining why.

## Screenshot capture for review

Mirrors the `## Proto visual reference (if server reachable)` step in `ari-argue/SKILL.md` — same reachability gate, same graceful-fallback discipline, run at the opposite end of the pipeline. That step captures proto ground truth before the contract is frozen; this one captures prod result during ari-port Step 3 validation, so a human reviewer gets proto and prod side by side instead of a bare PASS/FAIL plus prose blips.

**WHEN.** During the validation agent's Playwright pass (Step 3, checks D and E in `ari-port/SKILL.md`), after — or alongside — running the `expect`-clause checks. This is not a separate pass; it rides the same browser session that is already navigating to `feature_url` and exercising each check's steps.

**WHAT to capture.** One screenshot for each of:
1. Every `check` in the contract's `## Playwright verification` block — one shot of the state described by that check's `expect` clause (post-interaction, so the shot shows the outcome being verified, not the pre-click state).
2. Every major section/state named in the contract's `## Proto visual reference` block — so the prod screenshot set lines up 1:1 with the proto reference set for the same feature. A section in `## Proto visual reference` with no corresponding Playwright `check` still gets a screenshot; it just doesn't get an `expect` assertion.

The goal is 1:1 coverage between what the proto reference documented and what the prod screenshots show — a reviewer should be able to open the two side by side and compare claim-by-claim.

**WHERE to save.** `.anima-lite/work/<slug>/screenshots/`, one PNG per shot. Naming convention: `<claim-or-section-slug>-<state>.png`, where `<claim-or-section-slug>` is the check's claim name or the proto-reference section name, lowercased with spaces/punctuation converted to dashes, and `<state>` is a short descriptor of what's shown when a section has more than one state worth distinguishing (e.g. `default`, `expanded`, `locked`, `after-submit`). Use `default` when there's only one state. Examples:
- `claim-4-feedback-text-minimum-after-submit.png`
- `training-accordion-expanded.png`
- `locked-gate-state-default.png`

**Manifest (required, PNGs are not enough on their own).** PNGs are binary and would bloat the repo with no diffable content, so every capture pass also writes (or appends to) a markdown manifest — `.anima-lite/work/<slug>/screenshots.md` — with one prose line per screenshot:

```markdown
# Screenshots: <feature-name>
Captured: <date>, validation Step 3

- `claim-4-feedback-text-minimum-after-submit.png` — Textarea visible with character count label "0/10 characters minimum"; Submit button disabled (grey, no pointer cursor).
- `training-accordion-expanded.png` — Accordion expanded, 4 training cards visible, each with title, category badge, and Start button.
```

The prose line is the reviewable record (diffable in a PR, greppable, survives even if the PNG is never committed); the PNG is the human's eyeball aid layered on top. Write the same level of specificity the `expect` field rules above require: element counts, labels, badge text, button state — not "the section renders correctly."

**Gitignore note (flag for the driver, do not act on it here).** PNGs under `.anima-lite/work/<slug>/screenshots/` should be gitignored — they're regenerable review artifacts, not durable state, and binary diffs are useless in review. `screenshots.md` should be committed — it's the durable, diffable record. This spec does not edit `.gitignore`; the validation agent or the ari-port driver should treat "add `.anima-lite/work/*/screenshots/*.png` to `.gitignore`" as a follow-up action, not something to silently skip past.

**Reachability gating and fallback.** Same discipline as `ari-argue/SKILL.md`'s proto visual reference step — this is a fallback, never a failure:
1. Attempt to navigate to `feature_url` (already required for checks D/E). If it renders, proceed with capture as above.
2. If the target is not reachable — no JDK/Tomcat/browser runtime available, or the URL does not resolve — do not attempt capture, and do not block validation. Write to `screenshots.md` (creating it if needed):
   ```markdown
   screenshots: target-not-reachable — static review only
   ```
   and note the same in the validation summary. Validation still completes as a static review; the missing screenshots are a documented limitation, not a FAIL.

This mirrors the `playwright: proto-server-not-reached` convention from the proto-visual-reference step one-for-one — same shape, opposite end of the pipeline, so a reader who knows one convention recognizes the other immediately.
