/**
 * LIKE® Magazine — Shop the story
 * Loads /data/partners.json and renders a module for [data-shop-story="moduleId"].
 * Pending partner codes stay labeled; affiliate links get rel=sponsored.
 */
(function () {
  var STYLE_ID = 'like-shop-story-css';
  if (!document.getElementById(STYLE_ID)) {
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = [
      '.shop-story{margin:1.75rem 0 0;padding:1.1rem 1.15rem 1.25rem;background:var(--cream,#fffcf6);border:1px solid var(--rule,#d6ccbc);font-family:var(--sans,"Avenir Next",Helvetica,Arial,sans-serif)}',
      '.shop-story h2{margin:0 0 0.35rem;font-size:0.78rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--accent,#8b1515)}',
      '.shop-story .shop-story-note{margin:0 0 0.9rem;font-size:0.78rem;color:var(--muted,#6a6358);line-height:1.45}',
      '.shop-story-grid{display:grid;gap:0.85rem;grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}',
      '.shop-story-card{display:flex;flex-direction:column;gap:0.35rem;padding:0.85rem;border:1px solid var(--rule,#d6ccbc);background:#fff;color:inherit;text-decoration:none;min-height:100%}',
      '.shop-story-card:hover{border-color:var(--accent,#8b1515);text-decoration:none}',
      '.shop-story-card strong{font-size:0.92rem;line-height:1.25;color:var(--ink,#111)}',
      '.shop-story-card span{font-size:0.78rem;color:var(--muted,#6a6358);line-height:1.4;flex:1}',
      '.shop-story-card em{font-style:normal;font-size:0.72rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent,#8b1515);font-weight:700}',
      '.shop-story-card .pending{display:inline-block;margin-top:0.25rem;font-size:0.65rem;letter-spacing:0.06em;text-transform:uppercase;color:#9a6b00}',
      '.shop-story-foot{margin:0.85rem 0 0;font-size:0.7rem;color:var(--muted,#6a6358)}'
    ].join('');
    document.head.appendChild(s);
  }

  function partnerById(catalog, id) {
    var list = (catalog && catalog.partners) || [];
    for (var i = 0; i < list.length; i++) if (list[i].id === id) return list[i];
    return null;
  }

  function buildUrl(partner, item) {
    if (item.url) return item.url;
    if (!partner) return '#';
    var tpl = partner.urlTemplate || '#';
    var q = encodeURIComponent((item.query || '').replace(/\+/g, ' ')).replace(/%20/g, '+');
    return tpl
      .replace('{query}', item.query || q)
      .replace('{trackingCode}', partner.trackingCode || 'REPLACE_ME');
  }

  function render(el, catalog, moduleId) {
    var mod = (catalog.storyModules || {})[moduleId];
    if (!mod) {
      el.innerHTML = '<p class="shop-story-note">Shop module “' + moduleId + '” not found in partners.json.</p>';
      return;
    }
    var pending = false;
    var cards = (mod.items || []).map(function (item) {
      var p = partnerById(catalog, item.partnerId);
      var href = buildUrl(p, item);
      var isAff = !!item.affiliate;
      var needsCode = isAff && p && (!p.trackingCode || String(p.trackingCode).indexOf('REPLACE_') === 0);
      if (needsCode) pending = true;
      var rel = (p && p.rel) || (isAff ? 'sponsored noopener noreferrer' : 'noopener noreferrer');
      var badge = needsCode ? '<span class="pending">Partner code pending</span>' : '';
      return (
        '<a class="shop-story-card" href="' + href + '" rel="' + rel + '"' + (href.indexOf('http') === 0 ? ' target="_blank"' : '') + '>' +
          '<strong>' + (item.title || '') + '</strong>' +
          '<span>' + (item.blurb || '') + '</span>' +
          '<em>' + (item.cta || 'View') + '</em>' +
          badge +
        '</a>'
      );
    }).join('');

    var near = catalog.disclosureNearLinks || catalog.disclosure || '';
    el.classList.add('shop-story');
    el.innerHTML =
      '<h2>' + (mod.headline || 'Shop the story') + '</h2>' +
      '<p class="shop-story-note">' + near + (pending ? ' Some links await network approval — labeled below.' : '') + '</p>' +
      '<div class="shop-story-grid">' + cards + '</div>' +
      '<p class="shop-story-foot">' + (catalog.disclosure || '') + '</p>';
  }

  function boot() {
    var nodes = document.querySelectorAll('[data-shop-story]');
    if (!nodes.length) return;
    fetch('/data/partners.json')
      .then(function (r) { return r.json(); })
      .then(function (catalog) {
        nodes.forEach(function (el) {
          render(el, catalog, el.getAttribute('data-shop-story'));
        });
      })
      .catch(function () {
        nodes.forEach(function (el) {
          el.innerHTML = '<p class="shop-story-note">Partner catalog could not load.</p>';
        });
      });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
