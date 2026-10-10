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
- **csfsim** — CSF Flow in Motion (`e_csfsim.py`) · Neuro, after meninges. Choroid plexus → lateral ventricles → foramen of Monro →
  third ventricle → aqueduct → fourth ventricle → subarachnoid space → arachnoid granulations → sinus, plus the spinal canal
  (foramen magnum, C7, T12, conus, L3, L5, S2). `blk` (one, 11): Monro block, aqueductal stenosis, Dandy-Walker, communicating,
  NPH, ex vacuo, IIH, choroid plexus papilloma, syringomyelia, conus medullaris syndrome, cauda equina syndrome. The fourth-ventricle
  exits are drawn: Magendie (midline) and the paired Luschka (lateral), each with its own CSF dot; Dandy-Walker crosses out all three.
  Ventricles upstream
  of the block dilate and those downstream stay small. Readouts: ICP, lateral ventricle size, papilledema, leg reflexes, saddle anesthesia.
  10 cards. Checked in screenshots: aqueductal stenosis, default and Dandy-Walker. **UNVERIFIED (1):** Magendie midline /
  Luschka lateral (from the neuro question explanations; the csfflow card names only the foramina).
- **fetalsim** — Fetal Circulation in Motion (`c_fetalsim.py`) · Cardiac, after chd. Placenta → umbilical vein → ductus venosus →
  IVC → RA → foramen ovale → LA → brain; SVC → RV → pulmonary artery → ductus arteriosus → descending aorta → umbilical arteries.
  `st` (steps, auto): fetus, first breath, newborn (the shunts close and the remnant labels appear). `dx` (one, 6): PDA, PPHN, patent
  foramen ovale, D-TGA, indomethacin, alprostadil (PGE₁). Readouts: PVR, pulmonary blood flow, LA pressure, preductal − postductal
  sat, continuous murmur. 7 cards. Checked in screenshots: fetus, and newborn + PDA.
- **vestsim** — Vertigo in Motion (`d_vestsim.py`) · EENT, after cochflow. Both labyrinths (canals, utricle/saccule, cochlea) →
  CN VIII → vestibular nuclei (compare the sides) → MLF → eyes, plus the facial nerve to a face. The pupils show nystagmus as a drift
  (slow phase) and a jump (fast phase). `dx` (one, 11): head turn, warm/cold caloric, BPPV, Ménière, vestibular neuritis,
  labyrinthitis, vestibular schwannoma, AICA, PICA, Bell palsy. 5 readouts. 12 cards. Looked at: neuritis, AICA.
  **UNVERIFIED (1):** fast phase away from a one-sided loss — derived from two card lines (a lesion is read as a head turn away from
  that side; the fast phase follows the turn), not stated on one card.
- **murmursim** — Murmurs & Maneuvers in Motion (`c_murmursim.py`) · Cardiac, after valves. Chest with APT M + Erb point, a heart
  with the abnormal jet, and a phonocardiogram with a cursor. Two `one` switches: lesion (AS, HCM, MR, TR, VSD, ASD, MVP, AR, MS) ×
  maneuver (standing/Valsalva, squatting, leg raise, handgrip, inspiration, expiration); the murmur grows/shrinks, the MVP click
  moves. 3 readouts. 11 cards. Looked at: AS + handgrip, MVP + standing. **UNVERIFIED (1):** the card's general rules ("most
  murmurs"; expiration → left-sided louder) applied to lesions without their own line (TR, MS, VSD; MS, MVP).
- **pltsim** — Platelets in Motion (`l_pltsim.py`) · Heme/Onc, after coagflow. Injured vessel: collagen, vWF, adhesion row and
  aggregate; one platelet close up with GpIb, GpIIb/IIIa, P2Y12 and COX-1 sites. `dz` (one, 11): ITP, TTP/HUS, DIC, vWD,
  Bernard-Soulier, Glanzmann, uremia, aspirin, clopidogrel, abciximab, HIT. 5 readouts (count, bleeding time, PT, PTT,
  schistocytes). 12 cards. Looked at: Glanzmann, TTP.
