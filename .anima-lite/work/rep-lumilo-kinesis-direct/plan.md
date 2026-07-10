# Execution Plan: REP→lumilo-bridge direct Kinesis ingestion
Contract: .anima-lite/work/rep-lumilo-kinesis-direct/contract.md
Generated: 2026-07-10

## Claim changes
- **Claim C (mapping fix, extensible registry)**: lumilo-bridge repo,
  `graphql-server/src/services/mathiaKinesis.service.ts` (rewrite
  `decodeRecord()` into a per-class mapper registry) — new sibling module
  `graphql-server/src/services/mathiaKinesisMapping.ts` recommended to keep
  the poll-loop file from growing past its current shape; the registry maps
  `record.class` → a mapper function producing `LumiloEvent`, ported field-by-field
  from realtime-event-provider's `rep-delivery/index.js` five transform
  functions (read directly as source of truth, per contract).
- **Claim B (activation)**: lumilo-bridge repo — no code change; `KINESIS_STREAM_NAME`
  is already read by `mathiaKinesis.service.ts` at startup and already
  documented in `.env.example`. This claim's execution is a deploy-config
  action (setting the real stream name per environment), not a repo file
  change — logged as a blip pointing at where it needs to be set, not guessed.
- **Claim A (routing removal)**: aws-infrastructure repo, three files —
  `lambdas/realtime-event-provider/profiles/rep-delivery/environments/{prod,staging,qa}/stack-config.yml`
  — delete the `"lumilo-bridge": {...}` block from each file's
  `ApplicationRoutingConfig.applications` object. `lid-backend`'s block stays
  untouched in all three.

## Substrate translations
- None load-bearing beyond Claim C's mapper file organization (new sibling
  module vs. inline rewrite) — a medium choice, not argued.

## Order of operations
1. lumilo-bridge: implement Claim C (mapping registry) — this is the leg that
   must be correct before anything else proceeds, since REP already produces
   real records today.
2. lumilo-bridge: log Claim B as a blip (deploy-config action, not code).
3. aws-infrastructure: implement Claim A (three-file routing removal) — only
   after step 1 is committed and self-consistent, per the contract's explicit
   sequencing deviation (Open Questions §2): removing REP's lambda routing
   before lumilo-bridge's Kinesis path is verified correct would leave
   lumilo-bridge receiving nothing via either path.
4. realtime-event-provider: no changes. Read-only reference for step 1's field
   mapping.

## Blockers
None. Both remaining Open Questions from the contract were resolved by the
operator (2026-07-10): aws-infrastructure edit access confirmed; lumilo-bridge
adapter rewrite explicitly authorized (untested first LLM pass).
