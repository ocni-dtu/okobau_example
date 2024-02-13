from shared import get_epds


def parse_epd_list(data: dict):
    """Prints out the name and UUID of each EPD"""

    for epd in data.get("data"):
        print(f"Name: {epd.get('name')}\tUUID: {epd.get('uuid')}")


def list_epds():
    """Lists EPDs in the Ökobau database"""

    data = get_epds()
    parse_epd_list(data)


if __name__ == "__main__":
    list_epds()
