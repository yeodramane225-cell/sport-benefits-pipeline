from src.processing.rules import calcul_prime, jours_bien_etre, coherence_domicile_travail

def test_prime():
    assert calcul_prime(6, 5) == 250
    assert calcul_prime(1, 0) == 0

def test_jours_bien_etre():
    assert jours_bien_etre(6) == 2
    assert jours_bien_etre(4) == 1
    assert jours_bien_etre(1) == 0

def test_coherence():
    assert coherence_domicile_travail(10) is True
    assert coherence_domicile_travail(300) is False

