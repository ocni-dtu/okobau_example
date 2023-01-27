import json

import requests

OKOBAU_URL = "https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8"


def fetch_epd_data(uuid: str):
    """Fetches the data of a specific EPD given its UUID"""
    response = requests.get(f"{OKOBAU_URL}/processes/{uuid}?format=json&view=extended")

    response.raise_for_status()
    data = response.json()

    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    epd_id = "8be9edb5-c5b9-4be1-bfb8-b096f24a183b"
    fetch_epd_data(epd_id)
