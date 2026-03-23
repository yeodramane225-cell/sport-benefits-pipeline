import pandas as pd
from src.io.s3_utils import load_from_minio
from src.processing.rules import (
    calcul_prime,
    jours_bien_etre,
    coherence_domicile_travail
)


def transform_data():
    """
    Charge les données RH et Sport depuis MinIO,
    fusionne, nettoie, enrichit avec les règles métier
    et retourne un DataFrame final prêt pour Postgres.
    """

    # 1. Chargement des données depuis MinIO
    # Correction : on lit les fichiers réellement présents dans MinIO
    df_rh = load_from_minio("raw/hr_generated.csv")
    df_sport = load_from_minio("raw/sport_generated.csv")

    # 2. Fusion des deux DataFrames
    df = pd.merge(df_rh, df_sport, on="employee_id", how="left")

    # 3. Nettoyage des colonnes
    df["anciennete"] = df["anciennete"].fillna(0).astype(int)
    df["activite_sportive"] = df["activite_sportive"].fillna(0).astype(int)
    df["distance_km"] = df["distance_km"].fillna(0).astype(float)

    # 4. Application des règles métier
    df["prime"] = df.apply(
        lambda row: calcul_prime(row["anciennete"], row["activite_sportive"]),
        axis=1
    )

    df["jours_bien_etre"] = df["activite_sportive"].apply(jours_bien_etre)

    df["coherence_domicile_travail"] = df["distance_km"].apply(
        coherence_domicile_travail
    )

    # 5. Dataset final
    return df

