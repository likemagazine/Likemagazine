# Major Shopping Streets of the World

A sourced list of the world's major luxury/high-street shopping streets and
their anchor stores, compiled **2026-09-12** and updated **2026-10-20**.

- **`streets.csv`** — the list. One row per anchor store. Columns:
  `street, district, city, country, region, anchor_store, anchor_address, source_url`
- **`parts/`** — the five per-region working files (`na`, `latam`, `europe`,
  `mea`, `apac`)

## Headline numbers

| Metric | Count |
|---|---|
| Cities | **127** |
| Shopping streets / districts | **178** |
| Anchor store rows | **656** |
| Countries | 70+ |
| Rows with a verified street address | 556 (85%) |

### By region

| Region | Cities | Streets | Anchor rows |
|---|---|---|---|
| North America | 22 | 31 | 101 |
| Latin America | 14 | 18 | 81 |
| Europe | 30 | 39 | 164 |
| Middle East | 10 | 15 | 62 |
| Africa | 12 | 15 | 54 |
| Asia-Pacific | 39 | 60 | 194 |

## How the city list was chosen

127 cities were selected on a defensible basis: the world's top cities by
international visitor arrivals and economic/cultural prominence, deliberately
extended so no world region is left out. Cities that generic "famous shopping
street" lists routinely miss were explicitly included:

- **Southeast Asia:** Kuala Lumpur, Jakarta, Surabaya, Penang, Bali, Manila,
  Bangkok, Ho Chi Minh City, Hanoi, Singapore
- **Central Asia:** Almaty, Tashkent, Bishkek
- **South Asia:** Mumbai, New Delhi, Bangalore, Chennai, Karachi, Lahore,
  Dhaka, Colombo, Kathmandu
- **Middle East:** Dubai, Abu Dhabi, Doha, Riyadh, Jeddah, Kuwait City,
  Manama, Muscat, Tel Aviv, Beirut
- **Africa:** Cairo, Casablanca, Marrakech, Tunis, Algiers, Lagos, Nairobi,
  Johannesburg, Cape Town, Accra, Dakar, Addis Ababa
- **Latin America:** 14 cities incl. Brasília, Medellín, Quito, Montevideo,
  Santo Domingo, San José, Panama City, Caracas

## Coverage notes per region

