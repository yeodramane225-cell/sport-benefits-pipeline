import os

# --- Tests des fichiers sources fournis ---
def test_source_files_exist():
    assert os.path.exists("/home/yeo/Donneees_RH.xlsx")
    assert os.path.exists("/home/yeo/Donnees_Sportive.xlsx")

def test_source_files_not_empty():
    assert os.path.getsize("/home/yeo/Donneees_RH.xlsx") > 0
    assert os.path.getsize("/home/yeo/Donnees_Sportive.xlsx") > 0

def test_source_files_format():
    assert "/home/yeo/Donneees_RH.xlsx".endswith(".xlsx")
    assert "/home/yeo/Donnees_Sportive.xlsx".endswith(".xlsx")


# --- Tests des fichiers générés par Faker ---
def test_generated_files_exist():
    assert os.path.exists("hr_generated.csv")
    assert os.path.exists("sport_generated.csv")

def test_generated_files_not_empty():
    assert os.path.getsize("hr_generated.csv") > 0
    assert os.path.getsize("sport_generated.csv") > 0

