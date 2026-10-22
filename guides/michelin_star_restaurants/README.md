# Michelin Starred Restaurants — Worldwide

A sourced list of every restaurant in the world currently holding at least one
Michelin star (1, 2, or 3 stars), compiled **2026-10-14**.

- **`michelin_stars.csv`** — the list. Columns: `name, stars, city, country, guide_region, source_url`
- **`parts/`** — the seven per-region working files plus their build scripts
- **`work/`** — build scripts and research notes

## Headline numbers

| Metric | Count |
|---|---|
| Starred restaurants (total) | **3,640** |
| 1-star | 2,964 |
| 2-star | 513 |
| 3-star | 163 |
| Guides covered | 55 |

### Top countries by starred restaurants

1. France — 659
2. Italy — 394
3. Germany — 339
4. Spain — 306
5. United States — 280
6. Japan — 277
7. United Kingdom — 205
8. China — 158
9. Netherlands — 119
10. Austria — 101
11. Hong Kong — 77
12. Taiwan — 61
13. Portugal — 53
14. South Korea — 46
15. Singapore — 45

*(Jersey, Guernsey and the Faroe Islands are recorded as their own `country` values;
Hong Kong and Macau are split by city.)*

### Notable firsts in this edition
- **First 3-star restaurants in Latin America**: Evvai and Tuju (São Paulo, Brazil).
- **First 2-star restaurant in Vancouver**: AnnaLena (promoted Oct 2, 2026).
- **Michelin's first Oceania guide**: New Zealand 2026 (15 starred; Essence, Queenstown 2★; announced Jul 2026, missed by the original build, added 2026-09-15).
- **Mexico 2026** lost its famous taco-stand star — El Califa de León is no longer starred.

## Coverage notes per guide (edition used)

### Europe — France & Iberia
- MICHELIN Guide France — **2026** (659 restaurants, incl. ceremony Mar 2026). Monaco split out separately below.
- MICHELIN Guide France & Monaco — **2026**: 9 restaurants (1×3★, 3×2★, 5×1★; new stars: Elsa Marcel Ravin, Robuchon Monaco). *Discrepancy:* Monaco Life reported "10 starred restaurants" after the ceremony, but Wikipedia's 2026 table (citing guide.michelin.com) supports 9; Yoshi lost its star and Le Vistamar is closed.
- MICHELIN Guide Spain — **2026** (306; gala 25 Nov 2025, Málaga). Andorra's one star (Ibaya, Soldeu) filed under "MICHELIN Guide Spain & Andorra".
- MICHELIN Guide Portugal — **2026** (53).

### Europe — West
- MICHELIN Guide Italy — **2026** (394; matches official totals)
- MICHELIN Guide Germany — **2026** (339; matches official)
- MICHELIN Guide Austria — **2026** (101; matches official)
- MICHELIN Guide Netherlands — **2026** (119: 1×3★ De Librije (Zwolle), 20×2★, 98×1★; ceremony Oct 5, 2026 at MECC Maastricht). New stars: Azurite (Delft) and SUIS (Schin op Geul) awarded 2★ on debut (both newly opened); new 1★: Nassau (Groningen), Wild Atelier (Hoog Soeren), Rozewied (Kortgene), Bij Sidney (Loenen aan de Vecht), De Cuijt (Mierlo), Ambrozijn (Valkenburg), Le Epifaan (Veeningen). Lost stars: Daalder, De Juwelier (Amsterdam), Demain (Cadzand-Bad), De Woage (Gramsbergen), Flicka (Kerkdriel), Da Vinci (Maasbracht), Sense (Vught); 2★ closures Spectrum (Amsterdam) and De Groene Lantaarn (Staphorst). Le Epifaan is chef Jarno Eggen's new restaurant in Veeningen after closing De Groene Lantaarn.
- MICHELIN Guide Belgium & Luxembourg — **2026**: **partial — 25 rows** (Luxembourg 12 complete; Belgium 13 verified: retained 3-stars Zilte & Boury, new 2-stars Cuines 33 & The Jane, 9 new 1-stars. The retained 18×2★ and 96×1★ could not be individually verified against a complete public 2026 list → ~114 Belgium restaurants missing. See gap.)
- MICHELIN Guide Switzerland — **2025** (no 2026 announced): **partial — 25 rows** verified (4 retained 3-stars, 3 new 2-stars, 18 new 1-stars). ~120 retained 2★/1★ unverifiable from public sources → see gap.

