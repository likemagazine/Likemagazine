# Heads of State and Diplomatic Missions of UN Member States

A sourced reference guide covering all **193 UN member states**, compiled **2026-09-17** and updated **2026-10-20** (head-of-state rows; seven Geneva mission rows; Pakistan NY mission row updated 2026-10-13). The Holy See is excluded by design (UN observer state, not a member).

- **`heads_of_state.csv`** — one row per country. Columns:
  `country, head_of_state_name, title, salutation, spouse_name, office_address, office_phone, office_email, official_website, source_url, notes`
  - `title` is the constitutional title (President, King, Emperor, Emir, Sultan, Grand Duke, Co-Prince, Captain Regent, Supreme Leader, etc.). Head of *state*, not head of government (e.g., Iran lists the Supreme Leader; the UK lists the King).
  - `salutation` follows standard diplomatic protocol for the title (His/Her Excellency for presidents, His/Her Majesty for kings/queens/emperors/sultans, His Highness for emirs, His Royal Highness for the Grand Duke of Luxembourg, His Serene Highness for the Princes of Liechtenstein and Monaco, Their Excellencies for San Marino's Captains Regent, His Eminence for Iran's Supreme Leader). No personal styles invented.
  - `spouse_name` is populated ONLY where publicly documented in official biographies or major reference sources (129 of 193); never speculated.
  - `office_phone` / `office_email` contain ONLY officially published switchboard numbers or office emails — heads of state almost never publish these (15 / 3 of 193 have them). Blank is correct, not missing.
  - `notes` flags 2026 changes of head of state and explains complex cases (collective presidencies, divided authority, disputed legitimacy).
- **`diplomatic_posts.csv`** — one row per post (629 rows). Columns:
  `country, city, post_type, post_name, head_of_post_name, head_of_post_title, address, phone, fax, email, website, source_url, notes`
  - Four post types covered where they exist: Permanent Mission to the UN (New York), Permanent Mission to UNOG (Geneva), Embassy (Washington DC), Consulate-General (New York).
  - Embassies accredited to the United States sit in **Washington DC**, not New York — documented explicitly per row via the `city` column.
- **`heads_of_state.pdf`** — formatted landscape tables with clickable official-website and source links.

## Headline numbers

| Metric | Count |
|---|---|
| UN member states covered | **193** |
| Heads of state rows | **193** |
| Diplomatic post rows | **629** |
| — Permanent Missions to the UN (New York) | 193 |
| — Permanent Missions to UNOG (Geneva) | 187 |
| — Embassies (Washington DC) | 174 |
| — Consulates-General (New York) | 75 |
| Rows with official head-of-state website | 167 of 193 |
| Rows with documented spouse name | 129 of 193 |
| Rows with published office phone (heads of state) | 15 of 193 |

## Method

Eight parallel research workers (3 for missions, 5 for heads of state by region) worked from official sources first, cross-checking each head of state and each head of post against at least two sources. Currency is **October 2026** for heads of state; Geneva Permanent Representative names are current to **20 October 2026** (includes catch-up corrections for Malaysia, Albania, Nicaragua, Thailand, and Hungary, whose late-September/early-October appointments were missed by earlier weekly checks); other diplomatic post details remain September 2026 unless re-verified. Unverifiable fields were left blank rather than guessed; systematic blanks are documented in `notes`.

## Sources

- **NY Permanent Missions:** UN Protocol and Liaison Service Blue Book, *Permanent Missions to the United Nations, No. 311* (ST/PLS/SER.A/311), **January 2023** — the latest obtainable edition (print discontinued; the live Blue Book Online could not be fetched). Contact details are January 2023; **Permanent Representative names were individually updated to September 2026** (137 of 193 changed), cross-checked against Wikipedia's *List of current permanent representatives to the United Nations*.
- **Geneva Permanent Missions:** UNOG online Blue Book (live, English), each mission page individually read **17 September 2026** — current addresses, phones, faxes, emails, and ambassador names.
- **DC Embassies:** U.S. State Department Diplomatic Corps Order of Precedence (**19 September 2025**) via Wikipedia's *Lists of ambassadors to the United States*, with 2026 updates from official mission/MFA sites, State Dept consular pages, and Diplomatic Watch.
- **NY Consulates-General:** State Department consular listings and official consulate sites.
- **Heads of state:** official presidency, royal court, and government websites first; Britannica-level references and reputable news as second sources.

## Interpretation notes

