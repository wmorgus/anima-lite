---
name: ari-backlog
description: Manages .anima-lite/backlog.md — a two-speed pin system for captured-but-not-yet-scheduled work. Fast lane captures a pin mid-session with zero ceremony; slow lane shapes and sweeps the backlog into contractable batches. Called before every calibration run, and whenever a pin needs shaping, scheduling, or sweeping.
---

# ari-backlog

Backlog items are pins, not tickets. A pin exists so an observation made mid-session isn't lost and isn't forced into premature shape. Shaping happens later, in a batch, when there's enough context to name scope honestly.

## Inputs

- `.anima-lite/backlog.md` — the single source of truth. Committed, durable state.
- `.anima-lite/archive/backlog/done-<year>.md` — archived done pins, full block intact.
- Whatever surfaced the pin: a spine finding, an epistle, a session observation, a tabled decision.

## Preconditions

Invoke this skill when any of the following hold:

- Before a calibration run (sweep pass — mandatory).
- A pin needs to move stub level, status, or batch.
- A new item needs capturing (fast lane — any time, mid-session).
- The user requests a sweep or asks what's in the backlog.

## Active orientations

**Two-speed.** Fast lane and slow lane are not the same operation wearing different clothes — they have different obligations. Fast lane exists to protect against losing an observation; it must stay cheap or people stop using it. Slow lane exists to protect against a backlog that's all raw capture and no shaped work; it must be thorough or it stops meaning anything.

**Conservative default applies here too.** When unsure whether a pin is claim-shaped or substrate-shaped, classify it claim-shaped. The cost of an unnecessary light gate is small; the cost of scheduling a claim change with no review is the same failure mode this whole toolkit exists to prevent.

## Pin format

```markdown
### PIN-<n> — <one-line title>
captured: <date>
stub: <0|1|2>        # 0 = raw capture, 1 = shaped (scope named), 2 = contracted (ready to schedule)
status: <open|scheduled|in-progress|done|superseded|elsewhere>
home: <anima-lite | anima-corps | ...>
goes-stale: <one line — what would invalidate this pin>
relates-to: <spine §, FINDING-n, epistle path, blip — or "none yet">

<1 paragraph body. Only required content at stub:0.>

---
Shaping fields — `not traced` until stub advances past 0.

**Scope:** <in/out — not traced>
**Batch:** <batch name or "unbatched">
**Contract:** <inline claim paragraph, or "n/a — mechanical, no argument to preserve">
**Resolution:** <filled only at done/superseded>
```

**Lifecycle:** open → scheduled → in-progress → done. Side exits: superseded, elsewhere. There is no "cancelled" state — a pin that's no longer worth doing is superseded, with a Resolution line saying why. This keeps the record honest: nothing just vanishes.

## Fast lane (mid-session capture)

Zero ceremony. Append a new pin at `stub:0`: the 6 header lines plus one paragraph body. Everything under "Shaping fields" stays `not traced`. Do not stop the current work to shape it — that's the slow lane's job. The only obligation is that the paragraph is honest about what was observed, not what it might become.

## Slow lane (sweep process)

Run at every ari-backlog sweep invocation, in order:

1. **Read every pin.** Full backlog, not just open ones — a done pin might need archiving, an elsewhere pin might need re-checking.
2. **Check `goes-stale` against current state.** If the condition fired, flag the pin: either resolve it (superseded, with Resolution stating what changed) or update the pin to reflect new reality.
3. **Advance stubs where scope is now clear.** A `stub:0` pin with an obvious scope becomes `stub:1` — fill Scope and Batch. A `stub:1` pin ready to schedule becomes `stub:2` — fill Contract.
4. **Classify Contract as claim or substrate** for any pin crossing to `stub:2`. Substrate-shaped (mechanical fixes, plumbing): `Contract: n/a — mechanical, no argument to preserve`. Claim-shaped (changes what the harness promises its operator — gate semantics, stub-depth meaning, conservative-default behavior, required fields): write the one-paragraph Contract stating what the change promises differently.

   > **◎ OPTIONAL GATE — GATE-PIN-CLAIM (claim-shaped pin)**
   > Claim-shaped pin scheduled — review contract paragraph? (skip to proceed)

5. **Archive done pins.** Move the full block (decision record intact) to `.anima-lite/archive/backlog/done-<year>.md`. Replace it in `backlog.md` with a one-line pointer: `### PIN-n — <title> → done, archived: archive/backlog/done-<year>.md`.
6. **Flag un-exported elsewhere pins.** Any pin with `status: elsewhere` and no export confirmation resurfaces every sweep — do not let it go quiet. It stops resurfacing only when either (a) exported: status becomes `superseded`, Resolution reads `exported to <path>`, or (b) re-dated with a new `captured:` line noting why it's still here.

## Cross-repo handling

A pin whose `home:` is not `anima-lite` gets `status: elsewhere` and an export note naming the target path (even if that target doesn't exist yet — e.g. "export target: anima-corps backlog equivalent, not yet created"). It is never archived while un-exported, regardless of how old it is.

## Layout

Single `.anima-lite/backlog.md`, committed. Revisit the single-file layout only if it exceeds ~300 lines with nothing closing — that's a signal the sweep isn't running often enough, not a cue to shard the file preemptively.

## Sweep cadence

Precondition, not a schedule: invoke before every calibration run, or on user request. There is no background timer — if no one calls it, it doesn't run, which is itself a signal worth noticing at the next sweep.

## Escalation / Notes

**No priority ranks.** Batches plus status are the only ordering the backlog itself asserts. Intra-batch order is decided by whoever picks up the batch in a working session — the backlog records what's queued and how it's grouped, not what order to do it in.

**Self-application (future).** Backlog health — capture-to-done latency, age distribution by stub level, how often elsewhere pins go un-exported — belongs in the metrics/ system once it exists (see `.anima-lite/backlog.md` PIN-2/3 for the sensors sprint this depends on). Do not build metrics tracking here; note the intent and move on.
