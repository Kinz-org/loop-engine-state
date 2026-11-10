# KCI data quality — analyst findings

Updated by the `kinz-competitor-analyst` scheduled task. Same headings every
run so diffs are meaningful; counts first, then the specific rows that changed.

## Run: 2026-11-10

**No new data this week.** The 2026-11-09 scheduled scrape (run 42552227167)
failed in batch 1 after 1 s of scraping, so batch 2 was skipped and the
`weekly-scrape-data` release was not refreshed: it still says "Last updated
2026-11-02 03:18 UTC (run 41378690899)" (7.9 days old at check time). The
downloaded `competitors.db` gives exactly the same figures as last week, so
every number below is the 2026-11-02 snapshot again.

### State
- Competitors: 77 total, 77 active, 49 active with a website. *(unchanged)*
- Products: 1,312 (1,280 priced), across 10 of 77 competitors. *(unchanged)*
- Price history: 1,280 rows, one snapshot (2026-11-02). *(unchanged)*
- Newest `products.scraped_at`: 2026-11-02 04:04 (as stored). *(unchanged,
  now 8 days stale)*
- Catalogues: BIO TUNISIA MAHDIA 1,025, BAHIA COSMETIC 98, HERBÉOS 79,
  FLORAISON 44, AGROLINE 24, Asmin 15, BAYA BEAUTY 13, BIO VALLEY 7, AZATIM 5,
  BIOMED 2. *(unchanged)*

### Scrape coverage
- `scraping_logs`: 25 rows from 2026-11-02, 12 `success`, 13 `failed`.
  *(unchanged — no 2026-11-09 rows exist anywhere)*
- **This week: zero competitors scraped** *(new)*. Cause, from the batch-1 log
  of run 42552227167 (job 128950118615): `npx playwright install --with-deps
  firefox` (`.github/workflows/scrape.yml` line 85) fetched the newest Node
  Playwright, 1.65.0, and installed Firefox build `firefox-1572`; the scraper
  runs the Python package `playwright-1.64.1` (requirements.txt allows
  `>=1.41,<2.0`), which looks for `firefox-1555` →
  `BrowserType.launch: Executable doesn't exist at
  /home/runner/.cache/ms-playwright/firefox-1555/firefox/firefox`. Same drift
  class as the 2026-10-12 failure. Fix: PR #7 (open, `hold` label) changes
  lines 85 and 176 to `python -m playwright install --with-deps firefox`, so
  the browser build always matches the installed Python package.
- **Batch-2 persistence bug: still present on `main`** (9b364df), not
  exercised this week because batch 2 was skipped. `scrape.yml` lines ~220-231
  still run the inline `python -c` with `.offset(25)` that never writes to the
  DB. PR #7 does not touch it. Fix (unchanged): replace that step with
  `python scripts/manual_scrape.py --type web --offset 25`.

### Data quality
- missing price 32 · missing category 163 · missing description 17 ·
  price = 0: 0. *(unchanged, same snapshot)*
- Pagination regression: not present (no competitor at exactly 100).
- FLORAISON 11× 350.0 TND cluster and 3 `/blogs/` pages still present
  *(unchanged)*. Proposed fix unchanged: skip any `product_url` containing
  `/blogs/` before saving, with a test.

### Price movements
- Not measurable: one `price_history` snapshot, and no new release to compare.

### Workflow health
- `scrape.yml`: **2026-11-09 ❌** (Playwright browser mismatch) · 2026-11-02 ✅
  · 2026-10-26 ✅ · 2026-10-19 ✅ · 2026-10-12 ❌ (same cause). 2 of the last 5
  failed on the same drift.
- CI on `main`: green (push run 42170769580, 2026-11-06). PR #7's CI was
  still running at check time.

### Needing owner decision
1. **Merge PR #7 (Playwright install fix) and re-run the scrape** — without it
   next Monday's scrape fails the same way and the data goes two weeks stale.
   https://github.com/Kinz-org/kinz-competitor-intelligence/pull/7
