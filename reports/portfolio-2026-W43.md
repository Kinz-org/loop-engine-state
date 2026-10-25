# Portfolio review — 2026-W43

Scheduled Sunday run, 2026-10-25. Method: github-portfolio-builder, followed by hand. Audience: collaborators. Labels: verified / reported / unresolved.

**Reviewed:** the two public repos never reviewed (`Next.js-SaaS`, `kinz-fidelite`), then the one reviewed longest ago (`analytics-service-toolkit`, 2026-10-12).
- `Next.js-SaaS` @ `e350c37` (2026-10-24)
- `kinz-fidelite` @ `639b0d8` (2026-10-11)
- `analytics-service-toolkit` @ `03cf46e` (2026-10-14)

## Next.js-SaaS
A strong landing page: the quick-start prerequisites match `package.json`, every doc link resolves, and the build badge points at this repo's own `ci.yml`. But four README statements did not match the tree, and some headline claims cannot be checked from the repo.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Cloudflare deploy linked to `docs/DEPLOYMENT.md` (the Vercel checklist) instead of `docs/DEPLOYMENT-CLOUDFLARE.md` | README Deployment section | fixed in [PR #27](https://github.com/Kinz-org/Next.js-SaaS/pull/27) |
| verified | "Add a model" said to edit `AVAILABLE_MODELS` in `prisma/seed.ts`; seed imports it from `src/config/models.ts`. Also "21 models" (25), and a project tree with `(marketing)/`, `(auth)/` and a blog that don't exist | `prisma/seed.ts:4`, `src/app/` | fixed in [PR #27](https://github.com/Kinz-org/Next.js-SaaS/pull/27) |
| verified | Version badge says 1.1.0, `package.json` says 1.0.0; CHANGELOG's 1.1.0 is dated "2026-01-XX" | `package.json`, `docs/CHANGELOG.md` | needs owner |
| reported | "Total time saved 4-6 weeks", "0 minutes" to auth/billing/RAG, "the **only** AI SaaS boilerplate that ships with MCP" | README "Why use this?" | needs owner (no evidence in repo) |
| reported | Contact and credit links point at the personal `@nassim0014` account, not Kinz-org | README "Hire the author" | needs owner |

## kinz-fidelite
Clear and honest. The French README matches the code: the spec it links exists, `store\demarrer.ps1` exists, `db:up` maps Postgres to 5433, `ENV_FILE` is honoured by `seed-owner.ts`, and `TRUST_PROXY` and `no-referrer` are implemented as described. Maintenance-only repo, so nothing was changed.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | "Les trois espaces" table has four rows (`/admin` is the fourth) | README | needs owner (maintenance-only repo, left as is) |
| unresolved | "La CI GitHub lance tout à chaque pull request": `ci.yml` does run on `pull_request`, but Actions has never run in Kinz-org | registry note 2026-10-13, no runs listed | needs owner |
| verified | `package.json` has no `license` field; LICENSE is MIT | `package.json` | needs owner |

## analytics-service-toolkit
Still the best entry point of the three. Since the last review, the pinned-tag fix (#2) and docstrings (#3) landed. Re-ran it in a fresh venv: `astk demo` runs as written, `ruff check .` is clean, and `pytest` gives 84 passed and 2 skipped.

| label | finding | evidence | outcome |
|---|---|---|---|
| verified | Quick start, demo and dev commands work as written | ran in a fresh venv | nothing to fix |
| unresolved | No Actions runs on `main` since the Kinz-org move, so the README's CI-tested claims have no visible run | Actions API, empty for `main` | needs owner |
| reported | "four independent services" consume it; 2 of the 4 are private | README "Why this exists" | needs owner (unchanged from W42) |

## Needs the owner
- Actions never runs in `kinz-fidelite` and `analytics-service-toolkit` (and `kinz-stock-sync`). Check the org's Actions settings.
- Next.js-SaaS: decide the real version (badge 1.1.0 vs `package.json` 1.0.0) and whether the "only boilerplate with MCP" and time-saved claims stay.
- Next.js-SaaS: contact/credit links still name `@nassim0014`. Keep them or move them to Kinz-org?
- Merges are still denied by the session permission check, so PR #27 is open and waits for a merge.
