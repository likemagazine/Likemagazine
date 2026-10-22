# Nobel Prize Laureates 1901–2026

A sourced reference guide to every Nobel laureate — **1,036 prize-recipient rows** across all six categories, from the first prizes in 1901 through all the October 2026 announcements. Compiled **2026-09-17**; updated **2026-10-13**.

- **`nobel_laureates.csv`** — one row per prize-recipient. Columns:
  `full_name, category, prize_year, prize_share, motivation, affiliation_at_award, country, born, died, official_nobel_page, contact_address, source_url, notes`
  - Shared prizes get one row per recipient with `prize_share` as `1/1`, `1/2`, `1/3`, or `1/4` (shares sum to 1 for every prize year — validated).
  - `motivation` is the Nobel committee's official English wording. Rows whose wording came via a cited secondary source are flagged in `notes`.
  - `country` is the birth country as listed by Nobel (historical names kept, e.g. Prussia, Austria-Hungary); for Peace organizations, the headquarters country. Citizenship differences are noted where known.
  - `contact_address` holds ONLY publicly listed institutional addresses (no personal data anywhere; deceased laureates carry none — 25 rows, mostly Peace organizations).
  - Double winners appear once per prize (Bardeen, Sanger, Sharpless, Curie, Pauling — see notes below).
- **`nobel_laureates.pdf`** — formatted landscape tables sectioned by category, with 955 clickable nobelprize.org laureate-page links.

## Headline numbers (all verified against Nobel's official totals)

| Category | Prizes | Laureate rows | Nobel's official total |
|---|---|---|---|
| Physics | 120 | **231** (230 individuals; Bardeen ×2) | 231 laureates 1901–2026 ✓ |
| Chemistry | 118 | **202** (198 individuals; Sanger ×2, Sharpless ×2) | 202 laureates ✓ |
| Medicine | 117 | **235** | 235 laureates ✓ |
| Literature | 119 | **123** | 123 laureates ✓ |
| Peace | 107 | **144** (113 individuals + 31 organization awards to 28 orgs) | 144 awards ✓ |
| Economic Sciences | 58 | **101** | 101 laureates ✓ |
| **Total** | **639** | **1,036** | — |