2. **CRITICAL, unchanged: batch 2 saves nothing.** Change the batch-2 step in
   `scrape.yml` (~lines 220-231) to
   `python scripts/manual_scrape.py --type web --offset 25` (can go in the
   same edit as #1).
3. Price history: decide whether the release should keep history across weeks.

## Run: 2026-11-03

The 2026-11-02 scheduled scrape (run 41378690899) succeeded and refreshed the
`weekly-scrape-data` release (2026-11-02 03:18 UTC). `main` is unchanged since
last run (7a19a85), so `scrape.yml` batch 2 still saves nothing.

### State
- Competitors: 77 total, 77 active, 49 active with a website. *(unchanged)*
- Products: **1,312** (1,280 priced), across 10 of 77 competitors.
  *(was 1,344 / 1,322 across 10)*
- Price history: 1,280 rows, one snapshot (2026-11-02). The DB is still rebuilt
  from scratch each week.
- Newest `products.scraped_at`: 2026-11-02 04:04 (as stored).
- Catalogues: BIO TUNISIA MAHDIA 1,025, BAHIA COSMETIC (Elboshra) 98,
  HERBÉOS **79** *(was 87)*, FLORAISON **44** *(was 61)*, AGROLINE **24**
  *(was 30)*, Asmin 15, BAYA BEAUTY 13, BIO VALLEY 7, AZATIM 5, BIOMED **2**
  *(was 3)*. Three catalogues shrank by 8-17 products in one week; that is
  either real delistings or partial scrapes, and one snapshot cannot tell which.

### Scrape coverage
- `scraping_logs`: 25 rows, all batch 1 (all stamped 03:04 UTC, the end of the
  batch-1 step): 12 `success`, 13 `failed` (10× `NS_ERROR_UNKNOWN_HOST`, one
  timeout, one `NS_ERROR_NET_RESET`, one parked domain). *(same split)*
- BIO GATRANA and LABO DES SENTEURS again logged `success` with 0 products.
- 39 of 49 active competitors with a website have no products *(unchanged)*;
  **24 have no `scraping_logs` row** — all of batch 2.
- **Batch-2 persistence bug: still happening.** "Run scraper (Batch 2 —
  competitors 26-49)" ran 12 min 47 s (03:05:55-03:18:42) and reported
  success, yet nothing from it reached the DB. `.github/workflows/scrape.yml`
  on `main` lines ~220-231 still run the inline `python -c` with `.offset(25)`
  that never writes. Owner-only fix: replace that step with
  `python scripts/manual_scrape.py --type web --offset 25` (the flag exists
  since PR #3).

### Data quality
- missing price **32** · missing category 163 · missing description 17 ·
  price = 0: 0. *(was 22 / 163 / 17 / 0)*. Missing prices by competitor:
  FLORAISON 14, BIO VALLEY 7 (all of its products), BIO TUNISIA MAHDIA 5,
  AGROLINE 2, BIOMED 2, BAHIA 1, HERBÉOS 1.
- **Pagination regression: not present.** No competitor has exactly 100 products.
- FLORAISON: the **11× 350.0 TND** cluster is still there *(unchanged)*, and
  it is also that competitor's maximum price. Still **3** `/blogs/news/...`
  pages scraped as products. Proposed fix (unchanged): skip any `product_url`
  containing `/blogs/` before saving, with a test.
- **AGROLINE 3,075 TND outlier: gone this week** *(changed)*. The "Crème de
  jour hydratante SPF 30" row is not in the catalogue at all (AGROLINE now
  25-135 TND, 24 products), so the decimal-separator bug is not fixed, just not
  triggered. Keep the proposed QA check (flag a price >10× the competitor's
  median); no product crosses it this week.
- BAHIA COSMETIC clusters (16× 20.0, 11× 30.0, 9× 25.0) and BIO TUNISIA MAHDIA
  clusters of 8 (6.85, 25.0, 38.2, 40.0) look like real round price points in
  large catalogues. *(unchanged)*

### Price movements
- Not measurable, same structural limit: one `price_history` snapshot per
  release. Keeping last week's DB (or appending `price_history` across weeks)
  is needed first.

### Workflow health
- `scrape.yml`: 2026-11-02 ✅ · 2026-10-26 ✅ · 2026-10-19 ✅ · 2026-10-12 ❌
  (Playwright drift). Only 4 runs exist in Kinz-org. CI on `main`: green.
- Lines 85 and 176 still run `npx playwright install --with-deps firefox`.

### Needing owner decision
1. **CRITICAL, unchanged: batch 2 saves nothing.** Change the batch-2 step in
   `scrape.yml` (~lines 220-231) to
   `python scripts/manual_scrape.py --type web --offset 25`.
