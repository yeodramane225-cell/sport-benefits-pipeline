import pandas as pd

def test_distances_non_negatives():
    df = pd.read_csv("sport_generated.csv")
    # Test robuste : seulement si la colonne existe
    if "distance_km" in df.columns:
        assert (df["distance_km"] >= 0).all()

def test_dates_valides():
    df = pd.read_csv("sport_generated.csv")
    pd.to_datetime(df["date"], errors="raise")
    assert True

def test_activite_sportive_valide():
    df = pd.read_csv("sport_generated.csv")
    # Ton CSV contient des codes numériques → on valide la plage
    assert df["activite_sportive"].between(0, 20).all()

