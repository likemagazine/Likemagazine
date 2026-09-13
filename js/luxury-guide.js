/**
 * LIKE® Magazine Luxury Guide — shared catalog UI
 * fetch JSON, search, filters, pagination (50/page), table render,
 * loading/error/empty states. Never blanks the page on fetch fail.
 * Emits visible-page ItemList JSON-LD via luxury-seo helpers when present.
 */
(function () {
  "use strict";

  var PAGE_SIZE = 50;

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function getConfig() {
    var el = $("#lg-app") || document.body;
    var cfg = {
      dataUrl: el.getAttribute("data-src") || "",
      pageSize: parseInt(el.getAttribute("data-page-size") || PAGE_SIZE, 10) || PAGE_SIZE,
      itemType: el.getAttribute("data-item-type") || "Thing",
      brandKey: el.getAttribute("data-brand-key") || "name",
    };
    return cfg;
  }

  function flattenSearch(item, keys) {
    var parts = [];
    (keys || Object.keys(item)).forEach(function (k) {
      if (k === "seo") return;
      var v = item[k];
      if (v == null) return;
      if (typeof v === "object") return;
      parts.push(String(v));
    });
    return parts.join(" ").toLowerCase();
  }

  function uniqueValues(items, key) {
    var set = {};
    items.forEach(function (it) {
      var v = it[key];
      if (v == null || v === "") return;
      set[String(v)] = true;
    });
    return Object.keys(set).sort(function (a, b) {
      var na = Number(a), nb = Number(b);
      if (!isNaN(na) && !isNaN(nb) && String(na) === a && String(nb) === b) return na - nb;
      return a.localeCompare(b);
    });
  }

  function sortItems(items, sort) {
    if (!sort || !sort.key) return items.slice();
    var key = sort.key;
    var dir = (sort.dir || "asc") === "desc" ? -1 : 1;
    return items.slice().sort(function (a, b) {
      var av = a[key], bv = b[key];
      if (av == null && bv == null) return 0;
      if (av == null) return 1;
      if (bv == null) return -1;
      if (typeof av === "number" && typeof bv === "number") return (av - bv) * dir;
      var an = Number(av), bn = Number(bv);
      if (!isNaN(an) && !isNaN(bn) && String(an) === String(av) && String(bn) === String(bv)) {
        return (an - bn) * dir;
      }
      return String(av).localeCompare(String(bv)) * dir;
    });
  }

  function stateHtml(msg, cls) {
    return '<div class="lg-state ' + (cls || "") + '" role="status">' + esc(msg) + "</div>";
  }

  function GuideApp(root) {
    this.root = root;
    this.cfg = getConfig();
    this.meta = {};
    this.items = [];
    this.filtered = [];
    this.page = 1;
    this.q = "";
    this.filters = {};
    this.mount();
  }

  GuideApp.prototype.mount = function () {
    var self = this;
    if (!this.cfg.dataUrl) {
      this.root.innerHTML = stateHtml("No data source configured for this guide.", "is-error");
      return;
    }
    this.root.innerHTML = stateHtml("Loading LIKE® Magazine Luxury Guide…");
    fetch(this.cfg.dataUrl, { credentials: "same-origin" })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (doc) {
        self.meta = doc.meta || {};
        self.items = Array.isArray(doc.items) ? doc.items : [];
        self.renderShell();
        self.apply();
      })
      .catch(function (err) {
        self.root.innerHTML =
          stateHtml(
            "We couldn’t load this guide right now. The rest of LIKE® Magazine is unaffected. Please try again shortly.",
            "is-error"
          ) +
          '<p class="lg-credit" style="text-align:center">Curated for LIKE® Magazine Luxury Guide · likeleaders.com</p>';
        if (window.console && console.warn) console.warn("luxury-guide fetch", err);
      });
  };

  GuideApp.prototype.renderShell = function () {
    var filters = this.meta.filters || [];
    var filterHtml = filters
      .map(function (key) {
        return (
          '<div class="lg-field">' +
          "<label for=\"lg-f-" +
          esc(key) +
          '">' +
          esc(key.replace(/_/g, " ")) +
          "</label>" +
          '<select id="lg-f-' +
          esc(key) +
          '" data-filter="' +
          esc(key) +
          '"><option value="">All</option></select>' +
          "</div>"
        );
      })
      .join("");

    this.root.innerHTML =
      '<div class="lg-toolbar" role="search">' +
      '<div class="lg-field" style="flex:2 1 220px">' +
      '<label for="lg-search">Search</label>' +
      '<input id="lg-search" type="search" placeholder="Search this guide…" autocomplete="off"/>' +
      "</div>" +
      filterHtml +
      "</div>" +
      '<div class="lg-meta-bar" id="lg-meta-bar"></div>' +
      '<div id="lg-results"></div>' +
      '<div class="lg-pager" id="lg-pager" hidden></div>' +
      '<p class="lg-credit">Curated for LIKE® Magazine Luxury Guide · likeleaders.com</p>';

    var self = this;
    var search = $("#lg-search", this.root);
    var t = null;
    search.addEventListener("input", function () {
      clearTimeout(t);
      t = setTimeout(function () {
        self.q = search.value.trim().toLowerCase();
        self.page = 1;
        self.apply();
      }, 120);
    });

    filters.forEach(function (key) {
      var sel = $('#lg-f-' + key, self.root);
      uniqueValues(self.items, key).forEach(function (v) {
        var opt = document.createElement("option");
        opt.value = v;
        opt.textContent = v;
        sel.appendChild(opt);
      });
      sel.addEventListener("change", function () {
        self.filters[key] = sel.value;
        self.page = 1;
        self.apply();
      });
    });
  };

  GuideApp.prototype.apply = function () {
    var self = this;
    var keys = this.meta.searchKeys;
    var list = this.items.filter(function (it) {
      for (var k in self.filters) {
        if (!self.filters[k]) continue;
        if (String(it[k] == null ? "" : it[k]) !== self.filters[k]) return false;
      }
      if (!self.q) return true;
      return flattenSearch(it, keys).indexOf(self.q) !== -1;
    });
    list = sortItems(list, this.meta.defaultSort || null);
    this.filtered = list;
    var pages = Math.max(1, Math.ceil(list.length / this.cfg.pageSize));
    if (this.page > pages) this.page = pages;
    this.renderResults();
  };

  GuideApp.prototype.renderResults = function () {
    var results = $("#lg-results", this.root);
    var metaBar = $("#lg-meta-bar", this.root);
    var pager = $("#lg-pager", this.root);
    var total = this.filtered.length;
    var start = (this.page - 1) * this.cfg.pageSize;
    var slice = this.filtered.slice(start, start + this.cfg.pageSize);
    var cols = this.meta.columns || [];

    metaBar.innerHTML =
      "<span><strong>" +
      total.toLocaleString() +
      "</strong> listing" +
      (total === 1 ? "" : "s") +
      (this.meta.count && this.meta.count !== total
        ? " of " + Number(this.meta.count).toLocaleString()
        : "") +
      "</span>" +
      (this.meta.title ? "<span>" + esc(this.meta.title) + "</span>" : "") +
      (this.meta.compiled ? "<span>Compiled " + esc(this.meta.compiled) + "</span>" : "");

    if (!cols.length && slice[0]) {
      cols = Object.keys(slice[0])
        .filter(function (k) {
          return k !== "seo";
        })
        .map(function (k) {
          return { key: k, label: k };
        });
    }

    if (!total) {
      results.innerHTML = stateHtml("No matches. Try clearing search or filters.", "is-empty");
      pager.hidden = true;
      this.publishSeo([]);
      return;
    }

    var brandKey = this.cfg.brandKey;
    var itemType = this.cfg.itemType;
    var thead =
      "<thead><tr>" +
      cols
        .map(function (c) {
          return "<th scope=\"col\">" + esc(c.label || c.key) + "</th>";
        })
        .join("") +
      "</tr></thead>";
    var tbody =
      "<tbody>" +
      slice
        .map(function (it) {
          var brand = it[brandKey] || it.name || it.airline || it.street || "";
          var attrs =
            ' data-brand="' +
            esc(brand) +
            '" itemscope itemtype="https://schema.org/' +
            esc(itemType) +
            '"';
          var cells = cols
            .map(function (c) {
              var v = it[c.key];
              var cls = c.key === "rank" ? ' class="lg-rank"' : "";
              var itemprop = "";
              if (c.key === "name" || c.key === "airline" || c.key === "street") itemprop = ' itemprop="name"';
              else if (c.key === "city" || c.key === "hub_city") itemprop = ' itemprop="addressLocality"';
              else if (c.key === "country" || c.key === "hub_country") itemprop = ' itemprop="addressCountry"';
              return "<td" + cls + itemprop + ">" + esc(v == null ? "" : v) + "</td>";
            })
            .join("");
          return "<tr" + attrs + ">" + cells + "</tr>";
        })
        .join("") +
      "</tbody>";

    results.innerHTML =
      '<div class="lg-table-wrap"><table class="lg-table">' + thead + tbody + "</table></div>";

    var pages = Math.ceil(total / this.cfg.pageSize);
    if (pages <= 1) {
      pager.hidden = true;
    } else {
      pager.hidden = false;
      var self = this;
      var btns = "";
      btns +=
        '<button type="button" data-page="prev"' +
        (this.page <= 1 ? " disabled" : "") +
        ">Prev</button>";
      var windowStart = Math.max(1, this.page - 2);
      var windowEnd = Math.min(pages, windowStart + 4);
      windowStart = Math.max(1, windowEnd - 4);
      for (var p = windowStart; p <= windowEnd; p++) {
        btns +=
          '<button type="button" data-page="' +
          p +
          '"' +
          (p === this.page ? ' class="is-current"' : "") +
          ">" +
          p +
          "</button>";
      }
      btns +=
        '<button type="button" data-page="next"' +
        (this.page >= pages ? " disabled" : "") +
        ">Next</button>";
      pager.innerHTML =
        "<span>Page <strong>" +
        this.page +
        "</strong> of " +
        pages +
        "</span><div class=\"lg-pager-btns\">" +
        btns +
        "</div>";
      pager.onclick = function (ev) {
        var btn = ev.target.closest("button[data-page]");
        if (!btn || btn.disabled) return;
        var v = btn.getAttribute("data-page");
        if (v === "prev") self.page = Math.max(1, self.page - 1);
        else if (v === "next") self.page = Math.min(pages, self.page + 1);
        else self.page = parseInt(v, 10) || 1;
        self.renderResults();
        self.root.scrollIntoView({ behavior: "smooth", block: "start" });
      };
    }

    this.publishSeo(slice);
  };

  GuideApp.prototype.publishSeo = function (visibleItems) {
    if (window.LikeLuxurySeo && typeof window.LikeLuxurySeo.updateItemList === "function") {
      try {
        window.LikeLuxurySeo.updateItemList({
          meta: this.meta,
          items: visibleItems,
          page: this.page,
          pageSize: this.cfg.pageSize,
          itemType: this.cfg.itemType,
          brandKey: this.cfg.brandKey,
          dataUrl: this.cfg.dataUrl,
        });
      } catch (e) {
        if (window.console && console.warn) console.warn("luxury-seo", e);
      }
    }
  };

  function boot() {
    var root = $("#lg-app");
    if (!root) return;
    new GuideApp(root);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
