# Weekly summary 2026-W48 (17 Nov - 23 Nov)

## Shipped (13 PRs merged)
- accounting-analysis #14: CI now runs the report generators end to end (ledger, 17 Nov). https://github.com/Kinz-org/kinz-accounting-analysis-20260623-102129/pull/14
- margin-guardian #10: Dependabot config for pip and Actions (polish, 18 Nov). https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/10
- margin-guardian #12-#16: Dependabot bumps (sqlalchemy, slowapi, python-dotenv, httpx, pyjwt) (upkeep, 20-21 Nov). https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pulls?q=is%3Amerged
- margin-guardian #17: unknown ids now return 404 on PUT /thresholds and DELETE /products (polish, 20 Nov). https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/17
- Next.js-SaaS #42: webhook retries now reach the 24h step, plus retry tests (polish, 18 Nov). https://github.com/Kinz-org/Next.js-SaaS/pull/42
- Next.js-SaaS #43: webhook deliver() keeps DB writes out of the fetch try block (heartbeat, 22 Nov). https://github.com/Kinz-org/Next.js-SaaS/pull/43
- kinz-competitor-intelligence #8: tests for init_db's migration error branch (heartbeat, 20 Nov). https://github.com/Kinz-org/kinz-competitor-intelligence/pull/8
- feed-quality-gate #9: stuck_value_cluster check (polish, 20 Nov). https://github.com/Kinz-org/feed-quality-gate/pull/9
- feed-quality-gate #10: `fqg init` drafts a rules file from a sample feed (lab, 21 Nov). https://github.com/Kinz-org/feed-quality-gate/pull/10

## Broken or stuck
- Merging was denied by the session permission check on 19, 22 and 23 Nov. It worked on 20 and 21 Nov.
- Next.js-SaaS: Dependabot #28-#37 are now all green and conflict-free (upkeep updated them on 22 Nov). They only wait for a merge that the permission check keeps refusing.
- Open and ready, not merged yet: Next.js-SaaS #44 (coverage tooling, 3 new findings incl. an open redirect in /api/org/switch), margin-guardian #18 and feed-quality-gate #11 (README docs), kinz-competitor-intelligence #9 (this morning's heartbeat).
- analytics-service-toolkit: Actions still never runs, so the six agent PRs (#4-#10) cannot merge.
- btc-llm-sentiment: Docker build red. The fix (#4) edits ci.yml and waits for you. #7/#8 are blocked behind it.
- secure-commerce-hub: main red on Security scans (Trivy) since October. #5/#6 blocked.
- On hold, waiting for you: accounting-analysis #8-#11, #13, #15; margin-guardian #11 (edits ci.yml); kinz-competitor-intelligence #7 (scraper/Playwright fix). Vault #4 waits by design.
- Market watch: the 16 Nov scrape worked (1,304 products), but batch 2 still throws away its results (438 products from 24 competitors) until scrape.yml is edited (owner-only).
- kinz-fidelite, kinz-stock-sync, kinz-price-bridge and the vault had no CI activity this week.

## Jobs that did not run
- Every cloud job ran on every scheduled day: upkeep 7/7, heartbeat 7/7 (4 skipped because work had already landed), polish 3/3, ledger 3/3, market-watch, lab, portfolio, vault.
- kinz-genesis: no record for Wed 18 Nov. It runs on the laptop and has never written a record in this engine.

## Creative verdict
Lab ran 21 Nov: `fqg init` in feed-quality-gate, judged VERIFIED (5/5 checks) and merged (#10).
That makes 7 VERIFIED out of 7 experiments, with no rejection ever. The judge may be too easy.

## Next week
Rotation cursor is 5, so the next two repos are kinz-secure-commerce-hub and Next.js-SaaS.
All 12 registry repos are attached.
