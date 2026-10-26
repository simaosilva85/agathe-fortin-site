#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exporte le catalogue produits au format Meta Commerce (boutique Instagram/Facebook).

Usage : python3 export_meta.py [https://www.mondomaine.com]
Génère assets/meta-catalog.csv — à importer dans Meta Commerce Manager
(Catalogue → Sources de données → Flux de données → Importer un fichier).
"""
import csv, json, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://agathefortin.com").rstrip("/")

t = open(os.path.join(ROOT, "assets/data.js")).read()
data = json.loads(t[t.find("{"):t.rfind("}") + 1])

CATS = {
    "ceramiques": "Céramiques",
    "anduze": "Vases d'Anduze",
    "objets": "Objets décoratifs",
    "metal": "Peint sur métal",
}

out = os.path.join(ROOT, "assets/meta-catalog.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    # colonnes officielles du flux Meta Commerce
    w.writerow(["id", "title", "description", "availability", "condition",
                "price", "link", "image_link", "brand",
                "google_product_category", "product_type"])
    for p in data["products"]:
        title = p["name"] + (f" — {p['coloris']}" if p.get("coloris") else "")
        desc = (p.get("desc") or "") + f" Dimensions : {p.get('dimtxt', p['specs'])}."
        w.writerow([
            p["id"].upper(),
            title[:150],
            desc[:5000],
            "in stock",
            "new",
            f"{p['price']}.00 EUR" if p.get("price") else "",
            f"{BASE}/produit.html?id={p['id']}",
            f"{BASE}/{p['img']}",
            "Agathe Fortin Paysages",
            "Home & Garden > Lawn & Garden > Gardening > Pots & Planters",
            f"Décor > {CATS[p['cat']]}",
        ])

print(f"✓ {len(data['products'])} produits exportés → {out}")
print(f"  URLs basées sur : {BASE}  (relancer avec le vrai domaine une fois le site en ligne)")
