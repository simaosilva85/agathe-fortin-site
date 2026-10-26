#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agathe Fortin Paysages — v7 « Sobre ».
Charte du site d'origine : Montserrat + Lato, anthracite, or #a7782d, crème.
Aucune ligne décorative, aucun texte sur image, photos en format natif."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
V = "35"

NAV = [
    ("index.html", "Accueil"),
    ("vegetal.html", "Végétal"),
    ("projets.html", "Projets"),
    ("evenementiel.html", "Événementiel"),
    ("boutique.html", "Boutique"),
    ("contact.html", "Contact"),
]

def head(title, desc):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/showroom/salon.jpg">
<link rel="icon" href="assets/img/brand/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={V}">
</head>
"""

def header(active):
    links = "".join(
        f'<a class="nav-link{" active" if href == active else ""}" href="{href}">{label}</a>'
        for href, label in NAV
    )
    mob = "".join(
        f'<a class="mob-link{" active" if href == active else ""}" href="{href}">{label}</a>'
        for href, label in NAV
    )
    return f"""
<header id="header">
  <div class="header-inner">
    <a class="brand" href="index.html" aria-label="Agathe Fortin Paysages — accueil">
      <img src="assets/img/brand/logo.png" alt="Agathe Fortin Paysages">
    </a>
    <nav class="nav" aria-label="Navigation principale">{links}</nav>
    <div class="header-actions">
      <button class="cart-btn" data-cart-open aria-label="Ouvrir ma commande">
        <span class="cart-label">Commande</span>
        <span class="cart-count">0</span>
      </button>
      <button id="burger" class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<div id="mobile-menu">
  {mob}
  <div class="mob-foot">contact@agathefortin.com<br>+33 (0)9 63 52 35 95</div>
</div>
"""

FOOTER = """
<footer id="footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="assets/img/brand/logo.png" alt="Agathe Fortin Paysages">
        <p>Sélection et courtage de végétaux, céramiques et décors.<br>Entre Paris et Rouen, à 20 minutes de Giverny.</p>
      </div>
      <div>
        <h4>Navigation</h4>
        <ul>
          <li><a href="index.html">Accueil</a></li>
          <li><a href="vegetal.html">Végétal</a></li>
          <li><a href="projets.html">Projets</a></li>
          <li><a href="evenementiel.html">Événementiel</a></li>
          <li><a href="boutique.html">Boutique</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:contact@agathefortin.com">contact@agathefortin.com</a></li>
          <li><a href="tel:+33963523595">+33 (0)9 63 52 35 95</a></li>
          <li><a href="https://www.facebook.com/AgatheFortinPaysages/" target="_blank" rel="noopener">Facebook</a></li>
        </ul>
      </div>
      <div>
        <h4>Adresses</h4>
        <address>Bureau — 4, chemin du Raillard<br>27150 Gamaches-en-Vexin<br><br>Dépôt &amp; Showroom — 9, rue Oulgate<br>27150 Gamaches-en-Vexin</address>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; Agathe Fortin Paysages 2026</span>
      <a href="contact.html">Nous trouver</a>
    </div>
  </div>
</footer>

<div id="cart-backdrop"></div>
<aside id="cart-drawer" aria-label="Ma commande">
  <div class="cart-head">
    <div><h3>Ma commande</h3><span class="sub">0 article</span></div>
    <button class="modal-close cart-close" aria-label="Fermer">&#10005;</button>
  </div>
  <div class="cart-items"></div>
  <div class="cart-foot">
    <div class="row"><span>Total de la sélection</span><strong>—</strong></div>
    <button class="btn" data-checkout>Envoyer ma demande</button>
    <p class="hint">Disponibilité, livraison et paiement confirmés sous 48&nbsp;h.</p>
  </div>
</aside>

<div id="product-modal" class="modal" role="dialog" aria-modal="true">
  <div class="modal-backdrop" data-modal-close></div>
  <div class="modal-panel">
    <button class="modal-close" data-modal-close aria-label="Fermer">&#10005;</button>
    <div class="mp-img"><img src="" alt=""></div>
    <div class="mp-body">
      <span class="mp-cat">Céramique</span>
      <h3 class="mp-name"></h3>
      <p class="specs mp-specs"></p>
      <p class="mp-desc">Pièce sélectionnée par Agathe Fortin pour son showroom de Gamaches-en-Vexin. Dimensions en centimètres.</p>
      <div class="price-row">
        <span class="mp-price">Prix sur demande</span>
        <div class="qty">
          <button data-mq-dec aria-label="Moins">&minus;</button>
          <span class="q">1</span>
          <button data-mq-inc aria-label="Plus">+</button>
        </div>
      </div>
      <div class="actions">
        <button class="btn" data-modal-add>Ajouter à ma commande</button>
      </div>
    </div>
  </div>
