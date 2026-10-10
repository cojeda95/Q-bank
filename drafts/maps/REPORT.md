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

## Batch: big gaps · 2026-10-10 — eighteen moving maps, 0 new cards, every one `OK · 0 warnings`
All facts restate the pinned cards (fact-checked on the Mac); `fa` and `src` are the union of the pinned cards' pages and
textbook chapters. All 29 drafts modules were inserted together into a scratch copy and built cleanly (270 maps, 73 moving).
Screenshots looked at: syncope (AS, torsades), fever & rash (Kawasaki), name the bug (Shigella), anemia (B12, dark theme),
pancreatitis (gallstone), amyloid (AL + polarized light), neoplasia (metastasis + tumor suppressor), blisters (pemphigus,
pemphigoid), lesions (ulcer), bias (confounding).

**Twelve are decision trees** built by one shared layout (pasted into each module, no kit change): a `one` switch picks the answer, the
path to it lights up (drawn under the boxes) and a dot travels it; a clue box shows that answer's tell; the readouts give the labs.
- **sxsyncope** — Syncope (`k_sxsyncope.py`) · Symptoms, after sxchest. 11 answers (reflex ×3, orthostatic ×3, AS, HCM, complete
  block, torsades, seizure mimic). Readouts: BP on standing, heart rate, QT, murmur with Valsalva. 12 cards.
  **UNVERIFIED (1):** heart rate ↓ in vasovagal/carotid sinus (standard, not on the syncope card).
- **sxedema** — Edema (`k_sxedema.py`) · after sxdyspnea. 8 answers (DVT, lymphedema, HF, dihydropyridine CCB, nephrotic, cirrhosis,
  kwashiorkor, leaky capillaries). Readouts: the four Starling forces + albumin. 9 cards.
  **UNVERIFIED (1):** Pc ↑ for DVT and CCBs (capfluid lists only heart failure for ↑ Pc).
- **sxfever** — Fever & Hyperthermia (`k_sxfever.py`) · after sxams. Fever vs NMS, serotonin syndrome, malignant hyperthermia,
  anticholinergic, sympathomimetic, heat stroke, thyroid storm. Readouts: set point, CK, sweating, pupils, reflexes. 11 cards.
- **sxrash** — Fever & Rash (`k_sxrash.py`) · after sxams. 12 answers by morphology (vesicles, macules, red tongue, palms/soles,
  petechiae, targets). Readouts: platelets, ESR/CRP, ASO, RPR. 13 cards.
- **sxweight** — Weight Loss (`k_sxweight.py`) · after sxams. Appetite up (thyroid, T1DM) vs down (TB, Hodgkin, cachexia, Addison,
  celiac, MDD, anorexia). Readouts: appetite, TSH, glucose, Na⁺, K⁺. 11 cards.
- **sxjoint** — Joint Pain (`k_sxjoint.py`) · after sxams. Tap the hot joint (septic, gout, CPPD) or read the pattern (RA, OA, AS,
  PsA, reactive, SLE). Readouts: synovial WBC, ESR/CRP, RF/anti-CCP, HLA-B27, ANA. 10 cards.
- **sxgibleed** — GI Bleeding (`k_sxgibleed.py`) · after sxabdpain. Upper (PUD, varices, Mallory-Weiss) vs lower (diverticulosis,
  angiodysplasia, Meckel, hemorrhoids, CRC, UC). Readouts: BUN:Cr, Hb, platelets, PT. 12 cards.
- **anemiasim** — Anemia Work-Up (`l_anemiasim.py`) · Heme/Onc, after rbc. MCV → iron studies / reticulocyte index / MMA; 12 answers.
  Readouts: MCV, retic index, ferritin, TIBC, LDH, MMA. 17 cards.
- **lftsim** — Liver Tests Decoder (`l_lftsim.py`) · GI, after liver. Bilirubin only (Gilbert, hemolysis, Dubin-Johnson), hepatocellular
  (acetaminophen, viral, alcohol, MASLD, AIH), cholestatic (CBD stone, PBC, PSC), ALP from bone. 6 readouts. 13 cards.
