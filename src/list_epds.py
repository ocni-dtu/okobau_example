import requests

OKOBAU_URL = "https://oekobaudat.de/OEKOBAU.DAT/resource/datastocks/cd2bda71-760b-4fcc-8a0b-3877c10000a8"


def parse_epd_list(data: dict):
    """Prints out the name and UUID of each EPD"""

    for epd in data.get("data"):
        print(f"Name: {epd.get('name')}\tUUID: {epd.get('uuid')}")


def list_epds():
    """Lists EPDs in the Ökobau database"""

    response = requests.get(f"{OKOBAU_URL}/processes?format=json")
    response.raise_for_status()
    data = response.json()

    print(f"Retrieved {data.get('pageSize')} EPDs out of {data.get('totalCount')} from Ökobau")
    parse_epd_list(data)


if __name__ == "__main__":
    list_epds()
