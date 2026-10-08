"""SAE 1.01 - Réseaux sociaux et addiction : tests des fonctions de explore_ssma.py

Chaque fonction ci-dessous ne contient que deux tests : c'est un point de départ, pas un
travail terminé. Vous devez IMPERATIVEMENT compléter chacune d'elles avec des tests plus
complets, et notamment penser aux cas particuliers :
    - la liste passée en paramètre est vide,
    - la valeur cherchée n'existe pas (la fonction doit alors retourner None),
    - un même identifiant est attribué à des étudiants de pays différents,
    - k est plus grand que le nombre de profils disponibles.

Pour lancer les tests, tapez dans le terminal :   pytest -v test_explore_ssma.py
"""

import explore_ssma as ssma

# ---------------------------------------------------------------------------------------------
# Exemples de données pour vous aider à faire vos tests
# ---------------------------------------------------------------------------------------------

# exemples de profils
profil1 = (12, 'France', 'Instagram', 5.2, 6.5, 6, 8)
profil2 = (45, 'France', 'TikTok', 7.0, 5.0, 4, 9)
profil3 = (7, 'Italy', 'WhatsApp', 2.1, 7.5, 8, 3)
profil4 = (3, 'Belgium', 'Facebook', 3.0, 8.0, 7, 4)

# une liste de profils triée et sans doublon
liste1 = [(3, 'Belgium', 'Facebook', 3.0, 8.0, 7, 4),
          (17, 'Belgium', 'Instagram', 6.0, 5.5, 5, 8),
          (12, 'France', 'Instagram', 5.2, 6.5, 6, 8),
          (45, 'France', 'TikTok', 7.0, 5.0, 4, 9),
          (7, 'Italy', 'WhatsApp', 2.1, 7.5, 8, 3),
          (23, 'Spain', 'TikTok', 4.5, 7.0, 6, 5)]

# deux listes triées qui se recouvrent (leur fusion redonne liste1)
liste2 = [(3, 'Belgium', 'Facebook', 3.0, 8.0, 7, 4),
          (12, 'France', 'Instagram', 5.2, 6.5, 6, 8),
          (7, 'Italy', 'WhatsApp', 2.1, 7.5, 8, 3)]

liste3 = [(17, 'Belgium', 'Instagram', 6.0, 5.5, 5, 8),
          (12, 'France', 'Instagram', 5.2, 6.5, 6, 8),
          (45, 'France', 'TikTok', 7.0, 5.0, 4, 9),
          (23, 'Spain', 'TikTok', 4.5, 7.0, 6, 5)]

# une liste mal triée (Belgium 17 est placé avant Belgium 3)
liste4 = [(17, 'Belgium', 'Instagram', 6.0, 5.5, 5, 8),
          (3, 'Belgium', 'Facebook', 3.0, 8.0, 7, 4),
          (12, 'France', 'Instagram', 5.2, 6.5, 6, 8)]

# une liste de profils sans aucun étudiant dépendant
liste5 = [(7, 'Italy', 'WhatsApp', 2.1, 7.5, 8, 3),
          (23, 'Spain', 'TikTok', 4.5, 7.0, 6, 5)]

# une liste où un même identifiant est réutilisé dans plusieurs pays : un étudiant n'est
# identifié que par le COUPLE (pays, identifiant), jamais par son seul identifiant
liste_homonymes = [(12, 'Belgium', 'Facebook', 3.0, 8.0, 7, 4),
                   (45, 'Belgium', 'TikTok', 6.0, 5.5, 5, 8),
                   (12, 'France', 'Instagram', 5.2, 6.5, 6, 8),
                   (12, 'Italy', 'WhatsApp', 2.1, 7.5, 8, 3),
                   (45, 'Spain', 'Snapchat', 4.5, 7.0, 6, 5)]

# une liste utilisée pour les k plus proches voisins :
# les 3 premiers profils sont de petits consommateurs, les 3 derniers de gros consommateurs
liste_voisinage = [(1, 'Canada', 'Instagram', 2.0, 8.0, 8, 3),
                   (2, 'Canada', 'TikTok', 2.5, 7.5, 8, 3),
                   (3, 'Canada', 'Instagram', 3.0, 7.0, 7, 4),
                   (4, 'France', 'TikTok', 6.5, 5.0, 4, 8),
                   (5, 'France', 'Instagram', 7.0, 4.5, 4, 9),
                   (6, 'France', 'TikTok', 7.5, 4.0, 3, 9)]

# deux profils d'étudiants dont on veut prédire le score d'addiction
petit_consommateur = (99, 'Japan', 'Instagram', 2.2, 7.8, 8, 0)
gros_consommateur = (98, 'Japan', 'TikTok', 7.2, 4.2, 3, 0)


# ---------------------------------------------------------------------------------------------
# Exemples de tests à compléter impérativement
# ---------------------------------------------------------------------------------------------

