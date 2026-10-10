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

## Batch: the empty topics · 2026-10-10 — eight moving maps, 0 new cards, every one `OK · 0 warnings`
All facts restate pinned cards (fact-checked on the Mac) with their First Aid pages; curves, bar heights and example
numbers are schematic and say so on the map. Looked at one zoomed state of each.

### testsim — Diagnostic Test Simulator (`f_testsim.py`) · Biostats & Ethics, after biostats
- `cut` (steps: cutoff 44 / 50 / 56) × `prev` (steps: 1% / 10% / 50%). Healthy N(40, 8) and diseased N(60, 8) curves with FP/FN shaded,
  the ROC curve with the cutoff point, a 2 × 2 table for 1000 people and bars for sensitivity, specificity, PPV, NPV, plus LR+ — all
  computed from the formulas on `sensspec`, `ppvnpv`, `cutoff`, `likelihood`. Readouts (5) compare with middle cutoff at 10%,
  computed per state. Pins 10 cards. FA pp. 259–262. Looked at: low cutoff + 1% (PPV 3.2%, NPV 100%).

### pksim — Pharmacokinetics & Dose–Response Simulator (`g_pksim.py`) · Pharm, after pkpd
- `pk` (one): loading dose · double the dose · CYP inducer (t½ ×0.5) · CYP inhibitor (t½ ×2) · zero- vs first-order. A dose every
  half-life (bolus model) against a therapeutic window, with the 4–5 half-life steady-state band. `pd` (one): competitive ·
  noncompetitive · partial agonist · more potent agonist on a log dose–response curve. Readouts (5): steady-state level, time to steady
  state, half-life, potency, efficacy. Pins 12 cards (clearance, dosing, elimination, efficacypotency, antagonists, ti, cyp…).
  FA pp. 229–233, 251. Looked at: inhibitor + competitive antagonist.

### hypsim — Hypersensitivity Types in Motion (`h_hypsim.py`) · Immunology, after hypimm
- `ex` (one, 13): anaphylaxis, allergic asthma, blood in IgA deficiency · warm AIHA, myasthenia gravis, Graves, Goodpasture · SLE,
  serum sickness, Arthus · contact dermatitis, PPD, GVHD. Four mechanism columns (mast cell, antibody on a cell with the three outcomes,
  complexes in a vessel, T cells), a timeline of onset. Readouts (4): tryptase, allergen-specific IgE, complement, direct Coombs.
  Pins 16 cards. FA pp. 110–111. Looked at: myasthenia gravis.

### idsim — Immunodeficiency Simulator (`h_idsim.py`) · Immunology, after hypimm
- `id` (one, 12): Bruton, CVID, IgA deficiency, hyper-IgM, DiGeorge, SCID, Wiskott-Aldrich, Job, LAD, Chédiak-Higashi, CGD, C5–C9.
  The lymphocyte line and the neutrophil's path with an ✕ at the broken step, antibody bars per disorder, infection clues.
  Readouts (6): B cells, T cells, IgG, IgM, IgE, neutrophils — "–" where a card says "normal or ↓". Pins 17 cards. FA pp. 104–105,
  113–115, 126. Looked at: hyper-IgM.

### hypoxsim — Hypoxemia Simulator, A–a gradient & 100% O₂ (`i_hypoxsim.py`) · Pulmonary, after hypoxia
- `hx` (one): altitude, hypoventilation, V/Q mismatch, diffusion limitation, shunt, dead space (PE); `o2` toggle (100% O₂). One
  alveolus and capillary per cause, the alveolar gas equation worked through, the five causes checked off. Readouts (4): PaO₂, PaCO₂,
  A–a gradient, PaO₂ on 100% O₂. Pins 13 cards. FA pp. 684–687. Looked at: shunt on 100% O₂.
- **UNVERIFIED (2):** the example blood-gas numbers (illustrative, chosen for direction); the reason dead space widens the A–a gradient.

### pftsim — PFTs & Flow–Volume Loops (`i_pftsim.py`) · Pulmonary, after lungdz
- `pf` (one): emphysema/COPD, asthma, ILD, neuromuscular weakness, severe obesity. Flow–volume loop vs normal, RV/FRC/TLC bars, tags
  for FEV₁/FVC and DLCO. Readouts (5): FEV₁, FEV₁/FVC, TLC, RV, DLCO. Pins 9 cards. FA pp. 682–683, 692. Looked at: COPD.
- **Left "–":** RV in restriction and asthma's DLCO (no card gives them).

### injsim — Cell Injury & Death Simulator (`j_injsim.py`) · Pathology, after genpath
- `inj` (one): reversible, irreversible, apoptosis, coagulative, liquefactive, caseous, fat, fibrinoid, gangrenous. One cell through
  the stages and a tissue patch per necrosis pattern. Readouts (4): cell volume, membrane integrity, inflammation, serum enzymes.
  Pins 15 cards. FA pp. 202–206. Looked at: irreversible injury.
- **UNVERIFIED (1):** cell volume ↑ in irreversible injury.

### healsim — Inflammation & Wound Healing in Motion (`j_healsim.py`) · Pathology, after genpath
- `t` (steps, auto 5 s): minutes → inflammatory → proliferative → remodeling; `dx` (one): vitamin C, copper, zinc deficiency, LAD,
  hypertrophic scar, keloid. A venule with the four extravasation steps, a skin wound per phase, a tensile-strength bar. Readouts (4):
  neutrophils, macrophages, type III, type I collagen. Pins 5 cards. FA pp. 210–214. Looked at: proliferative + keloid.
- **UNVERIFIED (1):** macrophages shown ↑ only in the inflammatory step.
