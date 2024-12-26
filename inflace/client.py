import requests


ECOICOP_CPI_URL = (
    "https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&z=T&f=TABULKA&ds=ds2329&pvo="
    "CEN083A&skupId=2218&katalog=31779&o=false&evo=v2504_%21_CEN-SPO-BAZIC2015-EM_1&str=v514"
)


def get_ecoicop_html() -> str:
    response = requests.get(ECOICOP_CPI_URL)
    if not response.ok:
        raise Exception(f"Failed to get ECOICOP HTML. Status: {response.status_code}, text: {response.text}")
    return response.text