- **bugid** — Name the Bug (`m_bugid.py`) · Infectious, after microlab. 15 organisms through catalase → coagulase → novobiocin,
  hemolysis → optochin / bacitracin / 6.5% NaCl, maltose, lactose, oxidase, H₂S. Readouts are test results (↑ positive, ↓ negative):
  catalase, coagulase, lactose, oxidase. 20 cards.
- **ethicsim** — Who Decides? Consent & Capacity (`n_ethicsim.py`) · Biostats & Ethics, after ethics. Emergency, adult with capacity,
  therapeutic privilege, directive, surrogate, minor exceptions, emancipated, parents, Jehovah's Witness parent. No readouts (the
  answers are people). 7 cards.
- **designsim** — Study Design Picker (`n_designsim.py`) · after biostats. RCT, crossover, case series, cross-sectional, case-control,
  cohort, ecological, with the measure each gives. No readouts. 8 cards.

**Six are drawn:**
- **pancsim** — Pancreatitis in Motion (`l_pancsim.py`) · GI, after liver. Duodenum, ampulla, duct, acini, CBD; zymogens activate in
  the duodenum (enterokinase site) — or inside the gland for gallstone / alcohol / hypertriglyceridemia / hypercalcemia, with calcium
  soaps; chronic draws fibrosis and calcifications. Readouts: lipase, Ca²⁺, ALP/direct bili, TG, fecal elastase, glucose. 8 cards.
- **amylsim** — Amyloid in Motion (`o_amylsim.py`) · Pathology, after genpath. Precursor cell → β-sheet fibril → organs for AL, AA,
  β2-microglobulin, Aβ, calcitonin, amylin; toggle for Congo red under polarized light. 5 readouts. 11 cards.
  **UNVERIFIED (1):** "salmon pink under ordinary light" (the amyloidosis card gives only apple-green birefringence).
- **neosim** — Neoplasia in Motion (`o_neosim.py`) · Pathology, after neoplasia. `steps` (auto): normal → dysplasia → CIS → invasive →
  metastasis on a drawn epithelium/basement membrane/vessel; `one`: oncogene (one hit) vs tumor suppressor (two hits). Readouts: N:C
  ratio, basement membrane intact, E-cadherin, metalloproteinases. 11 cards.
- **blistsim** — Blisters — Where the Skin Splits (`m_blistsim.py`) · Musculoskeletal, after derm. SSSS, pemphigus, pemphigoid, DH,
  SJS/TEN drawn at their split level with the immunofluorescence pattern. Readouts (↑ present): Nikolsky, oral mucosa, eosinophils,
  anti-tTG. 9 cards.
- **lesionsim** — Skin Lesions Drawn to Scale (`m_lesionsim.py`) · after skinbasics. 14 lesion words in profile against a 1 cm ruler.
  Readouts: above the surface, > 1 cm, fluid-filled, below the basement membrane. 6 cards.
- **biassim** — Bias in Motion (`n_biassim.py`) · Biostats, after biostats. A study pipeline; 9 biases light the stage they enter
  (dropouts, confounder, screening timelines for lead-time/length-time) with the fix. No readouts. 5 cards. The lead-time years are
  illustrative and the map says so.

Dropped from the offer: the "gross vs micro pattern matcher" (injsim already draws each necrosis pattern) and a separate anemia
symptom map (anemiasim covers it).

## Features · 2026-10-10 — report a question, why-you-missed tags, Quiz me on moving maps (**the kit changed**; kit.js updated)
- **⚑ Report a problem** (`shared/app.js`, `shared/style.css`) on Practice, Review, Flagged and exam questions: reason + note → its own
  document `syncs/QREPORT-<block>-<ms>-<random>` in the sync's Firestore project (no PIN); unsent reports wait in `qbank_reports_v1`
  and retry when a block page opens. **`tools/reports.py`** lists them (`--block`, `--json`, `--delete <id>`). The rules already allow
  these document names (probe write + delete, both confirmed gone). Tested with Firestore intercepted in a headless browser.
