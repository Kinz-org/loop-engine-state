# loop-engine-state

Control repo for the KINZ organization's scheduled agent loops: what runs, when, with which
instructions, and a record of every run. Public, so the method is visible: the prompts, the
safety rules, the run records and the judge's verdicts are the evidence of how the loops work.
Nothing here is a work target for the loops.

This is the `Kinz-org` copy. It started from the same state as `nassim0014/loop-engine-state`
on 2026-10-11 and is developed separately from it on purpose: two versions can be compared to
see which steps build the better one, and if one breaks the other can take over. Config
(`registry.json`, `prompts/`, `scripts/`) points at `Kinz-org` repos. Records dated before
2026-10-11 (`runs/`, `experiments/`, `reports/`, `findings/`) describe the shared history and
keep their original `nassim0014` links.

## What the loops are for

In order of priority (owner, 2026-09-23):
1. Real improvements to the repos Nassim uses or shows people.
2. An active GitHub profile.
3. Learning how to build agent systems.

The agents work on their own, merges included. Nassim hears about it in two ways: a phone
alert when a run fails or needs him, and a weekly summary on Monday morning.

## What runs where (times are Africa/Tunis)

| Job id | Calendar name | When (Tunis) | Merges |
|---|---|---|---|
| `kinz-upkeep` | KINZ · Upkeep: dependency updates, red CI, conflicts, merge what's green | daily 01:45 | yes |
| `kinz-market-watch` | KINZ · Market watch: read-only check of the weekly competitor scrape | Tue 01:45 | no |
| `kinz-polish` | KINZ · Polish: top improvement item on 2 rotation repos | Mon, Wed, Fri 01:45 | yes |
| `kinz-ledger` | KINZ · Ledger: 1-3 tested fixes in the accounting repo | Sun, Tue, Thu 01:45 | yes, figure changes held |
| `kinz-lab` | KINZ · Lab: one creative idea, judged by a separate Opus agent | Sat 01:45 | if verified |
| `kinz-portfolio` | KINZ · Portfolio review: three public repos, small fixes merged | Sun 01:45 | yes |
| `kinz-vault` | KINZ · Vault gardener: Obsidian upkeep and weekly journal | Sun 06:45 | **no**, PR waits for Nassim |
| `kinz-heartbeat` | KINZ · Heartbeat: one small fix if nothing landed today | daily 06:45 | yes |
| `kinz-digest` | KINZ · Monday digest: the week in one page | Mon 06:45 | no |
| `kinz-genesis` | KINZ · Genesis: new private repo every 28 days | disabled (needs a laptop timer) | no |
| `kinz-zai` | KINZ · Z.ai session | paused | yes |

The job ids were renamed on 2026-10-11 so this engine can't be mistaken for the personal one
(`cloud-maintenance` became `kinz-upkeep`, and so on). Run records from before that date keep
the old names. `calendar/loop-engine.ics` holds every enabled job with a detailed description;
import it into any calendar app, or regenerate it with `python3 scripts/make_ics.py`.

"Loop engine" is one claude.ai routine that fires at 01:45 and 06:45 and runs the jobs that are
due (`prompts/dispatch.md`). It runs at night because the loops share the account's usage limit. The
repos are attached to that routine, so a new repo has to be attached there before any job can
see it.

For this `Kinz-org` copy the routine is "KINZ loop engine — night dispatcher"
(`trig_01RZePiYwx934QeB8rUvXGiP`), created 2026-10-11 in the KINZ claude.ai account. It starts a
fresh session at each fire and sends push notifications. Its repos are attached in the claude.ai
routines UI: `loop-engine-state`, every repo in `registry.json`, and `kinz-obsidian-vault`.

Genesis stays on the laptop because cloud sessions cannot create repositories. On the
personal engine its prompt is `~/.claude/scheduled-tasks/repo-genesis-loop/SKILL.md`, run by
the `loop-genesis` systemd timer. The Kinz-org copy (`kinz-genesis`) is disabled until a
second timer, signed in to `gh` as `kinzorg-afk`, is set up on the laptop.

## Files

| Path | What |
|---|---|
| `schedule.json` | Every job, its schedule and routine id. Source of the calendar. |
| `prompts/` | Instructions for the cloud jobs. Each routine only points here. |
| `registry.json` | The repos, which agent works each one, and notes for future runs. |
| `state.json` | Rotation position and each loop's last run. |
| `loop-settings.json` | Merge rules and genesis settings. |
| `runs/` | One record per run, with a link to the session that did it. |
| `experiments/` | Creative-job goals, written before the work, and the judge's verdict. |
| `reports/` | Weekly summaries. |
| `calendar/loop-engine.ics` | Calendar of all jobs. Regenerate with `python3 scripts/make_ics.py`. |
| `docs/STATE_PROTOCOL.md` | How writers share this repo without overwriting each other. |

## Checks

```
pip install jsonschema
python3 scripts/validate_config.py --runs
python3 scripts/test_make_ics.py && python3 scripts/make_ics.py --check
python3 scripts/test_three_way.py
```

CI runs all of these on every push.
