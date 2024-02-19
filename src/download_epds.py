import json
from pathlib import Path

from shared import get_epds, get_full_epd, get_folder


def download_epds(data_folder: Path):
    data = get_epds(50)
    for epd in data.get("data"):
        epd_id = epd.get('uuid')
        _epd = get_full_epd(epd_id)
        (data_folder / f"{epd_id}.json").write_text(json.dumps(_epd, indent=2))


if __name__ == "__main__":
    folder = get_folder(__file__, 'data')

    download_epds(folder)
