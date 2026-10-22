# World's Largest Pension Funds

**106 pension funds and major institutional investors across 3 categories, as of October 2026.**

- Labor pension funds: 39 rows (public-employee retirement systems, industry-wide/multi-employer and occupational pension funds)
- Corporate pension funds: 32 rows (single-employer company plans)
- Government pension funds: 32 rows (national public pension/reserve funds)
- Sovereign wealth funds (for reference): 3 rows (Russia National Wealth Fund, Temasek, GIC — each explicitly labeled "SWF, not a pension fund")

## Ranking backbone

Thinking Ahead Institute / Pensions & Investments **Global Top 300 Pension Funds 2026**, published **September 8, 2026**, based on year-end 2025 AUM. Top 300 total AUM: a record **$27.7 trillion** (+13.4% in 2025, fastest annual growth since 2017). The top 20 hold $11.9 trillion (+14.7%). Norway's Government Pension Fund crossed **$2 trillion** for the first time and is 12.7% larger than Japan's GPIF.

- **59 ranks confirmed in the 2026 edition** (official TAI/WTW release, the fund's own announcement of its 2026 rank, or reputable republication of the 2026 table).
- **37 ranks provisional** — carried over from the 2025 edition (published September 2025, 2024 year-end AUM, parsed from the official TAI/WTW report PDF), each flagged `provisional — 2025-edition rank, 2026 unconfirmed` in `notes`. Never presented as 2026-confirmed.
- **10 rows with blank ranks** — funds absent from both releases (e.g., Swedish AP2/AP3/AP4 post-consolidation); their latest published AUM in original currency sits in `notes` with no USD conversion applied, per the no-guess rule.

## Files

- `pension_funds.csv` — the master list (106 rows x 13 columns)
- `pension_funds.pdf` — formatted PDF with clickable website links
- `work/` — intermediate category part files, the 2026 top-20 seed, and the 2025-edition rank scaffold


## Changes — 20 October 2026 check

- **NPS (South Korea, rank 4)**: new CIO — Lee Kyu-hong appointed 14 Sep 2026, term from 15 Sep 2026 (two years, to 14 Sep 2028), succeeding Seo Won-joo; former CIO of Korea Teachers' Pension 2019–2023 (Markets Group / Yonhap Infomax / Mingtiandi). Chairman Kim Sung-joo made the appointment with Health and Welfare Minister's approval.
- **Aware Super (rank 37)**: TelstraSuper merger completed 30 Apr 2026 per Aware Super's Annual Financial Report FY2026 (notes updated). Prime Super merger still exploratory — MoU 4 Aug 2026, due diligence expected through end-2027, no new development.
- Watch only (no list change): Philippines SSS named a new CEO (Victor Limlingan, Oct 2026) but SSS is not in the guide (only GSIS is, rank 200). Russia NWF sanctions status unchanged — OFAC GL 13S (8 Oct 2026) is a routine renewal of the administrative-payments license through 9 Jan 2027; the 16 Oct US executive-order waiver explicitly does not affect the earlier Russia sanctions (Directive 4 restrictions on the NWF remain). Next NWF monthly valuation (1 Nov) not yet published — 1 Oct figure stands. AP2 CEO Eva Halvarsson still in post, successor not yet named. Full 2026 TAI table still not publicly released — the 37 provisional ranks remain unpromoted.

## Changes — 13 October 2026 check

- **Kwap (Malaysia)**: new CIO — Hazman Hilmi Sallahuddin appointed (AsianInvestor, Oct 2026).
- **Russia NWF (SWF reference row)**: value updated to ~US$151.9bn (RUB 12.98tn) at 1 Oct 2026 per Russian Finance Ministry monthly data (reported 7 Oct 2026); liquid assets ~US$44.5bn (RUB 3.8tn). Sanctions status unchanged (US Feb 2022 restrictions, EU 10th package).
- Watch only (no list change): Aware Super / Prime Super merger still exploratory (MoU Aug 2026, due diligence ongoing); Mercer Super Trust completed BT Super merger (~Aug 2026, A$63bn) but is outside the 2026 TAI table; Hostplus/Statewide was 2022. CIO moves at LPFA, West Yorkshire PF, PKZH, PBU, VBV and NatWest Group Pension Fund are all funds below the Top-300 threshold and not in the list. PensionDanmark's CIO retirement (Claus Stampe, end Jan 2027) is announced but not yet effective. Full 2026 TAI table still not publicly released — the 37 provisional ranks remain unpromoted.

## Changes — 6 October 2026 check

- **FRTIB (U.S.)**: CIO changed — Sean McCaffrey retired Feb 2026, succeeded by Deputy CIO Mike Jerue (promoted Mar 2026).
- **OMERS (Canada)**: CIO Ralph Berg departed 1 Jul 2026 for Temasek; President & CEO Blake Hutcheson assumed CIO duties.
- **Temasek (SWF reference row)**: Temasek Review 2026 (8 Jul 2026) — net portfolio value S$518bn (~US$401bn) at 31 Mar 2026, first year of full mark-to-market reporting; one-year TSR 10.5%; CEO Dilhan Pillay added.
- **Russia NWF (SWF reference row)**: value updated to ~US$154.1bn (RUB 13.19tn) at 1 Sep 2026 per Russian Finance Ministry monthly data; liquid assets ~US$46.7bn. Sanctions status unchanged (US Feb 2022 restrictions, EU 10th package).
- **Australian rank confirmations**: 2026-edition ranks confirmed via Super Review republication — ART 19, Aware Super 37, UniSuper 51, Hostplus 59, Cbus 93, Rest 96, HESTA 99. Full 2026 TAI table still not publicly released, so the 37 provisional ranks remain unpromoted.
- **CareSuper (Australia) added**: entered the 2026 Top-300 after its 1 Nov 2024 merger with Spirit Super; 2026 rank and USD AUM left blank (unconfirmed).
- **TRS Texas**: 2025-edition rank 18 flagged as 2026-unconfirmed — the fund is absent from the 2026 top-20 republication.

## Coverage (of 106 rows)

- Websites: 95
- Key people: 67
- Notable investments: 43
- AUM figures: 91
- HQ phones: 15 (published institutional lines only)
- Published general emails: 5
- Ranks: 59 confirmed-2026, 37 provisional, 10 blank

## Methodology and rules

- Official published sources only: fund websites, official press releases and annual reports, TAI/WTW releases, and reputable republications (P&I, IPE, Super Review). Trade press used for corporate actions (GE split, BTPS rebrand) where funds don't publish them.
- **Blank beats guessed.** Where no official phone, email, CEO/CIO, or AUM could be verified, the field is left blank and the gap is documented in `notes`.
- AUM figures come from the ranking where available; otherwise from the fund's own latest published figure (end-2025), flagged in `notes`. Currency of origin is preserved where no official USD figure exists.

## Structural notes (verified, September 2026)

- **GE split**: GE HealthCare spun off 3 Jan 2023, GE Vernova 2 Apr 2024; retirement plans allocated to the businesses. "GE" appears as two rows: GE Aerospace (rank 188, $36.2bn) and GE HealthCare (rank 239, $28.3bn).
- **BTPS Management rebranded as Brightwell** (2026).
- **Sweden's AP reform**: AP1 and AP6 are wound down/merged and marked historic; AP2/AP3/AP4 post-consolidation figures are in original currency with no rank assigned.
- **Alecta CEO**: Pablo Bernengo effective 1 September 2026.
- **Alecta and AMF Pension** are Swedish occupational schemes; kept in the labor section (removed from corporate, where they appeared in an early draft).
- **ATP (Denmark)** and **Chikyoren** appear once each (labor section); duplicate government-section rows were removed.
- Category boundaries for quasi-public providers (Keva, KLP, CDPQ, USS) are flagged per-row in `notes`.
- **Russia National Wealth Fund**: sanctions/status context included (US Feb 2022 restrictions, EU 10th package, ~€9bn frozen, liquid assets depleting); shown only as an SWF reference row.

## Systematic gaps (honest limitations)

1. **Corporate plan CIOs are rarely public in the US.** Only European/UK in-house managers and trustee chairs were consistently nameable; US single-employer plans almost never publish plan-level contacts — emails 0/34 corporate, phones 1/34.
2. **Named mid-tier funds are absent from the Top 300.** Siemens, TotalEnergies, Volkswagen, BASF, Bayer, BMW, Deutsche Post, Philips, Unilever, Novartis, ABB and Ericsson appear in neither the 2026 nor 2025 editions, so they were deliberately excluded rather than ranked by guesswork.
3. **Key people thin for sovereign and Asian funds.** Norway GPFG, China NSSF (CIO-level), Kuwait PIFSS, Temasek, GIC, Taiwan PSPF and several Japanese mutual-aid schemes publish no named investment leadership.
4. **Notable investments are patchy for mid-tier government funds** — left blank where no specific publicly disclosed holdings were found.
5. **Websites missing for some Asian schemes** (South Korea NPS, Chikyoren, KLP, FEFSS, Taiwan PSPF, Thailand GPF) — no official English-language site was verifiable.
