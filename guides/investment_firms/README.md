# Investment Firms Worldwide — Top 100

A sourced reference guide to the world's largest investment firms — asset managers, investment banks, and brokerage houses — compiled **2026-10-03/04** (brokerage expansion added 2026-10-04); last updated **2026-10-22** (full-depth refresh for the LIKE® Magazine Markets department; see the 2026-10-22 log below).

- **`investment_firms.csv`** — the database: 100 firms × 25 columns:  `firm_name, category, founded, ownership, parent_and_listing, hq_city, hq_country, aum_usd_bn, aum_as_of, aum_rank, revenue_usd_bn, ceo, president_coo, cfo, other_c_suite, investment_leadership, specialties_strategies, clients, major_offices, website, contact_route, general_contact_email, phone_hq, notes, sources`
  - **Field set (the depth standard, applied to all 100 entries in the CSV, the guide PDF/DOCX and the web article alike):** firm name; category; **founded** (year, with the basis stated where the firm is a division, brand or merger product); ownership; **parent and listing** (parent group and exchange/ticker, or an explicit not-listed statement); headquarters city and country; AUM or client assets in US$bn with **`aum_as_of`** (the figure's date and basis — every figure is dated and sourced; local-currency-only figures stay in `notes`); AUM rank where a ranking edition supplies one; revenue (investment banks); **chief executive, president/COO, chief financial officer and other C-suite/chair-level officers, all with exact published titles**; **named investment leadership**; **specialties and strategies in full**; **clients or client categories as the firm itself describes them**; major offices (HQ plus footprint); official website; **contact route** (the firm's published route in); general contact email and HQ phone, published values only.
  - **No silent blanks in the depth fields:** where a firm publishes nothing for a field, the cell says so plainly (e.g. "Not publicly named — see Notes", "Not published — contact form only (see Contact Route)", "No public investment-leadership role published — see Notes"). The two numeric figure columns (`aum_usd_bn`, `revenue_usd_bn`) stay blank where no figure is disclosed, with the reason carried in `aum_as_of` and `notes`.
  - `category` is `Asset Manager`, `Investment Bank`, `Brokerage`, or combinations (`Both`, `Asset Manager / Brokerage`, `Both / Brokerage`, `Investment Bank / Brokerage`) for diversified groups. Firms already in the guide with major brokerage arms (Fidelity, Vanguard, Morgan Stanley/E*TRADE, Merrill/Bank of America, Raymond James, Stifel, Wells Fargo Advisors) carry a Brokerage designation rather than duplicate rows.
  - `aum_usd_bn` covers asset managers (AUM) and brokerages (client assets — clarified per row in `notes`); blank for pure investment banks and where not disclosed.
  - `revenue_usd_bn` covers investment banks only (FY2025, investment-banking division revenue where the firm discloses it, otherwise total-firm revenue — basis stated in `notes`); blank for pure asset managers.
  - `general_contact_email` contains **only** addresses actually published on the firm's official site. Where the official site publishes no general email (the usual case — most firms offer only contact forms or function-specific inboxes), the cell reads "Not published — contact form only (see Contact Route)". No address was ever inferred from a guessed pattern.
  - `phone_hq` is the HQ main line only where published on the official site; elsewhere the cell reads "Not published on official site".
  - People cells carry full names + exact titles as the firm publishes them, current as of October 2026. Unverifiable people cells carry a plain statement (above) and the gap is named in `notes`.
  - `sources` lists the official/authoritative URLs actually consulted per row.
- **`investment_firms.pdf`** — formatted table with clickable firm-website links.
- **`investment_firms.html`** — SEO/AI-optimized web version: semantic HTML5, one section per firm, JSON-LD `Organization`/`FinancialService` markup.
- **`investment_firms_llms.txt`** — plain-text index of the full list for AI retrieval.
- **`work/`** — roster, enrichment batch files, and progress log behind the merge.

## Headline numbers