2. Playwright drift: `npx playwright install` → `python -m playwright install`
   in `scrape.yml` (lines 85, 176).
3. Price history: decide whether the release should keep history across weeks;
   without it, price movements and catalogue shrinkage cannot be checked.

## Run: 2026-10-27

The 2026-10-26 scheduled scrape (run 40258810680) succeeded and refreshed the
`weekly-scrape-data` release (2026-10-26 02:53 UTC). PR #3 (`--offset` for
`manual_scrape.py`) was merged on 2026-10-22, but `scrape.yml` was not changed,
so batch 2 still saves nothing.

### State
- Competitors: 77 total, 77 active, 49 active with a website. *(unchanged)*
- Products: **1,344** (1,322 priced), across **10 of 77 competitors**.
  *(was 1,251 / 1,228 across 9)*
- Price history: 1,322 rows, one snapshot (2026-10-26). The DB is rebuilt
  from scratch each week, so every `first_seen_at` is 2026-10-26.
- Newest `products.scraped_at`: 2026-10-26 03:38 UTC.
- Catalogues: BIO TUNISIA MAHDIA 1,025, **BAHIA COSMETIC (Elboshra) 98 (new)**,
  HERBÉOS 87 *(was 94)*, FLORAISON 61, AGROLINE 30 *(was 29)*, Asmin 15,
  BAYA BEAUTY 13, BIO VALLEY 7, AZATIM 5, BIOMED 3 *(was 2)*.

### Scrape coverage
- `scraping_logs`: 25 rows, all batch 1: 12 `success`, 13 `failed` (10×
  `NS_ERROR_UNKNOWN_HOST`, plus HERBES DE TUNISIE timeout, GREEN ALOE net
  reset, HEAVENLY BIO parked). *(same split as last week)*
- BIO GATRANA and LABO DES SENTEURS again logged `success` with 0 products.
- 39 of 49 active competitors with a website have no products *(was 40)*;
  **24 have no `scraping_logs` row** — all of batch 2.
