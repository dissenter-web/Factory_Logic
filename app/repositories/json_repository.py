import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FAULTS_PATH = BASE_DIR / "data" / "faults.json"

def load_faults():
    with open(FAULTS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)