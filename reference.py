"""Socle de référence : des règles positives, sans négation par absence."""
import json
from pathlib import Path
import exercices

OBSERVATIONS = {
    "aime_recits": "Le visiteur souhaite découvrir des récits",
    "aime_musique": "Le visiteur souhaite écouter de la musique",
    "aime_creer": "Le visiteur souhaite participer à une création",
    "temps_court": "Le visiteur dispose de moins de 30 minutes",
    "prefere_audio": "Le visiteur préfère un support audio au texte",
}


def construire_faits(reponses):
    faits = set()
    for nom, valeur in reponses.items():
        if valeur != "inconnu":
            faits.add(f"{nom}={valeur}")
    return faits


def regle_applicable(regle, faits):
    for condition in regle["si"]:
        if condition not in faits:
            return False
    return True


def extraire_conseils(faits):
    conseils = []
    for fait in faits:
        if fait.startswith("conseil_"):
            conseils.append(fait)
    return sorted(conseils)


def fonction_pedagogique(nom, *arguments):
    """Seul un exercice explicitement non réalisé utilise le socle fourni."""
    try:
        return getattr(exercices, nom)(*arguments), "personnel"
    except NotImplementedError:
        return globals()[nom](*arguments), "reference"


def charger_regles():
    chemin = Path(__file__).parent / "knowledge" / "regles.json"
    return json.loads(chemin.read_text(encoding="utf-8"))


def raisonner(reponses):
    if set(reponses) != set(OBSERVATIONS):
        raise ValueError("Les cinq observations doivent être renseignées.")
    if any(valeur not in {"oui", "non", "inconnu"} for valeur in reponses.values()):
        raise ValueError("Valeurs autorisées : oui, non, inconnu.")
    faits, mode_faits = fonction_pedagogique("construire_faits", reponses)
    faits = set(faits)
    initiaux = sorted(faits)
    trace = []
    modes = {"construire_faits": mode_faits}
    regles = charger_regles()
    # Au plus une conclusion nouvelle par règle : le nombre de faits est fini.
    while True:
        changement = False
        for regle in regles:
            applicable, mode = fonction_pedagogique("regle_applicable", regle, faits)
            modes["regle_applicable"] = mode
            if applicable and regle["alors"] not in faits:
                faits.add(regle["alors"])
                trace.append({**regle, "etape": len(trace) + 1})
                changement = True
        if not changement:
            break
    conseils, mode = fonction_pedagogique("extraire_conseils", faits)
    modes["extraire_conseils"] = mode
    return {"initiaux": initiaux, "faits": sorted(faits), "trace": trace,
            "conseils": conseils, "inconnus": [OBSERVATIONS[n] for n, v in reponses.items() if v == "inconnu"],
            "modes": modes}

