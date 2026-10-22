# Private Charter Aviation Operators — Worldwide

**Compiled:** 2026-09-12 · **Total operators:** 56

A worldwide list of private charter aviation companies across three categories — jet, turboprop, and helicopter operators — with home bases, fleet notes, and handling agents at the home base where verifiable.

## Files

- `operators.csv` — the full list. Columns:
  `name, category, home_base_airport, home_base_icao, home_base_iata, home_base_city, country, region, fleet_note, official_website, key_people, contact_email, contact_phone, additional_bases, handling_agent, handling_agent_url, source_url`
  Sorted by category, then region, then name.

## Depth uplift — 2026-10-22

Brought to the catalog depth standard (named leadership, published contacts, official website, additional bases/footprint, handling agent at home base):

- **official_website: 55/56** (blank only for Alpine Airlines, whose source remains a third-party operator page).
- **handling_agent: 24/56** (up from 12), 20 with a handler URL. The 12 newly verified this pass: Jet Aviation at Zurich for Comlux; Lane Aviation (KCMH) for NetJets; Port City Air (KPSM) for PlaneSense; Cleveland Jet Center for Flexjet at KCGF (Flexjet's own VP of Operations is quoted on the FBO's site); Linz Airport Handling (General Aviation Terminal) for GlobeAir; the Luxembourg Airport Business Aviation Center for Luxaviation; Signature Flight Support at Geneva for TAG Aviation (Signature acquired TAG's Geneva FBO in 2020); Biggin Hill Executive Handling for Castle Air; Maverick Helicopters' own Las Vegas terminal; Federal Airlines' own private terminal at OR Tambo; Helijet's own heliport operations (Pacific Heliport Services); and the HCAA-licensed GA handlers at Athens (Goldair / Skyserv / Swissport Hellas) for GainJet.
- **key_people: 12/56** — the majors, verified against official leadership pages and company releases: NetJets (Adam Johnson; Patrick Gallagher), VistaJet (Thomas Flohr), Flexjet (Kenn Ricci; Michael Silvestro), Wheels Up (George Mattson; John Verkamp), Luxaviation (Patrick Hansen), ExecuJet Middle East (group), Comlux (Richard Gaona; Andrea Zanetto), TAG Aviation (Joanne Goodall), PlaneSense (George A. Antoniadis), Clay Lacy Aviation (Brian Kirkdoffer; Clay Lacy), Helijet (Danny Sitnam; Alistair Maclennan), Maverick Helicopters (Greg Rochna, founder).
- **Published contacts:** contact_phone 5/56, contact_email 1/56 (Jet Linx: info@jetlinx.com / +1 402-991-8060; VistaJet +1 833-853-8872; TAG Aviation +41 22 717 00 00; Maverick +1 702-261-0007; Comlux +41 44 205 50 70). Most charter operators publish enquiry forms rather than addresses/numbers; the columns stay in the schema and are filled only from the operator's own published details.
- **additional_bases: 9/56** (NetJets exclusive-use terminals; ExecuJet FBO network; Clay Lacy FBOs; Jet Linx terminals; VistaJet offices; Luxaviation FBO network; Comlux Completion Indianapolis + Dubai facility; Helijet BC stations; Flexjet London House).
- **Residual gaps:** key_people for 44 mostly small/regional operators (leadership not published in a verifiable official source at this pass); handling_agent for 32 rows where no official FBO/airport source ties a handler to the operator's home base; contact details for most rows (form-only publication).

## Coverage

- **Jet operators: 29** — NetJets and NetJets Europe, VistaJet, Flexjet, Wheels Up, Jet Linx Aviation, Clay Lacy Aviation, flyExclusive, Priester Aviation, TAG Aviation and TAG Aviation Asia, Luxaviation, Comlux, Elit'Avia, GainJet, Air Hamburg, GlobeAir, Royal Jet, Qatar Executive, ExecuJet Middle East, Falcon Aviation Services, Empire Aviation Group, Jetex, MJets, Sino Jet, Deer Jet, Metrojet, Líder Aviação (Brazil), Aerolíneas Ejecutivas (Mexico)
- **Turboprop operators: 14** — Tradewind Aviation, Cape Air, PlaneSense, Advanced Air, AirGO, ASL Group, Alpine Airlines, Air Chathams, Hardy Aviation, Susi Air, Federal Airlines, Mack Air, Scenic Air Safaris, Solenta Aviation
- **Helicopter operators: 13** — HeliFlite, BLADE, Helijet International, Maverick Helicopters, Heli Securite, Starspeed, Castle Air, Heli Air Monaco, The Helicopter Company (Saudi Arabia), Caverton Helicopters (Nigeria), Tropic Air Kenya, Microflite (Australia), Toho Air Service (Japan)

**Regional spread:** North America 15 · Europe 16 · Middle East 7 · Africa 6 · Asia-Pacific 10 · Latin America 2

## Handling agents

- **24 of 56 rows** carry a verified handling agent (12 at original build, +12 in the 2026-10-22 depth uplift); 20 of those also carry a verified handler website.
- Verified handlers include own-FBO arrangements (MJets Private Jet Terminal, Líder Aviação's FBO network, Clay Lacy's FBO at KVNY, Jet Center Los Angeles at KHHR, Royal Jet's FBO, Qatar Executive's Premium Terminal, ExecuJet FBO, Jetex FBO, HKBAC at Hong Kong, Air Hamburg's Executive Handling).
- **32 rows have no handling agent listed** — handler relationships at an operator's home base could not be verified from an official FBO or airport-directory source, and were left empty rather than guessed.

## Known gaps and judgment calls

- **Geography skews Western:** North America and Europe dominate. Mexico, the Caribbean, Central America, mainland Southeast Asia, India, and China had no operator meeting the "real, currently operating, verifiable base + official URL" bar in this pass — an optional follow-up.
- **Latin America is thin (2):** Líder Aviação (Brazil) and Aerolíneas Ejecutivas (Mexico).
- **Associated Aircraft Group was deliberately excluded:** acquired by Directional Aviation in 2022 and folded into Flexjet's helicopter division — it no longer exists as an independent operator.
- **Clay Lacy Aviation:** Solairus's acquisition of its charter/management divisions was announced August 2026 but had not closed as of compilation; retained with its current fleet figures.
- **Wheels Up:** the company describes its fleet as "floating" with no fixed home base; its operational HQ airport (KPDK) is listed as the base.
- **BLADE:** an asset-light platform; listed at its primary Manhattan heliport hub (KJRA/JRA) with a fleet note stating flights are operated by partner carriers.
- **Susi Air:** home base listed as Halim Perdanakusuma (WIHH/HLP), its principal operating base; corporate HQ is Pangandaran.
- **The Helicopter Company (Riyadh):** based at King Khalid Intl (OERK/RUH) — well-supported but partly inferential, not an explicit "home base at OERK" statement by the company.
- **AirGO (Mainz-Finthen)** and **Starspeed (Fairoaks)** have no IATA code; fields left blank rather than guessed.
- **Toho Air Service (Tokyo Heliport, RJTI)** has no IATA code; left blank.
- **Alpine Airlines'** source_url is its Alternative Airlines operator page — its own official website could not be verified in search results.
- Fleet figures are snapshots as reported in 2024–2026 sources and change as deliveries continue (e.g., Flexjet's 314-aircraft figure is from Nov 2025).

## Method

Four parallel regional research passes (North America; Europe; Middle East & Africa; Asia-Pacific & Latin America). Sources: operator official websites (base, fleet, category), airport/FBO directories and handler official sites (handling-agent verification), aviation press (AIN, ch-aviation, Business Wire releases) as cross-checks. Every row carries a real source URL; no invented operators, bases, fleets, or handlers.
