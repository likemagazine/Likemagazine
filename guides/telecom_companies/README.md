# Major Telecom Companies Worldwide

**52 companies across 2 categories, as of October 2026.**

- Network operators: 40
- Network equipment & infrastructure: 12

## Files

- `telecom_companies.csv` — the master list (52 rows x 15 columns)
- `telecom_companies.pdf` — formatted PDF with clickable website links
- `work/` — intermediate category part files

## Coverage (of 52 rows)

- Websites: 52 (100%)
- Founded / history: 52 (100%)
- Key people (CEO/chairman): 52 (100%)
- Subscribers / revenue figures: 52 (100%)
- Specialties: 52 (100%)
- Ownership: 52 (100%)
- HQ phones: 2
- Published contact emails: 2

## Methodology and rules

- Official published sources only: company websites, annual reports, official press releases, stock-exchange filings (e.g., HKEX). Secondary outlets (Caixin, Light Reading, RCR Wireless) used only as leads where noted, or with explicit caveats in `notes`.
- Ranking backbone: the **24th Forbes Global 2000, 2026 edition (published ~June 2026)** used as a selection aid. The full public telecom ordering was never exposed, so no Forbes ordering is claimed — the CSV carries company-published operating figures (FY2025/FY2026 revenue, subscriber counts with year), not Forbes figures.
- **Blank beats guessed.** Where no official phone or general email could be verified, the field is left blank and the gap is documented in `notes`.
- Region is HQ-based, using five broad regions (North America, Latin America, Europe, Middle East & Africa, Asia-Pacific). Where a company's operating footprint differs markedly from its HQ (Millicom, VEON), the footprint is noted in `notes`.
- Every row has a `history` field: a concise founding story/milestones drawn from official materials, except where noted.

## Systematic gaps (honest limitations)

1. **HQ phones and general emails are near-nonexistent industry-wide (2/52 each).** Telecom giants route all contact through web forms, country-level support lines, or investor-relations portals. The two published contacts are Telkom Indonesia's published IR phone and email, and Ericsson's published media-relations line and email.
2. **CEO figures verified as of September 2026**, but leadership turns over — the Tuesday watch tracks changes. Notable: China Mobile's vacant CEO seat was filled — Chen Yangfan appointed Executive Director and CEO on Jun 16, 2026 (company announcement 2026-014); Ericsson CEO succession completed Oct 1, 2026 — Per Narvinger now President & CEO, Börje Ekholm stays as executive adviser until Jun 15, 2027.
3. **Ownership figures marked "(verify)" in-row** where they rest on widely reported but not directly extracted official data (e.g., stc/PIF, e&/UAE government, Ooredoo/Qatar, Turkcell/TWF, Singtel/Temasek, Telkom/Indonesian state).
4. **Samsung Networks does not break out standalone network revenue**; NEC and Samsung disclose network revenue only within broader segments (noted in rows).
5. **Subscriber/revenue figures mix FY2025 and FY2026** depending on each company's reporting calendar; every figure carries its year.

## Major consolidations captured (2025–2026)

- Vodafone UK–Three UK merger completed **31 May 2025**: combined business named **VodafoneThree** (51% Vodafone, 49% CK Hutchison), CEO Max Taylor; £11bn network investment.
- Orange completed acquisition of the remaining 50% of **MasOrange** from Lorca for €4.25bn on **8 June 2026** (full ownership); MasOrange corporate brand retired Sept 2026, reverted to Orange Spain.
- Verizon/Frontier closed **20 Jan 2026**; T-Mobile/UScellular closed **1 Aug 2025** (UScellular → Array Digital Infrastructure); Swisscom/Vodafone Italy completed (combined with Fastweb); Crown Castle sold fiber solutions (to Zayo) and small cells (to EQT's Arium Networks), closed **1 May 2026** — now pure-play ~40,000-tower company.
- Nokia: Infinera acquisition closed Feb 2025; Alcatel Submarine Networks sold to the French state (Apr 2025); leadership changes (Justin Hotard CEO; Timo Ihamuotila Chair); FWA business sold to Inseego, completed Oct 2026 (Nokia took ~11% Inseego equity stake plus warrants).
- VEON agreed to acquire 100% of Rubicon Wireless (trading as Perfectum) in Uzbekistan for ~US$207m incl. ~US$93m assumed debt (announced Oct 19, 2026; completion expected end-Oct 2026).
- BT Group acquired TalkTalk Telecommunications and PlatformX Communications (PXC) out of administration on **5 Oct 2026** (debt-free basis; c.£400m total FY27 cash impact; regulatory review pending, businesses operate separately meanwhile).
- ZTE: Fang Rong became Chairwoman (Jun 2026 AGM); Ericsson: CEO succession effective Oct 1, 2026; NEC: overseas network-equipment resale transfer agreed Aug 2026.

## Exclusions

- China Tower — infrastructure rather than operator/equipment, excluded by category scope.
- China Broadcasting Network (Broadnet) — ~9m 5G subscribers, insufficient scale for this list at this stage.
- Pure enterprise-IT/consumer arms excluded from equipment rows: Huawei consumer business, Cisco security/collaboration/observability, Samsung consumer electronics/semiconductors, Fujitsu IT services (Uvance), NEC IT services.

## Updates

This guide joins the Tuesday watch: checked weekly for new companies, closures, mergers, leadership changes, and rebrands.

- **2026-09-29:** China Mobile — Chen Yangfan appointed Executive Director and CEO effective Jun 16, 2026 (fills seat vacant since He Biao resigned Feb 12, 2026). China Unicom — HKEX filing confirms Dong Xin as Chairman and CEO of China Unicom (Hong Kong) Ltd from Jan 14, 2026 (note corrected; previously "pending confirmation").
- **2026-10-06:** Ericsson — CEO transition completed: Per Narvinger President & CEO since Oct 1, 2026 (confirmed on ericsson.com); Börje Ekholm remains executive adviser until Jun 15, 2027. BT Group — acquired TalkTalk Telecommunications and PlatformX Communications out of administration (Oct 5, 2026; c.£400m FY27 cash impact; regulatory review pending). Nokia — FWA business sale to Inseego completed (Oct 2026; ~11% equity stake plus warrants). Also repaired a pre-existing CSV parsing flaw in the China Unicom row (unquoted commas in notes); no data changed.
- **2026-10-20:** Etisalat — reverted from the e& group brand to Etisalat (announced Oct 6, 2026, 50th anniversary; ADX filing; confirmed on the company site); company_name updated from "e&" (history/notes refreshed; legal entity remains Emirates Telecommunications Group Company PJSC). Also recorded: Jul 2026 agreement to sell the entire 16.21% Vodafone Group stake to Vega (Xavier Niel vehicle) for £4.4bn (~US$5.95bn). VEON — agreed Oct 19, 2026 to acquire 100% of Rubicon Wireless (trading as Perfectum) in Uzbekistan for ~US$207m incl. ~US$93m assumed debt (~115 MHz spectrum, Nokia-built 5G SA network); completion expected end-Oct 2026.