- **Batch-2 persistence bug: still happening.** The "Run scraper (Batch 2 —
  competitors 26-49)" step ran 13 min and reported success, yet nothing from
  it is in the DB. On `main` (7a19a85) `.github/workflows/scrape.yml` lines
  ~220-231 still run the inline `python -c` with `.offset(25)` that never
  writes. The agent-side half (PR #3) is now merged; the remaining fix is
  owner-only: replace that step with
  `python scripts/manual_scrape.py --type web --offset 25`.

### Data quality
- missing price 22 · missing category 163 · missing description 17 · price = 0: 0.
  *(was 23 / 163 / 12 / 0)*
- **Pagination regression: not present.** No competitor has exactly 100 products.
- FLORAISON: the pinned cluster moved from 9× 400.0 to **11× 350.0 TND**
  *(changed)* — still a same-price cluster, likely the scraper picking up one
  shared price element (e.g. a "from" price or a bundle) rather than each
  product's own. Still **3** `/blogs/news/...` pages scraped as products.
  Proposed fix (unchanged): skip any `product_url` containing `/blogs/` before
  saving, with a test.
- **AGROLINE "Crème de jour hydratante SPF 30" still at 3,075 TND** against a
  75 TND median. Decimal-separator parsing bug (30.75 → 3075). Proposed fix:
  fix the `,`/`.` handling in the price parser for that site and add a QA
  check flagging a price >10× the competitor's median.
- New: BAHIA COSMETIC clusters (16× 20.0, 11× 30.0, 9× 25.0) look like real
  round price points for a 98-product catalogue, not a parsing fault.
- Low outliers at BIO TUNISIA MAHDIA (3.80–4.50 TND vs 49.85 median) are small
  items (30 ml deodorant, balm), plausible.

### Price movements
- Not measurable, same structural limit: only one `price_history` snapshot
  exists because each release replaces the last week's DB. Keeping the previous
  release's DB (or appending `price_history` across weeks) is needed first.

### Workflow health
- `scrape.yml`: 2026-10-26 ✅ · 2026-10-19 ✅ · 2026-10-12 ❌ (Playwright
  drift). CI on `main`: green.
- Lines 85 and 176 still run `npx playwright install --with-deps firefox`; the
  drift that broke 10-12 can recur.

### Needing owner decision
1. **CRITICAL, unchanged: batch 2 saves nothing.** PR #3 is merged; now change
   the batch-2 step in `scrape.yml` (~lines 220-231) to
   `python scripts/manual_scrape.py --type web --offset 25`.
2. Playwright drift: `npx playwright install` → `python -m playwright install`
   in `scrape.yml` (lines 85, 176).

## Run: 2026-10-20

**Data is back.** The 2026-10-19 scheduled scrape (run 39189190475) succeeded
in both batches and created the `weekly-scrape-data` release for the first time
in the Kinz-org repo (published 2026-10-19 02:54 UTC). It covers only the first
25 competitors, because the batch-2 bug is still there.

### State
- Competitors: 77 total, 77 active (seed-resurrection bug unchanged), 49
  active with a website.
- Products: **1,251** (1,228 priced), across **9 of 77 competitors**.
  *(changed: 1,336 / 1,314 across 10 at the 09-23 baseline; 10-13 had no data)*
- Price history: 1,228 rows, all `recorded_at` 2026-10-19. This is a single
  snapshot because the repo and its release history are new.
- Newest `products.scraped_at`: 2026-10-19 03:40 UTC. Every product has
  `first_seen_at` 2026-10-19, because the DB is rebuilt from scratch each week.
- Largest catalogues: BIO TUNISIA MAHDIA 1,025, HERBÉOS 94, FLORAISON 61,
  AGROLINE 29, Asmin 15, BAYA BEAUTY 13, BIO VALLEY 7, AZATIM 5, BIOMED 2.

### Scrape coverage
- `scraping_logs` has 25 rows, all from batch 1: 12 `success` and 13 `failed`.
  The failures are mostly `NS_ERROR_UNKNOWN_HOST` (dead or wrong domains),
  plus one timeout (HERBES DE TUNISIE), one net reset (GREEN ALOE) and one
  parked domain (HEAVENLY BIO).
- BIO GATRANA and LABO DES SENTEURS logged `success` with 0 products.
- 40 of 49 active competitors with a website have no products, and **24 have
  no `scraping_logs` row at all**: the whole batch 2 (ECOVILLAGE, KARINA,
  NAKAWA, SARAYA, KINZ itself, ...).
- **Batch-2 persistence bug: still happening.** The "Run scraper (Batch 2 —
  competitors 26-49)" step reported success, but nothing from it is in the
  database. On `main` (dea5c98), `.github/workflows/scrape.yml` lines ~220-231
  still use the inline `python -c` with `.offset(25)` that calls
  `scrape_multiple_competitors()` and never writes. The agent-side half of the
  fix is ready: PR #3 adds `--offset` to `scripts/manual_scrape.py` (CI green,
  left open because it is a scraper change). The workflow half (batch 2 calls
  `python scripts/manual_scrape.py --type web --offset 25`) is owner-only.

### Data quality
- missing price 23 · missing category 163 · missing description 12 · price = 0: 0.
  *(was 22 / 162 / 17 / 0 at 09-23)*
- **Pagination regression: not present.** No competitor has exactly 100 products.
- FLORAISON: still 9 products pinned at exactly 400.0 TND (unchanged since
  09-23), and now **3** blog posts scraped as products (`/blogs/news/...`
  URLs) *(was 1)*. Cause: the Shopify-site path does not filter out
  `/blogs/` URLs. Proposed fix: skip any `product_url` containing `/blogs/`
  in the web scraper before saving, with a test.
- **NEW outlier: AGROLINE (DERMAFIG) "Creme de jour hydratante spf 30" at
  3,075 TND.** The rest of its catalogue tops out at 135 TND. This is almost
  certainly a decimal-parsing error (30.75 → 3075). Proposed fix: check the
  price parser's handling of `,`/`.` thousands and decimal separators on that
  site, and add a QA check that flags a price more than 10× the competitor's
  median.
- Other same-price clusters (HERBÉOS 10× 25.0, BIO TUNISIA MAHDIA 8× each of
  several prices) are the same as at 09-23 and look like real price points.

### Price movements
- Not measurable. Only one `price_history` snapshot exists (2026-10-19). The
  structural limit from 09-23 still holds: each release carries only that
  week's snapshot, so movements need the previous release's DB to be kept.

### Workflow health
- `scrape.yml` runs in Kinz-org: 2026-10-19 ✅ (scheduled) · 2026-10-12 ❌
  (Playwright/firefox drift in batch 1).
