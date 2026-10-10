# NIB 1.0 : comprendre, modifier, tester en trois jours

Objectif : appliquer les bases du chapitre 1 dans un assistant culturel fonctionnel et acquérir de premières notions Python, HTML et CSS. Le serveur est fourni. Les parties à compléter sont petites et repérées. Prévoir 2 à 3 heures par jour ; arrêter quand les livrables du jour sont terminés.

## Avant de commencer : comprendre les fichiers

Une fonction Python reçoit des arguments et renvoie une valeur avec `return`. Un dictionnaire associe un nom à une valeur ; une liste contient plusieurs éléments ; un ensemble `set()` évite les doublons.

HTML décrit les éléments d'une page (`h1`, `p`, `form`, `button`). CSS règle leur apparence. Le navigateur affiche la page ; Python reçoit les préférences, applique les règles et construit la réponse. Le graphe est dessiné en SVG par le code fourni.

Le projet démarre même si les exercices ne sont pas finis, grâce aux fonctions de référence. L'écran indique quelles versions sont utilisées. Lire une correction est possible, mais essayer et expliquer sa propre solution d'abord.

## Jour 1 — Représenter les connaissances et découvrir HTML

### 1. Partir d'un besoin concret (20 min)

Une visiteuse dit « j'aime écouter des histoires ». La médiatrice veut proposer une activité adaptée.

| Niveau | Exemple |
|---|---|
| Donnée | oui |
| Information | La visiteuse a déclaré aimer les récits |
| Connaissance | Si le visiteur aime les récits, établir un intérêt narratif ; s'il a cet intérêt, proposer la séance de récits |

Les préférences du visiteur constituent la **base de faits**. Les règles générales constituent la **base de connaissances**. Les règles culturelles sont fictives : leur validation réelle demanderait un échange avec la médiatrice.

Répondre dans le bilan : quelle question d'entretien permettrait de vérifier que les activités proposées correspondent aux attentes ? Quelle ambiguïté se cache dans « je veux découvrir la culture » ?

### 2. Dessiner les relations dans draw.io (35 min)

Ouvrir https://app.diagrams.net/, choisir l'ouverture depuis l'appareil et charger `models/nib.drawio`.

Le socle contient Visiteur, Preference et Activite. Ajouter CentreCulturel et la relation « propose » vers Activite. Ajouter un exemple fictif VisiteurA et une activité SeanceRecits ; différencier les concepts et instances par la couleur et une légende. Conserver la source `.drawio` et exporter `docs/screenshots/01-modele.png`.

Une flèche doit porter un nom et un sens. Le schéma représente le domaine ; il n'exécute pas automatiquement les règles.

### 3. Compléter construire_faits (35 min)

Étudier ce fragment :

```python
reponses = {"aime_recits": "oui", "aime_musique": "inconnu"}
faits = set()
for nom, valeur in reponses.items():
    print(nom, valeur)
```

`items()` fournit chaque paire nom/valeur. `faits.add(texte)` ajoute un fait. `f"{nom}={valeur}"` construit le texte. Compléter `construire_faits` dans `exercices.py` : ne conserver que les valeurs différentes de `inconnu`, puis retourner l'ensemble.

Attendu : `{"aime_recits=oui"}`. La valeur `non`, si elle est saisie explicitement, reste un fait ; une absence n'en est pas un.

Lancer les tests. Le test de faits doit réussir ; les deux autres exercices peuvent rester ignorés.

### 4. Modifier le titre HTML (20 min)

Ouvrir `web/index.html`. Repérer :

```html
<h1>Une découverte, un conseil, une explication</h1>
```

Remplacer seulement le texte entre les balises, par exemple « Mon guide de découvertes culturelles ». `h1` est le titre principal ; `p` crée un paragraphe. Garder les balises ouvrante et fermante.

Lancer l'application et actualiser la page. Les noms `$champs`, `$resultat`, `$erreur`, `$regles` sont les emplacements que Python remplit : ne pas les renommer. Écrire dans le bilan la différence entre contenu HTML et règle de connaissance.

## Jour 2 — Exécuter les règles et découvrir CSS

### 1. Comprendre la chaîne R1 → R2 (20 min)

Fait initial `aime_recits=oui` → R1 ajoute `interet_narratif` → R2 ajoute `conseil_atelier_recits`.

C'est le **chaînage avant** : partir des faits et déduire. Le moteur parcourt les règles dans l'ordre du fichier, ajoute immédiatement les conclusions nouvelles et s'arrête quand rien ne change. Chaque règle produit au plus une nouvelle conclusion ; cet ensemble fini permet l'arrêt du moteur fourni.

Pour le chaînage arrière manuel, partir du conseil et rechercher ce qui le prouve : R2 nécessite l'intérêt narratif ; R1 nécessite le goût déclaré pour les récits.

### 2. Compléter regle_applicable (25 min)

