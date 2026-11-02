/* Theme control: System / Light / Dark. Applies a saved choice before first paint, then adds a
   three-button group to the site nav. System = no saved choice, so the page follows the device
   setting (prefers-color-scheme) and keeps following it when that changes. */
(function () {
  var KEY = 'bp-theme', root = document.documentElement;
  function read() { try { var v = localStorage.getItem(KEY); return v === 'light' || v === 'dark' ? v : 'system'; } catch (e) { return 'system'; } }
  function write(v) { try { if (v === 'system') localStorage.removeItem(KEY); else localStorage.setItem(KEY, v); } catch (e) {} }
  function apply(v) { if (v === 'system') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', v); }
  var mode = read(); apply(mode);
  var MON = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8M12 16v4"/></svg>';
  var SUN = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  var MOON = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
  var OPTS = [['system', 'System (follow device)', MON], ['light', 'Light', SUN], ['dark', 'Dark', MOON]];
  function init() {
    var nav = document.querySelector('nav.topnav, nav.ro-nav');
    if (!nav || nav.querySelector('.theme-seg')) return;
    var g = document.createElement('div');
    g.className = 'theme-seg'; g.setAttribute('role', 'group'); g.setAttribute('aria-label', 'Colour theme');
    function paint() {
      g.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-mode') === mode ? 'true' : 'false'); });
    }
    OPTS.forEach(function (o) {
      var b = document.createElement('button');
      b.type = 'button'; b.setAttribute('data-mode', o[0]); b.innerHTML = o[2];
      b.setAttribute('aria-label', o[1]); b.title = o[1];
      b.addEventListener('click', function () { mode = o[0]; apply(mode); write(mode); paint(); });
      g.appendChild(b);
    });
    paint(); nav.appendChild(g);
    /* keep other open tabs of the site in step */
    window.addEventListener('storage', function (e) { if (e.key === KEY || e.key === null) { mode = read(); apply(mode); paint(); } });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
