## Blip: lumilo-bridge removed from rep-delivery routing config, all 3 environments
Severity: info
Location: `lambdas/realtime-event-provider/profiles/rep-delivery/environments/{prod,staging,qa}/stack-config.yml`
— each file's `ApplicationRoutingConfig.applications` object.
What happened: deleted the `"lumilo-bridge": {...}` block entirely from all
three files. Verified each file still parses as valid YAML with valid embedded
JSON after the edit (`python3 -c "yaml.safe_load(...); json.loads(...)"`), and
that `lid-backend`'s block is untouched and is now the sole entry in
`applications` in every environment.
Why: contract Claim A, `.anima-lite/work/rep-lumilo-kinesis-direct/contract.md`
— per-target substrate mapping for this leg. No spine exists for this repo
(judgment call, documented in the contract) since the claim's rendering here
is a bounded config-block removal, not a code-behavior change.
Downstream consequence: once this branch (`wip/wmorgus/DEVOPS-10085-update-rep-routing-config`)
deploys, REP's `rep-delivery` Lambda has no route to lumilo-bridge in any
environment — per the contract's sequencing note, this should not deploy
before lumilo-bridge's Kinesis-direct path (Claims B/C/D) is verified working,
or lumilo-bridge would receive MATHia data via neither path in the gap.
Contracting failure?: n/a — contract already named exactly this edit, with
exact file paths, once Open Question 1 was resolved.

## Blip: prod's lid-backend and lumilo-bridge shared a tenant ID
Severity: info
Location: `lambdas/realtime-event-provider/profiles/rep-delivery/environments/prod/stack-config.yml`
— lid-backend's `validTenantIds` includes `lumiloreseb1i32w`, which was also
present in the now-deleted lumilo-bridge block's `validTenantIds`.
What happened: confirmed this tenant ID's presence on lid-backend's own entry
is untouched by removing lumilo-bridge's block — lid-backend continues
receiving this tenant's mutations exactly as before. No action needed; noting
for reviewer clarity, since seeing the same tenant ID vanish from one block
and stay in another during review could look like an accidental partial edit
rather than the two independent, correct entries it actually is.
Why: contract's Claim A per-target substrate mapping explicitly calls this
out as expected, non-overlapping behavior.
Contracting failure?: n/a.