| Metric | Count |
|---|---|
| Firms | **100** |
| Asset Manager | **49** (incl. 9 alternatives managers) |
| Investment Bank | **21** |
| Both | **8** (JPMorgan Chase, Goldman Sachs, UBS, BNP Paribas, HSBC, Deutsche Bank, Nomura, Macquarie) |
| Brokerage (new rows) | **15** (Charles Schwab, LPL Financial, Interactive Brokers, Robinhood, Ameriprise Financial, Edward Jones, SoFi Technologies, Webull, eToro, tastytrade, TradeStation, Saxo Bank, IG Group, CMC Markets, XTB) |
| Asset Manager / Brokerage | **2** (Fidelity Investments, Vanguard) |
| Both / Brokerage | **1** (Morgan Stanley — E*TRADE) |
| Investment Bank / Brokerage | **4** (Bank of America — Merrill; Wells Fargo — Wells Fargo Advisors; Raymond James; Stifel) |
| HQ countries | 13 (US 52 · UK 11 · France 4 · China 4 · Japan 3 · Canada 3 · Switzerland 2 · Germany 2 · others 4) |
| CEO named | 98 of 100 (98%) |
| CFO named | 62 of 100 (62%) |
| Investment leadership named | 34 of 100 (34%) |
| Founded | 100 of 100 (basis stated for divisions, brands and merger products) |
| Parent and listing | 100 of 100 |
| Specialties / strategies | 100 of 100 |
| Clients / client categories | 100 of 100 |
| Contact route | 100 of 100 |
| AUM dated and sourced (`aum_as_of`) | 100 of 100 |
| Official website | 100 of 100 (100%) |
| Published general contact email | 4 of 100 (4%) |
| HQ phone published | 37 of 100 (37%) |
| AUM figure (asset managers) | 52 of 60 (87%) |
| Revenue figure (investment banks) | 25 of 34 (74%) |
| Client-assets figure (pure brokerages) | 10 of 15 (67%) |

### Top asset managers by AUM (TAI/WTW World's 500, Nov 2025; end-2024 AUM)

1. BlackRock ($11.55tn) · 2. Vanguard ($10.11tn) · 3. Fidelity ($5.52tn) · 4. State Street Global Advisors ($4.72tn) · 5. JPMorgan Chase ($4.05tn) · 6. Goldman Sachs ($3.14tn) · 7. UBS ($2.86tn) · 8. Capital Group ($2.84tn) · 9. Allianz Group / PIMCO ($2.55tn) · 10. Amundi ($2.32tn)

### Top investment banks by 2025 IB fees (Dealogic full-year 2025)

1. JPMorgan (8.4% wallet share) · 2. Goldman Sachs · 3. BofA Securities · 4. Morgan Stanley · 5. Citi — global IB fees crossed $100bn in 2025, the second-highest total on record.

## Weekly watch updates

