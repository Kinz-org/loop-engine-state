# Portfolio review — 2026-W44

Scheduled Sunday run, 2026-11-01. Method: github-portfolio-builder, followed by hand (one subagent per repo, with a main-session spot check before each PR). Audience: collaborators. Labels: verified / reported / unresolved.

**Reviewed:** the three repos reviewed longest ago: `btc-llm-sentiment` and `feed-quality-gate` (2026-10-12), then `kinz-margin-guardian-pipeline` (2026-10-18; registry order among that run's three).
- `btc-llm-sentiment` @ `6eba14d` (2026-11-01)
- `feed-quality-gate` @ `1855513` (2026-11-01)
- `kinz-margin-guardian-pipeline` @ `409ff93` (2026-11-01)

## btc-llm-sentiment
The code is healthy (94 passed, 1 skipped, and ruff is clean in the light CI env), and the Streamlit quick start runs as written. But the README's "recommended" `make` path failed at once, and the Phase 2 results table doesn't match the committed outputs.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Every `make` target failed with `missing separator`: recipes indented with spaces since 6989242 (2026-08-21) | `make -n lint` on main | fixed in [PR #8](https://github.com/Kinz-org/btc-llm-sentiment/pull/8) |
| verified | Phase 2 table: README Simple `1.3630 / 2.39 / -8.60% / 10 trades` vs CSV `1.4774 / 2.55 / -13.96% / 4`. Risk-Managed `0.9995 / 1.89 / -0.99% / 51` vs `1.0096 / 1.48 / -0.68% / 54`. "avg position 2.65%" vs 3.46% | `outputs/strategy_comparison.csv`, `outputs/risk_managed_backtest_results.csv` | needs owner (results claim) |
| verified | Test counts (Risk-Managed 7 not 6, OOF 8 not 2, safe_pickle 16 not 12). The CI install line left out `pytest-cov`/`requests`. The `ml-smoke` job was not listed | `pytest --collect-only`, `ci.yml` | fixed in PR #8 |
| verified | Streamlit app and all 4 pages run. Relative links resolve. MIT license matches the badge | AppTest in a fresh venv | nothing to fix |
| reported | "production-grade"; Docker build red on main (`requirements.txt` re-pin); Streamlit badge points at the `nassim0014` deployment | carried from W42 | needs owner |

## feed-quality-gate
Still the most honest README of the lot. Install, the quick start, `fqg explain`, the exit codes and every link match a real run (69 passed, ruff clean). Two shipped correctness bugs weren't visible from the README.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | README says exit `2` = rules file "missing or invalid", but a misspelt key (`freshnes:`) is silently dropped: the default applies and the run exits `1` | `feed_quality_gate/rules.py` has no `extra="forbid"`; reproduced | caveat + backlog link in [PR #6](https://github.com/Kinz-org/feed-quality-gate/pull/6); code fix needs owner |
| verified | One future-dated timestamp lets a stale feed pass `freshness` ("-26419.0d old"). Tracked only in an unlinked `docs/IMPROVEMENTS.md` | reproduced through `evaluate()` | linked in PR #6; code fix needs owner |
| verified | CI never fires on push or pull request: all 5 runs ever were `workflow_dispatch`, so the badge shows a stale 2026-10-11 run | Actions run list | needs owner |
| verified | `ci.yml` L29-30 still says astk is a private repo | `.github/workflows/ci.yml` | needs owner (workflow file) |

## kinz-margin-guardian-pipeline
All of W42's fixes (#5) are on main and hold up: `make help` works, the route and init SQL are correct, the offline demo runs, and 88 tests pass with 1 skipped. SECURITY.md promised protections the code doesn't have.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | SECURITY.md claimed RBAC, bcrypt (12 rounds) and audit logging. Every token is `role: admin`, the password is compared in plain text to an env var, and there is no audit code | `api/main.py:73`, `api/auth.py:50` | fixed in [PR #6](https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/6) |
| verified | CONTRIBUTING called `make check` the "full local CI gate", but its venv lacks the API deps, so 2 test files are skipped (69 vs 96 tests) | ran `make check` | doc fixed in PR #6; Makefile needs owner |
| verified | README tree listed a non-existent `airflow/plugins/margin_operators.py` and left out `src/dag_logic.py`, `airflow/Dockerfile` and `requirements-*.txt` | `ls` | fixed in PR #6 |
| verified | "real-time" margins: the DAG is a daily batch (`0 6 * * *`) on simulated competitor prices (±5% noise) | `airflow/dags/margin_guardian_dag.py:367`, `:99` | needs owner (wording) |
| unresolved | Requirement files disagree: `requirements.txt` calls astk "Public", while the api/dashboard/airflow files and `src/alert_manager.py` call it "PRIVATE" | the files | needs owner |

## Needs the owner
- Actions never fires on push or PR in `feed-quality-gate` (or `analytics-service-toolkit`, `kinz-fidelite`, `kinz-stock-sync`), so their PRs can never meet "CI passed". Check Settings → Actions.
- btc-llm-sentiment: Phase 2 README table vs `outputs/` CSVs. Regenerate the outputs or update the table. The "production-grade" wording is still unbacked.
- btc-llm-sentiment: Docker build red on main (needs a `requirements.txt` re-pin, plus the held #4), so no PR there can merge.
- feed-quality-gate: reject unknown rule keys, and stop a future timestamp from passing `freshness` (both are code fixes).
- kinz-margin-guardian-pipeline: "real-time" wording; make `make setup` install the API test deps; is astk public or private?
- feed-quality-gate `ci.yml` L29-30 stale "private repo" comment (workflow edits are yours).
