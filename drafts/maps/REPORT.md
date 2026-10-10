# drafts/maps — report

## rtasim — Renal Tubular Acidosis Simulator (`a_rtasim.py`) · 2026-10-10
- **Switch** `rt` (one), teaching order: Type 1 — distal (`drta`) · Type 2 — proximal (`rta`) · Type 4 — hyperkalemic (`rta`) ·
  Diarrhea (gut loss) (`diarrheaapproach`) · Amphotericin B (`amphotericin`) · Acetazolamide (`acetazolamide`) ·
  Fanconi syndrome (`fanconisyn`) · Spironolactone (`mras`).
- **Drawing:** proximal tubule cell (NHE3, brush-border carbonic anhydrase, basolateral Na⁺–HCO₃⁻ cotransport, glutamine → NH₄⁺,
  new HCO₃⁻ out), collecting duct α-intercalated cell (H⁺-ATPase, Cl⁻–HCO₃⁻ exchanger) and principal cell (ENaC, ROMK, aldosterone
  receptor), colon (stool loss on Diarrhea), urine pH scale with the 5.5 cut-off, urinary anion gap scale, and a "what it leads to"
  row (CaPO₄ stones · hypophosphatemic rickets · serum K⁺).
- **What each option does:** type 1/amphotericin — H⁺-ATPase ✕ ("fails"), Cl⁻–HCO₃⁻ exchanger idle, no new HCO₃⁻ to blood, urine NH₄⁺
  low, pH marker above 5.5, UAG positive, stones lit. Type 2/Fanconi — NHE3 and basolateral cotransport less active, HCO₃⁻ piles
  up in the lumen and reaches the urine, pH markers alkaline at first then < 5.5 below threshold, rickets lit. Acetazolamide —
  carbonic anhydrase ✕, alkaline urine, stones lit. Type 4/spironolactone — receptor low/✕, ENaC and ROMK less active, less
  K⁺ in the urine, glutamine → NH₄⁺ slowed, UAG positive. Diarrhea — stool carries HCO₃⁻ and K⁺ out, NH₄⁺ production and H⁺
  secretion more active, UAG negative.
- **Readouts (5):** Serum HCO₃⁻ ↓ (all) · Serum Cl⁻ ↑ (all) · Anion gap ↔ (all) · Serum K⁺ ↑ type 4/spironolactone, ↓ the rest ·
  Urine NH₄⁺ ↓ type 1/4 and their causes, ↑ diarrhea, "–" for the proximal options (no source gives a direction).
- **Cards:** 0 new. 22 existing pinned on 9 nodes (rta, drta, hco3reabs, aldoaction, mras, nagma, agma, uag, newhco3, amphotericin,
  acetazolamide, ksparing, sulfonamides, fanconisyn, myeloma, wilson, vitddef, calcstone, stones, hypok, hyperk, diarrheaapproach).
- **Sources:** First Aid 2025 pp. 604, 610–611, 617 (as cited by the pinned cards) · Costanzo ch 7 · Guyton ch 31 · Katzung ch 15 ·
  Robbins ch 20. Every note, panel row and readout restates facts the pinned cards already carry (they passed the Mac-side check);
  no corpus was available here.
- **`# UNVERIFIED` (3 places, one fact):** type 4 urine pH < 5.5 — from memory of the FA p. 611 table; none of the pinned cards states
  it (note `rt:h4`, the urine-pH marker, panel row "Type 4 · hyperkalemic"). Cut it if FA doesn't say so.
- **Unsure / for the checker:** the scale markers sit at illustrative positions (the caption says so); the hollow "at first:
  alkaline" marker for type 2 is inferred from FA's "↑ HCO₃⁻ excretion in urine" and "urine pH < 5.5 once serum HCO₃⁻ falls below
  the threshold"; diarrhea's urine pH "can run above 5.3" comes from the `uag` card (Batlle 1988).
- **check.py:** `rtasim: 0 new cards, 9 nodes, 10 sites, 5 flows` · `OK · 0 warnings`. Looked at: default (full) and Type 1 (zoomed).

