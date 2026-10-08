"""SAE 1.01 - Réseaux sociaux et addiction

Un profil est un tuple de 7 composantes :
    0. identifiant (int)        : le numéro d'anonymat de l'étudiant
    1. pays (str)               : le pays de l'étudiant
    2. plateforme (str)         : le réseau social le plus utilisé
    3. heures_ecran (float)     : le temps d'écran moyen par jour, en heures
    4. heures_sommeil (float)   : le temps de sommeil moyen par nuit, en heures
    5. sante_mentale (int)      : le score de santé mentale, de 1 (mauvais) à 10 (excellent)
    6. score_addiction (int)    : le score d'addiction, de 1 (faible) à 10 (fort)

Les listes de profils sont sans doublons et triées par ordre alphabétique de pays,
puis par ordre croissant d'identifiant.
"""

def est_dependant(profil):
    """indique si l'étudiant est considéré comme dépendant aux réseaux sociaux,
    c'est-à-dire si son score d'addiction atteint le seuil SEUIL_ADDICTION

    Args:
        profil (tuple): le profil d'un étudiant

    Returns:
        bool: True si l'étudiant est dépendant, False sinon
    """
    pass


def est_avant(profil1, profil2):
    """indique si profil1 se place avant profil2 dans l'ordre de tri des listes de profils,
    c'est-à-dire dans l'ordre alphabétique des pays puis dans l'ordre croissant des identifiants.
    ATTENTION : cet ordre n'est pas celui des composantes du tuple, le pays étant en deuxième
    position et l'identifiant en première

    Args:
        profil1 (tuple): le profil d'un étudiant
        profil2 (tuple): le profil d'un autre étudiant

    Returns:
        bool: True si profil1 se place avant profil2, False sinon
    """
    pass


def moyenne_heures_ecran(liste_profils):
    """calcule le temps d'écran quotidien moyen des étudiants de la liste

    Args:
        liste_profils (list): une liste de profils

    Returns:
        float: le temps d'écran quotidien moyen en heures, ou None si la liste est vide
    """
    pass


def taux_dependance(liste_profils):
    """calcule le pourcentage d'étudiants dépendants aux réseaux sociaux dans la liste

    Args:
        liste_profils (list): une liste de profils

    Returns:
        float: le pourcentage d'étudiants dépendants, ou None si la liste est vide
    """
    pass


def profil_plus_dependant(liste_profils):
    """recherche le profil ayant le plus fort score d'addiction
    (le premier rencontré en cas d'égalité)

    Args:
        liste_profils (list): une liste de profils

    Returns:
        tuple: le profil ayant le plus fort score d'addiction, ou None si la liste est vide
    """
    pass


def filtre_plateforme(liste_profils, plateforme):
    """génère la sous-liste des profils dont le réseau social le plus utilisé
    est celui passé en paramètre

    Args:
        liste_profils (list): une liste de profils
        plateforme (str): le nom d'un réseau social

    Returns:
        list: la sous-liste des profils utilisant principalement ce réseau social
    """
    pass


def filtre_heures_ecran(liste_profils, heures_min, heures_max):
    """génère la sous-liste des profils dont le temps d'écran quotidien est compris
    entre heures_min et heures_max (bornes incluses)

    Args:
        liste_profils (list): une liste de profils
        heures_min (float): le temps d'écran quotidien minimum, en heures
        heures_max (float): le temps d'écran quotidien maximum, en heures

    Returns:
        list: la sous-liste des profils dont le temps d'écran est dans l'intervalle
    """
    pass


def inserer_plateforme(liste_noms, plateforme):
    """insère le nom d'un réseau social à sa place dans une liste de noms triée par ordre
    alphabétique, sans jamais créer de doublon : si le nom est déjà présent, la liste est
    inchangée

    Args:
        liste_noms (list): une liste de noms de réseaux sociaux (str), triée et sans doublon
        plateforme (str): le nom du réseau social à insérer

    Returns:
        list: la liste triée et sans doublon contenant les noms de liste_noms et plateforme
    """
    pass


def liste_plateformes(liste_profils):
    """retourne la liste des réseaux sociaux apparaissant dans la liste de profils.
    ATTENTION : la liste renvoyée doit être sans doublons et triée par ordre alphabétique

    Args:
        liste_profils (list): une liste de profils

    Returns:
        list: la liste triée et sans doublons des noms de réseaux sociaux (str)
    """
    pass


