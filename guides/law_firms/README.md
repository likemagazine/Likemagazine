# LIKE Magazine's Preferred Lawyers Worldwide

The world's 100 largest law firms by revenue, based on **The American Lawyer Global 200 2026** (Law.com, published September 15, 2026; ranked on FY2025 gross revenue). Aggregate Global 200 FY2025 revenue: **$248.5B (+11.9%)**.

**Edition:** 2026 Global 200 · **Compiled:** 2026-09-23 · **Rank verification pass:** 2026-09-26 (20 ranks still provisional) · **Watch update:** 2026-10-20 (1 row changed — Goodwin Procter managing partner; 20 ranks still provisional) · **Next watch:** Tuesday weekly maintenance (notify only on change)

## Files
- `law_firms.csv` — 100 rows × 15 columns (master data)
- `law_firms.pdf` — formatted landscape table with clickable firm-website links
- `law_firms.html` — SEO/AI-optimized semantic page with JSON-LD firm entities
- `law_firms_llms.txt` — plain-text AI index

## Column definitions
`firm_name` · `global_rank_2026` · `hq_city` · `hq_country` · `region` · `website` ·
`phone` (HQ switchboard as officially published) · `contact_email` (published only) ·
`key_people` (global chair/managing partner + practice-group leaders, with published lawyer headcount) ·
`specialties` (the firm's own listed practice areas) · `offices` (all offices from the firm's official office pages; associated/alliance offices flagged) ·
`notable_clients` (ONLY firm-publicly-disclosed) · `notable_matters` (ONLY firm-publicly-described) ·
`ranking_source` · `notes`

## Coverage (of 100 firms)
- Websites: **100** · HQ phones: **94** · Published contact emails: **1** ·
  Key people: **100** · Specialties: **100** · Offices: **100** ·
  Notable clients: **1** · Notable matters: **10**

## Systematic gaps (by design, not error)
- **Contact emails:** The top-100 global firms are essentially contact-form-only. No general published email exists for 99 firms; the field is blank rather than guessed. The single exception is Simmons & Simmons, whose `enquiries@simmons-simmons.com` is the firm's widely published general contact (firm letterheads, firm-provided directory profiles).
- **Notable clients / matters:** Included ONLY where the firm publicly discloses them. One firm (Paul Hastings) publishes client/matter highlights; ten rows carry firm-described matters. Blank means the firm does not publish them — not that they don't exist.
- **No personal data:** No direct-dial numbers, no personal or guessed email addresses (no inferred email patterns) anywhere in this guide.

