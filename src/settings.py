import json
import os
from typing import Dict


def load_config(path: str) -> Dict:
    if not os.path.exists(path):
        raise ValueError("Path does not exists!")
    with open(path, "r") as f:
        data = json.load(f)

    return {
        "history_path": data["history_path"],
        "key": data["key"],
        "theme": data["theme"],
        "font_size": data["font_size"],
        "font": data["font"],
    }
