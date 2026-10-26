/* ============================================================
   AGATHE FORTIN PAYSAGES — interactions & animations
   ============================================================ */
(() => {
  "use strict";
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const QA = location.search.indexOf("qa=1") !== -1;
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches || QA;
  if (QA) {
    const st = document.createElement("style");
    st.textContent = "*,*::before,*::after{transition:none!important;animation:none!important}" +
      ".hero-split{min-height:0!important}.hs-media{height:480px!important}" +
      ".hero-full{height:820px!important;min-height:0!important}" +
      ".hero-bleed{min-height:860px!important}";
    document.head.appendChild(st);
  }

  /* ---------- préchargeur : rapide, une seule fois par session ---------- */
  const loader = $("#loader");
  if (loader) {
    let seen = false;
    try { seen = sessionStorage.getItem("af_seen") === "1"; sessionStorage.setItem("af_seen", "1"); } catch {}
    const hide = () => { loader.classList.add("done"); document.body.classList.add("ready"); };
    if (reduced || seen) { document.body.classList.add("no-loader"); hide(); }
    else {
      const t = setTimeout(hide, 1400);
      addEventListener("load", () => { clearTimeout(t); setTimeout(hide, 500); });
    }
  }

  /* ---------- header ---------- */
  const header = $("#header");
  if (!$(".hero") && !$(".page-hero")) document.body.classList.add("light-header");
  let lastY = 0;
  const onScroll = () => {
    const y = scrollY;
    header.classList.toggle("scrolled", y > 40);
    if (!QA && y > 600 && y > lastY + 8) header.classList.add("hidden");
    else if (y < lastY - 8 || y < 200) header.classList.remove("hidden");
    lastY = y;
  };
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  const burger = $("#burger");
  if (burger) {
    burger.addEventListener("click", () => {
      const open = document.body.classList.toggle("menu-open");
      $$("#mobile-menu .mob-link").forEach((a, i) => {
        a.style.transitionDelay = open ? `${0.18 + i * 0.07}s` : "0s";
      });
    });
    $$("#mobile-menu a").forEach(a => a.addEventListener("click", () => document.body.classList.remove("menu-open")));
  }

  /* ---------- révélations au scroll ---------- */
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
  const observe = el => io.observe(el);
  $$(".rv, .rv-img, .rv-clip").forEach(observe);

  /* ---------- parallaxe douce ---------- */
  const pxEls = $$("[data-parallax]");
  if (pxEls.length && !reduced) {
    const tick = () => {
      const vh = innerHeight;
      pxEls.forEach(el => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        const p = (r.top + r.height / 2 - vh / 2) / vh;
        el.style.transform = `translateY(${p * parseFloat(el.dataset.parallax || 40)}px)`;
      });
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  /* ---------- compteurs ---------- */
  $$("[data-count]").forEach(el => {
    const target = parseInt(el.dataset.count, 10);
    const obs = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return;
      obs.disconnect();
      if (reduced) { el.textContent = target; return; }
      const t0 = performance.now(), dur = 1600;
      const step = t => {
        const p = Math.min((t - t0) / dur, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 4)));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }, { threshold: 0.5 });
    obs.observe(el);
  });

  /* ---------- slider héros ---------- */
  const heroSlides = $$(".hero-slide");
  if (heroSlides.length) {
    const dotsWrap = $(".hf-dots") || $(".hero-dots");
    let idx = 0, timer;
    heroSlides.forEach((_, i) => {
      const b = document.createElement("button");
      b.setAttribute("aria-label", `Image ${i + 1}`);
      b.addEventListener("click", () => go(i, true));
      dotsWrap.appendChild(b);
    });
    const dots = $$("button", dotsWrap);
    const go = (i, manual) => {
      idx = (i + heroSlides.length) % heroSlides.length;
      heroSlides.forEach((s, j) => s.classList.toggle("on", j === idx));
      dots.forEach((d, j) => d.classList.toggle("on", j === idx));
      if (manual) restart();
    };
    const restart = () => { clearInterval(timer); if (!reduced) timer = setInterval(() => go(idx + 1), 6500); };
    go(0); restart();
  }

  /* ============================================================
     DONNÉES / RENDU
     ============================================================ */
  const D = typeof AF_DATA !== "undefined" ? AF_DATA : null;
  const CATS = { ceramiques: "Céramique", anduze: "Anduze", objets: "Objet décoratif", metal: "Peint sur métal" };
  const productById = id => D.products.find(p => p.id === id);
  const fmtPrice = p => {
    if (!p.price) return "Prix sur demande";
    const eur = p.price.toLocaleString("fr-FR") + " €";
    return p.sizes > 1 ? "à partir de " + eur : eur;
  };

  const productCard = (p, i) => `
    <article class="product" style="--d:${(i % 6) * 0.07}s" data-id="${p.id}" data-cat="${p.cat}">
      <a class="ph" href="produit.html?id=${p.id}" aria-label="Voir ${p.name}">
        <span class="cat-tag">${CATS[p.cat]}</span>
        ${p.sizes > 1 ? `<span class="size-tag">${p.sizes} tailles</span>` : ""}
        <img src="${p.img}" alt="${p.name} — ${p.specs}" loading="lazy">
        <div class="quick">
          <button data-add="${p.id}" aria-label="Ajouter ${p.name} à ma commande">+</button>
        </div>
      </a>
      <div class="meta">
        <a href="produit.html?id=${p.id}"><h3>${p.name}${p.coloris ? ` <span class="col">— ${p.coloris}</span>` : ""}</h3></a>
        <span class="specs">${p.dimtxt || p.specs}</span>
        <span class="price">${fmtPrice(p)}</span>
      </div>
    </article>`;

  /* ---------- boutique ---------- */
  const shopGrid = $("#shop-grid");
  if (shopGrid && D && !$("#pp-root")) {
    const state = { cat: "all", q: "", sort: "featured" };
    const render = () => {
      let list = D.products.filter(p => state.cat === "all" || p.cat === state.cat);
      if (state.q) {
        const q = state.q.toLowerCase();
        list = list.filter(p => (p.name + " " + (p.coloris || "") + " " + CATS[p.cat] + " " + p.specs).toLowerCase().includes(q));
      }
      if (state.sort === "price-asc") list = [...list].sort((a, b) => (a.price || 9e9) - (b.price || 9e9));
      if (state.sort === "price-desc") list = [...list].sort((a, b) => (b.price || 0) - (a.price || 0));
      if (state.sort === "name") list = [...list].sort((a, b) => a.name.localeCompare(b.name, "fr"));
      shopGrid.innerHTML = list.length
        ? list.map(productCard).join("")
        : `<p class="shop-empty">Aucune pièce ne correspond à «&nbsp;${state.q}&nbsp;» — essayez un autre mot.</p>`;
      const c = $("#shop-count");
      if (c) c.textContent = `${list.length} pièce${list.length > 1 ? "s" : ""}`;
      $$(".product", shopGrid).forEach(observe);
    };
    render();
    $$("#shop-filters .chip").forEach(ch => ch.addEventListener("click", () => {
      $$("#shop-filters .chip").forEach(c => c.classList.remove("on"));
      ch.classList.add("on");
      state.cat = ch.dataset.cat;
      render();
    }));
    const sInput = $("#shop-search");
    sInput && sInput.addEventListener("input", () => { state.q = sInput.value.trim(); render(); });
    const sSel = $("#shop-sort");
    sSel && sSel.addEventListener("change", () => { state.sort = sSel.value; render(); });
    $$("[data-goto]").forEach(tile => tile.addEventListener("click", e => {
      e.preventDefault();
      const chip = $(`#shop-filters .chip[data-cat="${tile.dataset.goto}"]`);
      chip && chip.click();
      $("#shop-toolbar").scrollIntoView({ behavior: reduced ? "auto" : "smooth", block: "start" });
    }));
  }

  /* ---------- page produit ---------- */
  const ppRoot = $("#pp-root");
  if (ppRoot && D) {
    const id = new URLSearchParams(location.search).get("id");
    const p = productById(id) || D.products[0];
    let ppQty = 1;
    document.title = `${p.name}${p.coloris ? " " + p.coloris : ""} — Boutique Agathe Fortin Paysages`;
    $("#bc-name").textContent = p.name;
    $("#pp-img").src = p.img;
    $("#pp-img").alt = `${p.name} — ${p.specs}`;
    $("#pp-cat").textContent = CATS[p.cat];
    $("#pp-name").innerHTML = p.name + (p.coloris ? ` <em class="gold">${p.coloris}</em>` : "");
    $("#pp-price").textContent = fmtPrice(p);
    $("#pp-desc").textContent = p.desc || "";
    const rows = [];
    if (p.coloris) rows.push(["Coloris", p.coloris]);
    if (p.dimtxt) rows.push(["Dimensions", p.dimtxt]);
    if (p.sizes > 1) rows.push(["Tailles", `${p.sizes} tailles disponibles — précisez votre choix à la commande`]);
    rows.push(["Matière", p.cat === "metal" ? "Peinture sur métal" : "Céramique émaillée, résistante au gel"]);
    rows.push(["Référence", p.id.toUpperCase()]);
    $("#pp-specs").innerHTML = rows.map(r => `<tr><th>${r[0]}</th><td>${r[1]}</td></tr>`).join("");
    $("[data-pq-dec]").addEventListener("click", () => { ppQty = Math.max(1, ppQty - 1); $("#pp-qty").textContent = ppQty; });
    $("[data-pq-inc]").addEventListener("click", () => { ppQty++; $("#pp-qty").textContent = ppQty; });
    $("#pp-add").addEventListener("click", () => { addToCart(p.id, ppQty); openCart(); });
    // barre d'achat sticky (mobile) : apparaît quand le bouton principal sort de l'écran
    const sb = $("#pp-stickybar");
    if (sb) {
      $("#ppsb-price").textContent = fmtPrice(p);
      $("#ppsb-name").textContent = p.name + (p.coloris ? " — " + p.coloris : "");
      $("#ppsb-add").addEventListener("click", () => { addToCart(p.id, ppQty); openCart(); });
      const sbCheck = () => sb.classList.toggle("show", $("#pp-add").getBoundingClientRect().bottom < 0);
      addEventListener("scroll", sbCheck, { passive: true });
      sbCheck();
    }
    // suggestions : même catégorie d'abord, puis le reste
    const rel = D.products.filter(x => x.id !== p.id && x.cat === p.cat)
      .concat(D.products.filter(x => x.id !== p.id && x.cat !== p.cat)).slice(0, 4);
    $("#pp-related").innerHTML = rel.map(productCard).join("");
    $$("#pp-related .product").forEach(el => el.classList.add("in"));
    // données structurées (SEO / Google)
    const ld = document.createElement("script");
    ld.type = "application/ld+json";
    ld.textContent = JSON.stringify({
      "@context": "https://schema.org", "@type": "Product",
      name: p.name + (p.coloris ? " — " + p.coloris : ""),
      image: location.origin + "/" + p.img, description: p.desc,
      sku: p.id.toUpperCase(), brand: { "@type": "Brand", name: "Agathe Fortin Paysages" },
      offers: p.price ? { "@type": "Offer", priceCurrency: "EUR", price: p.price, availability: "https://schema.org/InStock" } : undefined,
    });
    document.head.appendChild(ld);
  }

  /* ---------- teaser boutique (accueil) ---------- */
  const teaser = $("#shop-teaser");
  if (teaser && D) {
    const picks = ["p03", "p06", "p13", "p21", "p28", "p31"].map(productById).filter(Boolean);
    teaser.innerHTML = picks.map(productCard).join("");
    $$(".product", teaser).forEach(el => el.classList.add("in"));
  }

  /* ---------- projets / événements ---------- */
  const worksGrid = $("#works-grid");
  if (worksGrid && D) {
    const kind = worksGrid.dataset.kind;
    const all = D[kind] || [];
    const isIntl = w => /MAROC|ETATS|UNIS/i.test(w.loc);
    const renderWorks = (f = "all") => {
      const list = all.filter(w => f === "all" || (f === "intl" ? isIntl(w) : !isIntl(w)));
      worksGrid.innerHTML = list.map((w, i) => `
        <article class="work" style="--d:${(i % 6) * 0.07}s" data-idx="${all.indexOf(w)}" tabindex="0" role="button" aria-label="Voir ${w.title}">
          <div class="ph">
            ${w.imgs.length > 1 ? `<span class="count">${w.imgs.length} photos</span>` : ""}
            <img src="${w.imgs[0]}" alt="${w.title} — ${w.loc}" loading="lazy">
            <span class="plus">&#8599;</span>
          </div>
          <div class="meta"><h3>${w.title}</h3><span class="loc">${w.loc}</span></div>
        </article>`).join("");
      const cEl = $("#works-count");
      if (cEl) cEl.textContent = `${list.length} réalisation${list.length > 1 ? "s" : ""}`;
      $$(".work", worksGrid).forEach(observe);
    };
    renderWorks();
    $$("#works-filters .chip").forEach(ch => ch.addEventListener("click", () => {
      $$("#works-filters .chip").forEach(c => c.classList.remove("on"));
      ch.classList.add("on");
      renderWorks(ch.dataset.f);
    }));
    worksGrid.addEventListener("click", e => {
      const card = e.target.closest(".work");
      if (!card) return;
      const w = all[+card.dataset.idx];
      openLightbox(w.imgs, w.title, w.loc);
    });
    worksGrid.addEventListener("keydown", e => {
      if (e.key === "Enter" && e.target.closest(".work")) e.target.closest(".work").click();
    });
  }

  /* ---------- galeries simples (strip) ---------- */
  $$(".gallery-strip").forEach(strip => {
    strip.addEventListener("click", e => {
      if (e.target.tagName !== "IMG") return;
      const imgs = $$("img", strip).map(i => i.getAttribute("src"));
      openLightbox(imgs, strip.dataset.title || "Galerie", strip.dataset.sub || "", imgs.indexOf(e.target.getAttribute("src")));
    });
  });

  /* ---------- visionneuse ---------- */
  let lb = null;
  function ensureLightbox() {
    if (lb) return lb;
    const el = document.createElement("div");
    el.id = "lightbox";
    el.innerHTML = `
      <div class="lb-top"><div class="lb-title"><span></span><small></small></div>
      <button class="lb-x" aria-label="Fermer">&#10005;</button></div>
      <div class="lb-stage">
        <button class="lb-nav lb-prev" aria-label="Précédente">&#8592;</button>
        <img alt="">
        <button class="lb-nav lb-next" aria-label="Suivante">&#8594;</button>
      </div>
      <div class="lb-count"></div>`;
    document.body.appendChild(el);
    lb = {
      el, img: $("img", el), title: $(".lb-title span", el), sub: $(".lb-title small", el),
      count: $(".lb-count", el), imgs: [], i: 0,
    };
    const show = i => {
      lb.i = (i + lb.imgs.length) % lb.imgs.length;
      lb.img.style.animation = "none"; void lb.img.offsetWidth; lb.img.style.animation = "";
      lb.img.src = lb.imgs[lb.i];
      lb.count.textContent = `${lb.i + 1} / ${lb.imgs.length}`;
      $(".lb-prev", el).style.visibility = $(".lb-next", el).style.visibility = lb.imgs.length > 1 ? "visible" : "hidden";
    };
    lb.show = show;
    $(".lb-x", el).addEventListener("click", closeLightbox);
    $(".lb-prev", el).addEventListener("click", () => show(lb.i - 1));
    $(".lb-next", el).addEventListener("click", () => show(lb.i + 1));
    el.addEventListener("click", e => { if (e.target === el || e.target.classList.contains("lb-stage")) closeLightbox(); });
    addEventListener("keydown", e => {
      if (!el.classList.contains("open")) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowLeft") show(lb.i - 1);
      if (e.key === "ArrowRight") show(lb.i + 1);
    });
    return lb;
  }
  function openLightbox(imgs, title, sub, start = 0) {
    const l = ensureLightbox();
    l.imgs = imgs; l.title.textContent = title; l.sub.textContent = sub;
    l.show(start);
    l.el.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  function closeLightbox() {
    lb.el.classList.remove("open");
    document.body.style.overflow = "";
  }

  /* ============================================================
     PANIER & COMMANDE
     ============================================================ */
  const CART_KEY = "af_cart_v1";
  const loadCart = () => { try { return JSON.parse(localStorage.getItem(CART_KEY)) || {}; } catch { return {}; } };
  let cart = loadCart();
  const saveCart = () => { try { localStorage.setItem(CART_KEY, JSON.stringify(cart)); } catch {} };
  const cartQty = () => Object.values(cart).reduce((a, b) => a + b, 0);

  const drawer = $("#cart-drawer"), backdrop = $("#cart-backdrop");

  function toast(msg) {
    let t = $("#toast");
    if (!t) {
      t = document.createElement("div");
      t.id = "toast";
      t.innerHTML = `<span class="dot"></span><span class="msg"></span>`;
      document.body.appendChild(t);
    }
    $(".msg", t).textContent = msg;
    t.classList.add("on");
    clearTimeout(t._h);
    t._h = setTimeout(() => t.classList.remove("on"), 2600);
  }

  function updateBadges(pulse) {
    $$(".cart-count").forEach(b => {
      b.textContent = cartQty();
      if (pulse) { b.classList.remove("pulse"); void b.offsetWidth; b.classList.add("pulse"); }
    });
  }

  function addToCart(id, qty = 1) {
    if (!D) return;
    cart[id] = (cart[id] || 0) + qty;
    saveCart(); updateBadges(true); renderCart();
    toast(`« ${productById(id).name} » ajouté à votre demande`);
  }
  function setQty(id, q) {
    if (q <= 0) delete cart[id]; else cart[id] = q;
    saveCart(); updateBadges(); renderCart();
  }

  function renderCart() {
    if (!drawer || !D) return;
    const box = $(".cart-items", drawer);
    const ids = Object.keys(cart);
    $(".cart-head .sub", drawer).textContent = `${cartQty()} article${cartQty() > 1 ? "s" : ""}`;
    if (!ids.length) {
      box.innerHTML = `<div class="cart-empty">
        <span class="serif gold-it">Votre sélection est vide</span>
        <p>Parcourez la boutique et composez<br>votre demande de commande.</p>
        <a href="boutique.html" class="btn btn--dark">Découvrir la boutique</a></div>`;
      $(".cart-foot", drawer).style.display = "none";
      return;
    }
    $(".cart-foot", drawer).style.display = "";
    box.innerHTML = ids.map(id => {
      const p = productById(id);
      const line = p.price ? (p.price * cart[id]).toLocaleString("fr-FR") + " €" : "sur devis";
      return `<div class="cart-item" data-id="${id}">
        <img src="${p.img}" alt="${p.name}">
        <div>
          <h4>${p.name}${p.coloris ? " — " + p.coloris : ""}</h4><div class="sp">${p.dimtxt || p.specs}</div>
          <div class="ci-row">
            <div class="qty">
              <button data-dec="${id}" aria-label="Moins">&minus;</button>
              <span class="q">${cart[id]}</span>
              <button data-inc="${id}" aria-label="Plus">+</button>
            </div>
            <span class="line-price">${line}</span>
          </div>
        </div>
        <button class="rm" data-rm="${id}" aria-label="Retirer">&#10005;</button>
      </div>`;
    }).join("");
    const hasUnpriced = ids.some(id => !productById(id).price);
    const total = ids.reduce((s, id) => s + (productById(id).price || 0) * cart[id], 0);
    $(".cart-foot .row strong", drawer).textContent =
      hasUnpriced ? `${total ? total.toLocaleString("fr-FR") + " € + " : ""}pièces sur devis`
                  : total.toLocaleString("fr-FR") + " €";
  }

  function openCart() {
    if (!drawer) return;
    renderCart();
    drawer.classList.add("open"); backdrop.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  function closeCart() {
    drawer.classList.remove("open"); backdrop.classList.remove("open");
    document.body.style.overflow = "";
  }
  $$("[data-cart-open]").forEach(b => b.addEventListener("click", openCart));
  backdrop && backdrop.addEventListener("click", closeCart);
  drawer && $(".cart-close", drawer).addEventListener("click", closeCart);

  /* ---------- fiche produit ---------- */
  const pModal = $("#product-modal");
  let modalQty = 1, modalId = null;
  function openProduct(id) {
    if (!pModal || !D || !id) return;
    const p = productById(id);
    modalId = id; modalQty = 1;
    $(".mp-img img", pModal).src = p.img;
    $(".mp-img img", pModal).alt = p.name;
    $(".mp-cat", pModal).textContent = CATS[p.cat];
    $(".mp-name", pModal).textContent = p.name;
    $(".mp-specs", pModal).textContent = p.specs;
    $(".q", pModal).textContent = "1";
    pModal.classList.add("open");
    document.body.style.overflow = "hidden";
  }
  if (pModal) {
    $$("[data-modal-close]", pModal).forEach(b => b.addEventListener("click", () => {
      pModal.classList.remove("open"); document.body.style.overflow = "";
    }));
    $("[data-mq-dec]", pModal).addEventListener("click", () => { modalQty = Math.max(1, modalQty - 1); $(".q", pModal).textContent = modalQty; });
    $("[data-mq-inc]", pModal).addEventListener("click", () => { modalQty++; $(".q", pModal).textContent = modalQty; });
    $("[data-modal-add]", pModal).addEventListener("click", () => {
      addToCart(modalId, modalQty);
      pModal.classList.remove("open"); document.body.style.overflow = "";
      openCart();
    });
  }

  /* ---------- délégation clics produits/panier ---------- */
  document.addEventListener("click", e => {
    const add = e.target.closest("[data-add]");
    if (add) { e.preventDefault(); e.stopPropagation(); addToCart(add.dataset.add); return; }
    const open = e.target.closest("[data-open]");
    if (open) { openProduct(open.dataset.open); return; }
    const inc = e.target.closest("[data-inc]");
    if (inc) { setQty(inc.dataset.inc, cart[inc.dataset.inc] + 1); return; }
    const dec = e.target.closest("[data-dec]");
    if (dec) { setQty(dec.dataset.dec, cart[dec.dataset.dec] - 1); return; }
    const rm = e.target.closest("[data-rm]");
    if (rm) { setQty(rm.dataset.rm, 0); return; }
  });
  addEventListener("keydown", e => {
    if (e.key === "Escape") {
      pModal && pModal.classList.remove("open");
      $("#order-modal") && $("#order-modal").classList.remove("open");
      closeCart();
      document.body.style.overflow = "";
    }
    if (e.key === "Enter") {
      const ph = e.target.closest && e.target.closest(".product .ph");
      if (ph) openProduct(ph.dataset.open);
    }
  });

  /* ---------- commande ---------- */
  const oModal = $("#order-modal");
  if (oModal) {
    $("[data-checkout]", drawer).addEventListener("click", () => {
      if (!cartQty()) return;
      closeCart();
      $(".order-form-wrap", oModal).style.display = "";
      $(".order-ok", oModal).style.display = "none";
      oModal.classList.add("open");
      document.body.style.overflow = "hidden";
    });
    $$("[data-modal-close]", oModal).forEach(b => b.addEventListener("click", () => {
      oModal.classList.remove("open"); document.body.style.overflow = "";
    }));
    $("#order-form").addEventListener("submit", e => {
      e.preventDefault();
      const f = new FormData(e.target);
      const lines = Object.keys(cart).map(id => {
        const p = productById(id);
        const pr = p.price ? ` — ${(p.price * cart[id]).toLocaleString("fr-FR")} €` : " — prix sur devis";
        return `• ${p.raw} (${p.specs}) — quantité : ${cart[id]}${pr}`;
      }).join("\n");
      const totalNum = Object.keys(cart).reduce((s, id) => s + (productById(id).price || 0) * cart[id], 0);
      const totalLine = totalNum ? `\nTotal indicatif : ${totalNum.toLocaleString("fr-FR")} € (à confirmer avec la disponibilité et la livraison)\n` : "";
      const mode = f.get("mode") === "livraison" ? "Livraison (sur devis)" : "Retrait au showroom — Gamaches-en-Vexin";
      const body =
`Bonjour,

Je souhaite passer commande des pièces suivantes :

${lines}
${totalLine}
Mode de réception : ${mode}

Coordonnées :
Nom : ${f.get("nom")}
Email : ${f.get("email")}
Téléphone : ${f.get("tel") || "—"}

Message :
${f.get("msg") || "—"}

Envoyé depuis la boutique agathefortin.com`;
      location.href = `mailto:contact@agathefortin.com?subject=${encodeURIComponent("Demande de commande — Boutique Décor")}&body=${encodeURIComponent(body)}`;
      $(".order-form-wrap", oModal).style.display = "none";
      $(".order-ok", oModal).style.display = "";
      cart = {}; saveCart(); updateBadges(); renderCart();
    });
  }

  /* ---------- apparitions douces (v8) ---------- */
  if (!reduced) {
    const fxEls = $$(".section .container > *, .hb-text > *, .cta-inner > *");
    fxEls.forEach((el, i) => { el.classList.add("fx"); el.style.transitionDelay = (i % 4) * 0.06 + "s"; });
    const fxIo = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("fx-in"); fxIo.unobserve(e.target); } });
    }, { threshold: 0.08, rootMargin: "0px 0px -4% 0px" });
    fxEls.forEach(el => fxIo.observe(el));
  }

  updateBadges();
  renderCart();

  /* ---------- formulaire contact ---------- */
  const cForm = $("#contact-form");
  if (cForm) {
    cForm.addEventListener("submit", e => {
      e.preventDefault();
      const f = new FormData(cForm);
      const body = `Nom : ${f.get("nom")}\nEmail : ${f.get("email")}\nTéléphone : ${f.get("tel") || "—"}\n\n${f.get("msg")}`;
      location.href = `mailto:contact@agathefortin.com?subject=${encodeURIComponent("Contact — " + (f.get("sujet") || "Site internet"))}&body=${encodeURIComponent(body)}`;
      toast("Votre message est prêt dans votre logiciel de messagerie.");
    });
  }
})();