</div>

<div id="order-modal" class="modal" role="dialog" aria-modal="true">
  <div class="modal-backdrop" data-modal-close></div>
  <div class="modal-panel checkout-panel">
    <button class="modal-close" data-modal-close aria-label="Fermer">&#10005;</button>
    <div class="mp-body">
      <div class="order-form-wrap">
        <h3 class="mp-name">Finaliser ma demande</h3>
        <p class="mp-desc">Nous revenons vers vous sous 48&nbsp;h avec la disponibilité des pièces, le devis et les modalités de réception.</p>
        <form id="order-form">
          <div class="form-grid">
            <div class="field"><label for="o-nom">Nom complet *</label><input id="o-nom" name="nom" required autocomplete="name"></div>
            <div class="field"><label for="o-email">Email *</label><input id="o-email" name="email" type="email" required autocomplete="email"></div>
            <div class="field"><label for="o-tel">Téléphone</label><input id="o-tel" name="tel" type="tel" autocomplete="tel"></div>
            <div class="field"><label>Réception</label>
              <div class="seg">
                <label><input type="radio" name="mode" value="retrait" checked><span>Retrait showroom</span></label>
                <label><input type="radio" name="mode" value="livraison"><span>Livraison (devis)</span></label>
              </div>
            </div>
            <div class="field full"><label for="o-msg">Message</label><textarea id="o-msg" name="msg"></textarea></div>
          </div>
          <div class="actions"><button class="btn" type="submit">Envoyer ma demande</button></div>
        </form>
      </div>
      <div class="order-ok" style="display:none">
        <div class="check">&#10003;</div>
        <h3>Votre demande est prête</h3>
        <p class="mp-desc">Votre logiciel de messagerie s'est ouvert avec le récapitulatif.<br>Il ne reste qu'à cliquer sur «&nbsp;Envoyer&nbsp;».</p>
        <button class="btn btn--dark" data-modal-close>Fermer</button>
      </div>
    </div>
  </div>
</div>

<script src="assets/data.js?v=%%V%%"></script>
<script src="assets/js/main.js?v=%%V%%"></script>
</body>
</html>
""".replace("%%V%%", V)

# ------------------------------------------------------------------
# En-tête de page interne : titre + texte, photo portrait à droite
# ------------------------------------------------------------------
def page_head(title, lead, img):
    return f"""
<section class="hero-bleed hero-bleed--page">
  <div class="hb-text">
    <h1>{title}</h1>
    <p>{lead}</p>
  </div>
  <div class="hb-media">
    <img src="{img}" alt="">
  </div>
