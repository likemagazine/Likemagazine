# World's Best Vineyards — Top 100, Organized by Wine Region

A sourced list of the World's Best Vineyards Top 100, one row per vineyard,
compiled **2026-09-12**.

- **`vineyards.csv`** — the list, sorted by wine region then rank. Columns:
  `name, rank, wine_region, country, nearest_city, known_for, source_url`
  - `known_for` is one short phrase naming signature wines or grape varieties.
  - `source_url` on every row is the vineyard's verified official website.
- **`parts/`** — the six per-region working files.

## Headline numbers

| Metric | Count |
|---|---|
| Vineyards (Top 100) | **100** (ranks 1–100 all present, zero duplicates) |
| Edition | **2025** (announced November 19, 2025, Margaret River, Australia) |
| Wine regions | 58 |
| Countries | 20 |

### Rank highlights

1. Vik (Millahue, Chile) · 2. Schloss Johannisberg (Rheingau, Germany) ·
3. Bodegas Ysios (Rioja, Spain) · 4. Bodega Garzón (Maldonado, Uruguay) ·
5. Château Smith Haut Lafitte (Bordeaux, France)

### Countries represented

France 14 · Spain 11 · Argentina 11 · Portugal 8 · USA 8 · Italy 7 ·
Chile 7 · New Zealand 7 · South Africa 6 · England 4 · Germany 2 ·
Austria 2 · Hungary 2 · Georgia 2 · Lebanon 2 · Japan 2 · Uruguay 2 ·
Bulgaria 1 · Canada 1 · Australia 1

## Why the 2025 edition

The ranking is officially "The World's 50 Best Vineyards" (by 50 Best) with an
extended 51–100 list, announced each November. The 2026 edition is scheduled
for November 16–20, 2026 in Santiago, Chile, and had **not been published** as
of 2026-09-12. The 2025 edition (top 50 revealed at the Margaret River ceremony
on November 19, 2025; 51–100 pre-announced November 5, 2025) is therefore the
latest available.

## Interpretation notes

- **One row per vineyard.** `wine_region` follows the region names used in the
  official ranking announcements (e.g. "Millahue", "Hemel-en-Aarde",
  "Texas Hill Country").
- **Known_for** records the signature wines or grape varieties per the
  vineyard's own site or the 50 Best Discovery profiles — a one-phrase summary,
  not an exhaustive list.
- **Nearest_city** is the nearest notable city or town (judgment call where the
  vineyard sits in a hamlet, e.g. Waipara/Kofu used over smaller localities).
- All 100 `source_url` values were verified live (homepage fetched or confirmed
  via official-domain search results). Two were corrected to their live
  canonical domains during verification: Disznókő → disznoko.hu, and
  Château Héritage → http://www.chateauheritage.com (https does not respond).

## Known gaps and staleness

- **Sitio La Estocada (rank 91)** has no standalone winery homepage beyond
  sitiolaestocada.com (verified live and listed on the official 50 Best site);
  it is a small Uco Valley project of winemaker Matías Michelini.
- Wine-region and signature-wine data reflects sources current to ~September
  2026; vineyard experiences and wine lineups can change.
- The ranking celebrates wine *tourism* experiences (voted by 700+ wine and
  travel professionals), not wine quality alone — some legendary estates that
  do not welcome visitors are absent by design.

## Method

Ranks 1–50 taken from the official 50 Best PR Newswire release of November 19,
2025; ranks 51–100 from the official PR Newswire 51–100 PDF of November 5, 2025.
Six parallel research agents each covered an assigned region using web search
and page-text fetches: vineyard official sites for URLs and signature wines,
Decanter/Wine Spectator/reputable wine press as secondary. The coordinator
merged the six parts (100 rows, ranks 1–100 all present, zero duplicates on
name + wine_region) and sorted by wine region, then rank.
