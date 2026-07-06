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
