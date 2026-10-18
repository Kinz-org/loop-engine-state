# Portfolio review — 2026-W42 (second run, 2026-10-18)

The scheduled Sunday run. `portfolio-2026-W42.md` (the 2026-10-12 manual test fire) already uses this week's name, so this report has a suffix. Method: github-portfolio-builder (followed by hand, because the skill was not loaded). Labels: verified / reported / unresolved.

**Reviewed:** the three public repos with no earlier review, in registry order.
- `kinz-margin-guardian-pipeline` @ `d5e0228` (2026-10-17)
- `kinz-price-bridge` @ `c4f3327` (2026-10-11)
- `kinz-secure-commerce-hub` @ `21f9250` (2026-10-14)

## kinz-margin-guardian-pipeline
The README is solid: the architecture, formula and Docker quick start match the code, and CI is green. But the README never mentioned the offline demo, and every `make` target that CONTRIBUTING.md tells you to run was broken.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Makefile recipes indented with spaces: `make help` → `Makefile:11: *** missing separator`, so `make check`/`up`/`seed` (CONTRIBUTING) never ran; `make ruff` also needed ruff, which `requirements.txt` lacked | ran `make`; fixed version: `make check` 69 passed + ruff clean | fixed in [PR #5](https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/5) |
| verified | README endpoint `GET /margins/latest`; the real route is `/products/margins/latest` (router prefix) | `api/main.py:79`, `api/routes/products.py:93` | fixed in PR #5 |
| verified | README init command `psql -f /docker-entrypoint-initdb.d/init_db.sql`: compose mounts the script as `01_init_db.sql`, which Postgres runs automatically | `docker-compose.yml:18` | fixed in PR #5 |
| verified | Offline `scripts/demo.py` (no Docker or secrets) was missing from the README; tree listed 2 of 8 test files; CONTRIBUTING "~54 tests" (89 now) | ran the demo and `pytest` (88 passed, 1 skipped) | fixed in PR #5 |
| reported | "real-time" margins: the DAG is a daily batch (`0 6 * * *`) on simulated competitor prices | README intro and the Airflow DAG section | needs owner (wording) |

## kinz-price-bridge
It works better than its README says: 39 tests pass, ruff is clean and CI is green. The README still describes the empty scaffold from 2026-08-20. Registry `worked_by: none`, so this job made no changes.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | "Status: Scaffold, no functional code yet" and "no tests yet - will pass vacuously"; in fact 629 lines in src/scripts, 7 test files, 39 passing | ran the quick start in a fresh venv | needs owner (repo not worked by loops) |
| verified | Layout lists `docs/`, which does not exist; it omits `src/logging_config.py` and 4 test files | `ls` | needs owner |
| verified | Purpose names Odoo as a sync target; no code in src/ or scripts/ mentions Odoo | `grep -rni odoo src scripts` → nothing | needs owner |
| verified | Quick start (`pip install -r requirements.txt`, `pytest -q`, `ruff check .`) works | fresh venv | nothing to fix |

## kinz-secure-commerce-hub
A rich README, and its security controls are visible in the code (rate limits, prod-start guards, a demo hash that matches the stated password). It oversells in places: five screenshots that don't exist, 2FA that doesn't exist, and "real" data that its own threat model calls synthetic.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Screenshots section embeds 5 PNGs; `docs/images/` holds only README.md, so 5 broken images | `ls docs/images` | fixed in [PR #4](https://github.com/Kinz-org/kinz-secure-commerce-hub/pull/4) |
| verified | "Login + 2FA screen": no 2FA/TOTP code anywhere | `grep -riE "2fa\|totp\|otp" src/api src/frontend/src` | fixed in PR #4 |
| verified | `sales_2023_2024.csv` "~13.7k line items": 12,869 rows, 4,500 orders | CSV count | fixed in PR #4 |
| verified | README: "real KINZ product data, real EDA, real insights"; `docs/threat-model.md:62`: "Sample dataset is synthetic". CLV 3.5×, +23%/+17% insight figures come from that data | README "Business Value", "Analytics" | needs owner |
| verified | The CI badge on main shows failing: Security scans (Trivy) red; every other job green | check-runs on `21f9250` | needs owner (known Trivy issue) |

## Needs the owner
- **Merges were denied by the session permission check.** margin-guardian #5 is fully green and meets every merge rule. secure-commerce-hub #4 is docs-only, but its Security scans check will be red, as it is on main. Both stay open for kinz-upkeep or for you.
- secure-commerce-hub: decide whether the README says the data is synthetic (as the threat model does) or real, and whether "production-grade" stays.
- secure-commerce-hub: Trivy keeps Security scans (and the README badge) red on main.
- kinz-price-bridge: README Status/Purpose/Layout describe the August scaffold. Update it, or set `worked_by: claude` so a loop can. The registry also still holds it out of rotation, although it has code.
- margin-guardian: "real-time" in the tagline; the pipeline is daily and uses simulated prices.
