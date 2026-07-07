### PIN-24 — validation agent captures Playwright screenshots for review
captured: 2026-07-07
stub: 2
status: open
home: anima-lite
goes-stale: superseded once ari-port Step 3 + playwright-spec.md carry the reachability-gated screenshot-capture step AND a run with a reachable target actually produces review screenshots
relates-to: .claude/skills/ari-argue/playwright-spec.md, .claude/skills/ari-port/SKILL.md (Step 3 validation D/E), .claude/skills/ari-argue/SKILL.md (proto-visual-reference pattern being mirrored), run4/run5 static-env constraint (JDK17/Tomcat/browser)

Pre-run5 request (2026-07-07): the end-of-port validation agent (ari-port Step 3) should, during its Playwright pass, CAPTURE screenshots of the ported feature and save them so human review is visual, not just PASS/FAIL + blips. Design constraint: the prod target needs a JDK17+Tomcat+browser runtime that is frequently unavailable (validation has been static-review-only). So capture MUST be reachability-gated with graceful fallback — mirror ari-argue's `proto-server-not-reached` pattern: capture when the URL renders, note `target-not-reachable — static review only` and continue when it doesn't. Never a validation failure.

---
Shaping fields.

**Scope:** In — (a) playwright-spec.md gains a screenshot-capture-for-review procedure: one shot per contract Playwright `check`/claim + each `## Proto visual reference` section, saved under `.anima-lite/ports/<slug>/screenshots/` with a naming convention + a prose markdown manifest (the diffable record; PNGs are the eyeball aid); (b) ari-port Step 3 instructs the validation agent to run it (referencing the spec), reachability-gated, and surface the screenshots path in the review path (validation/blips summary and/or pr.md). Likely a .gitignore follow-up (recommend gitignore the PNGs, commit the prose manifest) — driver-owned.
Out — mechanizing; standing up a prod runtime (separate env concern — see note); HARNESS edits (driver).

**Batch:** validation-review
**Contract:** n/a — harness/process change, no user-facing argument to preserve
**Env dependency:** DORMANT until a reachable target exists. In this env (JDK11, no Tomcat/browser) it degrades to the static-review fallback — so run5 produces screenshots ONLY if a prod runtime is stood up. Capability is added regardless; firing is gated on runtime.
**Resolution:** in-progress — landed 2026-07-07 (sonnet subagent, driver-validated): playwright-spec.md gained a `## Screenshot capture for review` section (WHEN/WHAT/WHERE/manifest/gitignore-note/reachability-fallback); ari-port Step 3 instructs the validation agent to capture (referencing the spec), reachability-gated, surfacing screenshots in the catchup + end-of-session review path. Driver added `.anima-lite/ports/*/screenshots/*.png` to `.gitignore` (PNGs regenerable; `screenshots.md` prose manifest is the committed record). Open follow-up (minor): Step 4e catchup template + Output end-of-session checklist don't yet carry a literal screenshots line-item — currently relies on the Step 3 instruction; wire mechanically if a run shows it's missed. Stays open pending a run with a reachable target actually producing review screenshots (dormant in this env).