- **watersim** — Water Balance in Motion (`r_watersim.py`) · Renal, after urineconc. Hypothalamus → posterior pituitary → ADH in the
  blood → V2 receptor → aquaporin-2 → water into the hyperosmotic medulla; urine cup. `dx` (one, 9): water deprivation, water load,
  SIADH, central DI, nephrogenic DI, primary polydipsia, lithium, desmopressin, vaptans; toggle `dd` gives desmopressin on top (the
  DI work-up). 5 readouts. 11 cards. Looked at: SIADH, nephrogenic DI, central DI + desmopressin.
- **odcsim** — The O₂ Curve in Motion (`i_odcsim.py`) · Pulmonary, after gasx. A schematic dissociation curve (shapes drawn, no
  P50 numbers shown) with a dot riding lungs → tissues and an "unloaded" bracket, plus a red cell. `sh` (one, 13): exercise, Bohr,
  fever, altitude, cold, HbF, myoglobin, CO, methemoglobin, anemia, polycythemia, cyanide, sickle cell. 5 readouts. 9 cards.
  Looked at: CO, Bohr.
- **archsim** — Pharyngeal Arches in Motion (`c_archsim.py`) · Repro & Development, after embryo. Clefts / arches / pouches (CAP)
  with neural crest flowing into the arches and the outflow tract; face and neck beside. `dx` (one, 7): DiGeorge, Treacher Collins,
  Pierre Robin, cleft lip, cleft palate, thyroglossal duct cyst, pharyngeal cleft cyst. 5 readouts. 6 cards. Looked at: DiGeorge,
  Pierre Robin.
- **toxinsim** — Bacterial Toxins in Motion (`m_toxinsim.py`) · Infectious, after toxins. A gut cell (Gs, Gi, adenylyl cyclase,
  GC-C, cAMP/cGMP → CFTR, ribosome/EF-2), two synapses (NMJ; inhibitory interneuron) and an APC–T-cell pair. `tx` (one, 10):
  cholera, E. coli LT and ST, pertussis, diphtheria, Pseudomonas exotoxin A, C. perfringens α-toxin, botulinum, tetanus,
  superantigen. 5 readouts. 9 cards. Looked at: cholera, tetanus.
- Kit unchanged for all seven.
- **aasim** — Amino Acid Disorders in Motion (`a_aasim.py`) · Biochemistry, after nitrogen. Three catabolic lines (Phe → Tyr →
  melanin / catecholamines / homogentisate → FAA → fumarate; BCAAs → α-ketoacids → propionyl-CoA → methylmalonyl-CoA → succinyl-CoA;
  Met → homocysteine → cystathionine → cysteine with remethylation) + a tubule with the two transporters. `dx` (one, 12): PKU, BH4,
  albinism, alkaptonuria, tyrosinemia I, MSUD, propionic, methylmalonic, homocystinuria (CBS / remethylation), Hartnup, cystinuria.
  Substrate piles up, spill box names the product. 6 readouts. 10 cards. Looked at: PKU, MMA.
- **faosim** — Fatty Acid Oxidation in Motion (`a_faosim.py`) · Biochemistry, after lipid. Blood → acyl-CoA → CPT-I/CPT-II →
  β-oxidation spiral → acetyl-CoA → ketones/ETC; peroxisome (ABCD1, α-oxidation, plasmalogens). `fast` toggle (default on) + `dx`
  (one, 7): carnitine deficiency, valproate, CPT-II, MCAD, Refsum, X-ALD, Zellweger. 7 readouts. 8 cards. Looked at: MCAD, X-ALD.
- **sugarsim** — Fructose & Galactose in Motion (`a_sugarsim.py`) · Biochemistry, after core. Fructose (fructokinase, aldolase B),
  galactose (lactase, galactokinase, GALT, aldose reductase → galactitol in the lens), polyol (aldose reductase, sorbitol DH).
  `dx` (one, 5): HFI, essential fructosuria, classic galactosemia, galactokinase, hyperglycemia. 6 readouts. 5 cards. Looked at: GALT.
- **chemosim** — Chemo & DNA Repair in Motion (`l_chemosim.py`) · Heme/Onc, after chemo. Cell-cycle wheel with cells moving and
  checkpoints, a DNA strip, nucleotide supply, spindle and the five repair pathways. `rx` (one, 13 drugs) piles cells at their phase,
  marks the DNA lesion, gives the toxicity; `rp` (one, 5): XP, Lynch, BRCA, Fanconi, A-T. 5 readouts. 20 cards. Looked at:
  vincristine, cisplatin + A-T.