### 2026-10-22 — full-depth refresh (LIKE Markets Guide edition)
- **Schema expanded 19 → 25 columns** for every one of the 100 firms: added `founded`, `parent_and_listing`, `aum_as_of` (dated, sourced figure basis), `specialties_strategies`, `clients`, and `contact_route`. Formerly blank people/contact cells now state the position plainly in the cell (see Field set above); the pre-refresh CSV is backed up at `work/investment_firms_backup_20261022.csv`, and the enrichment is reproducible from `work/refresh_20261022.py`.
- **Nuveen / Schroders — re-verified, no change to the rows' facts:** Nuveen's completion announcement (Oct. 1, 2026) confirms the £9.9bn acquisition closed that day; combined AUM about $2.6tn at Jun. 30, 2026; Schroders delisted from the LSE on Oct. 2, 2026, operates separately within Nuveen for 12–18 months, and Richard Oldfield continues as Group CEO reporting to Nuveen CEO William Huffman; Johanna Kyrklund is CIO of Public Markets & Solutions for the combined firm (already reflected in the rows; re-verification tags added to both rows' notes).
- **Janus Henderson — re-verified:** the firm's own completion release (added to the row's `sources`) confirms the take-private closed **Jun. 30, 2026** at $52.00 per share (Trian, General Catalyst, QIA, with Lunate, Sun Hung Kai & Co. and others), NYSE delisted, Ali Dibadj continuing as CEO, main presence London and Denver. Ownership already read Private; no leadership change.
- **Amova Asset Management — re-verified:** renamed from Nikko Asset Management effective **Sep. 1, 2025**; Stefanie Drews is President and CEO (CEO role added Apr. 1, 2025; Kuniyuki Shudo is Executive Chair); wholly owned by Sumitomo Mitsui Trust Group. Founded carried as 1959.
- **CORRECTION — Rothschild & Co (ownership):** earlier editions listed the firm as "Public (Euronext Paris; Rothschild family-controlled)". The firm was in fact **taken private by the Rothschild family (Concordia) and delisted from Euronext Paris in 2023**. `ownership` and `parent_and_listing` corrected, and the correction is tagged in the row's notes.
- **Macquarie — re-verified:** CEO handover (Shemara Wikramanayake → Greg Ward) remains scheduled for Nov. 7, 2026; no change as of this refresh. **Charles Schwab** Q3 2026 client-assets figure ($13.33tn, Sep. 30, 2026) and **Interactive Brokers** client equity ($964.7bn, Sep. 30, 2026) stand as updated on Oct. 20 / Oct. 6. No other leadership, name, ownership or ranking-edition changes were found between the Oct. 20 watch and this refresh; the TAI/WTW World's 500 (Nov. 2025) and Dealogic full-year 2025 editions remain the latest published ranking editions.
- **Deliverables built from the refreshed database (all staged, nothing published):** `investment_firms.html` and `investment_firms.pdf` rebuilt in this directory via the patched build scripts (now Top 100, with the new fields in the web version); **LIKE Markets Guide** PDF + DOCX at `~/workspace/your_files/The World's Investment Firms - LIKE Markets Guide.pdf` / `.docx` (full field set, all 100 entries, grouped: 51 asset managers, 9 diversified groups, 25 investment banks, 15 brokerages); staged article at `~/workspace/likeleaders-site/articles/like-worlds-investment-firms.html`; feature-card fragment at `~/workspace/likeleaders-site/fragments/markets-investment-firms.html`. `sections/markets.html` was **not** edited. Library copies (`~/workspace/your_files/investment_firms.csv` / `.pdf`) refreshed.

### 2026-10-20
- **Piper Sandler ↔ Perella Weinberg**: merger talks **abandoned 14 Oct 2026** per Reuters (FT first reported) — the parties could not agree financial and personnel terms; no merger. PWP closed −19.1% at $13 that day; Piper +0.96% at $64.50. Both rows' notes updated (the ~30 Sep WSJ talks report is now superseded).
- **Charles Schwab (notes/AUM)**: Q3 2026 results reported 15 Oct 2026 — total client assets **$13.33tn as of Sep 30, 2026** (up 15% YoY; prior Aug 31, 2026 figure was $13.41tn); record core net new assets $190.4bn (+38% YoY); 1.2m new brokerage accounts, 48.6m total client accounts; first full quarter of Schwab Crypto retail trading (bitcoin/ether). Row figure and notes updated from the company release.
- **Goldman Sachs (notes)**: on the 13 Oct 2026 Q3 earnings call, CEO Solomon said there is "no succession transition or timeline underway," dismissing reports as "noise" (Bloomberg Law); Q3 net revenue $18.7bn (+23% YoY), EPS $17.01 vs $13.50 expected. Waldron remains President/COO; titles unchanged.
- **Schroders (notes)**: Group CEO Richard Oldfield assumed direct responsibility for Schroders Capital (private markets, $116bn) upon Georg Wunderlin's departure at end-Oct 2026 (Bloomberg via Private Equity Wire, 30 Sep). Row already flagged Wunderlin's exit.
- **Janus Henderson (notes)**: Aug 2026 agreed acquisition of Insignia Financial's investment businesses — Antares Fixed Income, Antares Equities and Insignia's 40% stake in Fairview Equity Partners (~A$33bn; terms undisclosed), expected to close Q4 2026 subject to regulatory approval (Financial Standard, Investment International). Not previously recorded in the row.
- **Webull (notes)**: securities class-action notices (Glancy Prongay, Hagens Berman, Faruqi & Faruqi, Frank R. Cruz, Howard G. Smith) cite a 7 Dec 2026 lead-plaintiff deadline; the House Select Committee alleged Webull told investigators it had no China offices/employees while a mainland subsidiary employed ~863 people (62% of the global workforce) — Webull disputes the report. Client-assets figure unchanged ($24.6bn — no newer firm-published figure).
- **Nuveen/Schroders**: no new post-close fallout beyond recorded leadership detail. **Macquarie**: CEO handover (Wikramanayake → Greg Ward) still scheduled 7 Nov 2026; unchanged. **Aon/USI**: still pending regulatory approval; close expected Q4 2026 (not before 19 Oct). **Janus Henderson take-private**: no leadership change (Dibadj CEO, Grewal CFO).
- **Rankings**: no new TAI/WTW World's 500 (Nov 2025 edition still latest; next expected ~Nov 2026); no new full-year Dealogic/Refinitiv IB table. **Robinhood**: Q3 2026 results due 27 Oct — no newer firm-published client-assets figure yet. **Tradeweb's $1.97bn agreed acquisition of Trumid** (ann. 19 Oct 2026) concerns a bond-market platform, not a guide firm — no row change. No rebrands; no other leadership changes at guide firms.