</section>
"""

# ------------------------------------------------------------------
# ACCUEIL
# ------------------------------------------------------------------
INDEX = """
<section class="hero2">
  <div class="container hero2-grid">
    <div class="hero2-text">
      <h1>Céramiques, végétaux &amp; décors d'exception</h1>
      <p>Depuis 2005, Agathe Fortin sélectionne pièces et végétaux chez les meilleurs producteurs français et européens. Le showroom vous accueille à Gamaches-en-Vexin, à 20 minutes du jardin de Monet.</p>
      <div class="hero-ctas">
        <a class="btn" href="boutique.html">Découvrir la boutique</a>
        <a class="link-gold" href="contact.html">Visite sur rendez-vous</a>
      </div>
      <p class="hb-reassure">Retrait au showroom &nbsp;·&nbsp; Livraison France &nbsp;·&nbsp; Réponse sous 48&nbsp;h</p>
    </div>
    <div class="hero2-stack">
      <figure class="hs-col" data-plx="34"><img src="assets/img/showroom/turquoise.jpg" alt="Le coin turquoise du showroom"></figure>
      <figure class="hs-col" data-plx="12"><img src="assets/img/showroom/salon.jpg" alt="La halle du showroom" fetchpriority="high"></figure>
      <figure class="hs-col" data-plx="50"><img src="assets/img/showroom/pistache.jpg" alt="Les verts tendres du showroom"></figure>
      <div class="hs-badge">
        <img src="assets/img/brand/logo.png" alt="">
        <span><strong>Le showroom</strong>Gamaches-en-Vexin · sur rendez-vous</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="univers">
  <div class="container">
    <h2>Trois façons de nous découvrir</h2>
    <div class="cards3">
      <a class="card" href="boutique.html">
        <span class="imgwrap"><img src="assets/img/showroom/rouge.jpg" alt="Céramiques de la boutique" loading="lazy"></span>
        <h3>La boutique</h3>
        <p>Céramiques, vases d'Anduze et pièces choisies, à commander en ligne.</p>
      </a>
      <a class="card" href="vegetal.html">
        <span class="imgwrap"><img src="assets/img/slider2/agathe-fortin-paysages-28289.jpg" alt="Recherche de végétaux en pépinière" loading="lazy"></span>
        <h3>Le végétal</h3>
        <p>Recherche et courtage de végétaux, un service gratuit et personnalisé.</p>
      </a>
      <a class="card" href="projets.html">
        <span class="imgwrap"><img src="assets/img/projets/agathe-fortin-paysages-83602.jpg" alt="Jardin réalisé à Marrakech" loading="lazy"></span>
        <h3>Les projets</h3>
        <p>Jardins, terrasses et décors — de l'Eure à Marrakech.</p>
      </a>
    </div>
  </div>
</section>

<section class="cta-split">
  <div class="container cs-grid">
    <div class="cs-text">
      <h2>Un jardin, une terrasse, un décor à imaginer&nbsp;?</h2>
      <p>Un interlocuteur unique, de l'étude à la livraison. Racontez-nous votre projet — réponse sous 48&nbsp;h.</p>
      <a class="btn" href="contact.html">Parlons de votre projet</a>
    </div>
    <span class="imgwrap cs-img"><img src="assets/img/showroom/corail.jpg" alt="Hortensias séchés et céramiques du showroom" loading="lazy"></span>
  </div>
</section>



<section class="section" id="boutique-teaser">
  <div class="container">
    <div class="teaser-head">
      <h2>Pièces choisies</h2>
      <a class="link-gold" href="boutique.html">Toute la boutique</a>
    </div>
  </div>
  <div class="container">
    <div class="teaser-scroll" id="shop-teaser"></div>
  </div>
</section>

<section class="section section--white" id="equipe">
  <div class="container founder-grid">
    <span class="imgwrap founder-photo"><img src="assets/img/brand/agathe-fondatrice.jpg" alt="Agathe Fortin, fondatrice"></span>
    <div class="founder-text">
      <blockquote>«&nbsp;Peu de pépinières me sont inconnues. Mon métier, c'est dénicher le végétal d'exception — la perle rare.&nbsp;»</blockquote>
      <p class="founder-sign"><strong>Agathe Fortin</strong> · Fondatrice &amp; paysagiste — trente ans de métier</p>
      <div class="duo">
        <figure><img src="assets/img/brand/jean.png" alt="Jean-François Bourgeon"><figcaption><strong>Jean-François Bourgeon</strong><br>Dessinateur paysagiste</figcaption></figure>
        <figure><img src="assets/img/brand/laure.png" alt="Laure Nicolas"><figcaption><strong>Laure Nicolas</strong><br>Assistante de direction</figcaption></figure>
      </div>
    </div>
  </div>
</section>

