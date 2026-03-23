def calcul_prime(anciennete, activite_sportive):
    prime = 0

    # Prime liée à l'ancienneté
    if anciennete > 5:
        prime += 200
    elif anciennete > 2:
        prime += 100

    # Prime liée à l'activité sportive
    if activite_sportive >= 6:
        prime += 100
    elif activite_sportive >= 3:
        prime += 50

    return prime


def jours_bien_etre(activite_sportive):
    if activite_sportive >= 6:
        return 2
    elif activite_sportive >= 3:
        return 1
    return 0


def coherence_domicile_travail(distance_km):
    return 0 < distance_km < 200

