# Weekly summary 2026-W47 (10 Nov - 16 Nov)

## Shipped (12 PRs merged)
- feed-quality-gate #6: docs link the open-bug backlog (upkeep, 10 Nov). https://github.com/Kinz-org/feed-quality-gate/pull/6
- feed-quality-gate #7: freshness ignores future-dated rows (polish, 12 Nov). https://github.com/Kinz-org/feed-quality-gate/pull/7
- feed-quality-gate #8: unknown rules-file keys now fail instead of being ignored (polish, 16 Nov). https://github.com/Kinz-org/feed-quality-gate/pull/8
- margin-guardian #7: CORS limited to configured origins (12 Nov). https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/7
- margin-guardian #8: price floor and headroom CLI (12 Nov). https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/8
- margin-guardian #9: margin/retention settings listed in .env.example (12 Nov). https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/9
- kinz-competitor-intelligence #5: seed honours `is_active` (12 Nov). https://github.com/Kinz-org/kinz-competitor-intelligence/pull/5
- accounting-analysis #12: Shopify monthly money rounded to the millime (12 Nov). https://github.com/Kinz-org/kinz-accounting-analysis-20260623-102129/pull/12
- Next.js-SaaS #38: org-membership tests (12 Nov). https://github.com/Kinz-org/Next.js-SaaS/pull/38
- Next.js-SaaS #39: `pnpm cost:estimate` offline cost CLI (lab, 14 Nov). https://github.com/Kinz-org/Next.js-SaaS/pull/39
- Next.js-SaaS #40: README fixes for Prisma 7 (portfolio, 15 Nov). https://github.com/Kinz-org/Next.js-SaaS/pull/40
- Next.js-SaaS #41: exportUserData tests plus a null-URL fix (polish, 16 Nov). https://github.com/Kinz-org/Next.js-SaaS/pull/41

## Broken or stuck
- Merging worked again from 12 Nov. It was denied by the session permission check on 10 and 11 Nov.
- Next.js-SaaS: ten Dependabot PRs (#28-#37) red on Security Scans. They need `GITLEAKS_LICENSE` added as a Dependabot secret (only you can do this).
- analytics-service-toolkit: six agent PRs (#4, #5, #6, #8, #9, #10) and Actions never runs, so none can merge.
- btc-llm-sentiment #7/#8 red on the Docker build. The fix (#4) is on hold because it edits ci.yml.
- secure-commerce-hub: main and #5/#6 red on Security scans (Trivy). The fix needs a workflow edit.
- On hold, waiting for you: accounting-analysis #8-#11 and #13, kinz-competitor-intelligence #7 (scraper fix), btc #4. Vault #4 waits by design.
- Market watch: the 9 Nov scrape failed (Playwright/Firefox version mismatch). Data is still the 2 Nov snapshot until kci #7 lands.
- kinz-fidelite, kinz-stock-sync and the vault have no CI runs at all.

## Jobs that did not run
- Fri 13 Nov: no records at all from the 01:45 or 06:45 fire. Missing kinz-upkeep, kinz-polish and kinz-heartbeat.
- Sat 14 Nov: kinz-heartbeat missing. The 01:45 fire ran (upkeep, lab).
- kinz-genesis: no record for Wed 11 Nov. It runs on the laptop and has never written a record in this engine.
- Ran as scheduled: market-watch (10), ledger (10, 12, 15), lab (14), portfolio (15), vault (15), upkeep on the other 6 days, heartbeat on the other 5 days (4 skipped because work had already landed).

## Creative verdict
Lab ran 14 Nov: `pnpm cost:estimate` in Next.js-SaaS, judged VERIFIED and merged (#39).
That makes 6 VERIFIED out of 6 experiments, with no rejection ever. The judge may be too easy.

## Next week
Rotation cursor is 3, so the next two repos are kinz-competitor-intelligence and kinz-margin-guardian-pipeline.
All 12 registry repos are attached.
