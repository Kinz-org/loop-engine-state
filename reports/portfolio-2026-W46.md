# Portfolio review — 2026-W46

Scheduled Sunday run, 2026-11-15. Method: github-portfolio-builder, followed by hand. Audience: collaborators. Labels: verified / reported / unresolved.

**Reviewed:** the three repos reviewed longest ago: `Next.js-SaaS` and `kinz-fidelite` (2026-10-25), then `btc-llm-sentiment` (2026-11-01; first in registry order among that run's three).
- `Next.js-SaaS` @ `784b7d2` (2026-11-14)
- `kinz-fidelite` @ `639b0d8` (2026-10-11)
- `btc-llm-sentiment` @ `6eba14d` (2026-10-22)

## Next.js-SaaS
Still the strongest landing page. W43's fix (#27) is on main, CI is green on `main`, and the new `webhook:tool` and `cost:estimate` sections match the scripts. Two README statements were out of date with the code. The headline claims are unchanged.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Badge and tech-stack table said Prisma 6; `package.json` pins `@prisma/client`/`prisma` ^7.10 | `package.json:43,98`, `prisma.config.ts` | fixed in [PR #40](https://github.com/Kinz-org/Next.js-SaaS/pull/40) (merged) |
| verified | `pnpm cost:estimate` "works offline", but on a fresh install it crashes (`@prisma/client` has no export `Prisma`) until `pnpm db:generate` runs. That needs no database | ran it after `pnpm install`, then after generate | fixed in PR #40 |
| verified | Version badge 1.1.0 vs `package.json` 1.0.0 | `package.json:3` | needs owner (unchanged since W43) |
| reported | "4-6 weeks" saved, "0 minutes" to auth/billing/RAG, "the **only** AI SaaS boilerplate that ships with MCP" | README "Why use this?" | needs owner (no evidence in repo) |
| reported | Contact, copyright and credits name the personal `@nassim0014` account | README "Hire the author", `LICENSE:3` | needs owner |

## kinz-fidelite
No commit since the W43 review, so it still checks out: the French README matches the code. Registry `worked_by: none`, so this job changed nothing.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | "Les trois espaces" table has four rows (`/admin`) | README | needs owner |
| verified | "La CI GitHub lance tout à chaque pull request": `ci.yml` triggers on `pull_request`, but Actions still has 0 runs ever | `actions/runs` total_count 0 | needs owner |
| verified | `package.json` has no `license` field; LICENSE is MIT | `package.json` | needs owner |

## btc-llm-sentiment
No commit on `main` since the W44 review. W44's fix (PR #8, Makefile tabs and test counts) passes every check except Docker build. That job is red on `main` too, because Trivy can't find the image until held PR #4 (`load: true` in `ci.yml`) lands. So #8 and #7 can't merge.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Every `make` target still fails on `main` (spaces, not tabs) | main @ `6eba14d` | fix waits in [PR #8](https://github.com/Kinz-org/btc-llm-sentiment/pull/8), blocked by Docker build |
| verified | Docker build red on `main` and every PR; the fix edits `ci.yml` | PR #4 (`hold`), check-runs on #7/#8 | needs owner |
| verified | Phase 2 README table vs `outputs/*.csv` still disagree | carried from W44 | needs owner |
| reported | "production-grade"; Streamlit badge points at the `nassim0014` deployment | README | needs owner |

## Needs the owner
- btc-llm-sentiment: merge #4 (`ci.yml`, Trivy `load: true`). Until then `main` stays red and #7/#8 can't merge.
- Actions never runs in `kinz-fidelite` (also `analytics-service-toolkit`, `kinz-stock-sync`): check the org's Actions settings.
- Next.js-SaaS: pick the real version (badge 1.1.0 vs 1.0.0), and decide whether the "only boilerplate with MCP" and time-saved claims stay.
- Next.js-SaaS / btc-llm-sentiment: keep the personal `@nassim0014` links, or move them to Kinz-org?
- btc-llm-sentiment: regenerate `outputs/` or update the Phase 2 table.