- **Why did you miss it?** — after a wrong answer, three chips tag the attempt (`why`), synced (`sync.js mergeAttempts` keeps a tag
  from either side). Analytics → **Why You Miss**: counts, share, a tip for the top reason, and a Drill per reason (`#whymiss/<k>`).
- **Quiz me · 3 questions** — a chip on every moving map with linked questions, and on a Tour's last step (`mapQuizHref` in the kit);
  opens the block with the most linked questions at `#atlasmap/<map>/quick` (misses first, then unseen), ending on a summary with
  3 more / Practice the whole map / Back to the map. Tested on nephflow → nephro.
- PIPELINE.md documents all three.

## Batch: complement + ribs · 2026-10-10 — two moving maps, 0 new cards, both `OK · 0 warnings`
All 31 drafts modules insert and build together (272 maps).
- **complsim** — Complement in Motion (`h_complsim.py`) · Immunology, after innate. Classical / lectin / alternative entries feed a
  C3 hub that drives opsonization, anaphylatoxins and the MAC; the brakes (DAF/CD59 on a red cell, C1 esterase inhibitor) below.
  `def` (one): early components (C1q, C4, C2) · C3 deficiency · C5–C9 · eculizumab · HAE · PNH — ✕ on the broken step, flows stop or
  misfire (MAC onto the red cell in PNH, bradykinin in HAE). Readouts: C3, C4, CH50, LDH, haptoglobin. Pins 10 cards. FA pp. 104–106,
  113, 140, 427–428, 476, 676. Looked at: PNH.
  **UNVERIFIED (1):** "immune complexes cleared poorly" as the reason early-component deficiency predisposes to SLE.
