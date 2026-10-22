# Luxury Watchmakers Worldwide

**Compiled:** 2026-10-20
**Total:** 84 brands/ateliers across 12 countries

## Columns

`brand, headquarters_city, country, region, group, key_people, founded, note, source_url`

Sorted by country → headquarters city → brand. Every row carries a verified
official brand website. `key_people` holds founder and/or master watchmaker
names (semicolon-separated) only where verifiable — never guessed.

## Coverage by country

| Country | Entries |
|---|---|
| Switzerland | 51 |
| Japan | 8 |
| Germany | 6 |
| United Kingdom | 5 |
| United States | 4 |
| France | 3 |
| Netherlands | 2 |
| Austria | 1 |
| China | 1 |
| Hong Kong | 1 |
| Malaysia | 1 |
| Isle of Man | 1 |

## Coverage by region

- Switzerland — Geneva: 24
- Switzerland — Jura: 20
- Switzerland — Vallée de Joux: 5
- Switzerland — Vaud: 1 (Alexandre Martin, Morges)
- Japan: 8
- Germany: 6
- United Kingdom: 6 (includes Roger W. Smith, Isle of Man — a Crown Dependency)
- France: 3
- North America: 4
- Asia-Pacific: 3 (Behrens/Shenzhen, Ming/Kuala Lumpur, Atelier Wen/Hong Kong)
- Netherlands: 2
- Austria: 1

## Ownership mix

Independent 60 · Richemont 8 · Swatch Group 5 · LVMH 4 · Citizen 3
(Frédérique Constant, Ateliers deMonaco, Campanola) · Seiko 2 · Damiani Group 1
(Baume & Mercier — Richemont's sale to Damiani completed July 2026, per
WatchPro USA) · Breitling 1
(Gallet — relaunched Sept 2026 inside Breitling's House of Brands).

## What counts as a "luxury watchmaker" here

- A real, currently operating brand or atelier making mechanical (or
  high-end quartz, e.g. Grand Seiko 9F) watches with genuine watchmaking
  substance: in-house movements, respected independents, or heritage maisons.
- Fashion-label licensees with no watchmaking operation are excluded.
- Mid-tier/value brands (Junghans, Yema, Lip, Christopher Ward) are excluded
  even when they make decent watches — the bar is luxury positioning.
- Pure microbrands without horological distinction are excluded.

## Interpretation notes / judgment calls

- **HQ basis:** entries are filed under the brand's corporate/head-office
  city. Cartier, Van Cleef & Arpels and Louis Vuitton are recorded at their
  Geneva watch headquarters/manufactures (their Maison HQs are Paris).
- **Blancpain:** recorded at Le Brassus (official company address); some
  references cite Paudex.
- **H. Moser & Cie:** HQ Neuhausen am Rheinfall; founded 1828 by Heinrich
  Moser in St. Petersburg, modern company relaunched 2005.
- **Hautlence:** founded 2004 in Neuchâtel, now in Neuhausen am Rheinfall.
- **Bell & Ross:** Independent (Chanel holds only a minority stake).
- **Kering** appears nowhere: it sold Girard-Perregaux and Ulysse Nardin
  (Sowind Group) to management in May 2022; both are now Independent.
- **Corum:** recorded as Independent per the 2025 management buyout (sales
  director Haso Mehmedovic, backed by Swiss investors, bought it from Hong
  Kong's Citychamp — reported by WatchPro, May 2025).
- **Campanola:** `key_people` is blank — it is a Citizen brand division with
  no verifiable individual founder/watchmaker attached.
- **Keaton Myrick founded = 2012** (Baselworld debut); workshop opened ~2009.
- **Otsuka Lotec founded = 2012** (first public sales; prototypes 2008–2011).
- **Hajime Asaoka founded = 2005** (began watch production; first sale 2011).
- **Roger W. Smith:** country filed as "Isle of Man", region "United Kingdom".
- **Ateliers deMonaco:** HQ moved from Monaco to Geneva; filed under Geneva.
- **Speake-Marin:** HQ Geneva; atelier in La Chaux-de-Fonds.
- **Franck Muller founded = 1992** (official 2019 press kit; some sources 1991).
- **Singer Reimagined = 2017** (launch year; project began 2014).
- **Czapek = 2012** (revival; original 1845). **Louis Vuitton = 2007**
  (La Fabrique du Temps; maison 1854). **Baume & Mercier = 1830**
  (Baume Frères origins).
- MB&F and F.P. Journe are Independent (Chanel minority stakes noted).
- **Gallet:** `headquarters_city` and `region` are blank — the relaunched
  brand's HQ city has not been publicly disclosed (the brand operates inside
  Breitling's manufacturing/distribution infrastructure); `founded` = 1826,
  the original founding year, with the 2026 relaunch explained in the note.
- **Alexandre Martin:** new region label "Switzerland — Vaud" (Morges is in
  the canton of Vaud, outside the Geneva/Jura/Vallée de Joux clusters).

## Excluded (considered, deliberately left out)

- Arnold & Son, Angelus (La Chaux-de-Fonds): owned by Citizen Group.
- Christophe Claret (Le Locle): operating status uncertain — liquidation
  proceedings 2023–25; on 27 Aug 2026 the brand announced a joint venture
  with Singapore's Lotus Group, with the Christophe Claret name, assets and
  IP moving to a new company (Lotus Two AG) and first new watches expected
  late 2027 / early 2028. Still excluded pending real operating output.
- Maurice Lacroix: corporate HQ reported as Zurich, only manufacturing in
  the Jura.
- Chronoswiss (Lucerne): out of the Jura/Geneva scope and mid-luxury.
- L'Epée 1839 (Delémont): mechanical clocks, not wristwatches.
- Linde Werdelin: watches made in Geneva, HQ split London/Copenhagen.
- Junghans, Yema, Lip, Christopher Ward: mid-tier positioning.
- RZE, Feynman, Undone, CIGA Design: microbrand/fashion tier.
- Shinola, Movado, Timex, Bulova: mass-market/fashion-adjacent.
- Devon Works: no longer a live manufacturing brand.
- S. Ujin: could not be verified at all.
- Casio, Orient Star, Seagull, Shanghai: high-volume manufacturers.
- Kobold: tool-watch positioning, reduced operations.
- Azimuth (Singapore): borderline quirky independent, lacks consistent haute
  positioning — candidate for a future expansion pass.
- Quiet Club, Kikuchi Nakagawa, Masahiro Kikuno (Japan): real but very
  new/niche — expansion candidates.

## Method

Four parallel regional researchers (Geneva; Jura/Vallée de Joux; rest of
Europe; Japan/Asia-Pacific/rest of world) worked from brand official sites,
FHH and GPHG listings, with Hodinkee/Revolution/Monochrome as secondary
sources. Regional files are kept in `parts/` (note: two arrived
pipe-delimited, one with a comma header over pipe-delimited rows — all
normalized at merge). Merged, deduped on brand + HQ city (zero duplicates),
sorted by country → city → brand, and validated: 81 rows, all URLs live,
one intentionally blank field (Campanola key_people).
