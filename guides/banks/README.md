# The World's Banks — LIKE® Magazine Markets Guide

October 2026 · Markets department · Staged only — not published.

## Decision on investment banks
There is **no separate investment-bank list**. Investment banks are covered in narrative within entries: Goldman Sachs, Morgan Stanley and the investment-banking divisions of JPMorganChase, Bank of America, Citigroup, Barclays, BNP Paribas, Deutsche Bank, UBS, Santander, MUFG, Mizuho and peers are entries themselves, with their investment-banking businesses stated in Principal Businesses and Division Heads. Creating a second list would double-count the same groups.

## Roster
**50 banks.** Rank order follows S&P Global Market Intelligence, *Top 100 Banks in the World 2025* (assets at end-2024, published April 2025), filtered to the top tier and completed with verifiable major groups to 50. Where S&P gives a USD asset figure it is in `total_assets_usd_bn_sp_global_end2024`. For Crédit Agricole, Itaú Unibanco and Bradesco the annual report reports in EUR/BRL only in the form consulted — the CSV says so plainly and does **not** self-convert. Never padded: the cut line is KBC at 50.

## Exclusion named
**Sberbank — excluded.** It appears in global asset rankings, but it could not be verified to this guide's standard from official sources accessible at the October 2026 build (sanctions-related disclosure and access limits). It is named here as an exclusion rather than included with unverified fields or silently omitted. No other ranking bank was dropped silently; next-tier groups below the cut (e.g., additional Chinese joint-stock banks, Erste, Commerzbank standalone, Truist, PNC, Capital One post-Discover) are below the 50 cut, not exclusions for cause.

## Field set (applied in CSV, PDF, DOCX and web article alike)
Rank (S&P Global 2025); Bank Name; HQ City; HQ Country; Founded; Ownership / Listing; Total Assets (USD bn, S&P Global end-2024, dated and sourced); Chief Executive (exact title); Chair (exact title); CFO; President / COO or equivalent; Division Heads / Other C-Suite (heads of principal divisions where the bank publishes them); Principal Businesses (retail, commercial, investment banking, wealth/asset management — which each bank actually runs); Clients (published categories, else 'not disclosed' — here stated as published categories or flagged); Contact Published (official contact route; published emails/phones only where the bank itself publishes them — in practice almost every group here is form/branch-route only, and the cell says so; no guessed emails); Website; Footprint (named countries/regions or published presence counts); Notes; Sources.

Any unverifiable field says so plainly in the cell ('Not verified to standard at October 2026 build'); the column stays in the schema for every entry.

## Coverage and gaps
- CEO/Chair verified for the great majority; dated successions recorded: HSBC (Elhedery CEO Sep 2024; Tucker retired Sep 2025, Brendan Nelson interim Chair), UBS post-Credit Suisse (Ermotti/Kelleher), DBS (Tan Su Shan Mar 2025), TD (Raymond Chun Feb 2025), Morgan Stanley (Ted Pick Chair Jan 2025), Crédit Agricole S.A. (Olivier Gavalda May 2025), ANZ (Nuno Matos Jul 2025), Westpac (Anthony Miller Dec 2024).
- CFO/COO and Chinese joint-stock bank leadership are the thinnest fields — flagged per cell, never guessed. Bank of China President, SMFG Chair, several Chinese bank CFOs, Bradesco/KBC CFO splits are explicit gaps.
- Contact emails: **none published as a general inbox by any of the 50 on their official sites consulted** — all are official form/branch/investor-relations routes. That is the honest finding, stated per entry.
- Assets: S&P Global end-2024 USD for most; 3 entries local-currency only as above.

## Files
- `banks.csv` — master, 50 rows × 19 columns
- `README.md` — this file
- PDF/DOCX in `~/workspace/your_files/` as *The World's Banks - LIKE Markets Guide.pdf/.docx*
- Web article staged at `~/workspace/likeleaders-site/articles/like-worlds-banks.html`
- Fragment at `~/workspace/likeleaders-site/fragments/markets-banks.html` (not inserted into sections/markets.html)

Sources per row: S&P Global Top 100 2025; bank Annual Report 2024 / Integrated Report 2024 and official leadership pages, checked October 2026.
