# Boutique Instagram — mode d'emploi

Objectif : que chaque photo postée sur Instagram puisse être **taguée avec un produit**
(prix + lien « Voir la boutique »), et que le profil ait un onglet **Boutique**.

## Ce qui est déjà prêt dans ce projet

- ✅ Une **page par produit** avec URL unique (`produit.html?id=p01` … `p36`) — exigence Meta
- ✅ Prix, photo, description et données structurées (JSON-LD) sur chaque fiche
- ✅ Le **flux catalogue** : `python3 export_meta.py https://votre-domaine.com`
  → génère `assets/meta-catalog.csv` (36 produits, format officiel Meta)

## Les 6 étapes (≈ 1 h, dans l'ordre)

1. **Mettre le site en ligne** (Vercel/Netlify ou l'hébergement OVH récupéré).
   Instagram vérifie chaque URL produit : le site doit être accessible publiquement.

2. **Passer le compte Instagram en compte professionnel**
   (Réglages → Type de compte → Professionnel → catégorie « Magasin de meubles/décoration »
   ou « Service d'aménagement paysager »).

3. **Créer le Business Manager** sur business.facebook.com avec le compte
   Facebook de l'entreprise (la page FB « Agathe Fortin Paysages » existe déjà —
   il faut en être admin). Lier la page Facebook + le compte Instagram.

4. **Créer le catalogue** dans Commerce Manager (commerce facebook.com) :
   Catalogue → « E-commerce » → Sources de données → **Flux de données** →
   importer `assets/meta-catalog.csv`. Prévoir un ré-import à chaque changement
   de prix/produit (ou programmer une URL de flux hébergée).

5. **Vérifier le domaine** dans Business Manager (Paramètres → Sécurité de la marque
   → Domaines) : Meta donne une balise `<meta>` à coller dans le `<head>` du site —
   me la transmettre, je l'ajoute dans `build.py` en 1 minute.

6. **Activer Instagram Shopping** : Instagram → Réglages → Entreprise →
   Configurer la boutique → choisir le catalogue. Validation Meta sous quelques jours.
   Ensuite : taguer les produits sur chaque post/story, onglet Boutique actif.

## Règles d'or pour vendre (avec les photos existantes)

- 1 post = 1 pièce taguée, photo du showroom, légende courte : nom, dimensions,
  « retrait showroom / livraison France », prix dans le tag (pas dans la légende).
- Alterner : pièce seule → pièce en situation (jardin/terrasse des photos projets) →
  coulisses showroom → événement.
- Stories permanentes (à la une) : « La boutique », « Le showroom », « Livraison ».
- Toujours répondre en DM avec le lien direct `produit.html?id=…`.

⚠ Les prix actuels du site sont **indicatifs** (générés pour la maquette) :
les faire valider par Agathe avant l'import du catalogue dans Meta.
