import json
from pathlib import Path

import requests

OKOBAU_URL = "https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8"


def get_epds(limit=10) -> dict:
    """Get EPDs from Ökobau"""

    response = requests.get(f"{OKOBAU_URL}/processes?format=json&limit={limit}")
    response.raise_for_status()
    data = response.json()

    print(f"Retrieved {data.get('pageSize')} EPDs out of {data.get('totalCount')} from Ökobau")

    return data


def get_full_epd(uid: str) -> dict:
    """Get the full dataset for a single EPD"""

    base_url = f"{OKOBAU_URL}/processes/{uid}"
    response = requests.get(f"{base_url}?format=json&view=extended")

    response.raise_for_status()
    data = response.json()
    data["source"] = base_url

    return data


def get_full_epd_str(uid: str) -> str:
    """Get the full dataset for a single EPD and return it as a string"""
    return json.dumps(get_full_epd(uid))


def get_folder(source, name: str) -> Path:
    folder = Path(source).parent / name
    if not folder.exists():
        folder.mkdir()

    return folder