### Europe — North & East
- MICHELIN Guide Great Britain & Ireland — **2026** (230: 192/28/10, incl. Crown Dependencies Jersey — Bohemia — and Guernsey — Vraic)
- MICHELIN Guide Nordic Countries — **2026** (99: Denmark 41, Norway 23, Sweden 23, Finland 8, Iceland 3, Faroe Islands 1)
- MICHELIN Guide Türkiye — **2026** (17: 15×1★, 2×2★)
- MICHELIN Guide Croatia — **2026** (14)
- MICHELIN Guide Athens — **carried forward from 2024** (12). The 2026 selection (Athens/Thessaloniki/Santorini) was announced for H2 2026 but not yet unveiled as of 2026-09-12.
- MICHELIN Guide Poland — **2026** (11)
- MICHELIN Guide Hungary — **2025** (10; no 2026 announcement found)
- MICHELIN Guide Slovenia — **2026** (10, incl. 3-star Hiša Franko)
- MICHELIN Guide Czech Republic — **2026** (9)
- MICHELIN Guide Belgrade — **2026** (2)

### Asia — Pacific
- MICHELIN Guide Tokyo — **2026**: **partial — 76 rows** (12×3★ and 26×2★ complete; only 38 of 122 one-stars individually verified — see gap)
- MICHELIN Guide Kyoto & Osaka — **2026** (179)
- MICHELIN Guide Nara — **2026** (22)
- MICHELIN Guide Hong Kong & Macau — **2026** (98)
- MICHELIN Guide Singapore — **2026** (45; released 4 Aug 2026)
- MICHELIN Guide Taiwan — **2026** (61; includes expanded New Taipei/Hsinchu coverage)
- MICHELIN Guide Seoul & Busan — **2026** (46)
- MICHELIN Guide Thailand — **2026** (43)

### Asia — China & Southeast Asia
- MICHELIN Guide Shanghai | Jiangsu | Zhejiang — **2026** (77)
- MICHELIN Guide Beijing — **2026** (32; one ambiguity — see caveats)
- MICHELIN Guide Guangzhou & Shenzhen — **2026** (27)
- MICHELIN Guide Chengdu — **2027** (15; announced 3 Sep 2026: Xin Rong Ji promoted to 3★)
- MICHELIN Guide Fujian — **2026** (7×1★: Fuzhou — Jiangnan Wok ‧ Rong, Wenru No.9, Hatter; Xiamen — Fleurs Et Festin, Hokklo, Yanyu (Jiahe Road); Quanzhou — Qing You Yu. Second edition announced 25 Nov 2025, covers Fuzhou/Xiamen/Quanzhou/Ningde. Missed by the original Sep 12 build like New Zealand; added to the list 2026-10-13.)
- MICHELIN Guide Hanoi | Ho Chi Minh City | Da Nang — **2026** (11)
- MICHELIN Guide Kuala Lumpur & Penang — **2026** (9)
- MICHELIN Guide Manila and Environs & Cebu — **2026** (9)