<section class="section showroom" id="showroom">
  <div class="container sr-grid">
    <svg class="sr-arrow where-arrow" aria-hidden="true"><path class="wa-line" pathLength="1" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path class="wa-head" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div class="sr-text">
      <h2>Le showroom</h2>
      <p>Sous une grande halle, des centaines de céramiques réunies par couleurs : les rouges coquelicot, les bleus céladon, les verts émaillés, les ocres. Chaque pièce est choisie une à une.</p>
      <p>La visite se fait sur rendez-vous — et lors de nos week-ends portes ouvertes.</p>
      <a class="btn" href="contact.html">Prendre rendez-vous</a>
    </div>
    <div class="showroom-photos">
      <img src="assets/img/showroom/bleu.jpg" alt="Les bleus du showroom" loading="lazy">
      <img src="assets/img/showroom/vert.jpg" alt="Les verts du showroom" loading="lazy">
      <img src="assets/img/showroom/ocre.jpg" alt="Les ocres du showroom" loading="lazy">
    </div>
    <div class="sr-route">
      <a class="to-map" href="#ou">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z" fill="currentColor"/><circle cx="12" cy="10" r="2.6" fill="#fff"/></svg>
        <span><strong>9, rue Oulgate — Gamaches-en-Vexin</strong><em>À 20 minutes du jardin de Monet</em></span>
      </a>
      <svg class="where-arrow where-arrow--mob" viewBox="0 0 70 96" fill="none" aria-hidden="true">
        <path class="wa-line" pathLength="1" d="M22 4 C 8 40, 46 52, 34 88" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
        <path class="wa-head" d="M22 76 L 34 90 L 44 74" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <a class="map-card" id="ou" href="https://www.google.com/maps/search/?api=1&amp;query=9+rue+Oulgate+27150+Gamaches-en-Vexin" target="_blank" rel="noopener" aria-label="Itinéraire vers le showroom — ouvre Google Maps">
      <iframe src="https://www.openstreetmap.org/export/embed.html?bbox=1.6015%2C49.2629%2C1.6255%2C49.2739&amp;layer=mapnik" title="Carte du showroom" loading="lazy" tabindex="-1"></iframe>
      <span class="map-pin"><span class="map-pin-box"><img src="assets/img/brand/logo.png" alt=""></span></span>
      <span class="map-tag"><img src="assets/img/showroom/bleu.jpg" alt=""><span class="mt-txt"><strong>Le showroom</strong><span>Visite sur rendez-vous</span></span><em>Itinéraire &#8594;</em></span>
      <span class="map-credit">© OpenStreetMap</span>
    </a>
  </div>
</section>

"""

# ------------------------------------------------------------------
# VÉGÉTAL
# ------------------------------------------------------------------
VEG_CATS = [
    "Arbres & arbustes d'ornement", "Fruitiers", "Rosiers",
    "Conifères", "Vivaces & graminées", "Jeunes plants forestiers",
    "Plantes méditerranéennes", "Plantes exotiques", "Plantes aquatiques",
]
SLIDER2 = [
    "agathe-fortin-paysages-28289.jpg", "agathe-fortin-paysages-36398.jpg",
    "agathe-fortin-paysages-42456.jpg", "agathe-fortin-paysages-47966.jpg",
    "agathe-fortin-paysages-56776.jpg", "agathe-fortin-paysages-69926.jpg",
    "agathe-fortin-paysages-70482.jpg", "agathe-fortin-paysages-75173.jpg",
    "agathe-fortin-paysages-81655.jpg",
]

VEGETAL = page_head(
    "Le végétal",
    "Un service gratuit et personnalisé de recherche de végétaux : nous regroupons sur notre dépôt les meilleures pépinières françaises et européennes, et chaque commande expédiée est contrôlée par nos soins.",
    "assets/img/brand/bg-vegetal.jpg",
) + f"""
<section class="section section--white">
  <div class="container">
    <h2>Notre sélection</h2>
    <ul class="pill-list">
      {"".join(f'<li>{c}</li>' for c in VEG_CATS)}
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Pourquoi nous confier vos recherches</h2>
    <div class="cards3 cards3--text">
      <div class="tcard"><h3>30 ans d'expérience</h3><p>Une ancienneté qui nous vaut les meilleures relations avec nos fournisseurs, en France et en Europe.</p></div>
      <div class="tcard"><h3>Un interlocuteur unique</h3><p>De la recherche jusqu'à l'expédition, nous nous occupons de tout — budgets optimisés, juste prix.</p></div>
      <div class="tcard"><h3>Réponse sous 48 h</h3><p>Disponibilité et devis compris. Conseils de plantation et d'entretien inclus.</p></div>
    </div>
    <p class="services-line">Également : contrats de culture · études et plans de plantations · potagers «&nbsp;clé en main&nbsp;» · végétalisation de murs · métrage et estimations · assistance aux Entreprises du Paysage · créations d'ambiances.</p>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <h2>Le végétal en images</h2>
  </div>
  <div class="container">
    <div class="gallery-strip" data-title="Le végétal" data-sub="Dépôt de Gamaches-en-Vexin">
      {"".join(f'<img src="assets/img/slider2/{s}" alt="Végétaux — Agathe Fortin Paysages" loading="lazy">' for s in SLIDER2)}
    </div>
  </div>
