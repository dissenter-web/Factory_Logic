import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "vfd"

def load_vfd_data(manufacturer, model, data_type):
    data_dir = DATA_DIR / manufacturer / model
    with open(data_dir / f"{data_type}.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def load_spare_parts_data(data_type):
    with open(BASE_DIR/ "data" / "spare_parts" / f"spare_parts_{data_type}.json", "r", encoding="utf-8") as file:
        return json.load(file)