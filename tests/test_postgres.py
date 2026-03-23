import pandas as pd
from sqlalchemy import create_engine
from src.io.postgres_utils import load_to_postgres

def test_load_to_postgres():
    # DataFrame de test
    df = pd.DataFrame({
        "employee_id": [1, 2],
        "anciennete": [5, 3],
        "activite_sportive": [4, 2],
        "distance_km": [10.5, 7.2],
        "prime": [250, 150],
        "jours_bien_etre": [2, 1],
        "coherence_domicile_travail": [True, True]
    })

    # Chargement dans Postgres
    load_to_postgres(df, "test_table")

    # Vérification
    engine = create_engine("postgresql://kestra:kestra@localhost:5432/sportdb")
    result = pd.read_sql("SELECT * FROM test_table", engine)

    assert len(result) == 2
    assert list(result.columns) == list(df.columns)

