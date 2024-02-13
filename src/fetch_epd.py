import json

from shared import get_full_epd


def get_epd_by_id(uuid: str):
    """Fetches the data of a specific EPD given its UUID"""
    data = get_full_epd(uuid)

    print(json.dumps(data, indent=4))


if __name__ == '__main__':
    epd_id = "8be9edb5-c5b9-4be1-bfb8-b096f24a183b"
    get_epd_by_id(epd_id)
