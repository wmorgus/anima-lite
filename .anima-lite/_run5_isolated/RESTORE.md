# RESTORE.md — run5 workstream suspension manifest

**Status:** SUSPENDED 2026-07-07. This is a formal workstream suspension per
`.claude/skills/ari-backlog/SKILL.md` § "Workstream suspension" — the first
dogfood of that procedure. This file supersedes the ad-hoc isolation note
that previously lived here (content preserved below, under "Original
isolation record").

Pin of record: **PIN-30** in `.anima-lite/backlog.md` (`status: paused`).
The suspension commit hash is recorded in that pin's `State:` field.

## Why suspended

run5 (isolated naive-vs-disciplined port comparison of `monthly-report`) was
paused to clear the tree for the reorient batch — specifically the
`ports/` → `work/` directory rename (PIN-25, vocab decision 2b) and the new
`ari-intake` skill build (PIN-27) — both of which needed a clean working
tree in this repo. This is not an abandonment: the A/B comparison design is
still live, see run5-plan.md.

## Path inventory (git state at suspension)

All paths below are run5-owned. Git state as of the suspension commit:

| Path | State at suspension | Notes |
|---|---|---|
| `.anima-lite/features/monthly-report.md` → `.anima-lite/_run5_isolated/features/monthly-report.md` | staged rename (git mv), included in suspension commit | moved out of ari-map scan range so run5's fresh port can't read prior answers |
| `.anima-lite/ports/monthly-report/{blips,catchup,contract,plan,pr}.md` → `.anima-lite/_run5_isolated/ports/monthly-report/` | staged rename (git mv), included in suspension commit | prior port artifact set for monthly-report |
| `.anima-lite/ports/monthly-report-v1/{blips,contract,plan}.md` → `.anima-lite/_run5_isolated/ports/monthly-report-v1/` | staged rename (git mv), included in suspension commit | "good" benchmark artifact set (superseded, aborted — reference only, not ground truth) |
| `.anima-lite/_run5_isolated/RESTORE.md` (this file) | untracked → added, included in suspension commit | formal manifest, replaces ad-hoc note |
| `.anima-lite/_run5_isolated/run5-plan.md` | untracked → added, included in suspension commit | run5's comparison design; unchanged content, see below |

Also bundled into the same suspension commit (not run5-owned in origin, but
landed alongside run5 prep earlier the same day and were dirty in the tree
at suspension time — commit-everything policy per the suspension procedure
applies to the whole tree, not just run5's own paths):

| Path | State | Notes |
|---|---|---|
| `.anima-lite/spine-prod/{efficient,formal,material,telos}.md` | unstaged edits, included | spine-completeness batch edits (PIN-21/23), run5 depends on these spines being current for its port |
| `.anima-lite/spine-proto/{efficient,formal,material,telos}.md` | unstaged edits, included | same batch, proto side |
| `.claude/skills/ari-argue/playwright-spec.md` | unstaged edits, included | PIN-24 — screenshot-capture-for-review procedure |
| `.gitignore` | unstaged edits, included | PIN-24 follow-up — gitignores `ports/*/screenshots/*.png` |

**Explicitly NOT included** in the suspension commit: `.anima-lite/backlog.md`
and `.claude/skills/ari-backlog/SKILL.md`, both of which were also dirty at
suspension time (PIN-29 authoring — the very procedure this suspension is
executed under). Those are a separate, still-in-progress workstream and are
left untouched by the suspension commit. See "Procedure ambiguity" below.

## External state

- **Git worktrees:** checked via `git worktree list` — only the primary
  worktree (`/Users/wmorgus/Desktop/anima/anima-lite`, branch `main`)
  exists. No secondary worktree holds run5 state.
- **Prod-repo branches** (external repo, not this one): `monthly-report`
  (naive baseline, tagged `naive-monthly-report-v0`), `anima-lite-monthly-report`
  (superseded benchmark), `anima-lite-monthly-report-run5` (run5's working
  branch, at baseline `29d41e50`, no work committed to it yet), `weekly-report`
  (depends on `monthly-report`, must survive untouched). None of these were
  touched by this suspension — they are the external state a resume must
  re-verify still exist and are in the state run5-plan.md describes.
- **No running environments** (servers, containers) are known to be part of
  this workstream.

## Do-not-touch while paused

- `.anima-lite/_run5_isolated/**` — this is the frozen snapshot of run5's
  prior answers. Do not restore it into scan range, do not edit its
  contents, until run5 is explicitly resumed.
- Prod-repo branches listed above (`monthly-report`, `naive-monthly-report-v0`
  tag, `anima-lite-monthly-report`, `anima-lite-monthly-report-run5`,
  `weekly-report`) — do not delete, rebase, or force-push any of them.
- Do not let another workstream re-populate `.anima-lite/features/monthly-report.md`
  or `.anima-lite/ports/monthly-report*/` at their original (pre-isolation)
  paths while run5 is paused — that would collide with the resume step below.

## IMPORTANT — live-tree layout changed during the pause

Immediately after this suspension, the `ports/` → `work/` directory rename
(PIN-25, ratified vocab decision 2b) executes in the **live** tree. That
means:

- **Live tree, post-rename:** port artifacts live under `.anima-lite/work/<slug>/`.
- **This snapshot (`_run5_isolated/`), unaffected:** internally still uses
  the old `ports/` naming — `.anima-lite/_run5_isolated/ports/monthly-report/`,
  `.anima-lite/_run5_isolated/ports/monthly-report-v1/`. The rename does NOT
  reach into `_run5_isolated/` (it is out of ari-map's scan range by design,
  and the rename is scoped to live, in-scan-range directories).
- **On resume:** the exact-restore commands below (preserved from the
  original isolation record) will land run5's artifacts back at
  `.anima-lite/ports/monthly-report/` and `.anima-lite/ports/monthly-report-v1/`
  — but if the `work/` rename has landed by then, those target paths are
  **stale**. The resumer must retarget the `git mv` destinations to
  `.anima-lite/work/monthly-report/` and `.anima-lite/work/monthly-report-v1/`
  (or wherever the live layout has moved to by resume time — check
  `CLAUDE.md` and `HARNESS.md` §4 for the current canonical layout before
  running the restore commands verbatim).
- Also check `.anima-lite/_run5_isolated/features/monthly-report.md` and
  `run5-plan.md` for any path references that assume the old `ports/` layout
  (ari-map's scan-path config, any doc cross-references) — these may need
  updating to match whatever the live layout is at resume time.

## Resume steps

1. Read this manifest in full, then re-read `run5-plan.md` for the
   comparison design.
2. Verify external state is unchanged: confirm the prod-repo branches listed
   above still exist and are at the commits run5-plan.md records; confirm
   no other workstream has re-populated `.anima-lite/features/monthly-report.md`
   or `.anima-lite/ports/monthly-report*/` (or their `work/`-renamed
   equivalents) at the live paths.
3. Check whether the `ports/` → `work/` rename (see above) has landed. If it
   has, retarget the restore commands' destinations accordingly; if it
   hasn't, use the original paths as written.
4. Run the restore (from anima-lite repo root — adjust destination paths per
   step 3):
   ```
   git mv .anima-lite/_run5_isolated/features/monthly-report.md .anima-lite/features/monthly-report.md
   git mv .anima-lite/_run5_isolated/ports/monthly-report .anima-lite/ports/monthly-report
   git mv .anima-lite/_run5_isolated/ports/monthly-report-v1 .anima-lite/ports/monthly-report-v1
   ```
   (Original paths shown; retarget to `.anima-lite/work/...` if the rename
   has landed.)
5. After restoring, `.anima-lite/_run5_isolated/` should be empty except for
   this RESTORE.md and run5-plan.md — remove or archive those separately as
   desired once run5 concludes for good.
6. Set PIN-30's `status:` to `in-progress` with a dated resume note, per the
   ari-backlog resume procedure.
7. Confirm the spine files run5 depends on (`spine-prod/`, `spine-proto/`)
   are still current — if another workstream re-probed them since
   suspension, re-check run5-plan.md's assumptions against the fresh spines
   before resuming the port itself.

## Procedure ambiguity (dogfood note)

The suspension procedure says "commit-everything policy applies with no
exceptions" for the suspension commit, but this session's suspension commit
deliberately excludes `.anima-lite/backlog.md` and
`.claude/skills/ari-backlog/SKILL.md`, which were also dirty at the time —
because that dirt is a *different* in-progress workstream (PIN-29, the
suspension procedure itself), not run5's. The procedure as written doesn't
say what to do when the tree has dirt from more than one concurrent
workstream at suspension time: commit only the workstream being suspended
(what was done here), or commit everything regardless of ownership (literal
reading of "no exceptions")? This suspension took the narrower reading.
Flagging for whoever next revises the procedure.

---

## Original isolation record (pre-formalization, preserved verbatim)

# Isolation record — run5 monthly-report clean-run prep

Date: 2026-07-07

### Why

anima-lite's ari-map reads `.anima-lite/features/*.md` at probe time, and its
port history lives under `.anima-lite/ports/*/`. Both directories are inside
ari-map's scan paths. Calibration run5 requires anima-lite to port the
`monthly-report` feature completely fresh (for an A/B comparison against the
naive port on prod's `monthly-report` branch), so any file in scan-path that
records anima-lite's own prior monthly-report answers had to be moved out of
scan range before run5 starts. This is memory isolation for the *tool*, not a
change to the prototype feature source or the prod repo.

### What was moved (git mv, history preserved)

- `.anima-lite/features/monthly-report.md`
  → `.anima-lite/_run5_isolated/features/monthly-report.md`
- `.anima-lite/ports/monthly-report/` (blips.md, catchup.md, contract.md, plan.md, pr.md)
  → `.anima-lite/_run5_isolated/ports/monthly-report/`
- `.anima-lite/ports/monthly-report-v1/` (blips.md, contract.md, plan.md)
  → `.anima-lite/_run5_isolated/ports/monthly-report-v1/`

Nothing else under `.anima-lite/features/` or `.anima-lite/ports/` was touched
(recommend-sessions, weekly-report, main, and all other feature docs remain in
their original locations).

No commit was made as part of this move at the time it was written — the
renames were staged/pending in the working tree only. They are now included
in the formal suspension commit (see top of this file).

### How to restore after run5 (exact commands, as originally written)

Run from the anima-lite repo root:

```
git mv .anima-lite/_run5_isolated/features/monthly-report.md .anima-lite/features/monthly-report.md
git mv .anima-lite/_run5_isolated/ports/monthly-report .anima-lite/ports/monthly-report
git mv .anima-lite/_run5_isolated/ports/monthly-report-v1 .anima-lite/ports/monthly-report-v1
```

After restoring, `.anima-lite/_run5_isolated/` should be empty except for this
RESTORE.md and run5-plan.md (remove or archive those separately as desired).

**Note (added at formalization):** these commands assume the `ports/`
directory name is still live. See "IMPORTANT — live-tree layout changed
during the pause" above before running them.
