# Portfolio review — 2026-W45

Scheduled Sunday run, 2026-11-08. Method: github-portfolio-builder, followed by hand. Audience: collaborators. Labels: verified / reported / unresolved.

**Reviewed:** the three repos reviewed longest ago: `kinz-price-bridge` and `kinz-secure-commerce-hub` (2026-10-18), then `analytics-service-toolkit` (2026-10-25; first in registry order among that run's three).
- `kinz-price-bridge` @ `c4f3327` (2026-10-11)
- `kinz-secure-commerce-hub` @ `d5724cf` (2026-10-22)
- `analytics-service-toolkit` @ `03cf46e` (2026-10-14)

## kinz-price-bridge
No commit since the last review. The code still does more than the README says: 39 tests pass, ruff is clean, and CI is green on `main`. Registry `worked_by: none`, so this job changed nothing.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | README "Status: **Scaffold** … No functional code yet" and `pytest -q  # no tests yet - will pass vacuously`; in fact 39 tests pass | README:18, README:34; ran the quick start in a fresh venv | needs owner (repo not worked by loops) |
| verified | Layout lists `docs/`, which does not exist | README:54; `ls` | needs owner |
| verified | Purpose names Odoo; nothing in `src/` or `scripts/` mentions it | README:5 | needs owner |
| verified | Quick start (`pip install -r requirements.txt`, `pytest -q`, `ruff check .`) works | fresh venv | nothing to fix |

## kinz-secure-commerce-hub
Since the last review, PR #4 (broken screenshots, 2FA claim, row count) landed. The project tree, quick start, `.env.example`, localhost-only Postgres port and production docs switch all match the code, and `make check` gives 109 passed with ruff clean. What's left is the data and "production-grade" wording, plus the red Trivy job.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | CONTRIBUTING "Backend (67 tests, ~5s)"; `make check` runs 109 | `CONTRIBUTING.md:20`, ran `make check` | fixed in [PR #6](https://github.com/Kinz-org/kinz-secure-commerce-hub/pull/6) (waits for a merge) |
| verified | README:45 "real KINZ product data, real EDA, real insights" vs `docs/threat-model.md:62` "Sample dataset is synthetic" | both files | needs owner (unchanged from W42) |
| verified | Security scans (Trivy) red on `main`, so the README CI badge shows failing; every other job green | check-runs on `d5724cf` | needs owner |
| reported | "A production-grade, security-first … platform" (README:12) | no deployment or load evidence in the repo | needs owner (wording) |
| unresolved | External links (shields.io, docs.astral.sh, python.org) could not be fetched from this sandbox | proxy returned no response | recheck by hand |

## analytics-service-toolkit
No commit on `main` since the W43 review, so the earlier verification still holds (quick start, `astk demo`, ruff and pytest all work). Actions still has 0 runs, so open PRs #4, #5, #6, #8 have no checks and cannot be merged.

| label | finding | evidence | outcome |
|---|---|---|---|
| unresolved | 0 Actions runs ever in this repo; CI-tested claims have no visible run | `actions/runs` total_count 0 | needs owner |
| reported | "four independent services" consume it; 2 of the 4 are private | README "Why this exists" | needs owner (unchanged since W42) |

## Needs the owner
- **Merges are still denied by the session permission check** (fifth night in a row), so green PRs pile up, this week's secure-commerce-hub #6 included.
- Actions never runs in `analytics-service-toolkit` (also `kinz-fidelite`, `kinz-stock-sync`): check the org's Actions settings.
- kinz-price-bridge: README Status/Purpose/Layout still describe the August scaffold. Update it, or set `worked_by: claude` so a loop can.
- secure-commerce-hub: say "synthetic" (as the threat model does) or "real" for the data; decide whether "production-grade" stays; Trivy keeps `main` red.