- **The United States has no "Embassy" row** — it does not accredit an embassy to itself. This is correct, not a gap.
- **18 states have no embassy in Washington DC:** Afghanistan, Andorra, Bhutan, Comoros, Guinea-Bissau, Iran, Kiribati, Nauru, North Korea, Samoa, San Marino, Seychelles, Solomon Islands, São Tomé and Príncipe, Tonga, Tuvalu, Vanuatu, Venezuela. Some accredit from their UN mission in New York; Bhutan has no diplomatic relations with the US; Iran and North Korea have none.
- **6 states have no permanent mission in Geneva:** Guinea-Bissau, Palau, Saint Kitts and Nevis, Saint Vincent and the Grenadines, Tonga, Tuvalu.
- **117 states have no consulate-general in New York** — only the 75 listed maintain one.
- **Collective heads of state:** Bosnia and Herzegovina (three-member Presidency; the current Chair is listed, all three named in notes); San Marino (two Captains Regent, six-month terms); Andorra (two Co-Princes); Switzerland (the Federal Council collectively; the 2026 President of the Confederation is listed).
- **Iran:** the Supreme Leader is head of state; the president is head of government and is not listed.
- **17 DC ambassador posts are vacant** (chargé d'affaires a.i. where identified in notes): Belarus, Bolivia, Burkina Faso, Cuba, Dominica, Eritrea, Fiji, Libya, Madagascar, Micronesia, Montenegro, Myanmar, Papua New Guinea, Saint Kitts and Nevis, Slovenia, Tajikistan, Timor-Leste.

## 2026 changes of head of state (flagged in `notes`)

Africa: Benin (Wadagni elected), Republic of the Congo (Sassou Nguesso re-elected), Guinea (Doumbouya elected), Cabo Verde (interim president Janira Hopffer Almada pending Nov 2026 election), Zambia (Hichilema re-elected), Uganda (Museveni re-elected), Djibouti (Guelleh re-elected), Central African Republic (Touadéra re-election validated).
Americas: Venezuela (Delcy Rodríguez acting, extraordinary), Honduras (Asfura), Haiti (no president; interim executive authority), Peru (Fujimori), Chile (Kast), Costa Rica (Fernández Delgado), Colombia (de la Espriella).
Asia-Pacific: Bangladesh (Alamgir), Myanmar (Min Aung Hlaing), Vietnam (Tô Lâm), North Korea and Laos (reappointments/re-elections, same incumbents).
Europe: Estonia (Madise, sworn in 12 October 2026), Switzerland (Parmelin), Bulgaria (Iotova), Portugal (Seguro), Bosnia and Herzegovina (Bećirović chair), San Marino (Mina/Selva), Hungary (Baka), Norway (Haakon VIII on the death of Harald V), Serbia (Vučić resigned 27 September 2026; Ana Brnabić acting president — corrected in the guide 20 October 2026 after earlier weekly checks missed it).
Middle East & Central Asia: Iran (Mojtaba Khamenei succeeded his father, killed 28 Feb 2026), Iraq (Amidi elected April 2026).

## Known gaps and staleness

- **NY mission contact details are January 2023** (latest obtainable Blue Book). Addresses and phone numbers may have changed since; PR names are current to September 2026.
- **DC embassy and NYC consulate contact details** (address/phone/fax/email) for most rows were transcribed from countryaah.com, a secondary directory explicitly marked "verify before publication" — they should be re-verified against official mission sites or the State Department's Foreign Consular Offices list before any republication. Ambassador names are the stronger field (State Dept protocol baseline + 2026 updates).
- **All 75 NYC Consul-General names are blank** — not verified as of September 2026 (documented per row; the UN Permanent Representative was deliberately NOT substituted).
- **10 DC head-of-post names** rest on Washington Diplomat reporting awaiting official confirmation (Haiti, Lebanon, Moldova, Cambodia, Jamaica, Nepal, Oman, Senegal, Sierra Leone, Yemen); Tajikistan's ambassador is genuinely disputed between sources.
- **Dominica's DC embassy contact fields are blank** — published sources conflict on the address; omitted pending official verification.
- **Heads of state office phones/emails:** 178 of 193 publish no office phone and 190 of 193 no office email. This reflects official publication practice, not missing research.
- **26 heads-of-state rows have no official website** (no verifiable presidency/royal-court site, or transitional authorities without one, e.g., Syria, Yemen, Haiti, Nicaragua).
- **64 rows have no documented spouse** — left blank where no public record exists (includes unmarried, widowed, divorced, and undocumented cases; never speculated).
- Several presidency website URLs are long-established official domains not individually re-fetched on the compilation date; spot-check before republication.
