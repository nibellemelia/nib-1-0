# NIB 1.0 — Assistant de découvertes culturelles

**Recommander une activité et expliquer pourquoi, avec une base de connaissances.**

## Contexte

Dans un centre culturel fictif à Douala, une médiatrice accueille des visiteurs intéressés par les récits, la musique ou les activités créatives. Elle souhaite un petit outil pour recueillir leurs préférences et suggérer des activités avec une explication claire. NIB 1.0 répond à ce besoin par un système de règles.

Les activités et le centre sont fictifs. Les préférences sont déclarées, jamais déduites de l'origine, de l'âge ou de la langue du visiteur. Le projet ne prétend pas représenter toutes les cultures camerounaises et ne contient pas d'œuvres ni de récits traditionnels à redistribuer.

## Démonstration

Un visiteur indique qu'il aime les récits. **R1** établit un intérêt narratif ; **R2** propose une séance de récits. L'interface montre les faits, les conclusions et les étapes du raisonnement. Si une préférence reste inconnue, elle ne devient pas « non ».

Cette approche est de l'**IA symbolique** : la connaissance est explicite, puis un moteur applique les règles. NIB ne comporte pas de modèle entraîné ni de génération libre de textes.

## Trois jours, du démarrage à la conclusion

| Jour | Ce que NIB réalise | Résultat |
|---|---|---|
| 1 | Modèle draw.io ; fonction de construction des faits ; titre HTML | Représentation du domaine et premières modifications personnelles |
| 2 | Deux fonctions de règles/conseils ; schéma de raisonnement ; couleur CSS | Conseils expliqués et interface personnalisée |
| 3 | Six cas de validation ; paragraphe HTML ; captures et conclusion | Petite application locale terminée et documentée |

Prévoir **2 à 3 heures par jour**, installation comprise si elle est simple. Il s'agit d'un projet autonome : aucune étape future n'est nécessaire. [Guide pédagogique des trois jours](docs/3-jours.md).

## Lancer et tester

Python 3.10 ou plus récent, un navigateur. Aucune bibliothèque tierce à installer.

```powershell
python app.py
```

Ouvrir http://127.0.0.1:8765 ; arrêter avec Ctrl+C. Sous Windows, `py app.py` est aussi possible si le lanceur est installé. L'application reste locale.

```powershell
python -m unittest discover -s tests -v
```

L'interface est fournie. Les trois fonctions de `exercices.py` sont à compléter. Tant qu'une fonction lève `NotImplementedError`, sa version de référence est utilisée et signalée dans l'interface. Une mauvaise réponse personnelle n'est pas remplacée silencieusement.

Les tests d'exercices sont ignorés tant que le travail n'est pas réalisé : **ignoré ne signifie pas réussi**. Le socle est testé séparément. NIB devra valider ses propres fonctions.

## Repères dans le code

| Fichier | Rôle | Travail personnel |
|---|---|---|
| `knowledge/regles.json` | Six règles et leurs explications | Comprendre et suivre leur application |
| `exercices.py` | Trois fonctions courtes | Compléter les zones indiquées |
| `reference.py` | Corrections et moteur fourni | Lire la correction après essai |
| `web/index.html` | Structure de la page et formulaire | Modifier le titre, ajouter un paragraphe |
| `web/style.css` | Présentation graphique | Modifier la couleur principale |
| `app.py` | Serveur local, lien Python/HTML et graphe | Comprendre le trajet d'une demande, sans réécrire le serveur |
| `models/nib.drawio` | Schéma initial | Ajouter les relations et une page de raisonnement |
| `work/` | Validation et conclusion | Documenter les essais réels |

Outil de modélisation : [draw.io](https://app.diagrams.net/) uniquement. VS Code sert à éditer les fichiers. HTML structure la page ; CSS la présente ; Python applique les règles et renvoie le résultat. Le projet ne demande pas JavaScript.

## Captures à ajouter

| Emplacement | Preuve |
|---|---|
| `docs/screenshots/01-modele.png` | Schéma personnel draw.io |
| `docs/screenshots/02-interface.png` | Interface personnalisée, suggestion et trace |
| `docs/screenshots/03-tests.png` | Tests après complétion des fonctions |

Les images seront affichées quand elles auront été ajoutées. Les sources, le code et le bilan complètent les preuves visuelles.

## Statut et contribution

**Socle fonctionnel préparé ; travail personnel à réaliser.** La structure, le serveur et l'interface ont été préparés avec une assistance IA. NIB réalise les trois fonctions, les modifications HTML/CSS, les schémas, les essais et la conclusion. Cette contribution doit être décrite clairement en entretien.

Le partage approximatif 70 % fourni / 30 % personnel vise à faciliter l'apprentissage, pas à mesurer les lignes de code. Il ne permet pas de revendiquer une réalisation entièrement personnelle.

## Limites

Six règles pédagogiques, pas d'horaires réels, pas de réservation, pas de génération de contenu culturel. Plusieurs suggestions peuvent être compatibles. Les propositions de format court et de support audio sont des adaptations ; elles ne constituent pas une activité à elles seules. Les disponibilités doivent être confirmées auprès du centre.

Source pédagogique : chapitre 1 d'Ingénierie des connaissances IAR417, Yankam Ngueguim Joël Stéphane. Le chapitre intégral n'est pas redistribué.