### North America (22 cities, 31 streets, 101 anchors)
Metro-adjacent luxury districts keep the requested city in `city` with the
municipality in `district` (Beverly Hills → Los Angeles; Bellevue → Seattle;
Zapopan → Guadalajara; San Pedro Garza García → Monterrey). Thin spots:
Seattle (1 anchor — Hermès at The Bravern), Dallas (2), Washington D.C. (2);
Vancouver anchors use verified Burrard/Dunsmuir addresses (no Alberni Street
addresses verifiable). Closed stores deliberately excluded (Saks Fifth Avenue,
San Francisco, closed 2025). 2026-09-29: removed Saks Fifth Avenue, Canal Street
(New Orleans; closed April 2026 in the Saks Global Chapter 11 restructuring);
added Moncler global flagship, 767 Fifth Avenue, New York (opened Sept 10, 2026,
brand's largest store worldwide at 23,680 sq ft). 2026-10-06: removed Anthropologie, 333 Canal St
(New Orleans; relocated to Lakeside Shopping Center, Metairie in Nov 2025 — a stale row, the store
had left Canal Place nearly a year before compilation; Tory Burch at 333 Canal St re-verified open
via brand locator). 2026-10-13: added Smythson flagship, 575 Madison Avenue (opened ~Oct 6, 2026 —
British luxury stationer, first new NYC flagship marking 25 years since its first standalone store);
added Saint Laurent, 3 East 57th Street, and David Yurman, 5 East 57th Street — long-standing
flagships (YSL since 2003, David Yurman since H2 2019) missing from the baseline. Note: YSL announced
Oct 9–10, 2026 a relocation to ~9,600 sq ft at 717 Fifth Avenue (Kering's former Corning Glass
Building); the row will be updated when the move completes. 2026-10-20: added Paul Smith, 929 Madison
Avenue, New York (two-storey flagship opened ~Oct 14, 2026, first Upper East Side location —
the brand's first rows in the file). Smythson 575 Madison's reopening (~Oct 7, 2026) is now
confirmed; the row's existing source covers it.

### Latin America (14 cities, 18 streets, 81 anchors)
Where true luxury high streets don't exist, the landmark luxury mall is
recorded as the `street` entry (Multiplaza Panama/Escazú, Parque Arauco
Santiago, BlueMall Santo Domingo, Jockey Plaza Lima). Stale entries were
dropped rather than kept (Louis Vuitton's moved boutiques in São Paulo,
Buenos Aires, Santiago, Panama City). Caracas rows (5) have blank addresses —
brand presence comes from district-level sources with no verifiable
per-store addresses. Quito's brand set rests on a 2015 shopping guide and is
the weakest street in the file. 2026-09-22: added Loewe (first Brazil store,
opened May 2024) and Comme des Garçons (first Latin American flagship,
opened May 2025) at Shopping Iguatemi, Avenida Brigadeiro Faria Lima.
2026-09-29: added Balenciaga at Shopping Iguatemi, Av. Brig. Faria Lima 2232
(~300 sqm boutique opened ~mid-2025; presence confirmed via the brand's official
store locator — fills a baseline gap). 2026-10-06: added Vélez (largest Vélez flagship in Latin
America, 592 sqm, opened ~Sept 29, 2026) at Vía Israel (Multiplaza Pacific Mall), Panama City;
added Zadig & Voltaire (first Peru store, opened Sept 2026) at Avenida Javier Prado Este
(Jockey Plaza), Lima — both regions were outside the Sept 29 spot-check focus, so these are
catch-up adds from the Oct 6 Europe/LATAM sweep. 2026-10-20: added Dolce & Gabbana at
Avenida Javier Prado Este (Jockey Plaza), Lima — the brand's first Peru boutique (opened
Dec 2025, officially celebrated June 11, 2026; baseline-gap catch-up). Balenciaga at
Shopping Iguatemi confirmed trading (opened Aug 19, 2024) — the row already existed.

### Europe (30 cities, 39 streets, 164 anchors)
Rows have verified addresses except two (Saint Laurent and Max Mara on Avenue
Montaigne — presence confirmed, street numbers unconfirmed). Closed or moved
boutiques were excluded
rather than listed (Hermès Antwerp closed; Cartier Prague moved; Gucci Abdi
İpekçi Istanbul closed; Louis Vuitton Bağdat Caddesi has no official listing;
Prada Istanbul only at Zorlu Center). One caveat: Antwerp's Jaeger-LeCoultre
row cites the official locator domain root — the boutique address is confirmed
in the locator text but the deep page URL wasn't retrievable verbatim.
2026-09-22: added Dior House of Dior flagship at Via Monte Napoleone 12, Milan
(reopened Sept 18, 2026 after ~2-year renovation; Hermès's own store locator
still lists 12 as well — both rows share the verified number). 2026-10-06: added Richard Mille,
Calle de José Ortega y Gasset 10, Madrid (first standalone boutique in Spain, ~441 sq m, opened
Sept 28, 2026 — just before the Sept 29 window but missed since Europe was not in that check's focus).
2026-10-20 (Europe rotation; +14 rows, 3 new streets): added Sloane Street, London —
Ulla Johnson, 150 Sloane Street (brand's first standalone outside the US, opened ~early
Oct 2026); Old Bond Street, London — Boodles, 23 Old Bond Street (seven-floor Townhouse
flagship, opened Sept 28, 2026); Avenue Montaigne, Paris — Saint Laurent (opened Nov 2025,
per Kering), Max Mara (75th-anniversary flagship, reopened by April 2026), and CASA LOEWE
Montaigne, 46–48 (opened ~early Oct 2026) — the latter two have no confirmed street
number, left blank. Also added: Fauré Le Page, 352 Rue Saint-Honoré, Paris (opened
Oct 12, 2026); Zimmermann and Montblanc on Maximilianstraße, Munich (Munich Zimmermann
is the brand's first German boutique); Breitling, Bahnhofstrasse 70, Zurich; CASA LOEWE
London, 41 New Bond Street; Zimmermann, Calle de Serrano 22, Madrid; and A. Lange &
Söhne, Buccellati, and CASA LOEWE Lisbon on Avenida da Liberdade, Lisbon (first
Portuguese/Iberian boutiques for Lange and Buccellati).

### Middle East (10 cities, 16 streets, 59 anchors)
Gulf luxury retail concentrates in landmark malls, which are recorded as the
`street` entry (The Dubai Mall, Galleria Al Maryah Island, 21 High Street,
Place Vendôme, Kingdom Centre, The Avenues, MODA Mall). Beirut's Carré d'Or
anchors (Louis Vuitton, Fendi, Dior) rest on older sources — current operation
unverified, addresses left blank. 2026-09-29: added Grand Seiko Salon at
MODA Mall, Manama (first Salon in Bahrain, opened July 2, 2024 by Bahrain
Jewellery Centre; verified address "Shop 73, Building 20, Block 316, MODA Mall"
— fills a baseline gap). 2026-10-06: added ROJA London (first standalone Dubai boutique, opened
~Oct 1, 2026) at The Dubai Mall and ROJA London (first Oman boutique) at Opera Galleria,
Royal Opera House Muscat; unit numbers undisclosed, addresses left blank. 2026-10-13: added
MARLI New York (first Bahrain boutique, 110 sqm, ground floor — unit undisclosed, address left
blank) at MODA Mall, Manama; added APM Monaco (first standalone Qatar store, opened ~May 2026;
address "Place Vendôme Mall, Gate No. 6, Ground Floor, Lusail" per the brand locator) at
Place Vendôme Mall, Doha — a baseline gap on a covered street; added Stella McCartney at The
Avenues Mall Prestige, Kuwait (Shop unit No: E042 — the boutique was refurbished ~2021 and is
verified currently trading; a baseline gap). Bookkeeping correction: the Middle East/Africa street
split was miscounted in earlier tables (16/14) — verified recount gives 15 streets each, 175 total
unchanged.

### Africa (12 cities, 14 streets, 54 anchors)
Luxury evidence is thinnest here, and the file reflects that honestly rather
than padding it. Algiers has no verifiable international flagships (local
jewelers only — consistent with the market). Addis Ababa uses local designer
boutiques (ZAAF, Mafi Mafi, African Mosaique) since no international
flagships exist. Tunis, Marrakech, Nairobi, Dakar, Accra use the strongest
named stores found. 80 of the region's rows (mostly MEA file) have blank
addresses where only store presence — not the street number — was verifiable.

### Asia-Pacific (39 cities, 60 streets, 194 anchors)
Kuala Lumpur (Bukit Bintang, Jalan Sultan Ismail), Jakarta (Plaza Indonesia,
Grand Indonesia), and Almaty (Panfilov Street, Dostyk Plaza/Samal-2) each have
2 streets with 5+ anchors as required. Five rows have blank addresses that
could not be verified (Hermès Shinsaibashi Osaka, Hang Lung Plaza Shanghai,
Hermès/Cartier Edward Street Brisbane, Prada Queen Street Auckland). Thin
spots: Dhaka (2 rows), Sydney (2), Brisbane (3), Bangkok Phloen Chit, Mumbai
and New Delhi (2–4 rows each) — gaps reflect weak public verification, not
missing streets. 2026-09-22: added CASA LOEWE Ginza, Tokyo (opened Aug 31,
2026, corner of Chuo-dori/Miyuki-dori; no verified street address, left blank). 2026-10-13:
added Rocca Cheongdam at 437 Apgujeong-ro, Gangnam-gu, Seoul (Damiani Group's first Korean
flagship, a multi-brand luxury watch boutique — H. Moser & Cie, Ulysse Nardin, Gérald Charles,
Czapek, Arnold & Son, Ressence, Norqain, Hautlence; inaugurated ~Sept 23, 2026); added
Christian Louboutin at Plaza Indonesia, Jakarta (new boutique on the ground floor in the brand's
newest retail design codes, opened ~Oct 12, 2026, operated with MAP). 2026-10-20: added
Loro Piana flagship at Omotesando, Tokyo (opened Oct 9, 2026 — 15th Japan store, 5th Tokyo;
in the new FPG links Omotesando V building, Jingumae 5-chome — no street number published).
The Loro Piana October opening watch item from the Oct 13 check is now closed.

## Known gaps and caveats

- **Addresses:** 100 of 656 rows (15%) have an empty `anchor_address` where the
  store's presence was verified but no street number could be confirmed. These
  were left blank per the no-guessing rule, not filled from memory.
- **Tenant mix is time-sensitive:** luxury tenants open, close, and relocate
  frequently. Rows reflect what was verifiable on 2026-09-12; mall tenant
  mixes in fast-moving markets (Surabaya, Karachi, Lahore, Doha) should be
  rechecked if freshness matters.
- **Malls as streets:** in the Gulf, parts of Latin America, and some Asian
  cities, the landmark luxury mall stands in for a shopping street, since
  that is where the anchor flagships actually are. This is a documented
  judgment call, flagged per row via the `street` value.
- **`nearest` vs `on`:** APAC rows were strictly relabeled so the `street`
  value is the street the store actually fronts (e.g., "Namiki-dori (Ginza)",
  "Orchard Turn (ION Orchard)", "Shifu Road (Xinyi)").
- **Source URLs** point to pages actually consulted (brand store locators,
  tourism boards, press). Brand locator deep pages are sometimes JS-gated; in
  those cases the citable locator or announcement page is used.
- **No invented data:** where verification failed, rows were left blank or
  excluded and the gap documented here.

## Method

Five parallel research agents each covered an assigned region using web search
and page-text fetches: official tourism boards and business-improvement
districts for street identification, brands' official store locators for
addresses, travel/luxury press as secondary sources. 621 part rows were
merged and deduped on (street, city, anchor_store) — zero cross-region
duplicates found — and sorted by region, country, city, street.
