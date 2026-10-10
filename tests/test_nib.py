import unittest
import exercices
import reference
from app import page


def profil(**modifications):
    reponses = {nom: 'inconnu' for nom in reference.OBSERVATIONS}
    reponses.update(modifications)
    return reponses


class Socle(unittest.TestCase):
    def test_chaine_deux_regles(self):
        resultat = reference.raisonner(profil(aime_recits='oui'))
        self.assertEqual(resultat['conseils'], ['conseil_atelier_recits'])
        self.assertEqual([r['id'] for r in resultat['trace']], ['R1', 'R2'])

    def test_inconnu_ne_signifie_pas_non(self):
        resultat = reference.raisonner(profil())
        self.assertEqual(resultat['trace'], [])
        self.assertEqual(len(resultat['inconnus']), 5)

    def test_refus_ne_recommande_pas(self):
        self.assertEqual(reference.raisonner({n: 'non' for n in reference.OBSERVATIONS})['conseils'], [])

    def test_musique(self):
        self.assertEqual(reference.raisonner(profil(aime_musique='oui'))['conseils'], ['conseil_ecoute_musicale'])

    def test_plusieurs_preferences(self):
        resultat = reference.raisonner(profil(aime_recits='oui', aime_creer='oui', temps_court='oui', prefere_audio='oui'))
        self.assertEqual(set(resultat['conseils']), {'conseil_atelier_recits', 'conseil_atelier_creation', 'conseil_format_court', 'conseil_support_audio'})

    def test_recalcul_sans_ancien_conseil(self):
        reference.raisonner(profil(aime_recits='oui'))
        self.assertNotIn('conseil_atelier_recits', reference.raisonner(profil(aime_recits='non'))['faits'])

    def test_valeur_invalide(self):
        with self.assertRaises(ValueError):
            reference.raisonner(profil(aime_recits='peut-etre'))

    def test_interface_explique_et_echappe(self):
        html = page(profil(), reference.raisonner(profil(aime_recits='oui')), '<script>')
        self.assertIn('R1', html)
        self.assertIn('R2', html)
        self.assertIn('<svg', html)
        self.assertNotIn('<script>', html)
        self.assertNotIn('$resultat', html)
        self.assertIn('/style.css', html)


class ExercicesPersonnels(unittest.TestCase):
    def appeler(self, nom, *args):
        try:
            return getattr(exercices, nom)(*args)
        except NotImplementedError:
            self.skipTest(f'{nom} : exercice à compléter')

    def test_faits(self):
        self.assertEqual(self.appeler('construire_faits', {'a': 'oui', 'b': 'inconnu', 'c': 'non'}), {'a=oui', 'c=non'})

    def test_conditions(self):
        regle = {'si': ['a', 'b']}
        self.assertFalse(self.appeler('regle_applicable', regle, {'a'}))
        self.assertTrue(self.appeler('regle_applicable', regle, {'a', 'b'}))

    def test_conseils(self):
        self.assertEqual(self.appeler('extraire_conseils', {'x', 'conseil_z', 'conseil_a'}), ['conseil_a', 'conseil_z'])

