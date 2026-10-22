# Luxury Hotels Worldwide — Forbes Five-Star, AAA Five Diamond & Leading Hotels of the World

A sourced, deduped list of luxury hotels worldwide from three sources, compiled **2026-09-12**, updated **2026-10-20** (added five October 2026 LHW additions: Le Graal Cortina, Villa Argentina, The Nora Hotel, Recess Hotel & Club Savannah, Pemako Punakha).

- **`hotels.csv`** — the list. Columns: `name, sources, continent, region, country, nearest_city, source_url`
  - `sources` is semicolon-separated when a hotel appears in more than one list (e.g. `AAA;Forbes`)
  - `nearest_city` is the nearest major city — for rural/resort properties, the city a traveler would fly into
- **`parts/`** — the six per-source/per-region working files
- **`merge.py`** — the merge/dedupe script

## Headline numbers

| Metric | Count |
|---|---|
| Hotels (total, deduped) | **687** |
| In Forbes Travel Guide Five-Star (2026 Star Awards) | 288 |
| In AAA Five Diamond (2026) | 154 |
| In Leading Hotels of the World (current members) | 329 |
| Countries | 79 |

### Source overlaps (deduped)

| Combination | Hotels |
|---|---|
| Forbes only | 207 |
| LHW only | 300 |
| AAA only | 97 |
| Forbes + AAA | 54 |
| Forbes + LHW | 26 |
| AAA + LHW | 2 |
| All three | 1 (The Setai, Miami Beach) |

### By continent

| Continent | Hotels |
|---|---|
| Europe | 265 |
| North America | 256 |
| Asia | 130 |
| Africa | 26 |
| South America | 9 |
| Oceania | 1 |

### Top countries

United States 158 · Italy 66 · Mexico 54 · China 42 · Switzerland 40 · France 36 · United Kingdom 27 · Spain 18 · Japan 15 · UAE 13

## About the three sources

- **Forbes Travel Guide Five-Star** — Forbes Travel Guide's annual Star Awards (2026 edition announced Feb 2026) rate hotels Five-Star, Four-Star, or Recommended. Only Five-Star hotels are included here.
- **AAA Five Diamond** — AAA's annual Diamond ratings for the US, Canada, Mexico, and the Caribbean (2026 list, based on 2025 inspections). Only hotels are included, not AAA Five Diamond restaurants.
- **Leading Hotels of the World (LHW)** — a luxury hotel *membership collection*, not a star rating. Member hotels are included as requested and labeled `LHW` in the `sources` column.

## Coverage notes per source

### Forbes Five-Star — 288 hotels (substantially complete for the Americas and Europe; partial for Asia-Pacific/Africa/Middle East)
- **Americas (110):** extracted directly from Forbes Travel Guide's own property API (only records with a current Five-Star rating and hotel property type) — authoritative for 2026. US 78, Canada 5, Mexico 15, Caribbean 10, Central America 1 (Four Seasons Papagayo), South America 1 (Hotel das Cataratas, Iguassu Falls). No verified Five-Star hotels in Argentina, Chile, Peru, Colombia, Panama, Belize, Guatemala, or Jamaica in 2026. Verified exclusions: The Breakers, Peninsula Beverly Hills, Halekulani, and Eden Roc Cap Cana are Four-Star.
- **Europe (95, 16 countries):** baseline is the complete published 2025 winners list (334 hotels globally) plus 4 confirmed 2026 additions (Maybourne Riviera, One&Only Portonovi, Mandarin Oriental Barcelona, Mandarin Oriental Savoy Zurich); retention spot-checked. Countries with no Forbes Five-Star baseline at all (Germany, Austria, Belgium, Croatia, Poland, Georgia, Scandinavia) were not exhaustively re-screened for surprise 2026 additions.
- **Asia-Pacific / Africa / Middle East (87, 18 countries): PARTIAL.** Not fully verifiable from public sources: mainland China beyond Beijing/Shanghai/Macau; India; Sri Lanka; Thailand beyond Bangkok; Taiwan; Indonesia beyond two Four Seasons Bali resorts; Malaysia; Cambodia/Laos/Bhutan/Uzbekistan/Georgia; Maldives beyond 5 listed; Seychelles; Egypt; Israel; Jordan; Bahrain; Oman; Kuwait beyond Four Seasons Kuwait; Qatar's Raffles Doha; Abu Dhabi; Saudi Arabia beyond Nujuma + Four Seasons Riyadh; Dubai retentions beyond 9 verified.
- **Australia:** zero entries — corroborated that no Australian hotel holds Five-Star in 2026 (Crown Towers Perth was downgraded to Four-Star).