</section>

<section class="cta">
  <div class="container cta-inner">
    <h2>Confiez-nous l'étude de vos projets</h2>
    <p>Trente ans de courtage de végétaux — c'est notre métier.</p>
    <a class="btn btn--light" href="contact.html">Demander une étude</a>
  </div>
</section>
"""

# ------------------------------------------------------------------
# PROJETS / ÉVÉNEMENTIEL
# ------------------------------------------------------------------
def works_page(kind, title, lead, img, filters=True):
    chips = """
      <div class="chips" id="works-filters">
        <button class="chip on" data-f="all">Tout voir</button>
        <button class="chip" data-f="fr">France</button>
        <button class="chip" data-f="intl">International</button>
      </div>""" if filters else "<div></div>"
    return page_head(title, lead, img) + f"""
<section class="section section--white">
  <div class="container">
    <div class="shop-toolbar">
      {chips}
      <span class="shop-count" id="works-count"></span>
    </div>
    <div class="works-grid" id="works-grid" data-kind="{kind}"></div>
  </div>
</section>

<section class="cta">
  <div class="container cta-inner">
    <h2>Et si le prochain projet était le vôtre&nbsp;?</h2>
    <a class="btn btn--light" href="contact.html">Parlons-en</a>
  </div>
</section>
"""

PROJETS = works_page(
    "projets", "Projets & réalisations",
    "Jardins privés, patios, terrasses et décors végétaux — de l'Eure à Marrakech, de Paris à West Palm Beach. Ouvrez chaque réalisation pour parcourir sa galerie.",
    "assets/img/projets/agathe-fortin-paysages-83602.jpg",
)

EVENEMENTIEL = works_page(
    "evenements", "Événementiel",
    "Salons, fêtes des plantes, inaugurations et scénographies végétales — revivez nos événements en images.",
    "assets/img/evenements/agathe-fortin-paysages-53565.jpg",
    filters=False,
)

# ------------------------------------------------------------------
# BOUTIQUE
# ------------------------------------------------------------------
BOUTIQUE = page_head(
    "La boutique",
    "Les céramiques du showroom, sélectionnées pour durer — dehors comme dedans. Commandez en ligne : retrait à Gamaches-en-Vexin ou livraison soignée sur devis, réponse sous 48 h.",
    "assets/img/showroom/rouge.jpg",
) + """
<section class="section section--white" id="catalogue">
  <div class="container">
    <div class="shop-toolbar" id="shop-toolbar">
      <div class="chips" id="shop-filters">
        <button class="chip on" data-cat="all">Tout voir</button>
        <button class="chip" data-cat="ceramiques">Céramiques</button>
        <button class="chip" data-cat="anduze">Vases d'Anduze</button>
        <button class="chip" data-cat="objets">Objets</button>
        <button class="chip" data-cat="metal">Peint sur métal</button>
      </div>
      <div class="shop-tools">
        <input id="shop-search" type="search" placeholder="Rechercher…" aria-label="Rechercher une pièce">
        <select id="shop-sort" aria-label="Trier">
          <option value="featured">Notre sélection</option>
          <option value="price-asc">Prix croissant</option>
          <option value="price-desc">Prix décroissant</option>
          <option value="name">Nom A-Z</option>
        </select>
        <span class="shop-count" id="shop-count"></span>
      </div>
    </div>
    <div class="shop-grid" id="shop-grid"></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cards3 cards3--text">
      <div class="tcard"><h3>Sélection d'Agathe</h3><p>Chaque pièce est choisie en direct chez les meilleurs céramistes — trente ans d'œil expert.</p></div>
      <div class="tcard"><h3>Retrait au showroom</h3><p>À Gamaches-en-Vexin, à 20 minutes de Giverny. Venez voir les pièces en vrai.</p></div>
      <div class="tcard"><h3>Livraison soignée</h3><p>Sur devis partout en France, emballage adapté aux grandes céramiques. Confirmation sous 48&nbsp;h.</p></div>
    </div>
  </div>