/* ============================================================
   v9 — mouvement : reveals d'images, titres masqués,
   parallaxe douce, transitions de page
   ============================================================ */
(() => {
  "use strict";
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const QA = location.search.indexOf("qa=1") !== -1;
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches || QA;
  if (reduced) return;

  /* images : balayage au défilement */
  const imgTargets = $$(".imgwrap, .product .ph, .work .ph, .showroom-photos img, .gallery-strip img, .pp-photo");
  imgTargets.forEach(el => el.classList.add("reveal-img"));
  const imgIo = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("img-in"); imgIo.unobserve(e.target); }
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -4% 0px" });
  imgTargets.forEach(el => imgIo.observe(el));

  /* titres h1/h2 : ligne masquée qui monte */
  $$("main h2, .hb-text h1, .hero2-text h1").forEach(h => {
    if (h.closest(".teaser-head")) { /* garde l'alignement base-ligne */ }
    const span = document.createElement("span");
    span.className = "tl";
    const inner = document.createElement("span");
    while (h.firstChild) inner.appendChild(h.firstChild);
    span.appendChild(inner);
    h.appendChild(span);
  });
  const tlIo = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("tl-in"); tlIo.unobserve(e.target); }
    });
  }, { threshold: 0.4 });
  $$(".tl").forEach(el => tlIo.observe(el));
  requestAnimationFrame(() => $$(".hb-text .tl, .hero2-text .tl").forEach(el => el.classList.add("tl-in")));

  /* parallaxe très douce dans les grandes images */
  const plx = $$(".hb-media img, .showroom-photos img, .hs-col");
  if (plx.length) {
    plx.forEach(el => el.classList.add("plx"));
    let ticking = false;
    const update = () => {
      ticking = false;
      const vh = innerHeight;
      plx.forEach((el, i) => {
        const r = (el.closest(".hb-media") || el.closest(".hs-col") || el).getBoundingClientRect();
        if (r.bottom < -80 || r.top > vh + 80) return;
        const p = (r.top + r.height / 2 - vh / 2) / vh;
        const amp = el.dataset.plx ? +el.dataset.plx : (el.closest(".hb-media") ? 26 : (i % 2 ? 14 : 22));
        el.style.translate = "0 " + (p * amp).toFixed(1) + "px";
      });
    };
    addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }

  /* la flèche se dessine quand la section arrive */
  const arrows = document.querySelectorAll(".where-arrow");
  const route = document.querySelector(".sr-route");
  if (arrows.length && route) {
    let drawn = false;
    const draw = () => {
      if (drawn) return; drawn = true;
      arrows.forEach(a => a.classList.add("draw"));
      route.classList.add("drawn");
      const g = document.querySelector(".sr-grid"); if (g) g.classList.add("drawn");
      removeEventListener("scroll", check);
    };
    const check = () => {
      const r = route.getBoundingClientRect();
      if (r.top < innerHeight * 0.8 && r.bottom > 0) draw();
    };
    addEventListener("scroll", check, { passive: true });
    check();
  }

  /* showroom → carte : défilement doux puis halo d'arrivée */
  const toMap = document.querySelector(".to-map");
  const mapCard = document.querySelector(".showroom .map-card");
  if (toMap && mapCard) {
    toMap.addEventListener("click", e => {
      e.preventDefault();
      mapCard.scrollIntoView({ behavior: "smooth", block: "center" });
      let done = false;
      const land = () => {
        if (done) return; done = true;
        document.querySelectorAll(".where-arrow").forEach(a => a.classList.add("draw"));
        const rt = document.querySelector(".sr-route"); if (rt) rt.classList.add("drawn");
        const gg = document.querySelector(".sr-grid"); if (gg) gg.classList.add("drawn");
        mapCard.classList.remove("arrive"); void mapCard.offsetWidth; mapCard.classList.add("arrive");
      };
      if ("onscrollend" in window) addEventListener("scrollend", land, { once: true });
      setTimeout(land, 1100);
    });
  }

  /* transition de page en fondu */
  document.addEventListener("click", e => {
    if (e.defaultPrevented) return;
    const a = e.target.closest("a[href]");
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey || a.target === "_blank") return;
    const href = a.getAttribute("href");
    if (!href || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:") || href.startsWith("http")) return;
    e.preventDefault();
    document.body.classList.add("pageout");
    setTimeout(() => { location.href = href; }, 200);
  });
})();

