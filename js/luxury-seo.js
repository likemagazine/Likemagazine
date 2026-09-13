/**
 * LIKE® Magazine Luxury Guide — SEO helpers
 * Static publisher Organization lives in page <head> JSON-LD.
 * This module updates a compact ItemList for the currently visible page (≤50).
 */
(function (global) {
  "use strict";

  var SCRIPT_ID = "lg-itemlist-jsonld";
  var ORG_ID = "https://likeleaders.com/#organization";

  function ensureScript() {
    var el = document.getElementById(SCRIPT_ID);
    if (!el) {
      el = document.createElement("script");
      el.type = "application/ld+json";
      el.id = SCRIPT_ID;
      document.head.appendChild(el);
    }
    return el;
  }

  function nameOf(item, brandKey) {
    return (
      item[brandKey] ||
      item.name ||
      item.airline ||
      item.street ||
      item.seo && item.seo.title ||
      "Listing"
    );
  }

  function updateItemList(opts) {
    opts = opts || {};
    var meta = opts.meta || {};
    var items = opts.items || [];
    var itemType = opts.itemType || "Thing";
    var brandKey = opts.brandKey || "name";
    var page = opts.page || 1;
    var pageSize = opts.pageSize || 50;
    var seo = meta.seo || {};
    var title = seo.title || meta.title || "LIKE® Magazine Luxury Guide";
    var description =
      seo.description ||
      "Editorial luxury index curated for LIKE® Magazine · likeleaders.com";

    var path = (location && location.pathname) || "/sections/luxury-guide.html";
    var pageUrl = "https://likeleaders.com" + path + (page > 1 ? "?page=" + page : "");

    var elementList = items.map(function (it, idx) {
      var nm = nameOf(it, brandKey);
      var entry = {
        "@type": "ListItem",
        position: (page - 1) * pageSize + idx + 1,
        item: {
          "@type": itemType,
          name: nm,
          description: (it.seo && it.seo.description) || undefined,
        },
      };
      if (it.city || it.hub_city) entry.item.address = {
        "@type": "PostalAddress",
        addressLocality: it.city || it.hub_city || undefined,
        addressCountry: it.country || it.hub_country || undefined,
      };
      if (it.country && !entry.item.address) {
        entry.item.address = { "@type": "PostalAddress", addressCountry: it.country };
      }
      // drop undefined
      if (!entry.item.description) delete entry.item.description;
      return entry;
    });

    var graph = {
      "@context": "https://schema.org",
      "@type": "ItemList",
      name: title,
      description: description,
      url: pageUrl,
      numberOfItems: elementList.length,
      itemListOrder: "https://schema.org/ItemListOrderAscending",
      publisher: { "@id": ORG_ID },
      isPartOf: {
        "@type": "CollectionPage",
        name: meta.title || title,
        url: "https://likeleaders.com" + path,
        publisher: { "@id": ORG_ID },
      },
      itemListElement: elementList,
    };

    ensureScript().textContent = JSON.stringify(graph);
  }

  global.LikeLuxurySeo = { updateItemList: updateItemList };
})(window);
