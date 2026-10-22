# World's Best Airlines — Skytrax Top 100, Organized by Hub

A sourced list of the Skytrax World's Top 100 Airlines, one row per airline on its
primary hub airport, compiled **2026-09-22**.

- **`airlines.csv`** — the list, sorted alphabetically by hub ICAO code. Columns:
  `name, skytrax_rank, hub_airport, hub_city, hub_country, hub_region, hub_icao, hub_iata, other_hubs, classes, callsign, alliance, source_url`
  - `classes` is a semicolon-separated subset of `First;Business;Premium Economy;Economy`
    (classes actually offered fleet-wide; availability varies by aircraft and route).
  - `callsign` is the airline's ICAO telephony (spoken ATC) callsign, e.g. `SPEEDBIRD`.
  - `alliance` is the airline's membership in one of the three global alliances
    (Star Alliance, oneworld, SkyTeam); empty when the airline is in none. Air
    Canada rouge is a Star Alliance affiliate member of Air Canada.
  - `source_url` on every row is a page actually consulted (usually the airline's
    Wikipedia article, which cites official sources).
- **`parts/`** — the four per-region working files (rebuilt with each edition).
- **`CHANGES.md`** — dated log of edition changes since the 2025 baseline.

## Headline numbers

| Metric | Count |
|---|---|
| Airlines (Skytrax Top 100) | **100** |
| Skytrax edition | **2026** (announced September 21, 2026, London) |
| Hub countries | 51 |
| Airlines offering First Class | 23 |
| Airlines with all four classes | 16 |
| In Star Alliance | 20 (+1 affiliate: Air Canada rouge) |
| In oneworld | 14 |
| In SkyTeam | 11 |
| In no alliance | 54 |

### Rank highlights

1. Singapore Airlines · 2. Qatar Airways · 3. Cathay Pacific · 4. ANA All
Nippon Airways · 5. Turkish Airlines · 6. Emirates · 7. Air France ·
8. Hainan Airlines · 9. Japan Airlines · 10. Korean Air

## The 2026 edition

The Skytrax World Airline Awards 2026 Top 100 was announced at a ceremony in
London on **September 21, 2026** — just nine days after the previous
2025-based check, so this list is a full rebuild rather than a maintenance
pass. The 2026 awards are based on an online passenger survey conducted
September 2025 – August 2026, covering 325+ airlines with travellers from over
100 nationalities (source: official results page,
worldairlineawards.com/worlds-top-100-airlines-2026).

- **New #1:** Singapore Airlines returns to the top, trading places with 2025
  winner Qatar Airways (now #2).
- **New entries (5):** Pegasus Airlines (95, from 104 in 2025), LEVEL (96, from
  118), Discover Airlines (97, from 117), Royal Jordanian Airlines (98, from
  132), Sun PhuQuoc Airways (99, from 156 — the Vietnamese resort airline
  launched November 2025 is the first new-generation startup to crack the Top
  100 in years).
- **Dropouts (5):** Asiana Airlines (41 in 2025 — exits Star Alliance on
  December 16, 2026, when it is absorbed into Korean Air), China Eastern
  Airlines (98), Air Serbia (99 — entered the Top 100 only in 2025), Jetstar
  Asia (93 — ceased operations July 31, 2025), Hawaiian Airlines (100 —
  operated its final independent flight October 29, 2025 and is integrated
  into Alaska Airlines).
- **Biggest climbers:** Air India +27 (84→57), Egyptair +22 (68→46 — also
  named World's Most Improved Airline), American Airlines +18 (83→65),
  Porter Airlines +10 (44→34), Thai Airways +9 (29→20).
- **Biggest fallers:** Gulf Air −40 (35→75), IndiGo −22 (39→61), Garuda
  Indonesia −20 (46→66), Oman Air −12 (48→60).
- **Alliance changes in this edition:** Asiana (Star Alliance) leaves the
  list entirely; China Eastern (SkyTeam) drops out; Royal Jordanian returns to
  the Top 100 as a oneworld member; Discover Airlines enters as a non-member
  (Lufthansa leisure subsidiary, like Eurowings). Net counts: Star 21→20,
  oneworld 14→14, SkyTeam 12→11, no-alliance 52→54. Asiana Airlines is still
  formally a Star Alliance member until December 16, 2026, but it is no longer
  on the Top 100 list.
- **Name updates** to match Skytrax's 2026 official naming: "SAS Scandinavian"
  (was "SAS Scandinavian Airlines"), "LOT Polish" (was "LOT Polish
  Airlines"), "Azul Brazilian" (was "Azul Brazilian Airlines").

## Interpretation notes

- **One row per airline on its primary hub.** Multi-hub carriers list secondary
  hubs in `other_hubs`. Judgment calls: Air Canada → Toronto Pearson; Lufthansa
  → Frankfurt (Munich secondary); Air France → Paris-CDG; British Airways →
  Heathrow; Qantas → Sydney; ANA/JAL → Tokyo Haneda; SAS → Copenhagen;
  Discover Airlines → Frankfurt (Munich secondary).
- **Low-cost carriers with no formal hub** use their largest operational base
  (e.g. Ryanair → Dublin, easyJet → London Gatwick, Volotea → Nantes, Breeze →
  Charleston; Pegasus Airlines → Istanbul Sabiha Gökçen).
- **Callsigns** were verified against Wikipedia infoboxes and cross-checked
  across multiple language editions. New entries: Pegasus Airlines = `SUNTURK`,
  LEVEL = `DALI`, Discover Airlines = `OCEAN`, Royal Jordanian = `JORDANIAN`.
- **Classes** record cabins actually offered fleet-wide. Edge cases: Alaska's
  "Premium Class" is extra-legroom economy (not counted); ScootPlus is a bundled
  LCC product (not counted); Oman Air no longer sells First despite 787s with
  former First seats (recorded as Business;Economy); AirAsia/AirAsia X's Premium
  Flatbed is phasing out and is not one of the four classes. New entries:
  LEVEL = Premium Economy;Economy; Discover Airlines = Business;Premium
  Economy;Economy (long-haul fleet); Royal Jordanian = Business;Economy;
  Pegasus and Sun PhuQuoc = Economy only.
- **Alliances** verified 2026-09-22 against oneworld/Star Alliance/SkyTeam
  announcements and member lists. No alliance membership changes among listed
  airlines since the previous check (2026-09-12). Subsidiaries that are not
  alliance members themselves (Eurowings, Discover Airlines, Air Dolomiti,
  Iberia Express, Vueling, Scoot, Jetstar, QantasLink, HK Express, Transavia,
  SunExpress, LEVEL) are recorded as no alliance, even where the parent airline
  is a member.

## Known gaps and staleness

- **Sun PhuQuoc Airways (rank 99):** no ICAO telephony callsign could be
  verified from reputable sources for the new startup — the field is left empty
  rather than guessed.
- **Sun Country (rank 82)** was acquired by Allegiant Travel Company on May 13,
  2026 and still operates independently pending a single operating certificate.
- **Azerbaijan Airlines (rank 41)** is filed under Central Asia, per Skytrax's
  historical classification.
- Hub/fleet data reflects sources current to ~mid-2026; cabins and hubs can
  change with fleet renewal.

## Method

Four per-region working files (parts/) cover the world; for this rebuild, all
100 rows were re-verified against the official Skytrax 2026 Top 100 page
(worldairlineawards.com), then Wikipedia airline articles (which cite official
sources) for the five new entrants' hubs, callsigns, fleets, and alliances,
cross-checking callsigns where possible. Ranks 1–100 all present, zero
duplicates, sorted by hub ICAO code.