### North America
- MICHELIN Guide California — **2026** (83); Florida — **2026** (26); Southwest — **2026** (5); Québec — **2026** (13)
- MICHELIN Guide Northeast Cities — **2025** (118: NYC 72, Chicago 20, DC 22, Boston 1, Philadelphia 3). *DC note:* 3 of the 25 announced stars have since permanently closed (Kinship, Métier, Tail Up Goat) and are excluded; Gravitas (1★) is included but flagged — it closed Jan 2026 over unpaid taxes and its status should be rechecked.
- MICHELIN Guide American South — **2025** (19; 2026 ceremony in Nashville, Oct 2026)
- MICHELIN Guide Texas — **2026** (19; digital reveal Oct 8, 2026: new 1★ Fabrik & Kappo Kappo (Austin), Goldee's Bar-B-Q (Fort Worth, city's first star). Olamaie closed Jul 2026; la Barbecue lost its star but remains recommended.)
- MICHELIN Guide Colorado — **2026** (10; announced Sep 14, 2026: new 1★ Milpero (Denver); all nine 2025 stars retained, The Wolf's Tailor stays 2★. First statewide selection — previously Denver/Boulder/Aspen/Vail/Beaver Creek only.)
- MICHELIN Guide Toronto — **2026** (15: 1×2★ Restaurant Pearl Morissette, 14×1★; ceremony Sep 22, 2026. Aburi Hana lost its only star after reopening Sep 17 under a new chef/concept; Hexxagon (Oakville) closed earlier in 2026 and is excluded; no new stars awarded. Sushi Masaki Saito remains 1★ — its 2→1 demotion dated from the 2025 edition. The Pine now filed under Creemore.)
- MICHELIN Guide Vancouver — **2026** (11: 1×2★ AnnaLena (promoted from 1★ — the city's first 2-star restaurant), 10×1★; ceremony Oct 2, 2026. Barbara demoted from 1★ to Recommended; no other new stars awarded.)

### Latin America & Middle East
- MICHELIN Guide Mexico — **2026** (29: 27×1★, 2×2★ Pujol/Quintonil; expanded to Jalisco, Puebla, Yucatán; El Califa de León lost its star)
- MICHELIN Guide Rio de Janeiro & São Paulo — **2026** (24; 2×3★ — Evvai, Tuju — Latin America's first; Huto lost its star)
- MICHELIN Guide Buenos Aires & Mendoza — **2026** (14; revealed Jul 2026). **Warning:** Argentina's national government cut guide funding Apr 2026; BA/Mendoza funded this edition as a stopgap — the guide's future there is uncertain.
- MICHELIN Guide Dubai — **2026** (20: 2×3★, 4×2★, 14×1★; ceremony Oct 6, 2026 at Atlantis The Royal. Orfali Bros promoted 1→2★; new 1★ Birch and KIGO; La Dame de Pic Dubai lost its star.)
- MICHELIN Guide Abu Dhabi — **2026** (3)
- MICHELIN Guide Doha — **2026** (3)

### Oceania
- MICHELIN Guide New Zealand — **2026** (15: 1×2★ Essence (Queenstown), 14×1★ across Auckland, Wellington, Christchurch and Queenstown). Inaugural edition — Michelin's first guide in Oceania — announced 1–2 Jul 2026. Missed by the original Sep 12 build; added to the list 2026-09-15.
- MICHELIN Guide South Australia — **2027** (11: 1×2★ Magill Estate Restaurant (Magill), 10×1★ across Adelaide, the Adelaide Hills, Barossa, Clare Valley and McLaren Vale). Inaugural edition — Michelin's first-ever Australian guide — revealed 14 Oct 2026 at the Adelaide Convention Centre. Added to the list 2026-10-14.

## Known gaps (incompleteness, not guesses)

| Gap | Size |
|---|---|
| Tokyo one-stars unverifiable from public sources (~84 of 122) | ~84 rows missing |
| Switzerland retained 2★/1★ not individually verifiable (2025) | ~120 rows missing |
| Belgium retained 2★/1★ not individually verifiable (2026) | ~114 rows missing |
| Greece: 2026 selection not yet announced → carried forward 2024 | 12 rows possibly stale |
| Hungary: 2026 not announced → 2025 data | 10 rows possibly stale |
| Switzerland: 2025 is latest | 2026 not announced |
| Northeast Cities, American South, Philippines: on older editions | 2026/2027 selections pending (American South Nashville ceremony Oct 21; Philippines 2027 ceremony Oct 29; Northeast Cities 2026 — Dec 14, NYC) |
| Fujian 2026 | Entire guide previously missing from the list — added 2026-10-13 (7 rows, official press release) |
| Beijing: two sources disagree on whether "Forum" held a 2025 1★ — excluded; recheck against official list | 1 row ambiguous |

### Regions with no Michelin guide (zero rows, verified absent)
- **Saudi Arabia** (Riyadh/Jeddah/AlUla): inaugural 2026 guide awarded **no stars** — stars begin with the 2027 edition
- **Bahrain**: no guide exists
- **Tel Aviv**: announced but no selection ever published
- **Peru (Lima)**: no guide exists or announced
- **Indonesia (Bali)**: no restaurant guide (Michelin Keys hotel awards are separate)
- **Malaysia/Johor**: guide covers only Kuala Lumpur & Penang
- **American Great Lakes & South Australia**: upcoming inaugural 2027 guides — no selections yet

## Caveats & transcription notes
- `source_url` on every row is a page actually consulted (usually a Wikipedia regional
  list citing Michelin's official announcement, or a full-list press announcement).
  guide.michelin.com restaurant pages are JS-heavy and not individually fetchable by
  research agents, so official restaurant-page URLs could not be attached per row.
- Spelling notes from extraction: `La Table de Xaxier Mathieu` (France; likely
  source typo for "Xavier"); Portugal `Marlene` (source rendered `Marlene,`);
  `Kokoxta` per Wikipedia (real-world name Kokotxa); some Jiangsu/Zhejiang names are
  transliterations (Kelong No. 1, Lao Bian Restaurant, Dingshan Jiangyan,
  Pingjiangsong, Xi Ding Jia Yan, Cheng Yuan, Jiangnan Wok · Yun); some Taiwan names
  retain Chinese subtitles.
- Two distinct Italian restaurants named "San Martino" (Treviglio and Scorzè) are both
  legitimate; same-named restaurants in different French cities (Apicius, L'Essentiel,
  L'Orangerie) are likewise distinct rows. Dedupe key: (name, city, country).
- Fujian names transcribed verbatim from the official 2026 press release, including
  `Jiangnan Wok ‧ Rong` (Fuzhou) and `Yanyu (Jiahe Road)` (Xiamen); the branch
  parenthetical is kept to disambiguate the Xiamen restaurant.

## Method
Eight parallel research agents each covered an assigned set of guides using web
search and page-text fetches: official guide.michelin.com announcement pages first
(JA/JS rendering limited per-restaurant pages), then Wikipedia's per-region
"List of Michelin-starred restaurants" tables (which cite the official
announcements), cross-checked against official star totals and food-press
announcements. Monaco and Andorra (covered under the France and Spain guides)
were added by the coordinator. Final merge: 3,596 part rows + 10 coordinator
additions = **3,606**; zero cross-region duplicates found.