No-award years accounted for: Physics 1916, 1931, 1934, 1940–42; Chemistry 1916–17, 1919, 1933, 1940–42; Medicine 1915–18, 1921, 1925, 1940–42; Literature 1914, 1918, 1935, 1940–43 (2018's prize postponed, awarded 2019); Peace 19 years (1901–2025).

## Edition note

This guide covers **1901 through the complete 2026 prize cycle** — all six 2026 prizes announced: Medicine (2026-10-05), Physics (2026-10-06), Chemistry (2026-10-07), Literature (2026-10-08), Peace (2026-10-09), and Economic Sciences (2026-10-12).

## Method

Six parallel research workers — one per category — worked from nobelprize.org first: the public Nobel Prize API v2.1 (names, years, shares, official motivations) and individual laureate facts pages (affiliations, birth/death facts, birth countries). Where the API was unreachable mid-build, rows were completed from nobelprize.org HTML pages and Wikipedia's laureate lists with Nobel's official wording retained and the fallback flagged per row. Final counts were verified against Nobel's own published per-category totals — all six match exactly. Currency is October 2026 (the full 2026 prize cycle). Unverifiable fields were left blank rather than guessed.

## Sources

- Nobel Prize API v2.1 (`api.nobelprize.org/2.1/nobelPrizes`, `…/laureates`) — official motivations, shares, names, facts-page URLs.
- nobelprize.org laureate facts pages — affiliations, birth/death, birth countries.
- Nobel "Facts on the Nobel Prize in …" pages — official per-category totals.
- Wikipedia's per-category laureate lists — completeness cross-checks only.

## Interpretation notes

- **Multiple winners:** John Bardeen (Physics 1956, 1972); Marie Curie (Physics 1903, Chemistry 1911); Frederick Sanger (Chemistry 1958, 1980); Karl Barry Sharpless (Chemistry 2001, 2022); Linus Pauling (Chemistry 1954, Peace 1962) — each flagged in `notes`.
- **Declined:** Le Duc Tho (Peace 1973, declined); Jean-Paul Sartre (Literature 1964, declined); Boris Pasternak (Literature 1958, forced to decline).
- **Posthumous:** Erik Axel Karlfeldt (Literature 1931); Dag Hammarskjöld (Peace 1961); Ralph M. Steinman (Medicine 2011 — died three days before the announcement; the award stood).
- **Peace organizations:** 28 unique organizations (ICRC ×3, UNHCR ×2); `born`/`died` blank by design; 17 carry verified public headquarters addresses.
- **Economic Sciences** is formally the Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel, awarded since 1969 — not one of the original five prizes in Alfred Nobel's will.
- Spouse/family details are not systematically included; married laureate pairs are noted in `notes` only where genuinely notable and publicly documented.

## Change log

- **2026-10-13 (Tuesday watch):** Added the four remaining 2026 prizes — Chemistry (announced 2026-10-07: Henri B. Kagan and Kenso Soai, 1/2 each, for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis), Literature (announced 2026-10-08: Anne Carson, 1/1, for her bold and inventive oeuvre in playful dialogue with the classical tradition), Peace (announced 2026-10-09: Navanethem "Navi" Pillay, 1/1, for efforts to promote peace and international law), and Economic Sciences (announced 2026-10-12: Robert E. Hall and Michael Woodford, 1/2 each, for microeconomic foundations of macroeconomic stabilisation). All six rows carry `born`, `affiliation_at_award` (blank where Nobel lists none), `country`, and verified official nobelprize.org facts pages (HTTP 200) from the Nobel Prize API; announcement dates are labeled in `notes`; year-only birth dates for Soai, Hall, and Woodford are flagged. The 2026 prize cycle is now complete. Guide now 1,036 rows across 639 prizes.
- **2026-10-06 (Tuesday watch):** Added the first two 2026 prizes — Medicine (announced 2026-10-05: Karl Deisseroth, Peter Hegemann, Georg Nagel, 1/3 each, for discoveries concerning light-gated ion channels and optogenetics) and Physics (announced 2026-10-06: Francis Halzen, 1/1, for contributions to the IceCube Neutrino Observatory and the discovery of high-energy astrophysical neutrinos). All four rows carry `born`, `affiliation_at_award`, `country`, and verified official nobelprize.org facts pages (HTTP 200) from the Nobel Prize API; announcement dates are labeled in `notes`. Guide now 1,030 rows across 635 prizes. Chemistry, Literature, Peace, and Economic Sciences 2026 prizes are still to be announced (Oct 7, 8, 9, 12).

## Known gaps and staleness

- **Economic Sciences enrichment completed 2026-10-01**: all 99 rows now carry `born`, `died`, `affiliation_at_award`, `country`, and `official_nobel_page` from nobelprize.org where Nobel publishes them. Three residual gaps are flagged per row in `notes`: affiliation not listed by Nobel for the two 1974 laureates (Hayek, Myrdal); full birth date/place not published by Nobel for James A. Robinson (2024).
- **18 Economic Sciences rows (1999, 2006–2021, 2023–2024)** were built while the Nobel API was unreachable; motivations quote Nobel's official wording via cited secondary sources and are flagged in `notes`.
- `affiliation_at_award` blank on 2 Physics rows (Marie Curie 1903; Martinus Veltman 1999 — Nobel's own data lists none) and 2 Chemistry rows (Mullis 1993, Knowles 2001 — Nobel lists none); blanks are faithful, not missing research.
- `died` blank for living laureates (354 rows incl. organizations excluded) — correct as of 2026-10-13; the three oldest living Medicine laureates were spot-verified alive.
- A few birth facts are year-only where Nobel records only the year (e.g., John M. Martinis — no birthplace, so no country).
- Motivations are long official texts; the PDF renders them wrapped at small type.
