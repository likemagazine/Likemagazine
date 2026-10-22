# CEOs of the Fortune Global 500 — README

## What this is
All 500 chief executives of the Fortune Global 500, in the ranking's canonical order, with headquarters, industry, FY2025 revenue, and corporate contact details.

## Ranking backbone
- **Fortune Global 500 2026**, 37th running, **published July 28, 2026**, ranked by FY2025 revenue.
- No newer edition exists as of October 20, 2026.
- Headline: **Amazon (#1, $716.92B)** ended Walmart's 12-year run at the top. Aggregate: $43.1T revenue, $3.4T profits, 70.2M employees.
- Ranks, revenues, and industries sourced from Fortune (fortune.com ranking pages and the official Fortune China Global 500 2026 database); cross-checked across both.

## CEO verification approach
- CEO name/title for each company was verified against **official corporate sources as of October 2026**: corporate leadership pages, investor-relations releases, exchange filings (SEC, HKEX, SZSE/SSE), and official press releases.
- Fortune's own list can lag CEO transitions, so company sources are authoritative here; **2026 transitions are captured** (e.g., Walmart, Toyota, Berkshire Hathaway, BP, BMW, Kroger, Cigna, Disney, P&G, Bosch, Kia co-CEOs, Munich Re) and noted per row.
- Post-cutoff successions (effective after the last check) are noted but the incumbent retained until the effective date.
- Co-CEOs are both listed; interim/acting CEOs are flagged in notes.
- **Never-guess rule:** where no official source confirmed the CEO (6 rows), the field is blank with an explanatory note naming what was found and why the threshold wasn't met.

## Coverage (of 500)
| Field | Filled |
|---|---|
| CEO name / title | 494 |
| HQ city | 498 |
| HQ country | 500 |
| Industry | 500 |
| Revenue (USD B, FY2025) | 500 |
| Website | 488 |
| Employees | 113 |
| HQ phone (switchboard) | 40 |
| Contact email (general) | 6 |

## Systematic gaps (by design)
- **Phones (40/500) and emails (6/500):** most Global 500 companies publish no general corporate email or global switchboard; nothing was inferred — no personal emails, no direct dials, no email-pattern guessing, anywhere.
- **Employees (113/500):** filled only from official filings or Fortune's dataset; third-party estimates are flagged provisional in notes.
- **CEO blanks (6):** Jingye Group (306), Zhejiang Communications Investment Group (309), Susun Construction Group (340), Jinneng Holding Group (390), Hangzhou Industrial Investment Group (419), Beijing Jianlong Heavy Industry Group (484) — each with a documented search trail in notes. Apple (#6) was filled 2026-09-29 after its transition was confirmed by the official Apple Newsroom.
- Region mix: East Asia 175, North America 156, Europe 133, South Asia 10, Latin America 10, Southeast Asia 7, Oceania 6, Middle East 3. U.S. companies at an 18-year high (141); China 116.

## Files
- `ceos_multinational.csv` — master data (500 rows × 14 columns)
- `ceos_multinational.pdf` — formatted A3 landscape table with clickable company links
- `work/part_A–E.csv` — per-band working files and research notes

## Maintenance
On the Tuesday watch: new Fortune Global 500 edition expected ~July 2027; CEO transitions, HQ moves, and mergers tracked weekly in the meantime.

### Changelog
- **2026-10-20:** General Dynamics (#294) — announced succession (company release Oct 7, 2026): President Danny Deep elected CEO effective Jan 1, 2027; Phebe Novakovic to become executive chairman. CEO cell retains Novakovic until the effective date per pre-effective-date convention. HDFC Bank (#272) — re-verified: Anup Bagchi's Oct 27, 2026 effective date stands (exchange filings Oct 16 detail ~Rs 43 crore first-year package; shareholder nod sought); incumbent Sashidhar Jagdishan retained until the Oct 27 check per convention. Apple (#6) re-checked: John Ternus still CEO (TIME cover Oct 15, Oct 28 'Apple Experience' event announced, Ternus's third product event; no new transition). No other Global 500 CEO changes found; no new Fortune edition (next ~July 2027). CSV/PDF/Library copies refreshed.
- **2026-10-13:** Ahold Delhaize (#98) — Thierry Garnier's appointment approved by shareholders at the Oct 13, 2026 EGM; to succeed Frans Muller as President & CEO in 2027 (exact date TBD by supervisory board). CEO cell retains Muller until the effective date per pre-effective-date convention. No other Global 500 CEO changes found. Apple (#6) re-checked: John Ternus still CEO (Tim Cook interview Oct 7/8 confirms; no new transition). HDFC Bank (#272) pending: Anup Bagchi takes charge Oct 27, 2026 — flips to Bagchi in the Oct 20 check. No new Fortune edition (next ~July 2027). Coverage-note: Danaher (CEO Julie Sawyer Montgomery, effective Oct 1) and Kingfisher (Sebastian Gundel, effective Feb 1, 2027) are NOT on the Fortune Global 500 2026 — the edition's #500 cutoff is ~$33B revenue (PayPal, $33.172B), above both companies' FY2025 revenue; no roster gap. CSV/PDF/Library copies refreshed.
- **2026-10-06:** Tyson Foods (#283) — Jeff Schomburger took over as president & CEO Oct 4, 2026 (announced May 28; Donnie King remains on board). HDFC Bank (#272) — Anup Bagchi named MD & CEO effective Oct 27, 2026 (board and RBI approved Oct 1; Jagdishan's term ends Oct 26); incumbent retained per pre-effective-date convention, switches to Bagchi on Oct 27. Apple (#6) re-checked: John Ternus still CEO, no new transition. No other Global 500 CEO changes found; no new Fortune edition (next ~July 2027). CSV/PDF/Library copies refreshed.
- **2026-09-29:** Apple (#6) — John Ternus confirmed as CEO (effective Sept 1, 2026; Tim Cook to Executive Chairman) per official Apple Newsroom; CEO name/title filled (494/500). Tyson Foods Oct 4 succession (Jeff Schomburger) still pending — incumbent retained. No other Global 500 CEO changes found.
