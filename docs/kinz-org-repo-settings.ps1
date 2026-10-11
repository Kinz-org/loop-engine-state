# Repository descriptions and topics for the Kinz-org copies.
# Settings writes are blocked from cloud sessions, so run this from a machine where
# `gh auth status` shows an account with admin rights on Kinz-org.
#   pwsh -File docs/kinz-org-repo-settings.ps1

$repos = @(
  @{ n = "analytics-service-toolkit"; d = "Shared Python toolkit (astk) for the KINZ services: .env settings with secret redaction, Postgres connection with startup-race retry, Slack alerts with backoff, Streamlit KPI chrome."; t = "python,postgresql,streamlit,slack,toolkit,data-engineering" },
  @{ n = "feed-quality-gate"; d = "Declarative quality-and-freshness gate for scraped product/price feeds: profiles a feed, scores it against a rules file, splits safe rows from unsafe ones, exits non-zero when the feed should not be used."; t = "data-quality,data-engineering,python,cli,web-scraping,pricing" },
  @{ n = "kinz-price-bridge"; d = "Turns scraped competitor listings into a comparable daily price feed (size-aware normalisation, product matching) for the KINZ margin and accounting pipelines."; t = "pricing,data-engineering,python,e-commerce,competitor-intelligence,tunisia" },
  @{ n = "kinz-margin-guardian-pipeline"; d = "Data pipeline tracking KINZ product COGS against competitor prices: Airflow ingestion, B2B/B2C margin calculation, FastAPI, Streamlit dashboard and Slack alerts on margin erosion."; t = "airflow,alerting,data-engineering,docker,e-commerce,fastapi,margin-analysis,postgresql,streamlit,tunisia" },
  @{ n = "kinz-secure-commerce-hub"; d = "Security-first e-commerce intelligence platform for KINZ, a Tunisian natural cosmetics brand: Next.js front end, FastAPI back end, OWASP-aligned hardening, EDA notebooks."; t = "business-analytics,cybersecurity,data-pipeline,docker,e-commerce,eda,fastapi,nextjs,owasp,python,tunisia" },
  @{ n = "kinz-competitor-intelligence"; d = "Competitor intelligence for KINZ: weekly web and Instagram scraping, PDF catalogue parsing, price tracking, FastAPI service and Streamlit dashboard."; t = "competitor-intelligence,cosmetics,data-engineering,fastapi,instagram,pdf-parsing,price-tracking,streamlit,tunisia,web-scraping" },
  @{ n = "kinz-accounting-analysis-20260623-102129"; d = "KINZ accounting, sales and Tunisian tax-compliance analysis from Odoo (read-only extraction, audited) and Shopify orders, with a Streamlit dashboard and PDF/Excel reports."; t = "odoo,shopify,accounting,tunisia,data-analysis,streamlit,read-only" },
  @{ n = "kinz-stock-sync"; d = "Syncs KINZ stock from Shopify (the only source of truth) to the Odoo 19 POS and creates First Delivery parcels. Dry-run by default, idempotent, with a guard rail."; t = "shopify,odoo,inventory,sync,python,tunisia" },
  @{ n = "kinz-theme"; d = "Shopify theme for the KINZ store (kinzoils.com), including the loyalty card section."; t = "shopify,shopify-theme,liquid,e-commerce,loyalty" },
  @{ n = "kinz-fidelite"; d = "KINZ digital loyalty card (Le Code KINZ): customers keep the card on their phone, staff stamp it by scanning a QR code, levels 1-50 reward repeat visits. Next.js, Drizzle, Neon."; t = "nextjs,typescript,loyalty-program,qr-code,drizzle,vercel,tunisia" },
  @{ n = "Kinz-animations"; d = "TikTok animations (1080x1920) for KINZ in the brand's palette and typefaces, rendered from Python scripts, with a sorted asset inventory and posting plan."; t = "animation,tiktok,python,branding,video" },
  @{ n = "Next.js-SaaS"; d = "Next.js AI SaaS boilerplate with AI cost observability: Supabase + pgvector, Prisma, billing plans, MCP-ready, deploys to Cloudflare Pages. MIT or commercial license."; t = "nextjs,saas,boilerplate,supabase,prisma,mcp,typescript,cloudflare-pages" },
  @{ n = "btc-llm-sentiment"; d = "Bitcoin trading research pipeline: crypto news scored with LLM sentiment, technical features, LSTM forecasting, walk-forward backtesting and a Streamlit app."; t = "backtesting,bitcoin,btc,deep-learning,huggingface,lstm,machine-learning,sentiment-analysis,tensorflow,time-series,trading,yfinance" },
  @{ n = "loop-engine-state"; d = "Control repo for the KINZ scheduled agent loops: job prompts, schedule, repo registry, run records and verdicts. Developed separately from nassim0014/loop-engine-state."; t = "agents,automation,claude,scheduling,ai-agents" }
)

foreach ($r in $repos) {
  $ghArgs = @("repo", "edit", "Kinz-org/$($r.n)", "--description", $r.d)
  foreach ($topic in $r.t.Split(",")) { $ghArgs += @("--add-topic", $topic) }
  gh @ghArgs
  if ($LASTEXITCODE -eq 0) { Write-Host "ok   $($r.n)" } else { Write-Host "FAIL $($r.n)" }
}
