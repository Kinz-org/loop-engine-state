# Job: vault gardener (Sunday morning)

Loop name: `kinz-vault`. Read `prompts/_common.md` first; everything there applies, except the
merge rules: **this job never merges.** The vault is Nassim's own knowledge base, so every
change waits for him in a pull request.

**Goal:** keep the Obsidian vault `Kinz-org/kinz-obsidian-vault` navigable, and write down each
week what the loops did, so the vault stays the place where Nassim understands his own work.

The vault is at `/home/user/kinz-obsidian-vault`. If it is not there, report
`NEEDS YOU: attach Kinz-org/kinz-obsidian-vault to the Loop engine routine` and stop.

## The vault's conventions (keep them)

- Written in French. Notes use wikilinks (`[[Note]]`), resolved by file name, not markdown links.
- Every note has frontmatter: `title`, `date`, `type` (`moc`, `concept`, `note`,
  `project-log`, `decision-log`), `tags` as a YAML list, `summary`, sometimes `aliases`,
  `status`, `related`.
- `MOCs/Atlas — Index du Vault.md` is the entry point. Topic hubs (MOCs) live in `MOCs/`, and
  each working note ends with a link back to its hub.
- Grey links (wikilinks to notes that do not exist) are **deliberate leads, not errors.** Never
  "fix" one by deleting it or by creating an empty note.

## Never

- Move, rename or delete a note. Renames belong in Obsidian, which updates the links.
- Edit `.obsidian/`, `.claude/`, `.claudian/` or `Templates/`.
- Rewrite a note's body. You may add a line or a section, as described below, and fill a
  missing frontmatter field.
- Put secrets, tokens, customer data or anything from `data/competitors_seed.json` in a note.
- Merge the pull request.

## Steps

1. **Check.** Run, from the state repo:
   `python3 scripts/vault_check.py /home/user/kinz-obsidian-vault --ignore-source "MOCs/Atlas — Index du Vault.md"`
   It lists notes missing a `type`, orphans (no other note links to them) and the unwritten
   link targets ranked by how many notes cite them.
2. **Missing `type`.** Read each such note and add the type its content fits. A dated record
   of a work session is `project-log`, a record of a choice and its reasons is
   `decision-log`, a definition is `concept`, a hub is `moc`, anything else is `note`.
3. **Orphans.** Link each orphan from the hub it belongs to, as one line in that hub's list of
   notes (`- [[Note]] — what it is`). If no hub fits, list it in your report instead.
4. **Leads table.** In the Atlas, replace the table under `## Pistes à écrire` with the
   unwritten targets cited by 4 or more notes (from step 1), keeping the section's wording and
   updating its date. Leave the section alone if the list did not change.
5. **Weekly journal.** Write `Journal/Journal des boucles — <ISO-year>-W<week>.md`, in French:
   - frontmatter: `title`, `date` (today), `type: project-log`, `tags: [loop-engine, journal]`,
     `summary` (one sentence on the week),
   - from this week's `runs/*.json` in the state repo (the last 7 days): each job, how many times
     it ran and with what status, the PRs merged (one line each, with its link), and every
     `NEEDS YOU` still open,
   - the portfolio report of the week, if `kinz-portfolio` wrote one, as a link and two lines,
   - last line: `Rattaché à [[Journal des boucles]]`.

   If `MOCs/Journal des boucles.md` does not exist, create it as a hub (`type: moc`, a two-line
   intro, a list of the weekly notes, newest first) and add it to the Atlas's
   `## Index transversaux` section. Otherwise add the new week at the top of its list.
6. **3D view.** If any note was added or linked, run `python3 .claude/build-planets.py` in the
   vault so `kinz-planets.html` matches.
7. **Check again.** Run step 1 again. The counts of missing types and orphans must not have
   gone up. Put the before and after numbers in the PR body.
8. **Pull request.** Commit on `claude/loop-vault-<YYYYMMDD>`, push, and open one PR, ready for
   review, titled `Vault: semaine <ISO-year>-W<week>`. The body lists every file changed and
   why, then the check numbers, then `Run: <run link>`. Do not merge it, and do not label it.
   If a previous `claude/loop-vault-` PR is still open, do not open a second one: push this
   week's commits to that PR's branch and say so in its body.

## Final message

`NEEDS YOU: vault PR ready to review — <link>` when a PR was opened or updated. `OK: vault
unchanged` when there was nothing to do (no journal is written for a week with no runs).
