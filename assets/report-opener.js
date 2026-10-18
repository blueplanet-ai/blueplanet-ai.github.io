/* Report opener: icons, Cite and Share. Shared by every report page (visual refresh, part 2).
   Icons use the site's one set (24 x 24 grid, 1.6 stroke), the same drawings as the home page. */
(function(){
  var ICONS={
    shared:'<circle cx="8" cy="12" r="5"/><circle cx="16" cy="12" r="5"/>',
    mobility:'<path d="M2 17v-5l3-5h10l5 5h2v5h-3M8 17h7M2 17h2"/><circle cx="6" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
    travel:'<path d="M2 13l20-8-6 15-4-6z"/><path d="M12 14l4-4"/>',
    forces:'<path d="M3 18c4-1 6-5 9-12 3 7 5 11 9 12"/><path d="M3 21h18"/>',
    shifts:'<path d="M3 12h13M12 7l5 5-5 5"/><path d="M20 5v14"/>',
    signals:'<path d="M2 12h3l3-7 4 14 3-7h7"/>',
    opp:'<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9V16h7v-2.1A6 6 0 0 0 12 3z"/>',
    time:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    rss:'<path d="M5 5a14 14 0 0 1 14 14M5 11a8 8 0 0 1 8 8"/><circle cx="6" cy="18" r="1"/>',
    doc:'<path d="M5 4h11l3 3v13H5z"/><path d="M9 10h7M9 14h7M9 18h4"/>',
    calendar:'<path d="M4 6h16v14H4z"/><path d="M4 10h16M8 3v5M16 3v5"/>',
    history:'<path d="M4 12a8 8 0 1 0 2.3-5.6"/><path d="M4 4v3h3"/><path d="M12 8v4l3 2"/>',
    quote:'<path d="M4 11h5v7H4zM4 11c0-3 1-5 4-6M14 11h5v7h-5zM14 11c0-3 1-5 4-6"/>',
    share:'<circle cx="7.5" cy="12" r="2.5"/><circle cx="16.5" cy="6" r="2.5"/><circle cx="16.5" cy="18" r="2.5"/><path d="M9.7 11l4.6-3.4M9.7 13l4.6 3.4"/>',
    download:'<path d="M12 4v11M7 10l5 5 5-5M4 20h16"/>',
    person:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/>'
  };
  document.querySelectorAll('svg[data-ro-ico]').forEach(function(s){ s.innerHTML = ICONS[s.getAttribute('data-ro-ico')] || ''; });

  var status = document.getElementById('roStatus');
  function say(msg){ if(status){ status.textContent = msg; setTimeout(function(){ if(status.textContent === msg) status.textContent = ''; }, 4000); } }
  function copy(text, ok){
    if(navigator.clipboard && window.isSecureContext){
      navigator.clipboard.writeText(text).then(function(){ say(ok); }, function(){ fallback(text, ok); });
    } else { fallback(text, ok); }
  }
  function fallback(text, ok){
    try{
      var t = document.createElement('textarea');
      t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
      document.body.appendChild(t); t.select();
      var done = document.execCommand('copy');
      document.body.removeChild(t);
      say(done ? ok : 'Copy failed. Select the text below and copy it.');
    } catch(e){ say('Copy failed. Select the text below and copy it.'); }
  }

  var cite = document.getElementById('roCiteText');
  var citeBtn = document.getElementById('roCite');
  if(cite && citeBtn){
    citeBtn.addEventListener('click', function(){ copy(cite.textContent.trim(), 'Citation copied.'); });
  }
  var shareBtn = document.getElementById('roShare');
  if(shareBtn){
    shareBtn.addEventListener('click', function(){
      var url = (document.querySelector('link[rel="canonical"]') || {}).href || location.href;
      var title = document.title;
      if(navigator.share){
        navigator.share({ title: title, url: url }).catch(function(){});
      } else {
        copy(url, 'Link copied.');
      }
    });
  }
})();
