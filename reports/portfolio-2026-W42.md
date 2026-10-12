# Portfolio review — 2026-W42

First scheduled-job review (manual test fire, 2026-10-12). Method: github-portfolio-builder, audience collaborators. Labels: verified / reported / unresolved.

**Reviewed:** (no earlier `reports/portfolio-*.md`, so registry order)
- `analytics-service-toolkit` @ `eb94b62` (2026-10-11)
- `btc-llm-sentiment` @ `3a30c4e` (2026-10-11)
- `feed-quality-gate` @ `93a7d69` (2026-10-11)

## analytics-service-toolkit
Strong entry point: small, honest "not built yet" section, MIT, and both the `astk demo` and the Python quick start run as written. One README promise (pinned tags) had nothing behind it.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Compatibility section tells consumers to "pin a tag"; no tag exists, Install tracks `main` | `git ls-remote --tags` empty | fixed in [PR #2](https://github.com/Kinz-org/analytics-service-toolkit/pull/2) |
| verified | Quick start (`astk demo`, Python snippet, `astk doctor` flags) works as written | ran in a fresh venv | nothing to fix |
| reported | "four independent services" consume it; 2 of the 4 are private, so a visitor can't check the claim | README "Why this exists" | needs owner |
| unresolved | `PostgresDedupBackend` live test never ran (README says so itself) | README "What's not built yet" | needs owner (CI service container = workflow edit) |

## btc-llm-sentiment
Rich and well documented, but the README has drifted from the repo in several places, and its headline claims ("production-grade", backtest tables) aren't backed by anything in the repo. The vault's 2026-10-11 review already flags this.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | README says the alert log is committed on each alert; `sentiment_alert.yml` says it no longer commits and uploads an artifact | `.github/workflows/sentiment_alert.yml` L9, L43-48 | fixed in [PR #2](https://github.com/Kinz-org/btc-llm-sentiment/pull/2) |
| verified | Tree lists `workflows/test.yml` (is `ci.yml`), 2 Streamlit pages (4 exist), 1 test file (7 exist); "15 tests" (91 exist) | `ls pages tests`, `grep -c 'def test_'` | fixed in PR #2 |
| verified | "Optuna random search" + open roadmap item "Optuna TPE": the code already uses `TPESampler` | `src/cv/optuna_search.py:257` | fixed in PR #2 |
| verified | Local quick start (`make setup` = `pip install -r requirements.txt`) is not proven to install: Docker build, which installs it, is red on `main` | check runs on `main` (Docker build, Security scans: failure) | needs owner (coordinated re-pin) |
| reported | "production-grade", Sharpe/return tables, "LLM signal contributes meaningful information" | README top, Backtest Results, SHAP | needs owner (evidence missing; see vault note on the null result) |

## feed-quality-gate
Best-written of the three: the "Try it" output matches a real run, exit codes are documented and true, scope is stated plainly. One stale claim about astk being private.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | README and `pyproject.toml` say astk is private and CI can't install it; API: `private: false`; `pip install -e ".[astk]"` works | `GET /repos/Kinz-org/analytics-service-toolkit` | fixed in [PR #2](https://github.com/Kinz-org/feed-quality-gate/pull/2) |
| verified | "pytest # 56 tests"; suite has 60 | `pytest` → 60 passed | fixed in PR #2 |
| verified | `fqg check` example output and exit code 1 match a real run | ran in a fresh venv | nothing to fix |
| verified | `ci.yml` L29-30 repeats the "private repo" comment | `.github/workflows/ci.yml` | needs owner (workflow file) |

## Needs the owner
- **None of the three PRs could merge.** analytics-service-toolkit #2 and feed-quality-gate #2 got no CI run at all (no `pull_request` run was created; astk has never had a workflow run in Kinz-org, fqg only a manual one), so the merge rule "CI ran and passed" can't be met. Check Settings → Actions on both repos. btc-llm-sentiment #2: tests green, but "Security scans" is red, as it is on `main`. All three stay open for kinz-upkeep.
- btc-llm-sentiment: decide how to present results: "production-grade" and the backtest/SHAP tables have no reproducible evidence in the repo (vault: null-result note).
- btc-llm-sentiment: `requirements.txt` needs a coordinated re-pin; Docker build and Security scans are red on `main`, so the local quick start is unproven.
- btc-llm-sentiment: Streamlit badge points at `nassim0014-btc-llm-sentiment.streamlit.app` (the personal account's deployment); could not be opened from the cloud (proxy 403). Keep, or deploy from Kinz-org.
- analytics-service-toolkit: push a `v0.1.0` tag (the CHANGELOG already has a 0.1.0 entry) so consumers can pin a release.
- analytics-service-toolkit: "four services" claim names two private repos; reword or accept.
- feed-quality-gate: fix the "private repo" comment in `.github/workflows/ci.yml` L29-30 (workflow edits are yours).