- **aortasim** — The Aorta in Motion (`c_aortasim.py`) · Cardiac, after vasc. Heart → arch branches (vertebral) → descending →
  renals → iliacs, + an artery-wall inset; `pl` (steps, auto): dysfunction → fatty streak → fibrous plaque → complicated;
  `dx` (one, 8): AAA, TAA, dissection A/B, subclavian steal (vertebral flow reverses), PAD, cholesterol emboli, Mönckeberg.
  5 readouts. 8 cards. Looked at: steal + fibrous plaque, dissection A.
- **szsim** — Antiseizure Drugs in Motion (`e_szsim.py`) · Neuro, after seizhead. Excitatory neuron (Na⁺ channel, Ca²⁺ channel,
  SV2A, glutamate), inhibitory interneuron (GABA-A), glia (GABA transaminase), thalamocortical loop (T-type Ca²⁺), EEG strip.
  `sz` (one, 4) × `rx` (one, 9). 4 readouts. 12 cards. Looked at: absence; focal + valproate.
- **parasim** — Parasite Life Cycles in Motion (`m_parasim.py`) · Infectious, after fungpar. Schematic body with three ways in;
  `p` (one, 15) sends the parasite along its route (dashed path + moving dots), lights the organs it damages, tags finding + drug.
  5 readouts. 12 cards. Looked at: Strongyloides, P. vivax.
- **esosim** — Swallowing in Motion (`g_esosim.py`) · GI, after gitract. Pharynx → UES → esophagus → LES → stomach, bolus on a
  peristaltic wave; `liq` toggle (solids/liquids) + `dx` (one, 9): achalasia, distal esophageal spasm, GERD, Barrett, Schatzki ring,
  stricture, Plummer-Vinson web, Zenker, Mallory-Weiss. 5 readouts. 9 cards. Looked at: achalasia, Zenker.
- **pedsim** — Pedigree Simulator (`a_pedsim.py`) · Biochemistry, after genetics. One three-generation family; `mode` (steps, 5
  patterns) fills it in, `gen` (steps, auto) reveals generations while the mutant allele travels down. 3 readouts. 5 cards.
  Looked at: XLR, AR, mitochondrial. The families are illustrations (one possible family per pattern), stated on the map.
- **avsim** — Antiviral Targets in Motion (`m_avsim.py`) · Infectious, after antiviral. Four cells: herpes (drug → viral kinase →
  host kinases → DNA polymerase), HCV (polyprotein, NS3/4A, NS5A, NS5B), HBV (cccDNA, pgRNA, RT), influenza (PA endonuclease,
  neuraminidase). `hv` (steps HSV/CMV) + `tk` toggle (kinase-mutant) + `rx` (one, 10). 4 readouts. 13 cards. Looked at:
  acyclovir on CMV, foscarnet on a TK mutant. HIV left to hivflow.
- Kit unchanged for all ten. Also fixed: `chemosim` used `var(--ink-1)`, which isn't defined — now `var(--ink)`.
- **cransim** — Cranial Mechanism in Motion (`o_cransim.py`) · OMM, after cranial. Sphenoid and occiput at the SBS from the side
  (flexion/extension, `ph` steps auto), from behind (torsion, rotation) and from above (side bending, lateral strain), with CSF
  fluctuation moving. `st` (one, 6 strains) + `tx` (one: CV4, V-spread, venous sinus drainage, condylar). 3 readouts. 14 cards.
  `fa` empty — the cards cite the Atlas of Osteopathic Techniques ch 18 and OCOM OMM, no First Aid pages. Looked at: flexion +
  torsion; extension + lateral strain + venous sinus.
- **pelvsim** — Pelvis in Motion (`o_pelvsim.py`) · OMM, after cranial. Pelvis from the front (ASIS, pubic tubercles) and behind
  (PSIS under the thumbs); `ph` (steps auto: upright/bending) × `test` (standing/seated) × `dx` (one, 9 left-sided dysfunctions);
  the thumb on the restricted side rides farther up, landmarks move as the cards say. 3 readouts. 5 cards. `fa` empty (Foundations
  ch 31, 37–38; OCOM OMM). Looked at: standing + anterior innominate; outflare (caught and fixed reversed PSIS flare directions).