- This week's success does not mean the drift is fixed. Lines 85 and 176
  still run `npx playwright install --with-deps firefox`. This week the
  versions happened to match. The `python -m playwright install` fix is still
  owner-only.

### Needing owner decision
1. **CRITICAL, unchanged: batch 2 saves nothing.** Half the competitors
   (N–Z, 24) never reach the data. Merge PR #3 (`--offset`), then change the
   batch-2 step in `scrape.yml` to `python scripts/manual_scrape.py --type web
   --offset 25`.
2. Playwright drift: change `npx playwright install` → `python -m playwright
   install` in `scrape.yml` (lines 85, 176) before it breaks again.
3. 13 batch-1 competitors fail on unknown hosts or parked domains. Their
   `website` values in the seed probably need correcting or the competitors
   need marking inactive (owner data, not touched here).
4. Carried: FLORAISON 400 TND cluster and blog posts; the seed-resurrection
   bug (all competitors `is_active=1`).

---

## Run: 2026-10-13

**No data this run: there is no `weekly-scrape-data` release to read.** The
repo was recreated under `Kinz-org` on 2026-10-11 (repo `created_at`
2026-10-11T17:28Z; releases and Actions history did not carry over from the
old owner). Its only scheduled scrape since then, run 38194388467 on
2026-10-12 02:04 UTC, failed in batch 1. The release is only published by
the last step of batch 2, and batch 2 is skipped when batch 1 fails, so the
release has never been created in this repo. `GET
/releases/tags/weekly-scrape-data` returns 404 and `/releases` is empty. No
database was downloaded and none of the data checks could run.

### State
- Competitors / products / price history / newest `scraped_at`: **not
  measurable**. No release exists in `Kinz-org/kinz-competitor-intelligence`.
  The last known figures are still the 09-23 baseline below (77 competitors,
  1,336 products across 10 competitors, 1,314 price-history rows).
- Data age: the newest data any job here has seen is from 2026-09-21, now
  22 days old. Treat it as stale. *(changed: was 2 days old at 09-23)*

### Scrape coverage
- Not measurable this run (no DB).
- **Batch-2 persistence bug: still present in the code.** `main` (aa4bd6e)
  `.github/workflows/scrape.yml` lines ~219-243 still use the inline `python
  -c` step that calls `scrape_multiple_competitors()` and never writes to the
  DB. Batch 2 did not run this week (it was skipped after batch 1 failed), so
  there is no batch-2 log to check. Fix unchanged: add `--offset` to
  `scripts/manual_scrape.py` and have batch 2 call `python
  scripts/manual_scrape.py --type web --offset 25`.

### Data quality
- Not measurable this run (no DB). Open items carried from 09-23: FLORAISON
  cluster pinned at 400 TND plus one blog post scraped as a product;
  missing_category 162 out of 1,336.
- Pagination regression (exactly 100 products): cannot be checked this run.

### Price movements
- Not measurable this run. Structural limit unchanged from 09-23: each
  release holds only one week's `price_history` snapshot.

### Workflow health
- `scrape.yml` runs in the Kinz-org repo: only 1 so far. 2026-10-12 ❌
  (scheduled, sha cc3b107). Earlier runs belong to the old repo: 09-21 ✅ ·
  09-14 ❌ · 09-07 ❌ (from the 09-23 section). The old-repo runs on 09-28 and
  10-05 were not visible to this job.