Dans `exercices.py`, parcourir `regle["si"]`. Si une condition n'appartient pas à `faits`, retourner `False`. Retourner `True` après la boucle si toutes sont connues.

```python
condition = "aime_recits=oui"
presente = condition in faits
```

Même si les six règles initiales sont simples, la fonction doit vérifier **toutes** les conditions : le test emploie une règle à deux conditions. Une boucle Python évite de limiter le moteur à un seul domaine.

### 3. Compléter extraire_conseils (20 min)

Les faits intermédiaires ne sont pas des conseils. Créer une liste vide, parcourir les faits, conserver ceux dont `fait.startswith("conseil_")` est vrai avec `append()`, puis retourner `sorted(liste)`.

Lancer les tests : les trois exercices doivent réussir sans être ignorés. Une solution incorrecte reste visible ; comparer ensuite à `reference.py`.

### 4. Dessiner le raisonnement (25 min)

Dans draw.io, ajouter une page Raisonnement avec trois rectangles et deux flèches R1/R2. Distinguer fait initial, conclusion intermédiaire et conseil. Écrire une justification de deux phrases dans le bilan.

### 5. Personnaliser la couleur CSS (20 min)

Dans `web/style.css`, repérer :

```css
:root { --accent: #8a3d24; --fond: #fbf5ed; --texte: #33251c; }
```

`--accent` est une variable de couleur ; `var(--accent)` la réutilise pour le bouton, les liens et le graphe. Choisir une autre couleur sombre, par exemple `#305b45`, pour que le texte blanc du bouton reste lisible. Le préfixe `#` désigne une couleur hexadécimale.

Enregistrer puis actualiser. Une règle CSS transforme la présentation ; elle ne change pas la recommandation. La media query en bas du fichier empile les colonnes sur un petit écran. Observer la page dans une fenêtre plus étroite.

## Jour 3 — Valider l'application et conclure

### 1. Comprendre le trajet web (15 min)

Le navigateur demande `/` en GET pour afficher le formulaire. Le clic sur le bouton soumet les préférences en POST. Python lit les valeurs, forme les faits, applique les règles et renvoie du HTML. Le navigateur demande aussi `/style.css` pour la présentation. Aucun JavaScript n'est nécessaire ici.

### 2. Exécuter et vérifier (40 min)

Remplir les six cas de `work/validation.md`. Fixer l'attendu du cas personnel avant l'essai. Tester une préférence corrigée : un ancien conseil ne doit pas persister. Chaque requête repart d'une base de faits neuve.

Dans une session figée, les règles positives ajoutent des faits : raisonnement monotone. Recalculer après correction est une politique de révision, pas une implémentation générale de logique non monotone.

### 3. Ajouter un paragraphe HTML (15 min)

Dans `web/index.html`, sous le titre, ajouter :

```html
<p>Les activités sont fictives : leur disponibilité doit être confirmée auprès du centre.</p>
```

Reformuler cette limite avec ses propres mots. Le navigateur affiche le paragraphe après actualisation. Ne pas ajouter de nouveau champ au formulaire dans ce projet : cela demanderait de modifier aussi les observations et les règles.

### 4. Ajouter les preuves (25 min)

Faire les trois captures indiquées dans `docs/screenshots/README.md`. La capture de tests doit montrer le travail personnel réussi. Ajouter les images et légendes dans le README seulement une fois les fichiers créés.

### 5. Écrire la conclusion (25 min)

Compléter `work/bilan.md` : besoin, approche, résultat, contribution personnelle et limites. Préparer une explication orale de trois minutes. Le projet se termine au jour 3 ; le code reste réutilisable sans imposer une suite.

## Lien avec le chapitre 1

| Notion | Application dans NIB |
|---|---|
| Donnée / information / connaissance | Réponse brute, préférence contextualisée, règle |
| Déclaratif / procédural / contrôle | JSON, fonctions Python, ordre d'exécution |
| Acquisition et connaissances tacites | Question à la médiatrice, clarification d'une préférence |
| Représentation et qualité | Conditions précises ; règles lisibles ; six règles maintenables |
| Réseau sémantique et frame | Relations draw.io ; fiche d'un visiteur avec attributs |
| Composants SBC et système expert | Faits, connaissances, moteur, interface et explications |
| Cycle de développement | Besoin, modèle, programme, validation, bilan |
| Déduction | R1 puis R2 |
| Induction | Plusieurs avis de visiteurs pourraient suggérer une nouvelle règle, sans la prouver |
| Abduction | Un visiteur quitte une séance : ennui possible, mais contrainte horaire possible aussi |
| Monotone et révision | Session figée et nouvelle saisie corrigée |
| Monde ouvert / clos | Non renseigné n'est pas non ; comparer avec un catalogue déclaré exhaustif |
| Autres formalismes | Ontologie pour vocabulaire partagé ; Bayes pour incertitude ; Petri pour processus, sans implémentation ici |

Ce projet approfondit les bases et situe les autres formalismes. Il n'implémente pas tout le cours ni un modèle de langage.
