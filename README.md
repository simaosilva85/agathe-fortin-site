# Agathe Fortin Paysages — refonte 2026

Refonte complète de https://agathefortin.com — identité de marque conservée
(anthracite chaud, bronze doré `#8c7d64`, ocre `#a7782d`, crème), toutes les
photos originales rapatriées en local (256 fichiers, ~47 Mo).

## Lancer le site

```bash
cd ~/Downloads/agathe-fortin && python3 -m http.server 4601
```

Puis ouvrir http://localhost:4601 — site 100 % statique, aucune dépendance à installer.

## Structure

- `index.html` — accueil : héros slider Ken Burns, présentation, chiffres animés,
  philosophie, compétences, équipe, aperçu boutique, CTA
- `vegetal.html` — les 9 familles de végétaux, engagements, galerie du dépôt
- `projets.html` — 25 réalisations, filtres France/International, galeries lightbox
- `evenementiel.html` — 17 événements en galeries
- `boutique.html` — **vraie boutique e-commerce** : tuiles catégories, recherche,
  tri par prix, 36 pièces avec ⚠ prix INDICATIFS (générés pour la maquette —
  à faire valider par Agathe dans `assets/data.js`, champ `price`)
- `produit.html?id=pXX` — **page produit individuelle** (photo, prix, specs,
  quantité, suggestions, JSON-LD) — format exigé par Instagram Shopping
- `export_meta.py` — génère `assets/meta-catalog.csv`, le flux produits à
  importer dans Meta Commerce Manager (boutique Instagram/Facebook) ;
  voir `INSTAGRAM.md` pour les 6 étapes de mise en place
- `contact.html` — adresses, formulaire, plan OpenStreetMap
- `build.py` — régénère les 6 pages (header/footer/panier partagés) : `python3 build.py`
- `assets/data.js` — catalogue produits + projets + événements (source : site original)
- `?qa=1` sur n'importe quelle page — mode capture : désactive loader/animations

## Notes

- Panier = demande de commande (le site original n'affiche aucun prix) ;
  l'envoi ouvre un email pré-rempli vers contact@agathefortin.com.
- Polices Google Fonts (Cormorant Garamond, Montserrat, Lato) : nécessite internet.
