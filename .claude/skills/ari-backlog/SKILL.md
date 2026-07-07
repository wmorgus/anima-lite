---
name: ari-backlog
description: Manages the backlog — .anima-lite/backlog.md (index) plus .anima-lite/pins/PIN-<n>.md (one file per pin) — a two-speed pin system for captured-but-not-yet-scheduled work. Fast lane captures a pin mid-session with zero ceremony; slow lane shapes and sweeps the backlog into contractable batches. Called before every calibration run, and whenever a pin needs shaping, scheduling, or sweeping.
---

# ari-backlog

Backlog items are pins, not tickets. A pin exists so an observation made mid-session isn't lost and isn't forced into premature shape. Shaping happens later, in a batch, when there's enough context to name scope honestly.

## Inputs

- `.anima-lite/pins/PIN-<n>.md` — one file per pin, full block. Committed, durable state. The pin file is the source of truth.
- `.anima-lite/backlog.md` — the index: one searchable line per pin, derived from the pin files. Committed, durable state.
- `.anima-lite/archive/backlog/done-<year>.md` — archived done pins, full block intact.
- `.claude/skills/ari-port/metrics-spec.md` — canonical spec for the backlog-health row written at sweep step 7.
- Whatever surfaced the pin: a spine finding, an epistle, a session observation, a tabled decision, a `/ari-read` judgment (`work/<slug>/judgment.md`) surfacing a divergence.

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

Each pin lives in its own file, `.anima-lite/pins/PIN-<n>.md`, containing exactly one block:

```markdown
### PIN-<n> — <one-line title>
captured: <date>
stub: <0|1|2>        # 0 = raw capture, 1 = shaped (scope named), 2 = contracted (ready to schedule)
status: <open|scheduled|in-progress|paused|done|superseded|elsewhere>
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

**Index line** (in `backlog.md`, under "Live pins"): `- [PIN-<n>](pins/PIN-<n>.md) — <status>, stub:<n>, <batch> — <semantic hook>`. The semantic hook is one line carrying enough of the pin's key nouns that the pin is findable by grep/search without opening its file. The index line is derived state: any edit to a pin's status, stub, or batch updates its index line in the same edit. Archived pins keep a pointer line under "Archived pins" instead: `- PIN-<n> — done, archived: archive/backlog/done-<year>.md — <title>`.

**Lifecycle:** open → scheduled → in-progress → done. Side exits: superseded, elsewhere. In-progress ⇄ paused (workstream suspension, below). There is no "cancelled" state — a pin that's no longer worth doing is superseded, with a Resolution line saying why. This keeps the record honest: nothing just vanishes.

## Fast lane (mid-session capture)

Zero ceremony. Write `.anima-lite/pins/PIN-<n>.md` at `stub:0` — the 6 header lines plus one paragraph body — and add its index line to `backlog.md`. Everything under "Shaping fields" stays `not traced`. Do not stop the current work to shape it — that's the slow lane's job. The only obligation is that the paragraph is honest about what was observed, not what it might become.

## Slow lane (sweep process)

Run at every ari-backlog sweep invocation, in order:

1. **Read the index, then every pin file.** Full backlog, not just open ones — a done pin might need archiving, an elsewhere pin might need re-checking. Flag any index line whose status/stub/batch has drifted from its pin file (the pin file wins; fix the line).
2. **Check `goes-stale` against current state.** If the condition fired, flag the pin: either resolve it (superseded, with Resolution stating what changed) or update the pin to reflect new reality.
3. **Advance stubs where scope is now clear.** A `stub:0` pin with an obvious scope becomes `stub:1` — fill Scope and Batch. A `stub:1` pin ready to schedule becomes `stub:2` — fill Contract.
4. **Classify Contract as claim or substrate** for any pin crossing to `stub:2`. Substrate-shaped (mechanical fixes, plumbing): `Contract: n/a — mechanical, no argument to preserve`. Claim-shaped (changes what the harness promises its operator — gate semantics, stub-depth meaning, conservative-default behavior, required fields): write the one-paragraph Contract stating what the change promises differently.

   > **◎ OPTIONAL GATE — GATE-PIN-CLAIM (claim-shaped pin)**
   > Claim-shaped pin scheduled — review contract paragraph? (skip to proceed)

5. **Archive done pins.** Move the full block (decision record intact) from `pins/PIN-<n>.md` to `.anima-lite/archive/backlog/done-<year>.md` and delete the pin file. Move its index line to "Archived pins" as a pointer: `- PIN-<n> — done, archived: archive/backlog/done-<year>.md — <title>`.
6. **Flag un-exported elsewhere pins.** Any pin with `status: elsewhere` and no export confirmation resurfaces every sweep — do not let it go quiet. It stops resurfacing only when either (a) exported: status becomes `superseded`, Resolution reads `exported to <path>`, or (b) re-dated with a new `captured:` line noting why it's still here.
7. **Write the backlog-health row.** `.anima-lite/metrics/backlog-health-<date>.md`, per `.claude/skills/ari-port/metrics-spec.md` (canonical spec — this step points to it, not restated here). Fields: open pin count by stub level, count by status, age of oldest open pin, capture-to-done latency for pins closed since this sweep (from each closed pin's `captured:` line vs. the git commit date that added its `Resolution:` line), and the un-exported elsewhere count from step 6.

## Workstream suspension

**Workstream:** the live span of a work item from intake to harvest — a work item in flight, with state on disk (uncommitted or staged changes, partial artifacts, mid-lifecycle contracts). Pins capture future work; runs name attempts; the workstream is the thing that can be *paused*. A pin points at the suspension record; it doesn't contain it.

**Suspend** (in-progress → paused), in order:

1. **Write or refresh the state manifest** at the workstream's artifact home (e.g. `<workstream-dir>/RESTORE.md`). It inventories: every path the workstream owns (committed / staged / unstaged / untracked, stated explicitly), any external state (worktrees, running environments, remote branches), exact resume steps, and what must NOT be touched while paused. The manifest is written for a cold reader — resume may happen in a session with no memory of this one.
2. **Commit the suspended workstream's state** in a dedicated suspension commit (`pause(<slug>): <one line>`). Scope: everything *belonging to the suspended workstream* — its artifact dir, its manifest, its pin edit — and nothing else. Unrelated concurrent-workstream dirt in the same tree is explicitly excluded; sweeping it into the pause commit tangles other in-flight work into the wrong history. No dirty-tree pauses for the workstream's own files — an uncommitted pause is not durable.

   *Shared-file collision:* pin bodies live in per-pin files (PIN-35), so two in-flight pins can no longer collide there — the residual shared surface is `backlog.md` index lines. If the suspension pin's index-line edit collides with another in-flight pin's uncommitted index edit, split at hunk level — stage only the suspension pin's hunks (`git add -p` or equivalent) into the suspension commit; leave the other pin's edit in the tree.
3. **Set the pin** to `status: paused` and add a `State:` shaping field, format: `**State:** manifest <path>; suspension commit <hash>`. If no pin exists for the workstream, write one (fast lane is fine).

**Resume** (paused → in-progress): read the manifest first; check whether anything that landed during the pause touches the workstream's files (renames, spec changes, spine refreshes — the manifest's do-not-touch list is the checklist); update the manifest's resume notes if reality drifted; set `status: in-progress` with a dated note.

**Sweep obligation:** every sweep re-checks paused pins the same way it checks `goes-stale` — a pause with a stale manifest is a silent lie about resumability. Flag it, refresh it, or supersede the workstream honestly.

## Cross-repo handling

A pin whose `home:` is not `anima-lite` gets `status: elsewhere` and an export note naming the target path (even if that target doesn't exist yet — e.g. "export target: anima-corps backlog equivalent, not yet created"). It is never archived while un-exported, regardless of how old it is.

## Layout

`.anima-lite/backlog.md` is the index — one line per pin, committed. Each pin's full block lives in its own file, `.anima-lite/pins/PIN-<n>.md`, also committed. The pin file is the source of truth; the index line is the derived, searchable summary and moves with the pin in the same edit (sweep step 1 checks the sync). Sharded from the original single-file layout 2026-07-07 (PIN-35) when it passed ~500 lines — past the old ~300-line revisit threshold.

## Sweep cadence

Precondition, not a schedule: invoke before every calibration run, or on user request. There is no background timer — if no one calls it, it doesn't run, which is itself a signal worth noticing at the next sweep.

## Escalation / Notes

**No priority ranks.** Batches plus status are the only ordering the backlog itself asserts. Intra-batch order is decided by whoever picks up the batch in a working session — the backlog records what's queued and how it's grouped, not what order to do it in. The working order itself lives in `.anima-lite/session-backlog.md` — operator-owned, a ladder of pointers to pins, re-cut freely with no shaping ceremony; pin files remain the source of truth for content, that file asserts order only.

**Self-application (implemented).** Backlog health — capture-to-done latency, age distribution by stub level, how often elsewhere pins go un-exported — now feeds the metrics/ system via sweep step 7 above, per `.claude/skills/ari-port/metrics-spec.md`'s backlog-health row spec (PIN-2/3, sensors sprint).
