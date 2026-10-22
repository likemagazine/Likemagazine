# Top Insurance Brokerages Worldwide

The intermediaries' counterpart to the carriers guide: the world's leading insurance and reinsurance brokers, ranked by revenue, with leadership, offices, specialties, and access routes.

## Roster and ranking

- **25 firms**, ranked primarily by the **AM Best "Top Global Insurance Brokers — 2026 Edition"** (published July 2026; ranked by **2025 total revenue**), cross-checked against the AM Best 2025 edition (2024 revenue) and the Business Insurance "100 Largest Brokers of U.S. Business" 2026 ranking (July 2026; 2025 U.S. brokerage revenue).
- Revenue figures are labeled with their period in every row. Where a firm's 2025 figure was not publicly disclosed (private firms), the latest AM Best figure is used with the period labeled.

## Field set (depth standard — applied in CSV, PDF/DOCX and web article alike)

Per firm, wherever verifiable: company name; founded; history; headquarters city and country; region; official website; published phone and published contact email (only where the firm itself publishes them — never guessed); official contact route; CEO with exact title; president/COO with exact title; CFO with exact title; other C-suite; senior/practice leadership; major offices (HQ plus footprint — named cities/countries or published office count by region); specialties/practice areas in full; clients or client categories where published, else "not disclosed"; distinctiveness; access/entry route; brokerage revenue, dated and sourced; revenue rank; key people; ownership/parent/listing; notes; sources. **Any unverifiable field says so plainly in the cell** ("Not published by the firm" / "Not publicly disclosed"); the column stays in the schema for all 25 entries. The October 2026 refresh added the `clients` and `contact_route` columns and eliminated every silent blank: 25 rows × 26 columns, zero empty cells.

## Methodology

- Every fact verified against official/authoritative sources: company official sites, press releases, SEC filings and 10-Ks (FY2025 filings, Feb 2026), and the AM Best / Business Insurance rankings.
- Nothing inferred or guessed. Cells that could not be verified are left blank and flagged in `notes`.
- People: full names + exact titles as published by the firm.
- `major_offices`: major offices as listed by the firm; where no city list is published, the verified footprint (e.g. "130 countries") is recorded instead.
- `access_entry`: how clients engage (direct, RFP/tender, broker-of-record). Published minimums only — otherwise "not publicly disclosed".

## Coverage (25 firms, October 2026 refresh)

Every cell is filled; unverifiable fields state "Not published by the firm" (or equivalent) in the cell rather than sitting blank.

| Column | Substantively filled |
|---|---|
| CEO / Founded / history / Specialties / Clients / Distinctiveness / Access / Ownership | 25/25 |
| Website | 25/25 (Ardonagh gap closed Oct 2026) |
| Brokerage revenue | 24/25 (Newfront: not published — WTW subsidiary) |
| Other C-suite | 21/25 |
| CFO | 15/25 (Howden and WTW gaps closed Oct 2026) |
| Senior practice leadership | 11/25 |
| Published HQ phone | 6/25 |
| Published contact email | 3/25 |

## Known gaps (stated plainly in the cells, not oversight)

- **Contact emails/phones:** the brokerage industry is overwhelmingly contact-form-only; only 3 firms publish a contact email and 6 a phone in the sources verified. Aon's published media/investor emails and contact lines were added in the October 2026 refresh.
- **Senior practice leadership:** named practice heads are published by only 11 of 25 firms.
- **Newfront:** acquired by WTW (Jan 27, 2026, $1.3B); standalone revenue not published — row flagged as WTW subsidiary.
- **AssuredPartners:** Gallagher's $13.45B acquisition closed August 2025 — now a Gallagher subsidiary.
- **USI:** KKR agreed to sell USI to Aon for $17B (announced Aug 31, 2026; expected close Q4 2026) — still pending as of Oct 22, 2026.

## Notable current facts captured

- Marsh McLennan rebranded to **Marsh** (Jan 14, 2026; NYSE ticker MRSH); Guy Carpenter to become Marsh Re by 2027.
- Brown & Brown closed the **$9.83B Accession/RSC Topco** acquisition (Aug 2025) — largest in its history.
- Hub International confidentially filed for a U.S. IPO (June 2026).
- Ryan Specialty CEO is Timothy W. Turner (founder Patrick G. Ryan now Executive Chairman); 2025 revenue $3.05B verified.
- Ardonagh 2025 income $2.55B (+20.4%); Stone Point invested $2.5B at ~$14B valuation.
- Diot-Siaci 2025 revenue €1.31B (+28%); first AM Best top-20 appearance.

## Files

- `insurance_brokerages.csv` — master data (25 rows × 26 columns, UTF-8)
- `insurance_brokerages.pdf` — formatted landscape PDF
- `insurance_brokerages.html` / `insurance_brokerages_llms.txt` — SEO/AI web version
- Library copies: `~/workspace/your_files/insurance_brokerages.csv`, `insurance_brokerages.pdf`
- LIKE Markets slate (October 2026): `~/workspace/your_files/The World's Insurance Brokerages - LIKE Markets Guide.pdf` and `.docx`; staged article `~/workspace/likeleaders-site/articles/like-worlds-insurance-brokerages.html`; staged feature-card fragment `~/workspace/likeleaders-site/fragments/markets-insurance-brokerages.html` (sections/markets.html not edited; nothing published or pushed).

Compiled 2026-10-03; refreshed to the full depth standard 2026-10-22. Maintained by the Tuesday watch (first check 2026-10-06).

## Tuesday watch updates

