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