</section>
"""

# ------------------------------------------------------------------
# PRODUIT
# ------------------------------------------------------------------
PRODUIT = """
<section class="pp-wrap">
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="boutique.html">&#8592; Retour à la boutique</a>
    </nav>
    <div class="pp-grid" id="pp-root">
      <div class="pp-photo" id="pp-photo"><img src="" alt="" id="pp-img"></div>
      <div class="pp-info">
        <span class="mp-cat" id="pp-cat"></span>
        <h1 class="pp-name" id="pp-name"></h1>
        <div class="pp-price" id="pp-price"></div>
        <p class="pp-desc" id="pp-desc"></p>
        <table class="pp-specs" id="pp-specs"></table>
        <div class="pp-buy">
          <div class="qty">
            <button data-pq-dec aria-label="Moins">&minus;</button>
            <span class="q" id="pp-qty">1</span>
            <button data-pq-inc aria-label="Plus">+</button>
          </div>
          <button class="btn pp-add" id="pp-add">Ajouter à ma commande</button>
        </div>
        <ul class="pp-notes">
          <li>Retrait offert au showroom de Gamaches-en-Vexin (27)</li>
          <li>Livraison en France sur devis, emballage renforcé</li>
          <li>Disponibilité et délais confirmés sous 48&nbsp;h</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<div class="pp-stickybar" id="pp-stickybar">
  <div class="sb-info"><strong id="ppsb-price"></strong><span id="ppsb-name"></span></div>
  <button class="btn" id="ppsb-add">Ajouter</button>
</div>

<section class="section section--white" id="pp-related-sec">
  <div class="container">
    <div class="teaser-head">
      <h2>Vous aimerez aussi</h2>
      <a class="link-gold" href="boutique.html">Toute la boutique</a>
    </div>
    <div class="shop-grid" id="pp-related"></div>
  </div>
</section>
"""

# ------------------------------------------------------------------
# CONTACT
# ------------------------------------------------------------------
CONTACT = page_head(
    "Contact",
    "Entre Paris et Rouen, à 20 minutes du jardin de Claude Monet. Le showroom se visite sur rendez-vous — réponse sous 48 h.",
    "assets/img/showroom/turquoise.jpg",
) + """
<section class="section section--white" id="adresses">
  <div class="container">
    <div class="cards3 cards3--text">
      <div class="tcard"><h3>Bureau</h3><p>4, chemin du Raillard<br>27150 Gamaches-en-Vexin</p><p><a class="link-gold" href="tel:+33963523595">+33 (0)9 63 52 35 95</a><br><a class="link-gold" href="mailto:contact@agathefortin.com">contact@agathefortin.com</a></p></div>
      <div class="tcard"><h3>Dépôt &amp; Showroom</h3><p>9, rue Oulgate<br>27150 Gamaches-en-Vexin</p><p>Visite sur rendez-vous, et lors des week-ends portes ouvertes.</p></div>
      <div class="tcard"><h3>Suivez-nous</h3><p>L'actualité du showroom, les arrivages et les événements.</p><p><a class="link-gold" href="https://www.facebook.com/AgatheFortinPaysages/" target="_blank" rel="noopener">Facebook</a></p></div>
    </div>
  </div>
</section>

<section class="section" id="ecrire">
  <div class="container contact-grid">
    <div>
      <h2>Écrivez-nous</h2>
      <p>Décrivez-nous votre jardin, votre terrasse ou votre envie — nous revenons vers vous avec des idées, des végétaux et un chiffrage.</p>
    </div>
    <form id="contact-form">
      <div class="form-grid">
        <div class="field"><label for="c-nom">Nom complet *</label><input id="c-nom" name="nom" required autocomplete="name"></div>
        <div class="field"><label for="c-email">Email *</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
        <div class="field"><label for="c-tel">Téléphone</label><input id="c-tel" name="tel" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="c-sujet">Sujet</label>
          <select id="c-sujet" name="sujet">
            <option>Recherche de végétaux</option>
            <option>Étude paysagère</option>
            <option>Boutique &amp; décor</option>
            <option>Événementiel</option>
            <option>Autre demande</option>
          </select>
        </div>
        <div class="field full"><label for="c-msg">Votre message *</label><textarea id="c-msg" name="msg" required></textarea></div>
      </div>
      <div class="actions"><button class="btn" type="submit">Envoyer</button></div>
    </form>
  </div>
</section>

