import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_ROOT = BASE_DIR / "data"

VFD_DATA_DIR = DATA_ROOT / "vfd"

SPARE_PARTS_DIR = DATA_ROOT / "spare_parts"

def load_vfd_data(manufacturer, model, data_type):
    data_dir = VFD_DATA_DIR / manufacturer / model
    with open(data_dir / f"{data_type}.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def load_spare_parts_data(data_type):
    with open(SPARE_PARTS_DIR / f"spare_parts_{data_type}.json", "r", encoding="utf-8") as file:
        return json.load(file)