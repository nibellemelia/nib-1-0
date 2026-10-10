"""Trois petits exercices. Remplacer uniquement les lignes NotImplementedError.

Utiliser reference.py pour comparer après avoir essayé.
"""


def construire_faits(reponses):
    """Jour 1 : renvoyer un set de 'nom=valeur', sauf les valeurs 'inconnu'.

    Exemple : {'aime_recits': 'oui'} -> {'aime_recits=oui'}.
    Une boucle for parcourt reponses.items(), qui fournit nom et valeur.
    """
    raise NotImplementedError("Jour 1 : construire les faits")


def regle_applicable(regle, faits):
    """Jour 2 : True si CHAQUE condition de regle['si'] est dans faits.

    Parcourir les conditions ; retourner False dès qu'une condition manque.
    Retourner True après la boucle si toutes sont présentes.
    """
    raise NotImplementedError("Jour 2 : vérifier les conditions")


def extraire_conseils(faits):
    """Jour 2 : liste triée des faits commençant par 'conseil_'.

    Indices : une liste, append(), startswith(), puis sorted().
    """
    raise NotImplementedError("Jour 2 : extraire les conseils")
