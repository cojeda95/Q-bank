'use strict';
/**
 * announcements.js — the Announcements list on the OCOM Question Hub home page.
 *
 * This file is NEVER touched by the SDL pipeline (question authorship, validation,
 * docx builds, or sync_hub_data.js) — it's edited by hand, on purpose, only when
 * Carlos decides something is worth broadcasting to everyone who opens the site.
 *
 * To post an update: add a new entry at the TOP of the list, e.g.
 *     { date: '10/9/26', text: 'Nephro exam 3 questions final revisions pushed' },
 * Optional extras on any entry:
 *     tag: 'Nephro'   a short label shown as a chip (a block, Atlas, Exam, Site — any word)
 *     pinned: true    keeps it at the top and highlighted, above newer ones (an exam date, say)
 * The home page shows the newest three (pinned ones first) and folds the rest under
 * "Show older". To take one down, delete its entry. Nothing else on the site depends
 * on this file.
 */

const ANNOUNCEMENTS = [
  { date: '10/9/26', text: 'General: UX redesign, Lestion Atlas: Added dynamic maps with manipulative variables, Nephro: Added Moorjani split for exam 2' },
  { date: '10/7/26', text: 'Nephro: Revisited Exam 2-4 Q generation with some new changes, piloting new question format w/ arrows and a test batch of new Qs; Atlas: worked on new maps and added sources for each card against OCOM library, PubMed articles, and First Aid 2025' },
  { date: '10/6/26', text: 'Added OMM Midterm questions, Nephro exams 3 and 4 still under review; new atlas maps pushed, fixed PIN-sync error' },
  { date: '10/5/26', text: 'Added OMM Midterm questions, Nephro exam 2 questions final revisions pushed, exams 3 and 4 still under review' },
  { date: '10/4/26', text: 'last 3 questions on SDL 11 re-written due to OBJ mismatch' },
  { date: '10/2/26', text: 'Moorjani split added for Exam 1 for Nephro based on email' },
  { date: '9/29/26', text: 'Nephro block fully pushed, minor changes for exams 2-3 still being refined' },
  { date: '9/25/26', text: 'Dr. williams final exam split, site-wide dark mode support, more atlas stuff' },
  { date: '9/24/26', text: 'Added a Dr Williams final exam mode based on the email of the SDL split also added more maps to lesion atlas' },
  { date: '9/17/26', text: 'Changed questions across Exam 3 and 4, metabolic map turned into a multi-system diagram thingy now' },
  { date: '9/16/26', text: 'Added a metabolic map to help visualize drugs, ODs, toxicities, and genetic mutations, check it out!' },
  { date: '9/15/26', text: 'Re-worked obvious wrong choices again, QC re-ran with new parameters, progress might be reset sorry' },
  { date: '9/9/26', text: 'Re-worked question logic and responses to make less obvious; added strike-through option for choice selection' },
  { date: '9/8/26', text: 'Re-worked question logic and responses to make less obvious' },
];

window.ANNOUNCEMENTS = ANNOUNCEMENTS;
