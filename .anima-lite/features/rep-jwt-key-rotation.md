# Feature: JWT signing-key rotation
slug: rep-jwt-key-rotation
repo(s): realtime-event-provider
stub: 1
source: ari-map-probe
prod-commit: adf0caf
goes-stale: rep-key-rotation/index.js changes, or the Secrets Manager rotation-schedule/step contract changes

## Identity
Automatically rotates the RSA keypair (2048-bit) that `rep-delivery` uses to sign JWTs for its GraphQL-mutation calls, via the standard AWS Secrets Manager four-step rotation-lambda protocol (createSecret/setSecret/testSecret/finishSecret). Shared infrastructure for both `lid-backend` and `lumilo-bridge` delivery — not lumilo-bridge-specific, so unaffected in itself by the upcoming ripple (only the `lumilo-bridge`-audience token usage of the rotated key goes away).

## Entry points
Lambda `rep-key-rotation/index.js` `exports.handler`, invoked by AWS Secrets Manager's rotation scheduler with `{Step, ClientRequestToken}` — not traced further (trigger configuration for the rotation schedule itself lives in the external infrastructure repo, not in this repo).

## Primary data structure
not traced — feature is not built on a recurring domain entity (sessions/students/etc.), stub:1 is the appropriate stopping point per ledger-spec.

---
Everything below is enriched by ari-code-rhetoric after a port run.
At stub:0–2, all fields below are `not traced`.

## Full data flow
not traced.

## Client-side wiring
n/a — no client.

## State machine
Four-step AWS Secrets Manager rotation protocol: createSecret → setSecret → testSecret → finishSecret (confirmed in code, `ROTATION_STEPS` constant and `switch` in `exports.handler`).

## Feature gates
Requires `SERVICE_NAME`, `PRIVATE_KEY_SECRET_ARN`, `PUBLIC_KEY_SECRET_ARN` env vars — handler throws if any are missing.

## Seam-specific protocols
not traced.

## Known quirks
none.

## Port provenance
n/a until first port.