**2026-10-06** — The Baldwin Group: definitive take-private agreement announced Sept 14, 2026 — entity formed by Sequence Holdings and DFO Management (Michael Dell's family office) to acquire a majority interest in an all-cash ~$7.7B enterprise-value deal ($32.50/share; ~$4.6B equity + ~$3.1B debt assumed/refinanced; 88% premium to June 17, 2026 unaffected close); unanimously board-approved; expected close Q1 2027, after which Baldwin becomes privately held, delists from Nasdaq, and eligible colleagues retain a significant minority equity stake. Row updated (ownership, notes, sources); prior FT Sept 13 ~$4.14B figure was an unconfirmed pre-announcement and is superseded. Marsh: Tom Geraghty named CEO of Marsh Europe effective Nov 1, 2026, succeeding Christos Adamantiadis (new Global Head of Placement & Market Solutions, Marsh Risk); John Donnelly to retire early 2027; Marsh Agency (middle market): Matt Stadler CEO from Jan 1, 2027 succeeding David Eslick (becoming chairman), John Stanchina to succeed Stadler as president, Andrew Neary CEO of combined East/Northeast region. Senior leadership column updated. Aon–USI: no change — deal still pending, close expected Q4 2026. Hub International IPO: no new developments since the June 2026 confidential filing. AM Best 2026 edition (July) remains current; no new edition published.

**2026-10-13** — Howden: Elliot Richardson named Group Chief Commercial Officer (announced Oct 12, 2026, effective immediately; newly created role reporting to CEO David Howden; joins Group Executive Committee; remains Executive Chair of Howden Re; Howden Markets and Group Placement report to him as part of a new group commercial strategy). Row updated (other_c_suite, key_people, notes, sources). Aon–USI: still pending — merger agreement (Aug 30, 2026) has no close before Oct 19, 2026, outside date June 1, 2027, expected close Q4 2026; Nadin Virani remains interim CFO (executive-search firm engaged for a permanent CFO). Hub International IPO: no new public developments since the June 26, 2026 confidential S-1 filing. Baldwin Group: shareholder-rights law firms (Kaskela, Schall Brown & Schwartz, Halper Sadeh, others) announced fiduciary-duty investigations into the $32.50/share buyout price; no lawsuit filed, no deal-terms change, close still expected Q1 2027 — row unchanged. Marsh completed the tuck-in acquisition of Accel Holdings (Oct 2, 2026; ~130 employees, Iowa/Illinois/Missouri/Kansas, folded into Marsh Agency); Gallagher acquired NZ retail broker Albany Insurance Services (Oct 1, 2026, terms undisclosed) — both immaterial tuck-ins, list unchanged. AM Best 2026 edition (July) and Business Insurance 100 Largest Brokers 2026 (July) remain current; no new editions.

**2026-10-20** — No changes. Aon–USI: still pending — the deal is now past the agreement's no-close-before-Oct-19, 2026 floor, with regulatory approval still outstanding; expected close Q4 2026 (outside date June 1, 2027); Aon completed a $13.4B senior notes offering on Oct 2, 2026 to fund the cash consideration and refinance USI debt. Hub International IPO: no new public developments since the June 26, 2026 confidential S-1 filing. Baldwin Group: no deal-terms change — Sequence/DFO take-private still expected to close Q1 2027; the Oct 12 Kaskela Law investigation is the same routine shareholder-litigation noise noted 2026-10-13, no lawsuit filed; the Oct 14 Founder Shield brand consolidation is below the tracking bar. Leadership: no new group/segment/regional C-suite moves at list firms since the Oct 13 check. AM Best 2026 edition (July) and Business Insurance 2026 remain current; no new editions.

**2026-10-22 (full depth-standard refresh)** — Marsh: Q3 2026 results (Oct 15, 2026) confirm the brand transition completed ahead of schedule; segment reporting renamed (Guy Carpenter → "Reinsurance", Mercer → "People and Investments"); Mark McGivney now Executive Vice President, CFO **and COO**; vice-chair layer (Studer, Tomlinson, Moynihan) recorded. Aon–USI: **still pending** as of Oct 22, 2026 (Chubb Q3 results the same day speak of its gain "if Aon's acquisition closes"); Aon still guides to a Q4 2026 close; Nadin Virani remains Interim CFO (Oct 9, 2026 announcement); Denise Perlman's expanded middle-market reinsurance role (Oct 7, 2026; USI integration team) added; Aon's own published contact lines (+1 833 751 8114 / +1 312 381 3024) and media/investor emails recorded — phone/email coverage rises. Howden: **CFO gap filled** — Susan Panuccio, Group CFO effective Jan 6, 2026 (announced Oct 14, 2025); Mark Craig moved to Chief Investment Officer. WTW: **leadership gaps filled** — Alexis Faber (COO), Lucy Clarke (President, Risk & Broking), Julie Gebauer (President, Health, Wealth & Career), Adam Garrard (Chairman, Risk & Broking), Spike Lipkin (Chief AI Officer); Willis Re named Neil Eckert global CEO (Sept 9, 2026, joining by Mar 1, 2027). Ardonagh: **website gap filled** — ardonagh.com confirmed from the firm's own hosted statements (25/25 websites). Gallagher: October tuck-ins (Albany NZ Oct 1, Ornella Oct 7, Winter & Co) immaterial; AssuredPartners close (Aug 2025, $13.45B) reconfirmed. Hub IPO: no new public developments since June 26, 2026. Baldwin: no deal-terms change (further routine investigations, Amparo Oct 19, 2026). Schema: `clients` and `contact_route` columns added; every remaining unverifiable field now states so in the cell — zero empty cells. Pre-refresh CSV preserved at `work/insurance_brokerages_pre_oct2026_refresh.csv`.
