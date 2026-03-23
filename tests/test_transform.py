import pandas as pd
from io import BytesIO
import subprocess
from src.processing.transform import transform_data


def load_from_minio(path: str):
    """
    Charge un fichier CSV depuis MinIO via la commande `mc cat`.
    Retourne un DataFrame pandas.
    """
    try:
        result = subprocess.run(
            ["mc", "cat", f"minio/{path}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            raise FileNotFoundError(f"Impossible de lire {path} dans MinIO")

        data = result.stdout
        return pd.read_csv(BytesIO(data.encode("utf-8")))

    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement depuis MinIO : {e}")


def test_transform_data_output():
    """
    Test principal de l'étape 5 : Transformation.
    Vérifie que transform_data() produit un DataFrame propre et complet.
    """
    df = transform_data()

    # Vérifier que le DataFrame n'est pas vide
    assert not df.empty

    # Vérifier que les colonnes attendues existent
    expected_columns = [
        "employee_id",
        "anciennete",
        "activite_sportive",
        "distance_km",
        "prime",
        "jours_bien_etre",
        "coherence_domicile_travail"
    ]

    for col in expected_columns:
        assert col in df.columns

    # Vérifier les types
    assert df["anciennete"].dtype == "int64"
    assert df["activite_sportive"].dtype == "int64"
    assert df["distance_km"].dtype in ["float64", "float32"]

    # Vérifier qu'il n'y a pas de valeurs manquantes dans les colonnes critiques
    assert df["employee_id"].isna().sum() == 0
    assert df["prime"].isna().sum() == 0

