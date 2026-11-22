# Portfolio review — 2026-W47 (2026-11-22)

**Reviewed:** the three repos reviewed longest ago: `feed-quality-gate` and `kinz-margin-guardian-pipeline` (2026-11-01), then `analytics-service-toolkit` (2026-11-08; first in registry order among that run's three).
- `feed-quality-gate` @ `864dd48` (2026-11-21)
- `kinz-margin-guardian-pipeline` @ `a5c3874` (2026-11-21)
- `analytics-service-toolkit` @ `03cf46e` (2026-10-14)

## feed-quality-gate
Every README command behaves as documented (103 tests pass, ruff is clean), and the W44 bugs were fixed in #7 and #8. The README lagged behind the new freshness behaviour.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | README didn't say that future-dated rows are now ignored for freshness (`future_tolerance_hours`, default 1), or that `stuck_value_cluster` is off by default | `feed_quality_gate/checks.py` L147-185, `rules.example.yaml` | fixed in [PR #11](https://github.com/Kinz-org/feed-quality-gate/pull/11) (not merged: no checks run) |
| verified | `ci.yml` lists push and pull_request triggers, but all 10 runs ever were `workflow_dispatch`, so PRs get no checks and the badge only reflects manual runs | Actions run list | needs owner |
| verified | `ci.yml` L29-30 still calls astk a private repo. It is public (API `private: false`) | `.github/workflows/ci.yml` | needs owner (workflow file) |

## kinz-margin-guardian-pipeline
The offline demo and the new price-floor CLI run as documented, and 205 tests pass (1 skipped). The README had drifted behind #7, #10 and #17.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | README said "JWT auth on all API endpoints", but `/`, `/health` and `/auth/token` are open. The 404s from #17 and `CORS_ALLOW_ORIGINS` from #7 were undocumented | `api/main.py`, `.env.example` | fixed in [PR #18](https://github.com/Kinz-org/kinz-margin-guardian-pipeline/pull/18) |
| verified | README tree omitted `.github/dependabot.yml` and three new test files | `ls` | fixed in PR #18 |
| verified | `make check` still skips `tests/test_alert_manager.py`: its venv has neither astk nor the API deps | `pytest -rs` | needs owner (Makefile) |
| verified | "real-time" tagline vs a daily batch on simulated prices (unchanged since W44) | `airflow/dags/margin_guardian_dag.py` | needs owner (wording) |

## analytics-service-toolkit
No commit on `main` since 2026-10-14, so the W43/W45 verification still holds. Actions still shows 0 runs ever, so PRs #4-#10 have no checks and can't be merged.

| label | finding | evidence | outcome |
|---|---|---|---|
| unresolved | 0 Actions runs ever, though `ci.yml` triggers on push and PR | `actions/runs` total_count 0 | needs owner |

## Needs the owner
- Actions doesn't fire on push or PR in `analytics-service-toolkit`, `feed-quality-gate` (manual runs only), `kinz-fidelite` and `kinz-stock-sync`. Check the org/repo Actions settings; until then their PRs can never merge.
- feed-quality-gate: reword the "private repo" comment in `ci.yml` L29-30.
- margin-guardian: should `make setup` install the API deps and astk so `make check` runs the full suite? Keep or drop "real-time"?
- PR merges were denied to this run's session, so #11 and #18 wait for review or a later run.
