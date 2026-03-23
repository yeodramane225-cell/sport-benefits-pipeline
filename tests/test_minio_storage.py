import subprocess
from src.io.s3_utils import list_files, bucket_exists

def test_buckets_exist():
    assert bucket_exists("raw")
    assert bucket_exists("processed")
    assert bucket_exists("curated")

def test_raw_files_present():
    files = list_files("raw")
    assert "Donneees_RH.xlsx" in files
    assert "Donnees_Sportive.xlsx" in files

def test_raw_files_not_empty():
    files = list_files("raw")
    for f in files:
        result = subprocess.run(
            ["mc", "stat", f"minio/raw/{f}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        assert result.returncode == 0

        size_line = [line for line in result.stdout.splitlines() if "Size" in line][0]
        size_value = float(size_line.split(":")[1].strip().split()[0])
        assert size_value > 0


# --- Tests des fichiers Faker dans MinIO (raw) ---
def test_faker_files_present_in_raw():
    files = list_files("raw")
    assert "hr_generated.csv" in files
    assert "sport_generated.csv" in files

def test_faker_files_not_empty_in_raw():
    for f in ["hr_generated.csv", "sport_generated.csv"]:
        result = subprocess.run(
            ["mc", "stat", f"minio/raw/{f}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        assert result.returncode == 0

        size_line = [line for line in result.stdout.splitlines() if "Size" in line][0]
        size_value = float(size_line.split(":")[1].strip().split()[0])
        assert size_value > 0