<section id="plan">
  <div class="map-wrap">
    <iframe title="Plan — Gamaches-en-Vexin" loading="lazy"
      src="https://www.openstreetmap.org/export/embed.html?bbox=1.5895%2C49.2574%2C1.6375%2C49.2794&amp;layer=mapnik&amp;marker=49.2684%2C1.6135"></iframe>
  </div>
</section>
"""


# ------------------------------------------------------------------
# ACCUEIL — VERSION 2 (« le showroom de nuit »)
# ------------------------------------------------------------------
def _section(src, start_marker):
    a = src.index(start_marker)
    b = src.index("</section>", a) + len("</section>")
    return a, b

RIBBON = ["salon", "rouge", "turquoise", "vert", "ocre", "bleu", "pistache", "corail"]

def _ribbon_fig(i, n):
    load = 'fetchpriority="high"' if i < 3 else 'loading="lazy"'
    return f'      <figure><img src="assets/img/showroom/{n}.jpg" alt="Le showroom" {load}></figure>\n'
HERO_V2 = """<section class="v2h">
  <div class="container v2h-grid">
    <div class="v2h-card">
      <span class="v2-status"><i></i>Showroom ouvert sur rendez-vous</span>
      <h1>Céramiques, végétaux &amp; décors d'exception</h1>
      <p>Depuis 2005, Agathe Fortin sélectionne pièces et végétaux chez les meilleurs producteurs français et européens — à Gamaches-en-Vexin, à 20 minutes du jardin de Monet.</p>
      <div class="v2-ctas">
        <a class="btn" href="boutique.html">Découvrir la boutique</a>
        <a class="v2h-link" href="contact.html">Visite sur rendez-vous <span>&#8594;</span></a>
      </div>
    </div>
    <a class="v2-tile v2h-a" href="contact.html">
      <img src="assets/img/showroom/salon.jpg" alt="La halle du showroom" fetchpriority="high">
      <span class="v2-chip"><b>01</b><strong>La halle</strong><em>Des centaines de pièces</em><i class="v2-go">&#8594;</i></span>
    </a>
    <a class="v2-tile v2h-b" href="boutique.html">
      <img src="assets/img/showroom/turquoise.jpg" alt="Le coin turquoise du showroom">
      <span class="v2-chip v2-chip--sm"><strong>Pièces choisies</strong><i class="v2-go">&#8594;</i></span>
    </a>
    <a class="v2-tile v2h-c" href="projets.html">
      <img src="assets/img/showroom/pistache.jpg" alt="Les verts tendres du showroom">
      <span class="v2-chip v2-chip--sm"><strong>Projets sur-mesure</strong><i class="v2-go">&#8594;</i></span>
    </a>
  </div>
</section>"""

UNIVERS_V2 = """<section class="section v2-univers" id="univers">
  <div class="container">
    <div class="v2-head">
      <h2>Trois façons de nous découvrir</h2>
      <p>Une boutique de pièces choisies, un service de recherche de végétaux, et trente ans de jardins réalisés.</p>
    </div>
    <div class="v2-bento">
      <a class="v2-tile v2-tile--big" href="boutique.html">
        <img src="assets/img/showroom/rouge.jpg" alt="Céramiques de la boutique" loading="lazy">
        <span class="v2-chip"><b>01</b><strong>La boutique</strong><em>Céramiques &amp; pièces choisies</em><i class="v2-go">&#8594;</i></span>
      </a>
      <a class="v2-tile" href="vegetal.html">
        <img src="assets/img/slider2/agathe-fortin-paysages-28289.jpg" alt="Recherche de végétaux en pépinière" loading="lazy">
        <span class="v2-chip"><b>02</b><strong>Le végétal</strong><em>Recherche &amp; courtage, gratuit</em><i class="v2-go">&#8594;</i></span>
      </a>
      <a class="v2-tile" href="projets.html">
        <img src="assets/img/projets/agathe-fortin-paysages-83602.jpg" alt="Jardin réalisé à Marrakech" loading="lazy">
        <span class="v2-chip"><b>03</b><strong>Les projets</strong><em>De l'Eure à Marrakech</em><i class="v2-go">&#8594;</i></span>
      </a>
    </div>
  </div>