def test_est_dependant():
    assert ssma.est_dependant(profil1) is True
    assert ssma.est_dependant(profil3) is False


def test_est_avant():
    assert ssma.est_avant(profil4, profil1) is True    # Belgium avant France
    assert ssma.est_avant(profil1, profil4) is False


def test_moyenne_heures_ecran():
    assert ssma.moyenne_heures_ecran(liste5) == (2.1 + 4.5) / 2
    assert ssma.moyenne_heures_ecran([profil1]) == 5.2


def test_taux_dependance():
    assert ssma.taux_dependance(liste1) == 50.0
    assert ssma.taux_dependance(liste5) == 0.0


def test_profil_plus_dependant():
    assert ssma.profil_plus_dependant(liste1) == (45, 'France', 'TikTok', 7.0, 5.0, 4, 9)
    assert ssma.profil_plus_dependant([profil3]) == profil3


def test_filtre_plateforme():
    assert ssma.filtre_plateforme(liste1, 'Facebook') == [(3, 'Belgium', 'Facebook', 3.0, 8.0, 7, 4)]
    assert ssma.filtre_plateforme(liste1, 'YouTube') == []


def test_filtre_heures_ecran():
    assert ssma.filtre_heures_ecran(liste1, 6.5, 10.0) == [(45, 'France', 'TikTok', 7.0, 5.0, 4, 9)]
    assert ssma.filtre_heures_ecran(liste1, 10.0, 12.0) == []


def test_inserer_plateforme():
    assert ssma.inserer_plateforme([], 'TikTok') == ['TikTok']
    assert ssma.inserer_plateforme(['Facebook', 'TikTok'], 'Instagram') == ['Facebook', 'Instagram', 'TikTok']


def test_liste_plateformes():
    assert ssma.liste_plateformes(liste5) == ['TikTok', 'WhatsApp']
    assert ssma.liste_plateformes([profil1]) == ['Instagram']


def test_premier_profil_dependant():
    assert ssma.premier_profil_dependant(liste1) == (17, 'Belgium', 'Instagram', 6.0, 5.5, 5, 8)
    assert ssma.premier_profil_dependant(liste5) is None


def test_est_bien_triee():
    assert ssma.est_bien_triee(liste1) is True
    assert ssma.est_bien_triee(liste4) is False


def test_recherche_dichotomique():
    assert ssma.recherche_dichotomique(liste1, 'France', 45) == (45, 'France', 'TikTok', 7.0, 5.0, 4, 9)
    assert ssma.recherche_dichotomique(liste1, 'Germany', 3) is None


def test_fusionner_profils():
    assert ssma.fusionner_profils(liste2, liste3) == liste1
    assert ssma.fusionner_profils(liste1, []) == liste1


def test_distance():
    # écarts de 3 heures d'écran et 4 heures de sommeil : distance = 5
    assert ssma.distance((1, 'X', 'A', 3.0, 4.0, 5, 1), (2, 'Y', 'B', 6.0, 8.0, 5, 1)) == 5.0
    # deux profils identiques sur les trois critères : distance nulle
    assert ssma.distance(profil1, (99, 'Spain', 'TikTok', 5.2, 6.5, 6, 2)) == 0.0


def test_inserer_voisin():
    assert ssma.inserer_voisin([], (1.5, profil1), 3) == [(1.5, profil1)]
    assert ssma.inserer_voisin([(1.0, profil1), (3.0, profil3)], (2.0, profil2), 3) == \
        [(1.0, profil1), (2.0, profil2), (3.0, profil3)]


def test_k_plus_proches_voisins():
    # les trois voisins les plus proches d'un petit consommateur sont les trois Canadiens
    assert ssma.k_plus_proches_voisins(liste_voisinage, petit_consommateur, 3) == \
        [(1, 'Canada', 'Instagram', 2.0, 8.0, 8, 3),
         (2, 'Canada', 'TikTok', 2.5, 7.5, 8, 3),
         (3, 'Canada', 'Instagram', 3.0, 7.0, 7, 4)]
    assert ssma.k_plus_proches_voisins(liste_voisinage, petit_consommateur, 1) == \
        [(1, 'Canada', 'Instagram', 2.0, 8.0, 8, 3)]


def test_predire_score_addiction():
    assert ssma.predire_score_addiction(liste_voisinage, petit_consommateur, 3) == (3 + 3 + 4) / 3
    assert ssma.predire_score_addiction(liste_voisinage, gros_consommateur, 3) == (9 + 9 + 8) / 3


def test_predire_dependance():
    assert ssma.predire_dependance(liste_voisinage, petit_consommateur, 3) is False
    assert ssma.predire_dependance(liste_voisinage, gros_consommateur, 3) is True


def test_charger_profils():
    profils = ssma.charger_profils(chemin('ssma1.csv'))
    assert len(profils) == 705
    assert profils[0] == (105, 'Afghanistan', 'LinkedIn', 2.9, 7.0, 7, 5)
