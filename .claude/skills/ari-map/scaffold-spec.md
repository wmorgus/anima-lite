# Scaffold artifact spec

Canonical spec for `.anima-lite/spine-<label>/scaffold.md`. Referenced by `ari-map/SKILL.md` (writes it, always-produced/depth-gated), `ari-arete-pan/SKILL.md` (reads it as evidence for the nugget/ore/slag cut), and `ari-argue-rhetoric` (arete posture). Edit here; owning/reading skills point to this file rather than restating the shape — same discipline `ledger-spec.md` already holds for the feature ledger.

## Not a fifth cause

`scaffold.md` sits alongside `telos.md`/`material.md`/`formal.md`/`efficient.md` in the spine directory, but it is not a fifth Aristotelian cause. The four files map onto final/material/formal/efficient cause; `scaffold.md` doesn't correspond to a fifth cause of its own. It is a **coordinate backbone** — a `(scenario, path, step)` address space — that the material/formal/efficient *cells* attach to. Reading `scaffold.md` answers "how does this repo's process actually move, scenario by scenario" — a different question from "what is this repo made of / how is it organized / what acts on it," which the existing three cause files (plus the final-cause `telos.md`) already answer. Do not describe `scaffold.md` as completing or extending the four-cause set; describe it as the coordinate grid the four causes already populate.

## What it is for

A repo's telos names *what for*; `formal.md`/`material.md`/`efficient.md` name *what pattern, what stuff, what acts*. None of the four files name *how a scenario actually moves, step by step, and where paths diverge*. That's the gap `scaffold.md` closes: it gives a repo's process shape — not just its purpose — a first-class, addressable artifact.

## Schema

`scaffold.md` is one table per scenario. Each row is keyed by `(scenario, path, step)` — one row per step of one path through one scenario. Each row has exactly three content columns: **formal**, **material**, **efficient** — a one-line pointer or note for what that cause contributes at that step (not a restatement of the full cause-file entry; cite the cause file's §-number where useful).

- **Happy path is the default table.** Every scenario's default table is its happy path — the one sequence of steps assumed unless a row says otherwise.
- **Other paths get rows only where they diverge.** A non-happy path (error branch, alternate entry, degraded mode) does not get a full parallel table. It gets rows only at the steps where it diverges from the happy path. A step where the alternate path behaves identically to the happy path is not re-stated — it simply has no row for that path.
- **An empty column entry in a divergence row is a gap, not a missing row.** If a path's row exists (because the path diverges from the happy path at that step) but one of the three cause columns has nothing to say — because that cause genuinely doesn't differ from the happy path's own column at that step — the cell is left blank. A blank cell means "confirmed, no divergence here," not "unknown."

## Cell honesty — two distinct kinds of empty

`scaffold.md` uses two visually distinct forms of "nothing in this cell," and they must never collapse into the same blank:

- **`not traced`** — the cell has not been reached by a probe of sufficient depth yet. This is the ledger's own `not traced` discipline (`ledger-spec.md`), reused rather than reinvented: an unconfirmed cell is written `not traced`, never left blank. Blank reads as absence; `not traced` reads as unknown.
- **blank (empty column entry)** — the cell was reached and probed, and confirmed that this cause does not diverge from the happy path at this step (the divergence-gap case above). This is a confirmed fact, not a gap in probe depth.

A reader must be able to tell, from the artifact alone, whether a step wasn't looked at yet (`not traced`) or was looked at and found unremarkable (blank). Do not write `not traced` where a real "no divergence" finding exists, and do not leave a genuinely unprobed cell blank.

## Per-scenario `stub:0-3` field

Each scenario table carries its own `stub:0-3` field in its header, reusing the feature ledger's own stub vocabulary (`ledger-spec.md` "Stub depth") rather than inventing a parallel scale:

- `stub:0` — scenario named, existence confirmed, nothing else (no table rows yet).
- `stub:1` — scenarios named, cells unfilled — the happy-path table exists with its steps named, but the formal/material/efficient cells are `not traced`.
- `stub:2` — happy-path cells filled for the steps a probe could decisively confirm; divergent paths not yet walked.
- `stub:3` — happy path fully filled, and every named divergent path's rows are filled or confirmed-blank (not `not traced`).

Same honest-stub discipline as the ledger: a shallow `stub:1` (scenarios named, cells honestly `not traced`) is a correct artifact. A `stub:2`/`stub:3` scenario whose cells were filled with an assertion the probe didn't actually confirm is a dishonest stub and a worse artifact than the honest shallow one.

## File template

`.anima-lite/spine-<label>/scaffold.md`:

~~~markdown
# Scaffold: <repo-name> (<label>)
(Coordinate backbone — see "Not a fifth cause" above; not a fifth Aristotelian cause,
the material/formal/efficient cells below attach to this repo's own spine causes.)

## Scenario: <scenario name>
stub: <0|1|2|3>

### Happy path

| step | formal | material | efficient |
|---|---|---|---|
| 1. <step name> | <note or `not traced`> | <note or `not traced`> | <note or `not traced`> |
| 2. <step name> | ... | ... | ... |

### Path: <divergent path name>
<Rows only at steps where this path diverges from the happy path above. A blank
cell = confirmed no divergence at this step for this cause; `not traced` = not
yet probed.>

| step | formal | material | efficient |
|---|---|---|---|
| <n>. <step name> | <note, blank, or `not traced`> | ... | ... |

## Scenario: <next scenario name>
stub: <0|1|2|3>
...
~~~

## Escalation / Notes

Refreshed, never accreted — same discipline as the other four spine files (`PHILOSOPHY.md`'s spine self-correction rule; `ari-map/SKILL.md`'s "Skeleton, not flesh" note). `scaffold.md` is exactly-one-per-repo, comprehensive-by-intent, and refreshed in full on re-probe rather than patched incrementally. The feature ledger (`features/<slug>.md`) stays the only accretive artifact in this family — `scaffold.md` is a skeleton, not flesh.