- **vaxsim** — Vaccines in Motion (`h_vaxsim.py`) · Immunology, after vaccines. Injection site → APC → helper and cytotoxic T → B
  cell → plasma cells and memory, toxin box; `vx` (one, 7). Polysaccharide bypasses T cells, conjugate brings T help. 5 readouts.
  6 cards. Looked at: polysaccharide, conjugate.
- **mapksim** — Growth Signals in Motion (`l_mapksim.py`) · Heme/Onc, after carcino. Growth factor → EGFR/HER2 → RAS (NF1 brake) →
  BRAF → MEK → ERK → MYC; `mut` (one, 6 drivers) × `rx` (one, 4 drugs). A drug is shown working only against the driver its card
  names (no inferred downstream efficacy). 3 readouts. 6 cards. Looked at: KRAS + cetuximab, BRAF + BRAF/MEK.
- **bcellsim** — B Cells & Lymphomas in Motion (`l_bcellsim.py`) · Heme/Onc, after hemeonc. Marrow → blood → follicle (mantle,
  germinal center, marginal zone) → plasma/memory, spleen, brain, chronic-antigen box; `ly` (one, 10) lights where each arises or
  lives, only where the card names it (Burkitt says so). 4 readouts. 10 cards. Looked at: follicular.
- **embsim** — Embryo & Gut-Tube Defects in Motion (`c_embsim.py`) · Repro & Development, after embryo. Weeks 1–8 timeline (`wk`
  steps auto) with teratogen timing, and the fetal amniotic-fluid cycle (urine → fluid → swallowing → gut); `dx` (one, 8) breaks it,
  `tg` (one, 7 teratogens). 4 readouts. 13 cards. Looked at: week 3 + TEF; week 4 + Potter + thalidomide.
- **aqsim** — Aqueous Humor & Retina in Motion (`d_eyesim2.py`) · EENT, after eyesim. Ciliary body → posterior chamber → pupil →
  angle → Schlemm, plus retina with central artery/vein, macula, disc; `dx` (one, 12) × `rx` (one, 6 incl. contraindicated
  mydriatic). 5 readouts. 11 cards. Looked at: acute angle closure; CRAO + latanoprost.
- **utisim** — UTI & Incontinence in Motion (`r_utisim.py`) · Renal, after akickd. Kidneys → ureters → bladder → urethra, urine
  down and bacteria up; `dx` (one, 7: cystitis, acute and chronic pyelo, malakoplakia, stress/urgency/overflow). 5 readouts. 5 cards.
  Looked at: acute pyelonephritis.
