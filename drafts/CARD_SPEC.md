# m37 — Bootcamp batch: shared rules for every card writer

You are drafting Lesion Atlas cards for the OCOM Question Hub. The atlas source is
tools/atlas-src.html (read only for map writers — never edit it).
Your output is a Python file in drafts/m37/ (named in
your task) plus a short report as your final message.

## Sources — every line must be supported
- First Aid 2025: the corpus (not on this branch) (JSON: page number -> page text).
  Put the FA pages you used in `fa='…'` (e.g. fa='388, 391').
- Textbooks (plain text, one file per chapter) under the corpus (not on this branch):
  robbins/Ch_Robbins<N>.txt, katzung/Chapter_<N>_*.txt, guyton/Ch_Guyton<N>.txt, costanzo/Ch_<N>_*.txt,
  moore/, pawlina/, langman/Ch_<N>.txt, marks/, kaplan/, neurosci/ (Fundamental Neuroscience), degowin/.
  Cite with `full('Robbins', 24)` style (the helper builds the exact title — see below).
- Bootcamp decks (NEW source): the corpus (not on this branch)bootcamp/<subject>.txt
  (pages separated by "=== page N"; a content slide starts "Subject: Chapter" then "Bootcamp.com" then the slide title).
  Cite as a plain string: 'Bootcamp.com <Deck> — <Chapter>' e.g. 'Bootcamp.com Gastroenterology — Oral pathology',
  'Bootcamp.com Dermatology — Skin morphology', 'Bootcamp.com Hematology & Oncology — Transfusion medicine'.
  Deck names: Biochemistry, Biostatistics, Cardiology, Dermatology, Endocrinology, Gastroenterology, Genetics,
  Hematology & Oncology, Immunology, MSK, Microbiology, Nephrology, Neurology, Pathology, Pharmacology,
  Psychiatry, Public Health Sciences, Pulmonology, Reproduction.
- The decks also contain Bootcamp's own practice questions ("Question ID", answer choices). NEVER copy a
  question, its stem or its choices. Use the decks only as a source for facts, in your own words.
- Every fact on a card must be in at least one cited source. Prefer First Aid + a textbook; Bootcamp may be
  the only source for a line when FA/textbooks don't cover it. If you cannot find support, leave the line out.
- Write in your own words — short, plain, exam-useful. Never paste long passages.

## Card format (Python, using the shared helper)
```python
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full
RB = {c: full('Robbins', c) for c in (17,)}   # exact titles from titles.json
BC_GI = 'Bootcamp.com Gastroenterology — Oral pathology'

card('angcheil', 'Angular cheilitis', 'dz', 'orMuc', 'Cracks at the corners of the mouth', 1,
 '<one to three sentence mechanism, <b>bold</b> allowed>',
 ['<finding 1>', '<finding 2>'],          # find: 2–5 lines, HTML <b> allowed
 ['—'],                                   # labs: lines or ['—']
 ['<one short buzzword, NO html>'],       # buzz
 [RB[17], BC_GI],                         # src: textbook titles via full(), Bootcamp strings
 ['<treatment line>'],                    # tx: lines or ['—']
 ['angular cheilitis', 'angular stomatitis', '=cheilosis'],   # q: link terms (see below)
 alias='', fa='388')
```
- id: lowercase letters/digits, unique — check `grep -c '^<id>:{n:' tools/atlas-src.html` is 0.
- n (name): specific. The part before " — " becomes a link term, so never a generic word ("Overview", "Tumors").
- k: 'dz' (disease/finding), 'drug', or 'reg' (normal structure/physiology/process).
- p: the lane (path) key you define for the map (or the existing path key for gap cards).
- enz: one-line subtitle. hi: 1 if First Aid–level high yield, else 0.
- n / alias / enz / buzz must contain NO html tags. mech / find / labs / tx may use <b>.
- q (link terms): lowercase phrases ≥ 3 characters that would appear in a practice question's CORRECT ANSWER or
  the first sentence of its explanation when that question is about this card. Specific names, synonyms,
  eponyms, drug names. Never generic words ("pain", "tumor", "infection"). A term starting with "=" counts only
  in the answer itself — use it for longer answer-style phrases. 4–12 terms.
- Before writing a card, search atlas-src.html for an existing card on the same thing
  (grep -i the name and synonyms in lines starting with an id like `xxx:{n:"`). If one exists, DON'T duplicate —
  pin the existing card id on your map instead, and say so in your report.

## Map format (for new maps) — a variable MAP in your file
```python
MAP = dict(
  id='oral', title='Oral Cavity & Salivary Glands', topic='gi', after='gitract',   # topic id + the map it follows in the tab list
  sub='<one line: what the map covers, · separated>',
  fa='388–390', src=[RB[17], BC_GI],
  lanes=[  # 2–4 lanes; each lane has 1–2 rows of up to 5 nodes
    ('orMuc', 'Oral mucosa', 'glycolysis', 'Lips, tongue and mucosa', [
        [('o1', 'Angular cheilitis', 'cracked corners', ['angcheil'], 'hub'), ('o2', '…', '…', ['cardid']), …],
        [ … second row … ]]),
    ('orSal', 'Salivary glands', 'tca', 'Salivary glands', [[ … ]]),
  ],
  panels=[('<panel title (source)>', 0, [('<key>', '<value>'), …]), …],   # 1–2 panels, 3–7 rows each, sourced
  edges=[('o1','o2')],   # optional arrows, only between neighbours in the same row
)
```
- node tuple: (node id unique within map, label ≤ 26 chars, subtitle ≤ 40 chars, [card ids pinned], optional 'hub').
  Every node pins ≥ 1 card (new or existing). Lane colours: glycolysis, tca, gluconeo, ppp, glycogen, sugars.
  Lane keys: short camelCase, unique (prefix with your map's 2-letter code).
- Panels: tables of key facts (e.g. "Salivary gland tumors (Robbins ch 17)"). Every row sourced; title names the source.

## Report (your final message)
List: new card ids + names; existing cards you pinned; every source used; any claim you dropped for lack of
support; anything uncertain. Keep it under 300 words.