</section>"""

CTA_V2 = """<section class="section section--white v2-cta2">
  <div class="container">
    <div class="v2-cta2-card">
      <span class="v2-cta2-img"><img src="assets/img/showroom/corail.jpg" alt="Hortensias séchés et céramiques du showroom" loading="lazy"></span>
      <div class="v2-cta2-text">
        <span class="v2-cta2-num">Votre projet</span>
        <h2>Un jardin, une terrasse, un décor à imaginer&nbsp;?</h2>
        <p>Un interlocuteur unique, de l'étude à la livraison. Racontez-nous votre envie — réponse sous 48&nbsp;h.</p>
        <a class="btn" href="contact.html">Parlons de votre projet</a>
      </div>
    </div>
  </div>
</section>"""

_v = INDEX
a, b = _section(_v, '<section class="hero2">');                 _v = _v[:a] + HERO_V2 + _v[b:]
a, b = _section(_v, '<section class="section section--white" id="univers">'); _v = _v[:a] + UNIVERS_V2 + _v[b:]
a, b = _section(_v, '<section class="cta-split">');             _v = _v[:a] + CTA_V2 + _v[b:]
INDEX_V2 = _v

# la mosaïque des univers (aimée en V2) remplace les 3 cartes simples dans la V1
a, b = _section(INDEX, '<section class="section section--white" id="univers">')
INDEX = INDEX[:a] + UNIVERS_V2.replace('class="section v2-univers"', 'class="section section--white v2-univers"') + INDEX[b:]

SWITCHER = """
<nav class="ds-switch" aria-label="Changer de version du design">
  <span>Design</span>
  <a href="index.html" class="%s">V1</a>
  <a href="index-v2.html" class="%s">V2</a>
</nav>
"""

PAGES = {
    "index.html": ("Agathe Fortin Paysages — Céramiques & végétaux | Giverny, Vexin",
                   "Sélection et courtage de végétaux, céramiques et décors. Showroom à Gamaches-en-Vexin, à 20 minutes de Giverny.",
                   INDEX),
    "index-v2.html": ("Agathe Fortin Paysages — Céramiques & végétaux | Giverny, Vexin",
                   "Sélection et courtage de végétaux, céramiques et décors. Showroom à Gamaches-en-Vexin, à 20 minutes de Giverny.",
                   INDEX_V2),
    "vegetal.html": ("Le Végétal — Agathe Fortin Paysages",
                     "Recherche de végétaux gratuite et personnalisée : arbres, fruitiers, rosiers, conifères, vivaces… Les meilleurs producteurs français et européens.",
                     VEGETAL),
    "projets.html": ("Projets & Réalisations — Agathe Fortin Paysages",
                     "25 réalisations paysagères, de l'Eure à Marrakech : jardins privés, patios, terrasses et décors végétaux.",
                     PROJETS),
    "evenementiel.html": ("Événementiel — Agathe Fortin Paysages",
                          "Salons, fêtes des plantes, inaugurations et scénographies végétales par Agathe Fortin Paysages.",
                          EVENEMENTIEL),
    "boutique.html": ("La Boutique — Céramiques & Décors | Agathe Fortin Paysages",
                      "Céramiques, vases d'Anduze, objets et tableaux peints sur métal du showroom de Gamaches-en-Vexin. Commandez en ligne, réponse sous 48 h.",
                      BOUTIQUE),
    "produit.html": ("Boutique — Agathe Fortin Paysages",
                     "Céramiques, vases d'Anduze et pièces décoratives du showroom d'Agathe Fortin — retrait à Gamaches-en-Vexin ou livraison sur devis.",
                     PRODUIT),
    "contact.html": ("Contact — Agathe Fortin Paysages",
                     "Bureau, dépôt et showroom à Gamaches-en-Vexin (27). Tél : +33 (0)9 63 52 35 95 — contact@agathefortin.com.",
                     CONTACT),
}

for fname, (title, desc, content) in PAGES.items():
    is_v2 = fname == "index-v2.html"
    page_head_html = head(title, desc)
    if is_v2:
        page_head_html = page_head_html.replace("</head>", f'<link rel="stylesheet" href="assets/css/v2.css?v={V}">\n</head>')
    body = '<body class="v2">\n' if is_v2 else '<body>\n'
    switch = ""
    if fname in ("index.html", "index-v2.html"):
        switch = SWITCHER % (("" , "on") if is_v2 else ("on", ""))
    html = page_head_html + body + header("index.html" if is_v2 else fname) + '\n<main id="main">' + content + '</main>\n' + switch + FOOTER
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit :", fname)
