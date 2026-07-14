## Blip: worked examples cited fabricated content, not the real shelved case
Severity: review-suggested
Location: `.claude/skills/ari-map/SKILL.md` §2 worked example (~line 135) and §5 worked example (~line 331)
What happened: both worked examples for the `relates-to:` tag were written against the real repo/spine names (`spine-lumilo-bridge`, `spine-realtime-event-provider`) but the cited rule text, `lives-in:` path, and target `#§`-number did not actually exist in either real spine — invented prose dressed as citation, not a synthetic-and-labeled example.
Why: the contract's Disposition and Claim 2 required the worked example to be validated "against the real shelved case," not a synthetic stand-in using real names. No spine section covers fabrication risk directly; this is the same skeptical-citation discipline `ari-argue-rhetoric`'s "every classification cites the spine section it rests on" rule already enforces, applied here to a worked example rather than a claim classification.
Downstream consequence: a future agent reading the worked example would trust it as a real citation and either misquote it or fail to find the cited line, discovering the mismatch mid-work rather than at build time.
Contracting failure?: n/a — the contract's instruction to validate against the real case was correct; the execution subagent's citation discipline (not the contract) was the gap. Caught by independent validation, not self-caught.
Resolution: fixed — both worked examples now cite real, unmodified lines from `spine-lumilo-bridge/telos.md` §2 (first rule) and `spine-lumilo-bridge/formal.md` §5 (third finding), each paired with a real target section in `spine-realtime-event-provider` (`formal.md` §4 Seam protocols), one `dependency` edge and one `contract` edge, verified to exist by direct read.

## Blip: `relates-to:` reuse claim overclaimed vocabulary sharing with the backlog
Severity: info
Location: `.anima-lite/work/pin40-connective-tissue-v2/plan.md` ("reusing the backlog's already-ratified `relates-to:` vocabulary")
What happened: the backlog's `relates-to:` field (pin front-matter) is freeform prose with no `#<section> (<edge-kind>)` schema; the new spine tag shares the field name only, not the shape.
Why: no spine section covers cross-artifact naming conventions; noted for accuracy, not a functional defect.
Downstream consequence: none — same tag name across two artifact types with different shapes is a minor naming echo, not a collision (backlog pins and spine rules are never parsed by the same code path).
Contracting failure?: n/a — cosmetic framing note in the plan, not the contract.
Resolution: no code change; left as-is per validation's own characterization ("minor framing overclaim, not a functional bug").

## Blip: §10 External references omitted from the material.md cap-exemption enumeration
Severity: info
Location: `.claude/skills/ari-map/SKILL.md` "Cap exemption" paragraph (~line 391)
What happened: the paragraph enumerated §7/§8/§9 as cap-exempt lookup appendices but did not name the newly added §10, even though §10 is the same class of appendix content.
Why: propagation gap — Claim 4 added §10 to the material.md template but didn't touch this separate enumeration sentence.
Downstream consequence: a future spine author trusting the enumeration literally might assume §10 is narrative-capped when it isn't (though functionally it already falls outside the explicitly-capped §1–§6 range, so no immediate breakage).
Contracting failure?: n/a — cheap, obvious propagation fix once noticed.
Resolution: fixed — §10 added to the enumeration.

## Validation
Independent clean-context validation agent, 2026-07-14: all six claims structurally implemented correctly (PASS on check A). Check B (blip classification) found the "zero blips" claim from the execution pass did not hold — the worked-example fabrication above should have been logged and wasn't; verdict returned as PASS (pending review) with this one concrete defect. Check C (scope creep / internal consistency) confirmed the shelved ripple case's own files were genuinely untouched, found the `relates-to:` vocabulary-reuse framing overclaim (info, not fixed as a code change) and the §10 cap-exemption omission (info, fixed). All three findings addressed in this pass. Final status: **PASS**.