/* ============================================================
   v21 — flèche showroom : de l'épingle au bord de la carte,
   calculée sur les positions réelles
   ============================================================ */
(() => {
  const grid = document.querySelector(".sr-grid");
  const svg = grid && grid.querySelector(".sr-arrow");
  if (!svg) return;
  const pin = grid.querySelector(".to-map svg");
  const map = grid.querySelector(".map-card");
  const label = grid.querySelector(".sr-label");
  const line = svg.querySelector(".wa-line");
  const head = svg.querySelector(".wa-head");

  const layout = () => {
    if (innerWidth < 900) return;
    const chip = grid.querySelector(".to-map");
    const g = grid.getBoundingClientRect();
    const c = chip.getBoundingClientRect();
    const m = map.getBoundingClientRect();
    const sx = c.right + 12 - g.left;
    const sy = c.top + c.height / 2 - g.top;
    const ex = m.left - 12 - g.left;
    const ey = m.top + m.height / 2 - g.top;
    const dx = ex - sx;
    const sag = Math.min(46, Math.max(22, dx * 0.32));
    const c1x = sx + dx * 0.32, c1y = sy + sag;
    const c2x = sx + dx * 0.7, c2y = ey + sag * 0.55;
    svg.setAttribute("width", g.width);
    svg.setAttribute("height", g.height);
    svg.setAttribute("viewBox", `0 0 ${g.width} ${g.height}`);
    line.setAttribute("d", `M${sx} ${sy} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${ex} ${ey}`);
    // pointe orientée selon la tangente d'arrivée
    const a = Math.atan2(ey - c2y, ex - c2x), L = 14, w = 0.55;
    const p1x = ex - L * Math.cos(a - w), p1y = ey - L * Math.sin(a - w);
    const p2x = ex - L * Math.cos(a + w), p2y = ey - L * Math.sin(a + w);
    head.setAttribute("d", `M${p1x} ${p1y} L ${ex} ${ey} L ${p2x} ${p2y}`);
  };
  layout();
  addEventListener("resize", layout);
  addEventListener("load", layout);
  if (document.fonts) document.fonts.ready.then(layout);
  if ("ResizeObserver" in window) new ResizeObserver(layout).observe(grid);
})();