## Kit change — ABG calculator on the acid–base timeline (site feature) · 2026-10-10
**The kit changed** (tools/atlas-src.html; drafts/tools/kit.js updated to match) — copy it into the batch tooling.
- New last-row chip "Check a blood gas" on any map listed in `DYN_ABG` (only `abtime` now). It opens a dialog (same style as Compare):
  type pH / PaCO₂ / HCO₃⁻ → a Henderson–Hasselbalch consistency check, the primary disorder, the expected compensation and whether a
  second disorder is present. "Show it on the graphs" switches the map to the matching disorder and time step (acute → minutes,
  chronic → 3–5 days, metabolic → 1 day; met + resp acidosis → the mixed option) and marks the patient's three values on the graphs
  in the current time column (▲/▼ when off the scale). The chip then reads "Blood gas: 7.33 / 60 / 30"; "Clear it" or Reset removes it.
  Hidden while a Name-it question is unanswered.
- New code: `DYN_ABG`, `ABG_N`, `abgShort`, `r1`, `abgRead`, `abgMarks`, `dynAbg`; hooks in `dynSections`, `dynSet` (`abg:open|clear`),
  `kitArt` (draws the marks); `.abg-*` styles after `.dcmp`. Not in the address (Copy link doesn't carry the blood gas).
- **Rules = the ones abtime draws**: Winters ±2; met. alkalosis PaCO₂ +0.6 per HCO₃⁻ (±2 display tolerance — UNVERIFIED design
  choice); resp. acidosis HCO₃⁻ +1 (acute) / +3 (chronic) per 10 mm Hg; resp. alkalosis −2 / −4. **Conflict to resolve:** the
  `abcompensation` card says chronic respiratory acidosis ≈ +4 per 10 mm Hg, the map says +3 — fix whichever is wrong, and if the
  map changes, change `abgRead` too.
- `# UNVERIFIED`: normal ranges pH 7.35–7.45, PaCO₂ 35–45, HCO₃⁻ 22–26 (`ABG_N`).
- Tested in Chromium: 9 blood gases read as the rules give; dialog → graph marks → chip → clear; no chip on other moving maps;
  no page errors. `abtime`'s dyn data is untouched — the axes are copied into `DYN_ABG.abtime` (from a_abtime.py: X0 420, CW 475,
  plot tops 1180/1460/1740, height 220); if that module's layout moves, update them.

## lyteecg — Electrolytes & the ECG (`c_lyteecg.py`) · 2026-10-10 · topic Cardiac, after ecgsim
- **Switches:** `ly` (one) — Low K⁺ (`hypok`) · High K⁺ early / worse / severe (`hyperk`, First Aid's progression peaked T → wide
  QRS + P lost → sine wave) · High Ca²⁺ (`ecglytes`) · Low Ca²⁺ (`hypopara`) · Low Mg²⁺ (`mgpo4`). `rx` (one) — treat high K⁺ in
  order: IV calcium gluconate · insulin + glucose · β₂-agonist · bicarbonate · loop diuretic · binder (patiromer) · dialysis.
- **Drawing:** a lead II strip (3 beats, generated per state; sine wave and torsades drawn as their own traces) with the parts
  labelled and a QT bracket (normal / short / long); a muscle cell (Na⁺/K⁺-ATPase, K⁺ channel, calcium gluconate site); K⁺ exit
  routes (kidney, gut, dialysis) lit by the treatment; a "what the patient shows" row.
- **Readouts (6):** Serum K⁺ · T wave · QRS width · QT interval · Serum Ca²⁺ · K⁺ after the drug (↔ calcium gluconate, ↓ the rest).
- **Cards:** 0 new; 16 existing pinned on 7 nodes (ecglytes, hyperk, tls, rhabdo, digoxin, hypok, periodicpara, kinsulin,
  khandling, nakpump, hypopara, hyperpara1, mgpo4, longqt, loopdiuretics, ksparing).