### 2026-10-13
- **Webull (notes)**: 7 Oct 2026 US House Select Committee on China report ("Free Trades, Hidden Ties") alleged structural PRC ties; Webull disputed the findings, says US customer data is stored and access-controlled in the US. BULL fell ~19%. Robinhood (3% transfer match, 7–16 Oct), SoFi (3%, 8–15 Oct) and Public.com (3%, 7–26 Oct) offered Webull customers transfer bonuses; a class-action lawsuit alleging misleading investors was filed. Client-assets figure unchanged ($24.6bn, firm's Dec 31, 2025 figure — no newer firm-published figure).
- **Goldman Sachs (notes)**: 9 Oct 2026 Reuters follow-up to the Waldron succession story — internal speculation that CFO Denis Coleman or Global Banking & Markets co-head Ashok Varadhan could succeed Waldron as COO if he becomes CEO; Goldman spokesman dismissed it as "chattering class speculation." No leadership change; titles unchanged.
- **Piper Sandler–Perella Weinberg**: still acquisition talks only (no deal announced); row flag stands.
- **Aon/USI**: still pending regulatory approval; closing expected Q4 2026 (not before 19 Oct per merger agreement). No change.
- **Nuveen/Schroders**: post-close leadership detail confirmed — Richard Oldfield continues as Schroders CEO reporting to Nuveen CEO William Huffman; Johanna Kyrklund named CIO of Public Markets & Solutions for the combined firm; Schroders to operate separately 12–18 months; LSE delisting effective 2 Oct. Already reflected in rows — no change.
- **Macquarie**: CEO handover (Wikramanayake → Greg Ward) effective 7 Nov 2026 — still future; rows unchanged.
- **Rankings**: no new TAI/WTW World's 500 (Nov 2025 edition still latest; next expected ~Nov 2026); no new full-year Dealogic/Refinitiv IB table.
- **QFTA–TradeStation deal chatter checked**: the Quantum FinTech Acquisition Corp. "combination" announcement dates to November 2021 (expired/never completed); TradeStation remains a Monex Group subsidiary. No change.

### Earlier

- **2026-10-06 (first Tuesday watch):** two rows refreshed.
  - **Interactive Brokers** — client equity updated from $780bn (Dec 31, 2025) to **$964.7bn as of Sep 30, 2026** (5.576M client accounts), per the firm's Oct 1, 2026 monthly metrics release (Business Wire). Up ~24% since year-end on market appreciation plus 35% YoY account growth.
  - **Charles Schwab** — notes now record the **Forge Global acquisition completed Mar 2, 2026** ($660m all-cash, $45/share; private-markets platform operating within Schwab's alternatives offering), an M&A event missed in the original build.
  - Checked and confirmed no change: Nuveen/Schroders close verified (scheme effective Oct 1, LSE delisting Oct 2 — as recorded); Piper Sandler–Perella Weinberg still in talks only (WSJ Sep 29, no finalization); TPG president vacancy / CVC co-CEO succession as recorded (Sep 2026 announcements); Macquarie CEO handover still scheduled for Nov 7, 2026; no new TAI/WTW World's 500 edition (Nov 2025 edition remains latest; next expected ~Nov 2026); no new full-year Dealogic/Refinitiv IB league table; no finalized discount-broker consolidation; no leadership changes at guide firms since Oct 3.

## Ranking sources and editions

- **Asset managers:** Thinking Ahead Institute / WTW, *"World's 500 largest asset managers"*, published **10 Nov 2025** on **end-2024 AUM** (total $139.9tn). This is the latest published edition as of 2026-10-03 — no TAI end-2025 edition has been released. The top-20 figures and ranks in `aum_usd_bn`/`aum_rank` are from this edition; firms outside the top 20 use their own latest disclosed AUM (as-of date in `notes`) with `aum_rank` left blank and "in TAI/WTW top 500; exact rank not verified" noted. Cross-reference: IPE's Top 500 Asset Managers 2026 (Dec 31, 2025 AUM) shows an unchanged top 5, with Goldman Sachs AM overtaking Capital Group at #7 and PIMCO taking #9 from BNY.
- **Investment banks:** **Dealogic full-year 2025** global investment-banking fee league table (JPMorgan #1, 8.4% wallet share; then Goldman Sachs, BofA Securities, Morgan Stanley, Citi), cross-checked against LSEG/Dealogic regional tables. Elite boutiques (Evercore, Lazard, Moelis, Centerview, PJT, Perella Weinberg, Greenhill, Rothschild & Co, Houlihan Lokey) and regional players (RBC/TD/BMO Capital Markets, CITIC Securities, CICC, Raymond James, Stifel, Piper Sandler, William Blair, Baird, Jefferies, Mizuho, Barclays, Wells Fargo) were added for coverage beyond the bulge bracket.
- **Scope note:** hedge funds are excluded by design; alternatives managers (Blackstone, KKR, Apollo, Carlyle, Ares, TPG, CVC, Brookfield) are included as asset managers.

## Method

Six parallel research agents each covered an assigned batch (mega managers; large asset managers; APAC + alternatives; alternatives + bulge-bracket banks; boutiques + regional banks; plus a single-firm correction for JPMorgan), verifying every field against the firm's official site, press releases, and regulatory filings (10-K/annual reports). A top-up pass filled official websites for six batch-C rows. Unverifiable fields were left blank and named in `notes` — never guessed (in the Oct. 22, 2026 refresh those blanks became plain in-cell statements; see the Field set above). Currency conversions use only stated official rates (IRS 2025 yearly averages for CAD/EUR revenues; Reuters spot rates where cited); CNY/EUR/JPY/AUD/GBP-only figures are kept in `notes` unconverted rather than self-converted.

## Corrections caught during verification

- **TAI rank #5 is J.P. Morgan Chase ($4,045.0bn), not "BlackRock"** — the draft roster repeated a mislabeled row from a third-party republication of the WTW table; the official WTW press release names J.P. Morgan Chase. The bogus "BlackRock" placeholder was dropped and replaced with a fully verified JPMorgan Chase & Co. row (Both, rank 5).
- **Nuveen's acquisition of Schroders closed 1 Oct 2026** (Schroders delisted 2 Oct); rows are kept standalone with the double-counting risk flagged (~$2.6tn combined).
- **Janus Henderson taken private 30 Jun 2026** (Trian/General Catalyst/QIA consortium); ownership updated from Public to Private.
- **Nikko Asset Management renamed Amova Asset Management** effective 1 Sep 2025 (wholly owned subsidiary of Sumitomo Mitsui Trust Group).
- **Aberdeen**: legal name Aberdeen Group plc (the "abrdn" rebrand reversed effective 12 Mar 2025); row filed under Abrdn.
- **Ares CFO is Jarrod Phillips** (Michael McFerran dismissed Aug 2021); **CVC CFO is John Hourican** effective 1 Sep 2026 (Fred Watt retired); **CVC is Public** (Euronext Amsterdam listing, Apr 2024), not private.
- **PGIM CEO is Jacques Chappuis** (effective 1 May 2025), not David Hunt; **Artisan Partners CEO is Jason Gottlieb** (succeeded Eric Colson); **Brookfield AM CEO is Connor Teskey** (3 Feb 2026, succeeding Bruce Flatt); **Macquarie CEO transition**: Shemara Wikramanayake retires 6 Nov 2026, Greg Ward takes over 7 Nov 2026; **Moelis CEO**: Ken Moelis handed to Navid Mahmoodzadegan 1 Oct 2025; **CITIC Securities chairman**: Zou Yingguang succeeded Zhang Youjun ~30 Sep 2026.
- **Natixis/Generali JV terminated Dec 2025** — ownership remains Subsidiary of Groupe BPCE.
- **DWS** is phasing in the "Deutsche Asset Management" umbrella brand Nov 2026–Mar 2027; parent remains DWS Group GmbH & Co. KGaA (~80% Deutsche Bank-owned).
- **Greenhill** ownership verified: acquired by Mizuho Financial Group, closed 1 Dec 2023 ($550m all-cash).
- **AllianceBernstein succession**: Seth Bernstein CEO through 31 Mar 2027; Onur Erzan (President) becomes CEO 1 Apr 2027.
- **Brookfield Asset Management HQ** recorded as New York (moved from Toronto Dec 2024, per the firm's filings) — contradicts older third-party directories that still show Toronto.

## Known gaps (left blank, never guessed)

- **No general contact email published** (96 of 100): only MFS Investment Management, Baillie Gifford, Robeco, and Aviva Investors publish a general inbox; everyone else is form-only or function-specific. Documented per row.
- **CEO not publicly named** (2): E Fund Management (general manager / CEO-equivalent not disclosed); Greenhill (no official leadership disclosure newer than the Dec 2023 Mizuho acquisition announcement).
- **CFO not publicly named** (38, as of the Oct. 22, 2026 refresh — cells read "Not publicly named — see Notes"): concentrated in private/partnership firms (Fidelity, Wellington, Baillie Gifford, Dodge & Cox, William Blair, Baird, Centerview), divisions (SSGA, Nuveen, RBC/TD/BMO Capital Markets), and Chinese firms (ChinaAMC, E Fund) — each flagged in `notes`.
- **president_coo carries a no-separate-role statement** (72): most firms simply have no such role (combined CEO/President titles, or no COO); flagged where the role is vacant (e.g., TPG's president Todd Sisitsky resigned 6 Sep 2026, no successor named).
- **investment_leadership carries a no-public-role statement** (66): pure advisory boutiques and investment banks publish no CIO/research/strategy roles by design ("advisory boutique; no public investment-leadership roles"); some asset managers disclose only at strategy level.
- **AUM blank** (8 of 60 asset-manager/brokerage rows; 38 of 100 rows in total, the balance being investment banks carried on revenue): firms disclosing only in non-USD currencies with no official USD figure (Robeco EUR, Candriam EUR, Ninety One GBP, Aviva Investors GBP, E Fund RMB, DWS EUR, Nomura JPY, Macquarie AUD) — local-currency figures kept in `notes`, and `aum_as_of` states the position plainly.
- **Revenue blank** (9 of 34): private boutiques not disclosing revenue (Centerview, William Blair, Baird); CNY-only reporters (CITIC Securities RMB 74.854bn, CICC CNY 28.48bn, kept in `notes`); division revenue not disclosed in USD.
- **HQ phone unpublished** (63, as of the Oct. 22, 2026 refresh — cells read "Not published on official site"): not published on official sites; never taken from directories (one exception, Franklin Templeton, flagged as directory-sourced).
- **major_offices** is HQ-only for firms that publish no concise hub roster (flagged "partial" where applicable); **JPMorgan major_offices is blank** — the firm discloses 100+ markets but no official hub list.
- **Geode CEO conflict**: Wikipedia/Glassdoor name David Lane (President & CEO); an Apr 2025 industry profile names Robert Minicus — recorded with the conflict in `notes`.
- **WSJ ~30 Sep 2026 reported Piper Sandler acquisition talks with Perella Weinberg** — unfinalized; flagged in `notes`, not treated as fact.
- **Leadership currency**: investment firms turn over executives frequently; all titles verified as of early October 2026 — verify before use.
