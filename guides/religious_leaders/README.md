# Leaders of the World's Major Religions

A sourced reference guide to the current principal living leaders of the world's major religious traditions, compiled **17 September 2026**.

- **`religious_leaders.csv`** — one row per leader (83 rows). Columns:
  `religion, tradition_branch, leader_name, title, salutation, spouse_name, office_address, office_phone, office_email, official_website, source_url, notes`
  - `salutation` is the form the office itself uses (His Holiness, His All-Holiness, His Eminence, His Beatitude, The Most Reverend, etc.). Never invented; left blank where no official source confirmed one.
  - `spouse_name` is populated ONLY where publicly documented; for celibate/monastic offices the spouse field is blank and `notes` records "celibate office".
  - `office_phone` / `office_email` / `office_address` contain ONLY officially published contact details. Blank is correct, not missing.
- **`religious_leaders.pdf`** — formatted landscape tables with clickable official-website and source links.

## Inclusion rule

The guide covers every religion/tradition with roughly **15 million or more adherents**, PLUS globally significant organized faiths below that threshold with a clear, verifiable top office. Adherent figures below are rough, widely cited estimates (Pew Research Center 2015/2017, World Religion Database, official communion figures) — included to make the scope defensible, not as precise claims:

| Religion | Approx. adherents | Leaders listed |
|---|---|---|
| Christianity | ~2.4B (Catholic ~1.4B, Orthodox ~220M, Protestant ~1B) | 33 |
| Islam | ~2.0B (Sunni ~1.8B, Twelver Shi'a ~180M, Ismaili ~15M, Ahmadiyya ~15–20M, Bohra ~2M) | 16 |
| Hinduism | ~1.2B | 7 |
| Buddhism | ~500M | 9 |
| Sikhism | ~30M | 1 |
| Shinto | ~100M (practitioner estimates vary widely) | 1 |
| Judaism | ~15M | 4 |
| Baháʼí | ~8M | 1 (collective body) |
| Jainism | ~7M | 2 |
| Taoism | ~12M+ (estimates vary widely) | 1 |
| Druze | ~1M | 3 |
| Tenrikyo | ~1.5M | 1 |
| Yazidism | ~0.5–1M | 2 |
| Zoroastrianism | ~0.1–0.2M | 2 |

## Headline numbers

| Metric | Count |
|---|---|
| Religious leaders listed | **83** |
| Religions/traditions covered | **14** |
| Rows with official website | see CSV |
| Rows with documented spouse | see CSV |
| Rows with published office phone | very few — religious offices rarely publish these (see gaps) |

## Method

Four parallel research workers (Christianity; Islam; Hinduism/Buddhism/Sikhism/Jainism/Shinto/Taoism; Judaism/Baháʼí/Zoroastrianism/Yazidism/Druze/others) worked from official sources first — vatican.va, ec-patr.org, mospat.ru, al-Azhar, Diyanet, the.ismaili, dalailama.com, SGPC, bahai.org, chiefrabbi.org, communion world-body sites — cross-checking every leader against at least two sources, one being the office's own site wherever one publishes usable material. Currency is **September 2026**. Unverifiable fields were left blank rather than guessed; systematic blanks are documented in `notes`. Tone is strictly neutral: offices and facts only, no theological ranking or commentary.

## Traditions with no single leader (documented, not omitted silently)

- **Hinduism** — no single head; the guide lists the four cardinal Shankaracharyas plus heads of major sampradayas with clear top offices (BAPS, Ramakrishna Mission, Chinmaya Mission).
- **Buddhism** — no world head; listed are the Dalai Lama, both 17th Karmapa claimants (dispute noted), Theravada supreme patriarchs, and heads of the Sakya and Gelug schools. Zen and the Nyingma school have no single head.
- **Judaism** — no world head; listed are the two Chief Rabbis of Israel plus the UK and French chief rabbis.
- **Zoroastrianism** — no world head; the two concurrent high priests of Udvada's Iranshah Atash Behram are listed with that caveat.
- **Druze** — no single world head; the three regional sheikh al-aql offices are listed.
- **Jehovah's Witnesses / ISKCON / Baháʼí** — governed by collective bodies, listed as such.
- **Confucianism** — excluded: no clergy, no religious head, no headquarters.
- **Caodaism** — excluded: the papal office has been vacant since 1959 with no verifiable successor.
- **Quakers and much of congregational Protestantism** — no single head by design; not listed.

## 2025–2026 successions (flagged in `notes`)

Pope Leo XIV (elected 8 May 2025); Archbishop of Canterbury Sarah Mullally (28 Jan 2026, first woman in the office); LDS President Dallin H. Oaks (Oct 2025); SDA President Erton C. Köhler (Jul 2025); Aga Khan V (Feb 2025); Saudi Grand Mufti Saleh al-Fawzan (Oct 2025); Diyanet President Safi Arpaguş (Sep 2025); Egypt Grand Mufti Nazir Ayyad (2024); Georgian Catholicos-Patriarch Shio III (May 2026); Albanian Archbishop Joani (Mar 2025); Eritrean Patriarch Abune Basilios (Jan 2025); WCRC President Karen Georgia Thompson (Oct 2025); Akal Takht Acting Jathedar Giani Kuldeep Singh Gargaj; CTA President Li Guangfu re-elected (Dec 2025). Iran's Supreme Leader succession (Mojtaba Khamenei, Mar 2026) is recorded in the religious-office capacity only, with the contested circumstances noted factually.

## Known gaps and staleness

- **Contact details are sparse by design.** Monastic and primatial offices rarely publish phones or emails. Only a handful of rows carry official contacts (LWF Geneva office, Baháʼí World Centre, Israeli Chief Rabbinate, UK Chief Rabbi's office, one Polish Orthodox diocesan entry, one Malankara parish-published contact, one dated Athens address). Blanks reflect official publication practice, not missing research.
- **Second-source limitations:** for some Eastern rows (Dwarka and Jyotirmath mathas, Thai/Sri Lankan patriarchates, Akal Takht, Jinja Honcho, CTA, Dalai Lama's office) verification rests on two secondary sources (news, government publications, encyclopedias) because official pages surfaced only as search snippets under the text-only research constraint. Rows are flagged in `notes` where this applies.
- **Jehovah's Witnesses Governing Body membership** rests on the official October-2025 *Watchtower* announcement (j.w.org's public FAQ was stale at research time) — strongly corroborated but the article page itself did not render in text fetch.
- **Name spellings:** variant transliterations are noted per row (e.g., Sadanand/Sadananda; Gargaj/Gadgaj/Garhgaj; Rastislav; Joani/John).
- **Salutations** are blank wherever no official source confirmed the office's own form.
- **Disputed successions** (Karmapa, Jyotirmath, Bohra, Iran, OCU canonical status, Syrian Druze leadership) are presented factually with the dispute stated; no position is taken.