- **bonesim** — Bones & Kids by Age in Motion (`j_bonesim.py`) · Musculoskeletal, after bone. Long bone (epiphysis, physis,
  metaphysis, diaphysis), child's hip, tibial tuberosity, elbow, forearm; `age` (steps auto, 6) × `dx` (one, 15). 3 readouts.
  14 cards. Looked at: adolescent + osteosarcoma; 5–7 + Perthes. **UNVERIFIED (1):** Ewing ("boy") and osteochondroma ("young
  male") placed in the adolescent band — the cards give no age range.
- Kit unchanged for all nine. Also fixed in passing: two shapes drawn with `when=[]` (always shown) in mapksim and bonesim drafts
  before they were saved.

## Batch: nine more moving maps · 2026-10-10 — 0 new cards, all `OK · 0 warnings`
Facts drawn only from the pinned cards; where a card is silent the map leaves the step out and says so in the module header.
All 78 drafts modules pass check; no duplicate map ids or lane keys.
- **colsim** — Collagen Assembly in Motion (`a_colsim.py`) · Biochemistry, after collagen. α-chains (Gly-X-Y) → hydroxylation (vit C,
  Fe²⁺) → triple helix → propeptides cut → lysyl oxidase cross-links (Cu); `dx` (one, 8: scurvy, OI, kyphoscoliotic, arthrochalasia,
  dermatosparaxis, Menkes, vascular, classic) × `ty` (one, types I–IV). No glycosylation step and no in/out-of-cell location — no card
  states them. 11 cards. `fa` 48, 49, 67, 212.
- **frysim** — Spinal Mechanics & OMT in Motion (`o_frysim.py`) · OMM, after omt. T3–T9 from behind + top-view vertebra; `fr` (one:
  type I group curve, type II single segment, Principle III) × `tx` (one, 7 techniques) on an ease–neutral–barrier strip. 8 cards.
  `fa` empty (OMM cards cite no First Aid pages).
- **lbpsim** — Low Back Pain in Motion (`o_lbpsim.py`) · OMM, after lbp. Lumbar side view with `pos` (steps auto: flexion, neutral,
  extension) + pelvis/legs from behind; `dx` (one, 6: disc, stenosis, spondylolisthesis, psoas, leg length, iliolumbar), each with
  its OMT line. 6 cards. `fa` empty.
- **pnasim** — Pneumonia in Motion (`i_pnasim.py`) · Pulmonary, after respinf. Mucociliary escalator, alveolar macrophage, one lobe
  through `st` (steps auto: congestion → red → gray hepatization → resolution); `dx` (one, 6 defense failures, mycoplasma, abscess).
  4 readouts. 5 cards. `fa` 125, 134, 148, 188, 680, 702.
- **gxsim** — Bacterial Gene Transfer in Motion (`m_gxsim.py`) · Infectious, after microlab. Donor → recipient; `gx` (one:
  transformation, F⁺ conjugation, Hfr, generalized and specialized transduction, transposition) + `dnase` toggle (blocks
  transformation only). 4 cards. `fa` 128, 129.
- **altsim** — Climbing to Altitude in Motion (`i_altsim.py`) · Pulmonary, after highalt. Climber on a mountain, `alt` (steps auto:
  sea level, 10,000 ft, 20,000 ft, 20,000 ft acclimatized) with barometric and alveolar PO₂ bars (card numbers only), ventilation
  1.65× → ≈5×, renal HCO₃⁻ excretion, Hct 40–45 → ≈60%; `dx` (one, 6: AMS, HACE, HAPE, chronic mountain sickness, natives, O₂).
  5 readouts. 5 cards. `fa` 299, 688. Looked at: acclimatized; 20,000 ft + HAPE.
- **scrotsim** — The Scrotum in Motion (`c_scrotsim.py`) · Repro & Development, after malerepro. Aorta, IVC, kidneys, testicular
  arteries, gonadal veins (left into the renal vein at a right angle), close-up testis/epididymis/tunica; `dx` (one, 8: torsion,
  epididymitis, left and right varicocele, hydrocele, spermatocele, cryptorchidism, germ cell tumor) + `lift` (Prehn) and `light`
  (transillumination) toggles, both off by default. The descent path is a labelled schematic — no card gives its stages. 5 readouts.
  6 cards. `fa` 669, 670, 671. Looked at: torsion; hydrocele + light (caught and fixed toggles starting on — `def_` was not remapped).
- **btsim** — Brain Tumors in Motion (`e_btsim.py`) · Heme/Onc, after tumcns. Midline brain with ventricles, aqueduct, 4th ventricle,
  pineal, sella, cerebellum, tentorium and cord, CSF flowing; `tu` (one, 11) grows each tumor where its card puts it — those that
  block CSF dilate the ventricles, medulloblastoma drops metastases, hemangioblastoma raises red cells; `ag` (one: children, adults)
  rings the tumors the cards tie to each age. CPA drawn on the midline view, labelled lateral. 6 readouts. 12 cards. `fa` 539, 540,
  542. Looked at: medulloblastoma; glioblastoma + children; meningioma (moved the corpus callosum label off the butterfly).
- **myelsim** — Myeloid Neoplasms in Motion (`l_myelsim.py`) · Heme/Onc, after hemeonc. Stem cell → red-cell, granulocyte and
  platelet lanes → blood, spleen, skull/skin box; `dx` (one, 9: AML, APL, MDS, CML, blast crisis, PV, ET, myelofibrosis, LCH) +
  `drug` toggle (card-stated treatment for AML, APL, CML, PV). Intermediate granulocyte stages left unnamed — no card names them.
  6 readouts. 6 cards. `fa` 436, 437, 438, 439, 440, 447. Looked at: APL; myelofibrosis.
- **UNVERIFIED (0)** in this batch. Kit unchanged for all nine.

## Batch: twelve more moving maps · 2026-10-10 — 0 new cards, all `OK · 0 warnings`
Facts drawn only from the pinned cards; where a card is silent the map leaves it out and says so in the module header. All 90
drafts modules pass check; no duplicate map ids (the emboli map was first drafted as `embsim`, which the embryo map already
uses — renamed `embolsim` before saving) or lane keys. Readout note: the kit **sums** readout mods, so a `d=0` mod does not
cancel an overlapping `d=±1`; four drafts in this batch had such overlaps and were fixed (hasim, myelsim, embolsim, cyansim).
The previously pushed maps were audited — their `d=0` mods are all on mutually exclusive options, so they are unaffected.
- **bleedsim** — Head Bleeds in Motion (`e_bleedsim.py`) · Neuro, after neuroer. Coronal section with sutures, dura, falx,
  tentorium, foramen magnum; `dx` (one: epidural, acute and chronic subdural, SAH) × `ph` (steps auto: injury, early, later — lucid
  interval, midline shift, vasospasm) × `hx` (one: subfalcine, uncal, central, tonsillar herniation). 5 readouts. 4 cards.
  `fa` 528, 530, 543. Looked at: epidural late + uncal; chronic subdural; SAH + tonsillar (moved cerebellum and brainstem inside the skull).
- **sacsim** — The Sacrum in Motion (`o_sacsim.py`) · OMM, after ommmech. Posterior view, sulci, ILAs, oblique axes; `walk` (steps
  auto, shown only when nothing is stuck) × `dx` (one, 6: L-on-L, L-on-R, left unilateral flexion, right unilateral extension,
  bilateral flexion/extension) + `sphinx` toggle. Only card-stated landmark sets drawn — no mirrored R-on-R / R-on-L. 2 readouts.
  5 cards. `fa` empty (OMM cards cite no First Aid pages).
- **akisim** — Acute Kidney Injury in Motion (`r_akisim.py`) · Renal, after akickd. Aorta → arterioles → glomerulus → tubule →
  bladder → prostate; `dx` (one, 8: hypovolemia, NSAID, ACEi/ARB, ATN oliguric and recovery, AIN, GN, BPH) with Na⁺ reclaim, casts,
  back-pressure and the card cut-offs (BUN:Cr, FENa, Uosm). 4 readouts. 5 cards. `fa` 597, 601, 607, 612, 618, 620, 621.
- **embolsim** — Emboli in Motion (`p_embolsim.py`) · Pathology, after thromboemb. Whole-body circulation; `dx` (one, 6: DVT → PE,
  fat, central-line air, decompression bubbles, amniotic fluid, left-atrial thrombus) + `pfo` toggle (paradoxical). 5 readouts.
  6 cards. `fa` 284, 321, 691.
- **bowelsim** — Bowel Blockages in Motion (`g_bowelsim.py`) · GI, after gitract. Gut as one tube with aorta/SMA; `dx` (one, 10: SBO,
  ileus, intussusception, midgut and sigmoid volvulus, mesenteric and colonic ischemia, appendicitis, Hirschsprung, NEC). 5 readouts.
  7 cards. `fa` 61, 390, 391, 392, 393.
- **cyansim** — Cyanotic Heart Disease in Motion (`c_cyansim.py`) · Cardiac, after chd. Four chambers, lungs, body, blue/red/mixed
  blood; `dx` (one, 6: truncus, tricuspid atresia, TAPVR, Ebstein, TOF, d-TGA) + `squat` and `pda` toggles. 3 readouts. 6 cards.
  `fa` 285, 302.
- **demsim** — Dementias Over Time (`e_demsim.py`) · Neuro, after cortex. Side view with lobes, hippocampus, ventricles, midbrain;
  `dx` (one, 7: Alzheimer, FTD, Lewy, vascular, PSP, CJD, NPH) × `yr` (steps auto: early, middle, late) + `shunt` toggle. Spread
  drawn only as far as each card states. 3 readouts. 8 cards. `fa` 174, 534, 535, 536.
- **spreadsim** — Seizure Spread in Motion (`e_spreadsim.py`) · Neuro, after seizhead. Top view of both hemispheres + thalamus +
  schematic EEG; `ph` (steps auto: aura, ictal, postictal) × `ty` (one, 6: focal aware, focal impaired, secondarily generalized,
  absence, status, PNES) × `age` (one: causes by age, febrile). 3 readouts. 6 cards. `fa` 177, 530, 531.
- **papezsim** — The Papez Circuit in Motion (`b_papezsim.py`) · Psych & Behavior, after limbmem. Midline limbic loop + hippocampal
  inset (EC → DG → CA3 → CA1 → subiculum), amygdala fear output, VTA → accumbens; `dx` (one, 9 lesions). Positions schematic.
  4 readouts. 8 cards. `fa` 64, 505, 509, 524, 575.
- **lcsim** — Lung Cancer in Motion (`i_lcsim.py`) · Pulmonary, after lungcancer. Chest with SVC and mediastinal nerves, target organs;
  `dx` (one, 7: adeno, squamous, small cell, large cell, carcinoid, Pancoast, SVC syndrome) with card-stated hormones (ACTH, ADH,
  PTHrP, hCG) + `tki` toggle. 4 readouts. 8 cards. `fa` 224, 352, 446, 703, 704.
- **carditsim** — Heart Infection & Inflammation in Motion (`c_carditsim.py`) · Cardiac, after valves. Heart and valves, throat,
  joints, embolic targets; `dx` (one, 8: acute, subacute and tricuspid endocarditis, acute rheumatic fever, chronic rheumatic
  stenosis, NBTE, myocarditis, myxoma). 5 readouts. 5 cards. `fa` 318, 319, 320.
- **hasim** — Headaches in Motion (`e_hasim.py`) · Neuro, after seizhead. Side view with meningeal vessels, trigeminal V1–V3, CN V
  root; `dx` (one: migraine, tension, cluster, trigeminal neuralgia) × `ph` (steps auto: aura, headache) × `rx` (one, 6) — a drug
  works only where its card lists it for that headache. Aura origin not drawn (card silent). 4 readouts. 4 cards. `fa` 532.
- **UNVERIFIED (0)** in this batch. Kit unchanged for all twelve.

## Batch: twelve more moving maps (protozoa → viruses) · 2026-10-10 — 0 new cards, all `OK · 0 warnings`
Facts drawn only from the pinned cards; where a card is silent the map leaves it out or labels the drawing schematic. All 102
drafts modules pass check; no duplicate map ids. Lane-key note: check.py compares lane keys only against the live atlas, so a
clash between two drafts slips past it — the pain map first reused `pnDz` (pneumonia map) and was renamed `pwDz`/`pwPath`.
- **protosim** — Protozoa in Motion (`m_protosim.py`) · Infectious, after fungpar. Body with brain, nodes, heart, gut, liver/spleen,
  skin, red cells, genital tract; `dx` (one, 6: Naegleria, T brucei, Babesia, T cruzi, Leishmania, Trichomonas) + `asplen` and
  `treat` toggles. Vectors named only where the card names them. 5 readouts. 6 cards. `fa` 153, 154, 155.
- **shsim** — The Shoulder in Motion (`j_shsim.py`) · Musculoskeletal, after shoulder. Arm abducts in `ab` steps (0–150°) with SALT
  muscles lighting; `dx` (one, 5: impingement, cuff tear, frozen shoulder, GH OA, AC OA). Frozen-shoulder stop angle is schematic.
  4 readouts. 5 cards. `fa` 451.
- **anessim** — Anesthetics in Motion (`n_anessim.py`) · Pharm, after anesth. Alveolus → blood → brain bars with a MAC line; `ag`
  (one: N₂O, volatile, propofol, etomidate) × `t` (steps) + `sux` (malignant hyperthermia) and `ptx` toggles. Bar heights schematic.
  6 readouts. 4 cards. `fa` 565, 566.
- **laxsim** — Laxatives in Motion (`g_laxsim.py`) · GI, after gidrugs. Lumen, epithelium (ClC-2, GC-C → CFTR, NHE3), enteric plexus;
  `rx` (one, 9) + `opioid` toggle (PAMORA undoes it). 3 readouts. 5 cards. `fa` 130, 399, 408, 567.
- **cystsim** — Kidney Cysts in Motion (`r_cystsim.py`) · Renal, after renvasc. Kidney section sized per disease + primary-cilium
  inset; `dx` (one, 8: ADPKD, ARPKD, medullary cystic, nephronophthisis, sponge kidney, multicystic dysplasia, simple, complex).
  4 readouts. 8 cards. `fa` 58, 596, 597, 622.
- **footsim** — The Foot in Motion (`j_footsim.py`) · Musculoskeletal, after footleg. Medial side view + forefoot top view; `st`
  (steps: heel, midfoot, push-off) × `dx` (one, 8) + `morning` toggle. Geometry schematic. 4 readouts. 6 cards. `fa` 465, 491, 538, 545.
- **fxsim** — Growth Plates & Arm Injuries in Motion (`j_fxsim.py`) · Musculoskeletal, after sportsortho. Salter-Harris I–V on a bone
  end (`sh`) + upper limb with the nerve at each landmark (`inj`, one, 9). 3 readouts. 6 cards. `fa` 450, 463, 467.
- **painsim** — Pain Gone Wrong in Motion (`n_painsim.py`) · Pharm, after pain. Spinothalamic route to VPL and S1; `dx` (one:
  neuropathic, thalamic, phantom, fibromyalgia) × `rx` (one, 5) — pain eases only where the card pairs drug and condition.
  4 readouts. 6 cards. `fa` 235, 477, 529.
- **labsim** — Lab Techniques in Motion (`a_labsim.py`) · Biochemistry, after molbio. `tech` (one, 9: PCR, Southern, Northern, Western,
  ELISA, flow, karyotype, FISH, CRISPR) × `ph` (steps 1–3). Drawings schematic. 2 readouts. 4 cards. `fa` 50, 51, 52, 53.
- **alvdzsim** — Alveoli in Trouble in Motion (`i_alvdzsim.py`) · Pulmonary, after lungdz. Two alveoli (Laplace), lungs with apices and
  bases, RV; `dx` (one, 7: neonatal RDS, coal, silica, asbestos, beryllium, PAP, pulmonary hypertension) + `beta` toggle.
  5 readouts. 4 cards. `fa` 679, 696, 698, 706.
- **prossim** — The Prostate in Motion (`c_prossim.py`) · Repro, after prosobs. Zones, urethra, ejaculatory ducts, rectum, spine,
  gland-lining and Gleason insets; `dx` (one: BPH, HGPIN, adenocarcinoma) × `gl` (one, 4 scores) + α₁-blocker and finasteride
  toggles. Zone shapes schematic. 4 readouts. 6 cards. `fa` 646, 647, 672, 673.
- **negsim** — Negative-Strand Viruses in Motion (`m_negsim.py`) · Infectious, after virus. Body with nerve, airway, glands, vessels;
  `dx` (one: rabies, RSV, croup, mumps, Ebola) + `pep` toggle (rabies immune globulin + vaccine; palivizumab). 5 readouts. 5 cards.
  `fa` 164, 166, 167, 169.
- **UNVERIFIED (0)** in this batch. Kit unchanged for all twelve.

## Feature · 2026-10-10 — floating switches on wider screens (**the kit changed**; kit.js updated)
- On screens wider than 1000 px the phone sheet (#dynSheet) now also serves as a **floating, draggable, resizable card**
  over the map. It keeps the same on-screen size at any zoom. **Auto** (default): it appears once the canvas panel is
  less than ~85% on screen (you zoomed in) and disappears when the panel is back in view. **Pin** keeps it up at any zoom;
  **Hide** leaves a "Switches ▴" button that brings it back pinned. Position and mode are remembered per device
  (`mla-dsfloat`, `mla-dsfloat-pos`). Phones keep the docked sheet unchanged.
- Code: kit section (`dsDesk`, `dynPanelOut`, `dynFloatCheck`, `dsPlace`, `dsSave`; `dynSheetRender` / `dynSheetInit`
  branches), **plus two edits outside the kit section** that the owner's batch tooling does not carry: `applyCam` now calls
  `dynFloatCheck()`, and a `@media (min-width:1001px)` CSS block after the m40 phone-sheet CSS.
- Tested headless (Chromium, 1600×1000, Nephron in Motion): hidden at Fit → appears after 4× zoom-in → a chip click
  switches the map and the address → drag moves it and saves the spot → Fit hides it → Hide shows the button → button
  pins it, still up at Fit → at 420 px wide the old docked sheet shows. No page errors. PIPELINE.md documents it.