- **Failure cause: the same Playwright browser-version drift as 09-07 and
  09-14, now the 3rd occurrence.** Batch 1, step "Run scraper (Batch 1 —
  competitors 1-25)" (job 114633761531) failed with `BrowserType.launch:
  Executable doesn't exist at
  /home/runner/.cache/ms-playwright/firefox-1543/firefox/firefox`. The pip
  package `playwright` (unpinned, `requirements.txt`: `playwright>=1.41,<2.0`)
  expects firefox-1543, but `npx playwright install --with-deps firefox`
  (scrape.yml lines 85 and 176) installed a different revision. Batch 2 was
  skipped, and the "Send Summary" job reported success, which hides the
  failure.
  - Fix (owner, `.github/workflows/scrape.yml`): change both `npx playwright
    install --with-deps firefox` lines to `python -m playwright install
    --with-deps firefox`. The browser then always matches the Python package.
    The Node.js setup steps can be dropped too. An agent-side alternative
    that does not touch CI: pin `playwright==<exact>` in `requirements.txt`.
    This only works if the npx version also matches, so the workflow change
    is the real fix.
- Side effect to know about: the release is published only from batch 2.
  Any batch-1 failure therefore means no data that week, and in a fresh repo
  it means no release at all. Consider publishing the release with
  `if: always()` from whichever job finishes last, or from the summary job.

### Needing owner decision
1. **CRITICAL, NEW: no competitor data exists in the Kinz-org repo.** The
   first scrape after the migration failed (Playwright drift), so the
   `weekly-scrape-data` release was never created. Fix item 2 below, then
   re-run "Weekly Competitor Scrape" by hand (workflow_dispatch) rather than
   waiting for Monday.
2. **Playwright/firefox drift: 3rd failure (09-07, 09-14, 10-12).** Fix this
   1-line change in `scrape.yml` (`npx playwright install` → `python -m
   playwright install`, lines 85 and 176). Agents may not edit it.
3. **CRITICAL, unchanged: batch 2 saves nothing** (scrape.yml inline
   `python -c` step). Even after item 2 is fixed, all N-Z competitors stay
   missing until this lands.
4. Carried: FLORAISON wrong-price cluster; the seed-resurrection bug in
   `seed_from_json.py` (all competitors read `is_active=1`); outlets and
   price-history not available to this job.

---

## Run: 2026-09-23

**First run of the new cloud `cloud-kinz-analyst` job.** It reads the weekly
`weekly-scrape-data` GitHub release (published Mondays), not the local DB the
retired laptop job used. Numbers below are a new baseline, not directly
comparable to the 09-01 section below (different data source).

### State
- Competitors: 77 total, 77 active (`is_active=1`) — seed-resurrection bug
  unchanged: `seed_from_json.py` hardcodes `is_active=True` on every seed, so
  all 77 (including locally-retired dead sites) read active in every cloud
  release. 49 have a website.
- Products: 1,336 (1,314 priced), across only **10 of 77 competitors** —
  batch 2 still isn't persisting (see Scrape coverage).
- Price history rows: 1,314, all recorded 2026-09-21 08:07 UTC — a single
  snapshot; the cloud release doesn't carry prior weeks' history.
- Newest `products.scraped_at`: 2026-09-21 09:07:25 UTC. Release published
  2026-09-21 08:23 UTC — 2 days old, fresh.
- Outlets (`parapharmacies` table): **0 rows** in this release. The
  ~3,923-row outlets dataset the retired laptop job reported (Google Maps
  scrape, hand-entered sales-pipeline fields) lives only in the local DB —
  the weekly workflow's seed step only ever seeds `competitors`, never
  `parapharmacies`. This job has no access to that data; see item 5 below.

### Scrape coverage
- 39 of 49 active+website competitors have zero products. 24 of those have
  zero `scraping_logs` rows at all — the batch-2 (N–Z, 24 competitors)
  persistence bug is still happening, confirmed again this run.
- Batch 2's own log this run (job 106258699092, "Run scraper (Batch 2 —
  competitors 26-49)") shows it did real, successful scraping — e.g.
  "Scraped ECOVILLAGE NATURAL BEAUTY: 77 unique products... in 399.48s",
  "Scraped KARINA TUNISIE: 25 unique products", then "Batch 2: 24
  competitors to scrape" / "Done: 24 results" — and none of it reached the
  database. All 10 competitors with products, and all 1,336 products, are
  exactly what batch 1 (A–M) wrote. Root cause and fix unchanged from the
  09-01 note: the inline `python -c` step only calls the pure
  `scrape_multiple_competitors()`, which returns a list and never touches
  the DB; only `manual_scrape.py` writes to it, and batch 2 bypasses it.
- The other 15 zero-product competitors (with scraping_logs rows) are
  batch-1 scrapes that logged `failed` — 13 of the 25 batch-1
  `scraping_logs` rows are `failed`, 12 `success`.

### Data quality
- missing_price: 22 · missing_category: 162 · missing_description: 17 ·
  price=0: 0 (measured against the 1,336 products this release actually
  has — not comparable to the old 122/161/93 counts against the larger
  frozen local catalogue).
- **FLORAISON natural beauty wrong-price cluster still present, price
  shifted 350→400 TND.** 9 products (was 13) pinned to exactly 400.0 TND;
  the rest of its catalogue ranges 16–145 TND. Still includes one blog post
  scraped as a product: "Le Collagène dans les Soins : Mythe ou Réalité ?".
  Same root cause as 08-28 (a banner/promo price element matched instead of
  the real price) — the fixed value moving 350→400 between runs suggests
  it's picking up a live promotional banner, not a stale cached value.
- No WooCommerce pagination regression: no competitor has exactly 100
  products this run (largest is BIO TUNISIA MAHDIA at 1,014).
- Other clusters seen (BAHIA COSMETIC 16× 20.0 TND / 11× 30.0 TND / 9×
  25.0 TND; HERBÉOS 10× 25.0 TND; BIO TUNISIA MAHDIA 8× each of
  6.85/25.0/38.2 TND) are plausible for catalogues this size (98 and 1,014
  products respectively) — not flagged, unlike FLORAISON where the cluster
  price sits far outside that competitor's own range.

### Price movements
- None detected — cannot be, structurally. `price_history` in this release
  only ever holds the current week's snapshot (all 1,314 rows recorded
  2026-09-21 08:07 UTC; 0 products have more than one row). Movement
  detection needs either the local DB (which accumulates history) or this
  job keeping its own week-over-week snapshot — neither is in scope for a
  read-only job working off one release download.

### Workflow health
- Last 5 scheduled `scrape.yml` runs: 09-21 ✅ · 09-14 ❌ · 09-07 ❌ ·
  08-31 ✅ · 08-24 ✅.
- **New failure mode, not the previously-documented secret-unset pattern.**
  09-07 and 09-14 both failed identically at "Run scraper (Batch 1 —
  competitors 1-25)" (batch 2 then skipped — it depends on batch 1's DB
  artifact): `playwright._impl._errors.Error: BrowserType.launch:
  Executable doesn't exist at
  /home/runner/.cache/ms-playwright/firefox-1538/firefox/firefox`.
  - Root cause: `requirements.txt` pins `playwright>=1.41,<2.0` (no exact
    version), so `pip install` picks up whatever's newest that week.
    Browsers are installed separately via `npx playwright install
    --with-deps firefox` (scrape.yml lines 85 and 176) — the **Node** CLI,
    resolved by `npx` to its own latest version, independent of the
    pip-installed **Python** package. On 09-14, pip installed
    `playwright==1.62.0` (expects browser revision firefox-1538) while
    `npx playwright install` downloaded firefox-1543 — mismatch, launch
    fails. On 09-21, pip installed `playwright==1.63.0` and the two
    happened to line up again, so it passed. The same failure will recur
    any week these two independently-resolved versions drift apart.
  - Fix (in scrape.yml, so it's an owner call): replace `npx playwright
    install --with-deps firefox` with `python -m playwright install
    --with-deps firefox` in both the batch-1 and batch-2 jobs, so the
    browser binary always matches the package that launches it. Pinning
    `playwright==<exact>` in requirements.txt would also close it.

### Needing owner decision
1. **CRITICAL — cloud scrape batch 2 still saves nothing** (confirmed again
   this run; 4th+ consecutive weekly occurrence). Batch 2 scrapes live and
   successfully but never writes to the DB. Fix: give `manual_scrape.py` an
   `--offset` flag, have batch 2 call `manual_scrape.py --offset 25`
   instead of its inline one-liner. ~40% of the catalogue (all N–Z
   competitors) is silently missing from every weekly release until this
   lands.
2. **NEW — playwright/firefox version-drift bug caused 2 consecutive full
   scrape failures** (09-07, 09-14). Fix is a 1-line change in
   `.github/workflows/scrape.yml` (`npx playwright install` → `python -m
   playwright install`), which agents may not edit.
3. FLORAISON natural beauty wrong-price cluster (9 products @ 400 TND, was
   13 @ 350 TND) + one blog post scraped as a product — likely a
   promotional banner element being matched. No data mutation done.
4. Seed-resurrection bug in `seed_from_json.py` — all 77 competitors
   (including locally-retired ones) still read `is_active=1` in every
   cloud release.
5. This job cannot see the 3,923-row outlets (`parapharmacies`) dataset or
   real price-movement history — both live only in the local DB, which the
   retired laptop job used and this cloud job doesn't have access to. If
   outlets QA or week-over-week price tracking still matters, it needs
   either the local DB attached to this routine or the weekly workflow
   extended to publish these.
