import sys
import os

# Chemin racine du projet
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chemin vers src/
SRC_PATH = os.path.join(ROOT_DIR, "src")

# Ajout au PYTHONPATH
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)