- **ribsim** — Rib Motion in Motion (`n_ribsim.py`) · OMM, after ommmech. `br` (steps, auto 3 s): exhale/inhale drives four panels —
  pump handle (side), bucket handle (front), caliper ribs 11–12 (top), ribs 1–12. `dys` (one): ribs 4–6 as an inhaled group (key
  rib = bottom) or exhaled group (key rib = top) — BITE. `met` (one): the muscle-energy muscle for an exhaled rib at each level (rib 1
  anterior/middle scalenes · 2 posterior scalene · 3–5 pectoralis minor · 6–9 serratus anterior · 10–11 latissimus dorsi · 12 quadratus
  lumborum, from the ribresp card's course-slide table). Readouts: front-to-back depth, side-to-side width. Pins 6 cards. No FA pages
  (`fa=''`); sources Foundations ch 31/35, Atlas of Osteopathic Techniques ch 9–10, OCOM OMM texts. Looked at: inhale + exhaled
  group + ribs 6–9. The rib drawings are schematic.

## Batch: moving versions of ten static topics · 2026-10-10 — ten moving maps, 0 new cards, all `OK · 0 warnings`
Each sits next to the static map it animates (pins that map's cards; the static map is untouched). All 41 drafts modules
insert and build together (282 maps, 85 moving). Looked at one zoomed state of each.
- **energysim** — Energy Metabolism in Motion (`a_energysim.py`) · Biochemistry, after core. Glycolysis → PDH → TCA → complexes I–IV
  pumping H⁺ → ATP synthase. `blk` (one, 11): PK deficiency, PDH deficiency, thiamine, arsenic, fluoroacetate, rotenone, antimycin,
  cyanide, CO, oligomycin, uncoupler. Readouts: lactate, O₂ use, ATP, venous O₂ sat, temperature, citrate. 12 cards. Looked at: cyanide.
- **ureasim** — Urea Cycle in Motion (`a_ureasim.py`) · after nitrogen. Hepatocyte mitochondrion + cytosol; gut → liver → astrocyte.
  `def` (one): CPS-1/NAGS, OTC, ASS, ASL, arginase, hepatic encephalopathy, orotic aciduria (the look-alike). Readouts: ammonia, BUN,
  orotic acid, citrulline, MCV. 7 cards. Looked at: OTC. **UNVERIFIED (1):** aspartate in at ASS / fumarate out at ASL.
- **gsdsim** — Glycogen Storage Diseases in Motion (`a_gsdsim.py`) · after core. Liver (fasting) and muscle (exercise) side by side,
  `st` (steps) + `gsd` (one, 7: von Gierke, Pompe, Cori, Andersen, McArdle, Hers, Tarui). 6 readouts. 7 cards. Looked at: fasting + von
  Gierke. **UNVERIFIED (1):** muscle lacks glucose-6-phosphatase (the card lists liver, kidney, gut).
- **lsdsim** — Lysosomal Storage in Motion (`a_lsdsim.py`) · after lysosome. Golgi M6P tag → lysosome; `lsd` (one, 9) fills the
  lysosome with that substrate, or (I-cell) sends enzymes to the blood. Readouts (↑ present): HSM, cherry-red spot, corneal clouding,
  neuropathy, urinary GAGs, plasma enzymes. 11 cards. Looked at: Hurler.
- **rxsim** — Psych Drugs at the Receptors (`b_rxsim.py`) · Psych & Behavior, after psyrxprin. D₂ in the four dopamine pathways +
  5-HT₂A, H₁, muscarinic, α₁, Na⁺ channel, NET/SERT; `rx` (one, 7): haloperidol, chlorpromazine, clozapine, olanzapine, risperidone,
  aripiprazole, amitriptyline. 6 readouts. 9 cards. Looked at: chlorpromazine. **UNVERIFIED (1):** chlorpromazine's effects drawn at
  H₁/muscarinic/α₁ (the card names the effects, not the receptors).
- **sleepsim** — Sleep Stages in Motion (`b_sleepsim.py`) · after sleepdev. EEG per stage (`stg` steps, auto) + a schematic hypnogram
  with a moving dot; `who` (one): depression, narcolepsy, alcohol/benzodiazepines, aging. 4 readouts. 9 cards. Looked at: N2 + narcolepsy.
- **sexsim** — Sex Differentiation in Motion (`c_sexsim.py`) · Repro & Development, after sexdev. Gonad → ducts → external genitalia
  with AMH, testosterone and DHT flowing; `dx` (one, 9): typical XY/XX, Swyer, AIS, 5α-reductase, PMDS, CAH (46,XX), Turner,
  Klinefelter. Readouts: androgens, DHT, LH, FSH, estradiol. 9 cards. Looked at: PMDS. **UNVERIFIED (1):** Wolffian duct regressed in AIS.
- **pregsim** — Pregnancy Hormones in Motion (`c_pregsim.py`) · after placenta. A schematic 40-week hCG/progesterone/estriol chart with a
  cursor (`wk` steps) + corpus luteum, placenta, fetoplacental unit; `dx` (one): ectopic, mole, twins, trisomy 21, trisomy 18. 3 readouts.
  9 cards. Looked at: weeks 12–20 + trisomy 21.
- **antidsim** — Poison & Antidote in Motion (`g_antidsim.py`) · Pharm, after tox. Poison → target → harm; `give` toggle sends the
  antidote, which competes, binds (pair excreted), blocks/replenishes, or bypasses/replaces; `p` (one, 16 poisons). 4 readouts. 18 cards.
  Looked at: digoxin + Fab. **UNVERIFIED (1):** the mechanism lines for physostigmine, methylene blue and 100% O₂.
- **tcellsim** — T-Cell Activation in Motion (`h_tcellsim.py`) · Immunology, after immune. APC–T-cell synapse (MHC II–TCR, B7–CD28,
  CTLA-4, PD-1) → calcineurin → NFAT → IL-2 → CD25 → mTOR → clones; `x` (one, 8): anergy, superantigen, cyclosporine/tacrolimus,
  abatacept/belatacept, basiliximab, sirolimus, checkpoint inhibitor, bare lymphocyte syndrome. 4 readouts. 11 cards. Looked at:
  cyclosporine. **UNVERIFIED (1):** PD-L1 drawn on the APC (the card places it on tumor cells; the label says so).