def premier_profil_dependant(liste_profils):
    """recherche le premier profil dépendant de la liste.
    Le parcours de la liste s'arrête dès qu'un tel profil est trouvé.

    Args:
        liste_profils (list): une liste de profils

    Returns:
        tuple: le premier profil dépendant de la liste, ou None s'il n'y en a aucun
    """
    pass


def est_bien_triee(liste_profils):
    """vérifie qu'une liste de profils est bien triée par ordre alphabétique de pays,
    puis par ordre croissant d'identifiant, et qu'elle ne comporte pas de doublon.
    Le parcours de la liste s'arrête dès qu'un défaut est détecté.

    Args:
        liste_profils (list): une liste de profils

    Returns:
        bool: True si la liste est bien triée et sans doublon, False sinon
    """
    pass


def recherche_dichotomique(liste_profils, pays, identifiant):
    """recherche, par dichotomie, le profil d'un étudiant à partir de son pays et de son
    identifiant dans une liste de profils triée

    Args:
        liste_profils (list): une liste de profils triée
        pays (str): le pays de l'étudiant recherché
        identifiant (int): l'identifiant de l'étudiant recherché

    Returns:
        tuple: le profil recherché, ou None s'il n'est pas dans la liste
    """
    pass


def fusionner_profils(liste_profils1, liste_profils2):
    """fusionne deux listes de profils triées et sans doublons en une seule liste triée et
    sans doublon, sachant qu'un même profil peut être présent dans les deux listes

    Args:
        liste_profils1 (list): la première liste de profils
        liste_profils2 (list): la seconde liste de profils

    Returns:
        list: la liste triée et sans doublon de tous les profils des deux listes
    """
    pass


def distance(profil1, profil2):
    """calcule la distance entre deux profils, c'est-à-dire la racine carrée de la somme des
    carrés des écarts entre leurs temps d'écran, leurs temps de sommeil et leurs scores de
    santé mentale

    Args:
        profil1 (tuple): le profil d'un étudiant
        profil2 (tuple): le profil d'un autre étudiant

    Returns:
        float: la distance entre les deux profils
    """
    pass


def inserer_voisin(liste_voisins, voisin, k):
    """insère un voisin dans une liste de voisins triée par distance croissante, en
    conservant au plus les k voisins les plus proches.
    Un voisin est un couple (distance, profil).

    Args:
        liste_voisins (list): une liste d'au plus k couples (distance, profil), triée par
                              distance croissante
        voisin (tuple): le couple (distance, profil) à insérer
        k (int): le nombre maximum de voisins à conserver

    Returns:
        list: la liste triée des au plus k voisins les plus proches
    """
    pass


def k_plus_proches_voisins(liste_profils, profil, k):
    """recherche les k profils de la liste les plus proches du profil passé en paramètre

    Args:
        liste_profils (list): une liste de profils
        profil (tuple): le profil d'un étudiant
        k (int): le nombre de voisins recherchés

    Returns:
        list: la liste des k profils les plus proches, du plus proche au plus éloigné
    """
    pass


def predire_score_addiction(liste_profils, profil, k):
    """prédit le score d'addiction d'un étudiant en calculant la moyenne des scores
    d'addiction de ses k plus proches voisins dans la liste de profils

    Args:
        liste_profils (list): une liste de profils
        profil (tuple): le profil d'un étudiant
        k (int): le nombre de voisins utilisés pour la prédiction

    Returns:
        float: le score d'addiction prédit, ou None si aucun voisin n'a été trouvé
    """
    pass


def predire_dependance(liste_profils, profil, k):
    """prédit si un étudiant est dépendant aux réseaux sociaux par un vote majoritaire de ses
    k plus proches voisins dans la liste de profils

    Args:
        liste_profils (list): une liste de profils
        profil (tuple): le profil d'un étudiant
        k (int): le nombre de voisins utilisés pour la prédiction

    Returns:
        bool: True si la majorité des voisins sont dépendants, False sinon,
              ou None si aucun voisin n'a été trouvé
    """
    pass


def charger_profils(nom_fichier):
    """charge un fichier de profils au format CSV en une liste de profils

    Args:
        nom_fichier (str): le nom du fichier CSV contenant les profils

    Returns:
        list: la liste des profils contenus dans le fichier
    """
    pass
