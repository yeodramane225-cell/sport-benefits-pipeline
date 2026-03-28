import pandas as pd
import boto3
from src.config.settings import *
from src.processing.rules import *

def run_transform():
    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY
    )

    # Lecture des fichiers dans le bucket "raw"
    hr = pd.read_csv(s3.get_object(Bucket=S3_BUCKET, Key="hr_generated.csv")["Body"])
    sport = pd.read_csv(s3.get_object(Bucket=S3_BUCKET, Key="sport_generated.csv")["Body"])

    # Jointure sur employee_id
    df = sport.merge(hr, on="employee_id")

    # Correction des colonnes mal nommées
    df = df.rename(columns={
        "date": "activite_label",
        "type_activite": "activite_detail"
    })

    # Application des règles métier
    df["prime"] = df.apply(
        lambda row: calcul_prime(row["anciennete"], row["activite_sportive"]),
        axis=1
    )
    df["jours_bien_etre"] = df["activite_sportive"].apply(jours_bien_etre)

    # Réordonner les colonnes pour éviter les corruptions CSV
    ordered_cols = [
        "employee_id",
        "activite_label",
        "activite_sportive",
        "activite_detail",
        "duree_totale_min",
        "nom",
        "prenom",
        "date_embauche",
        "anciennete",
        "departement",
        "distance_km",
        "prime",
        "jours_bien_etre"
    ]

    df = df[ordered_cols]

    # Export propre
    df.to_csv("/tmp/processed.csv", index=False)
    df.to_csv("/tmp/sport_benefits_curated.csv", index=False)

if __name__ == "__main__":
    run_transform()

