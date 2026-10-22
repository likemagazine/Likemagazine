# Fine Tableware Houses Worldwide

**92 luxury tableware houses across 4 categories. Compiled September 2026; contact-verification pass completed 2026-09-28; Tuesday watch updates applied 2026-10-13.**

- Crystal: 21 houses
- Porcelain / fine china: 31 houses
- Flatware / silverware: 22 houses
- Table linens: 18 houses

## Files

- `fine_dining_ware.csv` — the master list (92 rows x 16 columns)
- `fine_dining_ware.pdf` — formatted PDF with clickable website links
- `work/` — intermediate category part files and the merge script

## Coverage (of 92 rows)

- Websites: 92 (100%)
- History: 92 (100%)
- Specialties: 92 (100%)
- Ownership: 69
- Key people: 64 (was 46 before the 2026-09-28 verification pass)
- Boutiques/showrooms: 54
- HQ phones: 63 (was 32)
- Published general emails: 56 (was 25)
- Notable clients: 19

## Verification pass (2026-09-28)

At the user's request, all 92 rows were re-verified in four category passes (crystal, porcelain, flatware, linens) for named leadership, HQ phones, and published general emails, checked against official house/group websites (imprint, contact, terms pages) and authoritative trade press.

- Key people: 46 → 64. New leadership verified from official pages; registry-sourced names (e.g. French commercial register, UK Companies House) are flagged as such in `notes`; trade-press-only leadership carries the "per trade press, unverified on official site" caveat.
- HQ phones: 32 → 63. Customer-service-only lines were left blank per the HQ/main-switchboard rule, with explanatory notes.
- Published general emails: 25 → 56. Inferred addresses were removed (e.g. Pratesi); only addresses appearing on official pages were kept or added.
- Corrections caught: Georg Jensen CEO updated (Jacob Siboni replaced outdated Mehul Tank); Arthur Price CEO transition corrected to already-occurred; Villeroy & Boch CEO corrected (Georg Lörz spokesperson, Dr Peter Domma Dining & Lifestyle — stale "Gabriele Schupp" removed after her 2026-05-31 departure); Garnier-Thiebaut CEO corrected (Nikita Mulard, DG of the house, not Jean-Philippe Krukowicz of the US arm); Koch & Bergfeld entity conflict resolved (former GmbH insolvent 2023; details are for the active Silbermanufaktur KG); Eisch/Zwiesel marketing-director names removed per the marketing-director rule; Augarten phone/email removed (travel-guide-sourced only).
- Conflict flags preserved: Baccarat CEO (Laurence Nicolas per official 2025 release vs Margareth "Maggie" Henriquez per trade press); Dartington phone (two different official numbers on different official pages).
- Status note added: D. Porthault entered redressement judiciaire in May 2026 (BODACC).
- Busatti's `shop@busatti.com` is officially published but order-specific; it is included with that qualification in `notes`.

## Methodology and rules

- Official published sources only: house websites, official press releases, official corporate reports, trade-press announcements (Reuters etc.), and industry directories where official material was not available.
- **Blank beats guessed.** Where no official phone, email, CEO, or marketing director could be verified, the field is left blank and the gap is documented in `notes`.
- Every row has a `history` field: a concise founding story/milestones drawn from official materials, except where no official history exists (noted in `notes`).

## Systematic gaps (honest limitations)

1. **Marketing directors / CMOs are rarely published.** No named marketing lead could be verified from official materials for any row. Where marketing leadership was found (e.g. Le Jacquard Français), it is included; otherwise `key_people` carries the CEO only, or is blank.
2. **CEOs change often and some houses don't name them.** Several `key_people` entries rely on industry directories or press rather than official leadership pages; these are flagged in `notes` as not recently reverified.
3. **Direct phone/email are often unpublished.** Luxury houses typically route contact through forms or flagship phones; where only a flagship boutique phone exists, that is given with context.
4. **Ownership is opaque for some private houses.** Baccarat's ownership is per trade press (Fortune Fountain Limited, controlled since Dec 2020 by four Hong Kong funds); Moser and some others publish nothing.
5. **Region granularity is mixed** (Europe vs Western/Northern/Southern/Eastern Europe) because the four category passes used slightly different conventions.
6. **Baccarat CEO conflict:** trade press (Reuters, Dec 2021) lists Margareth "Maggie" Henriquez as CEO from April 2022, while an official 2025 Baccarat release names Laurence Nicolas as CEO. Both are recorded; current status unconfirmed on official pages fetched.

## Exclusions

- Dormant or discontinued houses: Cristal de Sèvres, Steuben, Edinburgh Crystal, Royal Worcester, Minton, Aynsley, Royal Albert.
- Below strict luxury fit / insufficient table relevance: NUDE, Spiegelau, Nachtmann, Reflections Copenhagen.
- Mass-market tableware brands under large groups (Royal Doulton, Spode, Deshoulières, Apilco) — not luxury-tier; documented here rather than included.
- Fashion-house home lines (Armani Casa, Missoni Home, Loro Piana Interiors) — not dedicated tableware houses.
- No separate rows for absorbed brands: Tétard Frères/Biennais/Rouge Pullon under Odiot; Boin-Taburet into Ercuis; Cardeilhac into Christofle.

## Updates

This guide joins the Tuesday watch: checked weekly for new houses, closures, CEO/ownership changes, and HQ moves.

## Tuesday watch updates — 2026-10-13 (first weekly run)

Four rows updated; total still 92 (no houses added or removed).

- **Pickard (Porcelain, USA)** — ownership: acquired by Chicago artist Theaster Gates in Sept 2026 (undisclosed sum), ending 133 years of Pickard-family ownership (reported Oct 3, 2026 by NPR; Oct 12, 2026 by Gift Shop Magazine). Gates is owner/President leading creative direction; Andy Pickard Morgan (President and CEO 2006–2026) retained in an executive role. Notes now carry the source URLs.
- **Vista Alegre (Porcelain, Portugal)** — ownership: delisted from Euronext Lisbon effective 17 Sept 2026 (CMVM approved, following the 29 May shareholder vote); now fully private under Grupo Visabeira, which is buying out dissenting shareholders at €1.07/share over three months (Lusa, 17 Sept 2026).
- **Okura Art China (Porcelain, Japan)** — ownership: Noritake Co., Limited acquired additional shares in Q1 FY2026 (Apr–Jun 2026), making Okura a consolidated subsidiary (¥498M gain on bargain purchase booked; previously ~37.4% major shareholder). Per Noritake's official Q1 FY2026 results.
- **Baccarat (Crystal, France)** — leadership note: Thais Roda appointed CEO, North America (announced 2026; WWD reported 3 Apr 2026). The house's own appointment announcement quotes "Laurence Nicolas, Global CEO, Baccarat" — official-side confirmation of his global role in the previously flagged Henriquez-vs-Nicolas CEO conflict.

Watch for next run: **Odiot → Lapparra** acquisition (exclusive negotiations announced July 2026; deal close targeted by 31 Oct 2026); **D. Porthault** redressement observation period expires 06/11/2026. Villeroy & Boch Wikipedia key-people edit (Patrick Grundke) unverified — not acted on.
