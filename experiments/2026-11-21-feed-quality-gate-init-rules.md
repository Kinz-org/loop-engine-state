# 2026-11-21 · feed-quality-gate · `fqg init` drafts a rules file from a feed

**Idea.** Onboarding a new feed today means hand-writing a rules YAML from `rules.example.yaml`.
`fqg init -i <feed>` profiles the feed and drafts a commented rules file for it: it guesses the
id column (unique, fully populated) and the timestamp column (parses as dates), and sets each
column's `max_null_ratio` from the gaps it actually observed, so the human only has to review it.

Repo: `Kinz-org/feed-quality-gate`, branch `claude/loop-creative-20261121-fqg-init`.
Setup: `python3 -m venv /tmp/v && /tmp/v/bin/pip install -e '.[dev]'`, then use `/tmp/v/bin/fqg`.

## Success checks

1. `fqg init -i examples/sample_feed.csv` exits 0 and prints YAML containing
   `id_column: product_id` and `timestamp_column: scraped_at`.
2. `fqg init -i examples/sample_feed.csv -o /tmp/r.yaml` writes a file that
   `fqg explain -r /tmp/r.yaml` accepts (exit 0), and that file lists every column of the
   sample feed except the id and timestamp columns under `completeness.columns`.
3. A feed with no gaps and recent timestamps passes `fqg check` against the rules drafted
   from it (exit 0); `tests/test_init.py` contains a test that proves this.
4. Running `fqg init ... -o <existing file>` without `--force` exits 2 and leaves the
   existing file unchanged; with `--force` it overwrites it.
5. `pytest -q` (whole suite) and `ruff check .` both pass, and the CI smoke step
   (`fqg check -i examples/sample_feed.csv -r rules.example.yaml` must exit 1) still holds.
