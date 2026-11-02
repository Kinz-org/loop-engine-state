# Weekly summary 2026-W45 (26 Oct - 2 Nov)

## Shipped (8 PRs merged)
- feed-quality-gate #5: a valid row that shares an id with a quarantined one now stays clean (2 regression tests).
- kinz-margin-guardian-pipeline #6: SECURITY.md, CONTRIBUTING and the README tree now match the code.
- Next.js-SaaS #27: four README statements the code contradicted.
- kinz-accounting-analysis #3, #6, #7 (merged 27 Oct): margin wording tiered, supplier payments no longer counted as "Payments Received", only confirmed sale orders in product sales.
- kinz-stock-sync #3 and #4: Shopify drafts and merged soaps; loyalty stamps for till sales.

## Broken or stuck
- Next.js-SaaS: 10 Dependabot PRs (#28-#37) open; Security Scans are red on gitleaks only (per upkeep).
- kinz-accounting-analysis #8 (A/R and A/P reconciliation) is labelled `hold`: it changes a reported figure, so it waits for you.
- analytics-service-toolkit: #5 and #6 are open with no checks, so they cannot merge. Heartbeat opened #7, a duplicate of #6, and closed it this run.
- btc-llm-sentiment #7 duplicates the closed #6; #8 open. secure-commerce-hub #5 (Trivy red, pre-existing). feed-quality-gate #6 and vault #4 open (vault never auto-merges).
- Merges were denied by the session permission check in upkeep for three runs in a row (up to 27 Oct).
- Actions now shows push and dynamic runs on Next.js-SaaS, but a pull_request run failed on 26 Oct.

## Jobs that did not run
- kinz-upkeep: missing 28, 29, 30, 31 Oct and 2 Nov (ran 26 Oct, 27 Oct, 1 Nov).
- kinz-polish: missing 28 Oct, 30 Oct and 2 Nov (ran 26 Oct).
- kinz-ledger: missing 29 Oct (ran 27 Oct, 1 Nov).
- kinz-lab: missing 31 Oct.
- kinz-heartbeat: missing 29 and 31 Oct.
- kinz-genesis: no record for Wed 28 Oct (runs on the laptop).
- Market-watch, portfolio and vault ran as scheduled.

## Creative verdict
No experiment file for this week (lab did not run on 31 Oct).

## Next week
Rotation cursor is 3: next rotation repos are kinz-competitor-intelligence, then kinz-margin-guardian-pipeline. All 13 registry repos are attached to the routine.
