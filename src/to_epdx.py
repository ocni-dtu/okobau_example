import epdx

from shared import get_epds, get_folder, get_full_epd_str


def to_epdx():
    """Get EPDs from Ökobau and turn them into EPDx"""

    data = get_epds()
    folder = get_folder(__file__, "epdx_data")

    for _epd in data.get("data"):
        print(f"\nEPD {_epd.get('uuid')}")

        # Get full EPD from Ökobau
        epd_str = get_full_epd_str(_epd.get("uuid"))

        # Turn EPD into EPDx JSON string that can be saved to disk.
        epdx_str = epdx.convert_ilcd(epd_str, as_type='str')
        (folder / f"{_epd.get('uuid')}.epdx.json").write_text(epdx_str)

        # Turn EPD into EPDx dict
        epdx_dict = epdx.convert_ilcd(epd_str)
        print('EPDx Dict')
        print(epdx_dict)

        # Turn EPD into an EPDx Pydantic Class
        epdx_pydantic = epdx.convert_ilcd(epd_str, as_type='pydantic')
        print('\nEPDx Pydantic')
        print(epdx_pydantic)
        print("---------\n")


if __name__ == "__main__":
    to_epdx()
