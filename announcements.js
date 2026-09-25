'use strict';
/**
 * announcements.js — manual site banner for the OCOM Question Hub homepage.
 *
 * This file is NEVER touched by the SDL pipeline (question authorship, validation,
 * docx builds, or sync_hub_data.js) — it's edited by hand, on purpose, only when
 * Carlos decides something is worth broadcasting to everyone who opens the site.
 *
 * To post an update: fill in ANNOUNCEMENT below and set text to a non-empty string.
 * To take it down: set text back to '' (or the whole object to null). Either way
 * hides the banner — nothing else on the site depends on this file.
 *
 * Only one message shows at a time (the banner replaces its content each time you
 * edit this file) — this is intentionally not a running list/changelog.
 */

const ANNOUNCEMENT = {
  text: 'Added a Dr Williams final exam mode based on the email of the SDL split also added more maps to lesion atlas',
  // Optional short date label shown next to the message, e.g. 'Sep 8'. Leave '' to omit.
  date: '9/24/26',
};

// Example of a populated announcement (for reference — delete or ignore):
// const ANNOUNCEMENT = { text: 'SDL 12–42 question banks fixed for an answer-pattern issue — re-download if you saved copies before Sep 8.', date: 'Sep 8' };

window.ANNOUNCEMENT = ANNOUNCEMENT;