- **Sources:** First Aid 2025 pp. 298, 348–349, 608–609 (as the pinned cards cite) · Costanzo ch 6 · Katzung ch 14–15 · Guyton ch 80.
- **`# UNVERIFIED` (2 facts):** calcium gluconate leaves K⁺ unchanged (readout ↔ + note) — inferred from the stabilize → shift →
  remove order; patiromer acting in the gut (the gut route box).
- Waveforms are schematic (caption says so). check.py: `lyteecg: 0 new cards, 7 nodes, 3 sites, 5 flows` · `OK · 0 warnings`.
  Looked at: Low K⁺; High K⁺ worse + loop diuretic (both zoomed).

## pthsim — Calcium & PTH Lab Simulator (`e_pthsim.py`) · 2026-10-10 · topic Endocrine, after hormones
- **Switch** `dz` (one): Primary (`hyperpara1`) · Secondary — kidney disease (`hyperpara2`) · Tertiary (`renalod`) · Vitamin D
  deficiency (`vitddef`) · Hypoparathyroidism (`hypopara`) · Pseudohypoparathyroidism (`pha`) · FHH (`fhh`) · Malignancy — PTHrP
  (`hcmalig`) · Sarcoidosis (`sarcoid`).
- **Drawing:** the four glands behind the thyroid (one adenoma / all four enlarged / dimmed / suppressed per option) with the
  Ca²⁺-sensing receptor (✕ "set too high" for FHH); bone with its PTH receptor; kidney — proximal PO₄³⁻ reabsorption, distal
  Ca²⁺ reabsorption, 1α-hydroxylase; gut Ca²⁺ absorption; the feedback loop with a tumor (PTHrP) or granulomas (calcitriol);
  a "what the patient shows" row. PTH receptors show ✕ "no response" for pseudohypoparathyroidism.
- **Readouts (5):** Serum Ca²⁺ · Serum PO₄³⁻ · PTH · Calcitriol · Urine Ca²⁺ — "–" wherever the pinned cards give no direction
  (e.g., PO₄³⁻ in FHH and sarcoidosis, calcitriol in vitamin D deficiency, urine Ca²⁺ outside primary and FHH).
- **Cards:** 0 new; 17 existing pinned on 9 nodes (pthaction, casr, calcitriol, vitddef, pthneph, renalpo4, hyperpara1,
  hyperpara2, renalod, hypopara, pha, hcmalig, sarcoid, fhh, ckdphos, ckd, calciumdrugs).
- **Sources:** First Aid 2025 pp. 336–337, 348–349, 361, 621–622 · Costanzo ch 9 · Guyton ch 80 · Katzung ch 42 · Robbins ch 24.
- **`# UNVERIFIED` (1 fact):** PTH ↓ in sarcoidosis (inferred from the hypercalcemia). Also for the checker: tertiary PO₄³⁻ ↑ rests on
  the `ckdphos` card (late CKD keeps phosphate high despite high PTH); the panel's "High Ca²⁺, PTH low → … vitamin D excess" row
  comes from the `vitddef` card's toxicity line.
- check.py: `pthsim: 0 new cards, 9 nodes, 7 sites, 6 flows` · `OK · 0 warnings`. Looked at: Primary; FHH (both zoomed).

## Site features · 2026-10-10 (code only — no sourcing)
- **"Missed it? Watch it move"** (`shared/app.js` `atlasLinksHtml`, `shared/style.css` `.atlas-move-cta`): after a wrong answer, when
  a moving map covers the right answer's card, the "See it move" link becomes a highlighted prompt at the top of the atlas box
  (practice, flagged, review and exam results all use this function). Unchanged after a right answer. Tested on nephro
  (5α-reductase question → Steroid Synthesis & CAH in Motion, 5α-Reductase switch on).
- **Weakest-maps mix** (atlas kit + Index — **the kit changed again**; kit.js updated): `weakMaps(n)` is now shared by the Index
  list and a new mix scope `"weak"`. The Index section "Your weakest moving maps" gets "▶ Mix your weakest — 10 Name-it
  questions"; the mix reads "Moving-map mix (your weakest maps)", missed options come back first as before, the scope chip
  offers "All moving maps", and if the weak list empties mid-mix it falls back to all moving maps. Tested with seeded scores.
