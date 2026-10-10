"""Serveur local fourni : Python relie le formulaire HTML au moteur de règles."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from html import escape
from pathlib import Path
from string import Template
import json
from reference import OBSERVATIONS, charger_regles, raisonner

WEB = Path(__file__).parent / "web"


def graphe(trace):
    """Dessine la trace en SVG. Les numéros indiquent l'ordre des déductions."""
    if not trace:
        return '<p>Aucune déduction : les faits connus ne déclenchent pas de règle.</p>'
    lignes = []
    for i, regle in enumerate(trace):
        y = i * 110 + 45
        conditions = escape(" ET ".join(regle["si"]))
        conclusion = escape(regle["alors"])
        lignes.append(f'<circle cx="35" cy="{y}" r="19" class="noeud"/><text x="35" y="{y+5}" text-anchor="middle" fill="white">{regle["etape"]}</text><line x1="65" y1="{y}" x2="395" y2="{y}" class="liaison"/><text x="85" y="{y-12}" font-size="13">{conditions}</text><text x="270" y="{y+23}">{escape(regle["id"])} →</text><rect x="410" y="{y-24}" width="365" height="48" rx="12" class="conclusion"/><text x="424" y="{y+5}" font-size="13">{conclusion}</text>')
    return f'<div class="graph"><svg role="img" aria-label="Étapes du raisonnement" viewBox="0 0 800 {len(trace)*110}">{"".join(lignes)}</svg></div>'


def page(reponses=None, resultat=None, erreur=""):
    reponses = reponses or {nom: "inconnu" for nom in OBSERVATIONS}
    champs = []
    for nom, titre in OBSERVATIONS.items():
        options = ''.join(f'<option value="{val}" {"selected" if reponses.get(nom) == val else ""}>{label}</option>' for val, label in [("inconnu", "Non renseigné"), ("oui", "Oui"), ("non", "Non")])
        champs.append(f'<label>{escape(titre)}<select name="{nom}">{options}</select></label>')
    rendu = '<h2>Vos prochaines découvertes</h2><p>Renseignez les préférences du visiteur puis lancez les règles.</p>'
    if resultat is not None:
        explications = {r['alors']: r['explication'] for r in charger_regles()}
        conseils = ''.join(f'<li>{escape(explications.get(c, c))}</li>' for c in resultat['conseils'])
        rendu = ('<h2>Suggestions culturelles</h2><ul>' + conseils + '</ul>') if conseils else '<h2>Aucune suggestion établie</h2><p>Les faits connus ne suffisent pas à proposer une activité. Cela ne signifie pas que le visiteur n’a aucun intérêt.</p>'
        if resultat['inconnus']:
            rendu += '<h3>Préférences à préciser</h3><ul>' + ''.join(f'<li>{escape(t)}</li>' for t in resultat['inconnus']) + '</ul>'
        rendu += '<h3>Chemin de raisonnement</h3>' + graphe(resultat['trace'])
        rendu += '<h3>Pourquoi ces suggestions ?</h3><ol>' + ''.join(f'<li><strong>{escape(r["id"])}</strong> : {escape(r["explication"])}</li>' for r in resultat['trace']) + '</ol>'
        rendu += '<details><summary>Faits initiaux et déduits</summary><pre>' + escape(json.dumps({"initiaux": resultat['initiaux'], "tous": resultat['faits']}, ensure_ascii=False, indent=2)) + '</pre></details>'
        rendu += '<p class="mode">Fonctions : ' + escape(', '.join(f'{n} = {m}' for n, m in resultat['modes'].items())) + '</p>'
    regles = ''.join(f'<li><strong>{escape(r["id"])}</strong> : {escape(" ET ".join(r["si"]))} → {escape(r["alors"])}</li>' for r in charger_regles())
    return Template((WEB / 'index.html').read_text(encoding='utf-8')).substitute(
        champs=''.join(champs), resultat=rendu, erreur=escape(erreur), regles=regles)


class Interface(BaseHTTPRequestHandler):
    def envoyer(self, contenu, statut=200, type_contenu='text/html; charset=utf-8'):
        donnees = contenu.encode('utf-8')
        self.send_response(statut)
        self.send_header('Content-Type', type_contenu)
        self.send_header('Content-Length', str(len(donnees)))
        self.end_headers()
        self.wfile.write(donnees)

    def do_GET(self):
        if self.path == '/':
            self.envoyer(page())
        elif self.path == '/style.css':
            self.envoyer((WEB / 'style.css').read_text(encoding='utf-8'), type_contenu='text/css; charset=utf-8')
        else:
            self.envoyer('Page introuvable', 404)

    def do_POST(self):
        if self.path != '/':
            self.envoyer('Page introuvable', 404)
            return
        try:
            taille = int(self.headers.get('Content-Length', '0'))
            if taille < 0 or taille > 10000:
                raise ValueError('Formulaire trop volumineux.')
            valeurs = parse_qs(self.rfile.read(taille).decode('utf-8'))
            reponses = {nom: valeurs.get(nom, ['inconnu'])[0] for nom in OBSERVATIONS}
            self.envoyer(page(reponses, raisonner(reponses)))
        except (ValueError, UnicodeError) as erreur:
            self.envoyer(page(erreur=str(erreur)), 400)
        except Exception:
            self.envoyer(page(erreur='Une fonction personnelle ou le modèle HTML a échoué. Vérifiez les exercices et les emplacements du modèle.'), 500)
            raise


if __name__ == '__main__':
    print('NIB 1.0 : ouvrir http://127.0.0.1:8765 — Ctrl+C pour arrêter')
    try:
        HTTPServer(('127.0.0.1', 8765), Interface).serve_forever()
    except KeyboardInterrupt:
        print('\nNIB arrêté.')

