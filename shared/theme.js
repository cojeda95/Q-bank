/* Site-wide light/dark theme.
   Load in <head>, after the stylesheets, so the saved theme is applied before the
   page paints. It shares the Lesion Atlas's storage key ('mla-theme'), so one choice
   covers the hub, every block, Live Session, the OMM explorer and the atlas. Light is
   the default, as in the atlas. Once the page has loaded it adds a ◐ button to the
   right end of the top bar, and a change made in one tab reaches any other open tab. */
(function () {
  var KEY = 'mla-theme';
  var root = document.documentElement;

  function saved() {
    try { return localStorage.getItem(KEY) === 'dark' ? 'dark' : 'light'; }
    catch (e) { return 'light'; }
  }
  function label(btn) {
    var dark = root.getAttribute('data-theme') === 'dark';
    btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    btn.title = dark ? 'Light mode' : 'Dark mode';
  }
  function apply(theme) {
    root.setAttribute('data-theme', theme);
    var btn = document.getElementById('themeToggle');
    if (btn) label(btn);
  }

  apply(saved());

  window.addEventListener('storage', function (e) {
    if (e.key === KEY) apply(saved());
  });

  function addButton() {
    var bar = document.querySelector('.topbar-inner');
    if (!bar || document.getElementById('themeToggle')) return;
    var actions = document.createElement('span');
    actions.className = 'topbar-actions';
    // Keep the block pages' Home button beside the toggle, on the right.
    var home = document.getElementById('homeBtn');
    if (home && home.parentNode === bar) actions.appendChild(home);
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.id = 'themeToggle';
    btn.className = 'theme-btn';
    btn.textContent = '◐';
    label(btn);
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) { /* non-fatal */ }
    });
    actions.appendChild(btn);
    bar.appendChild(actions);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', addButton);
  else addButton();
})();
