import subprocess
import pandas as pd
from io import BytesIO


def bucket_exists(bucket_name: str) -> bool:
    """
    Vérifie si un bucket existe dans MinIO via la commande `mc ls`.
    """
    try:
        result = subprocess.run(
            ["mc", "ls", f"minio/{bucket_name}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception:
        return False


def list_files(bucket_name: str):
    """
    Liste les fichiers d'un bucket MinIO via `mc ls`.
    Retourne une liste de noms de fichiers.
    """
    try:
        result = subprocess.run(
            ["mc", "ls", f"minio/{bucket_name}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            return []

        files = []
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 4:
                filename = parts[-1]
                files.append(filename)

        return files

    except Exception:
        return []


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