### AAA Five Diamond — 154 hotels (complete published 2026 list)
- Backbone is AAA's official "Five Diamond Hotels 2026" PDF (newsroom.aaa.com), extracted programmatically and cross-checked 1:1 (152 hotels), plus the 2 newest additions from AAA's August 31, 2026 announcement (One&Only Mandarina and Rosewood Mandarina, Nayarit, Mexico).
- US 96 · Mexico 39 · Caribbean 12 · Canada 7.

### Leading Hotels of the World — 329 hotels (current 2026 membership; substantially complete)
- **Americas + Europe (244):** 52 North America, 8 South America, 184 Europe — mostly verified against Amex's current LHW directory and LHW press announcements (2025–2026 additions). Europe E–Z tail and DACH entries rest partly on destination-page snippets and a 2026 Wikipedia list, so a handful of current members may still be missing (most likely France/Italy/Spain); a 2026-10-06 cross-check of LHW's Winter Collection added Argos in Cappadocia (Türkiye), which had been missed.
- **Asia-Pacific / Africa / Middle East (80):** 59 Asia (incl. 9 Middle East), 20 Africa, 1 Oceania — from LHW's current continent directory pages. Kenya's first LHW member, Hemingways Nairobi, joined the collection 2026-10-06.
- **Oceania gap:** only one Oceania member could be verified (Jackalope Hotel, Australia); no current evidence for New Zealand, Fiji, or French Polynesia.
- **October 2026 additions:** announced 2026-10-19 — Le Graal Cortina (Cortina d'Ampezzo, Italy), Villa Argentina (Dubrovnik, Croatia), The Nora Hotel (West Palm Beach, Florida, USA), Recess Hotel & Club Savannah (Savannah, Georgia, USA), Pemako Punakha (Punakha, Bhutan — LHW's first Bhutan member; Bhutan is a new country in the list). Hemingways Nairobi (Kenya) was part of the same October announcement but had already been added on 2026-10-13.
- Hotels suspected of having left the collection were excluded rather than guessed.

## Caveats & judgment calls
- **Transcontinental hotels** (Address Istanbul, Four Seasons Istanbul Sultanahmet, Four Seasons Istanbul at the Bosphorus, Four Seasons Hotel Baku) are filed under **Europe**, following Forbes Travel Guide's own regional grouping in its awards releases.
- `nearest_city` uses fly-in gateways for remote resorts (e.g. Jackson for Amangani, Missoula for Montana ranches, Male for Maldives, Umluj for Nujuma) — inherently approximate.
- `source_url` on each row is a page actually consulted (official announcement, brand press release, or directory page). Forbes's and LHW's hotel detail pages are JS-heavy and were not individually fetchable, so URLs point to the announcement/directory pages used.
- Dedupe key: normalized (name, nearest_city, country). Same-name variants ("New York" vs "New York City", "Cabo San Lucas" vs "Los Cabos") were canonicalized during the merge.

## Method
Six parallel research agents each covered an assigned source/region using web search and page-text fetches: official lists first (FTG Star Awards announcements/API, AAA's official 2026 Five Diamond PDF, lhw.com directories), then reputable secondary compilations and brand press releases. 768 part rows were merged and deduped to **680** unique hotels; Argos in Cappadocia was added on 2026-10-06 (681 rows); Hemingways Nairobi was added on 2026-10-13 (682 rows); the five other October 2026 LHW additions (Le Graal Cortina, Villa Argentina, The Nora Hotel, Recess Hotel & Club Savannah, Pemako Punakha) were added on 2026-10-20 (now 687 rows); cross-source duplicates carry all applicable sources.
