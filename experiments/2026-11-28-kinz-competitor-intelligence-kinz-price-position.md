# Experiment 2026-11-28 · kinz-competitor-intelligence · KINZ price positioning

Loop: kinz-lab · Run: https://claude.ai/code/session_01FRg7pJeUs742rzWDJRXnuL

## Idea

A new offline report, `scripts/kinz_price_position.py`, places each KINZ product against the
competitor prices already in the database for the same category (count, min, median, max,
KINZ's percentile, and a verdict: below / within / above the market's middle half, or "too few
competitors"). It answers "are we priced like the market?" from the data this repo already
collects, without scraping anything.

## Success checks

1. `python scripts/kinz_price_position.py --demo` runs with no database, no network and no
   secrets, exits 0, and prints a table with one row per demo KINZ product (at least 4 rows)
   that has columns for category, KINZ price, competitor count, competitor median and verdict.
2. In that demo output, at least one product is verdict `below`, one `within`, one `above`, and
   one `too few competitors` (fewer than `--min-peers`, default 3).
3. A KINZ product whose category is not given is categorised from its name with the repo's
   existing `CATEGORY_KEYWORDS` (e.g. "Huile de figue de barbarie 30ml" → "Huile"), not a
   second keyword list. Confirmed by reading the code and by a test.
4. `--csv <path>` writes the same rows to a CSV file with a header row, and the KINZ input can
   be a CSV (`product,price_tnd[,category]`) or the `data/kinz_products.xlsx` workbook
   that `scripts/scrape_kinz.py` writes. Both input paths are covered by tests.
5. `pytest tests/test_kinz_price_position.py` passes, including a test that loads competitor
   prices from the test database (inactive competitors and null/zero prices excluded), and the
   full suite plus `ruff check .` still pass.

## Verdict (fresh Opus judge, 2026-11-28): VERIFIED

PR: https://github.com/Kinz-org/kinz-competitor-intelligence/pull/11 (branch
`claude/loop-creative-20261128-kinz-price-position`, head 4a1d98c). CI: Tests and Lint green.

1. PASS. `--demo` exited 0 with `DATABASE_URL` pointed at a scratch path (no file created),
   sockets patched to fail, and `src.database`/`sqlalchemy` never imported. 5 rows with
   Category, KINZ TND, Competitors, Median TND and Verdict columns; Huile quartiles
   (23.5/28/32.5) checked by hand.
2. PASS. Summary line "above: 1, within: 1, below: 1, too few competitors: 2" (Hydrolat has 2
   competitors, under the default 3).
3. PASS. `categorise()` calls `web_scraper.extract_category(..., product_text=name)`, which
   reads the module's `CATEGORY_KEYWORDS`; no second list in the repo.
   `test_categorise_follows_changes_to_scraper_keyword_list` monkeypatches that list and the
   answer follows.
4. PASS. `--csv` writes a header plus the same rows. CSV and workbook inputs are both tested;
   the judge also built a workbook with the real `scrape_kinz.write_excel` (no network) and the
   reader parsed it correctly, end to end through the CLI.
5. PASS. 25/25 in the new test file, 704 in the full suite, `ruff check .` clean;
   `test_load_competitor_prices_filters_inactive_kinz_and_bad_prices` excludes inactive, KINZ,
   null, zero and uncategorised rows.

Outside the checks: `--kinz` against an uninitialised database (no tables) fails with a raw
`OperationalError` traceback rather than a clean message.

Merge: not done. Merging was denied by the session's permission check earlier in this run
(kinz-upkeep), so the PR is left open, ready, for kinz-upkeep or Nassim.