## Rank bands and how they were sourced
- **Ranks 1–25:** Built from official firm websites (ranks 1–8 from a recovered prior build, enriched and verified; ranks 9–25 freshly researched).
- **Ranks 26–75:** Rebuilt against the authoritative Law.com chart transcription (the first attempt's ranks were a provisional scaffold and were fully corrected).
- **Ranks 76, 77, 92, 93, 94:** Per the chart transcription — Dacheng Law Offices (76), Hunton Andrews Kurth (77), Baker Botts (92), Womble Bond Dickinson (93), Ogletree Deakins (94).
- **Ranks 78–91 and 95–100 (20 slots): PROVISIONAL.** The Law.com 2026 chart is paywalled and no firm-published 2026 Global 200 announcement (press release, newsroom, accolades page, LinkedIn) could be found for any candidate firm after two independent sourcing passes (firm newsrooms checked directly, Sept 8–23, 2026 — early for firms to publish), **plus a third verification round on Sept 25–26, 2026**: a live-browser pass and three bounded parallel research passes (~35 additional targeted searches/fetches across firm sites, The Lawyer, Law Gazette, Legal Week, Canadian Lawyer, Lexpert, Above the Law, Law360, and Bloomberg Law) returned no explicit 2026-chart rank for any of the 20 firms. Two leads were checked and debunked: (1) Gordon Rees Scully Mansukhani's accolades page states "#86 Law Firm by Global Revenue, 2025" — that is the **2025** chart (firm press release Sept 22, 2025), not the 2026 chart; (2) Iberian Lawyer's September 2026 Global 200 roundup covers only Spanish firms (Garrigues 125, Cuatrecasas 143, Uría Menéndez 186) and contains no ranks for the UK provisional firms, contrary to an earlier misreport. These 20 rows carry `global_rank_2026 = "provisional"`, are sorted alphabetically in the CSV, and are grouped in a clearly labeled provisional section in the PDF/HTML. The candidate identities come from the 2025 Global 200 pool; presence in the 2026 top 100 is unconfirmed. Notably, Jackson Lewis P.C. (2025 rank 100) was excluded by positional inference, not confirmed fact.
- **Recommendation:** resolve this band via a live-browser read of the paywalled Law.com chart, or in a later Tuesday-watch pass once firm announcements are indexed. Do not cite these 20 ranks as confirmed.
- **Update 2026-10-13:** a fourth bounded verification pass (~13 targeted searches across firm newsrooms, The Lawyer, Law Gazette, Legal Week, Canadian Lawyer, Lexpert, Above the Law, Law360, Bloomberg Law) found no firm-published or Law.com-explicit 2026-chart rank for any of the 20 firms. All 20 rows remain provisional; the provisional band note above stands unchanged.

## Notable structural notes
- **Mergers new to the 2026 ranking:** McDermott Will & Schulte (#20, effective Aug 1, 2025); Herbert Smith Freehills Kramer (#29, combination completed June 1, 2025); Troutman Pepper Locke (#39, effective Jan 1, 2025).
- **Ashurst (#50) / Perkins Coie (#61):** ranked on standalone FY2025 figures; the Ashurst–Perkins Coie combination closed ~June 2026 and is noted on both rows.
- **Hogan Lovells (#14):** ranked on pre-Cadwalader FY2025 figures; the Hogan Lovells Cadwalader combination launched July 1, 2026.
- **Winston Taylor (#58):** the combination of Winston & Strawn LLP and Taylor Wessing's UK-led business launched **1 Jun 2026** as "Winston Taylor" (~1,400 lawyers, ~£1.2bn combined revenue, 20 offices, per the firms' launch release). Row updated 2026-10-13 (firm name, leadership, headcount); the office list still reflects the pre-combination network pending the official combined directory. The 2026 Global 200 rank reflects pre-combination FY2025 figures.
- **King & Wood Mallesons (#59):** the verein dissolved March 31, 2026; row reflects the successor structure.
- **Goodwin Procter (#25):** Josh Klatzkin became Managing Partner Oct 1, 2026, succeeding Mark T. Bettencourt (firm announcement 20 Oct 2025, updated 13 Mar 2026). Row updated 2026-10-20.
- **Verein/EEIG firms** (DLA Piper, Baker McKenzie, Dentons, Norton Rose Fulbright, CMS, Squire Patton Boggs): HQ positions and office networks are recorded per each firm's own statements; Dentons states it has no headquarters and publishes no global switchboard (phone blank).
- **Yingke (#51):** official site used is yingkelawyer.com (the firm's published domain); leadership in transition (founding partner Mei Xiangrong resigned March 2026).
- **HSF Kramer merger date** is June 1, 2025 per the firms' official launch release (not May 1).
- **DLA Piper** publishes no single global switchboard (London is its international base); **Squire Patton Boggs** publishes no global switchboard; **Dentons** publishes no global switchboard — all blank with notes.

## Rebuild history
- 2026-09-23: Initial build, 100 firms, 2026 Global 200 edition.
- 2026-10-13: First Tuesday watch — 2 rows changed: (1) Winston & Strawn LLP → **Winston Taylor** (Taylor Wessing UK-led combination closed 1 Jun 2026; firm name, leadership, headcount updated; office list still pre-combination); (2) Mintz leadership transition (Mike Fantozzi Managing Member from Jun 2027; Bob Bodian to Chair; firm press release 29 Sep 2026). PDF not rebuilt (no PDF build script retained in workspace) — CSV/HTML/llms.txt updated; Library CSV copies refreshed.
- 2026-10-20: Second Tuesday watch — 1 row changed: (3) Goodwin Procter (#25) managing partner transition (Mark T. Bettencourt → **Josh Klatzkin**, effective 1 Oct 2026; firm announcement 20 Oct 2025). Weil Gotshal merger talk (Law.com, 19 Oct 2026) is source-speculation the firm on-record denied ("not engaged in merger discussions with any firm"); no row change. PDF not rebuilt (no PDF build script retained) — CSV/HTML/llms.txt updated; Library CSV copy refreshed.
