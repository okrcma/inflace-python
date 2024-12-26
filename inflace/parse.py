import pandas as pd
import bs4


_EXPECTED_HEAD = [
    "Oddíl ECOICOP",
    "Úhrn",
    "Potraviny a nealkoholické nápoje",
    "Alkoholické nápoje,tabák",
    "Odívání a obuv",
    "Bydlení, voda, energie,paliva",
    "Bytové vybavení,zařízení domácnosti;opravy",
    "Zdraví",
    "Doprava",
    "Pošty a telekomunikace",
    "Rekreace a kultura",
    "Vzdělávání",
    "Stravování a ubytování",
    "Ostatní zboží a služby",
]


def parse_table(html: str) -> pd.DataFrame:
    soup = bs4.BeautifulSoup(html, "html.parser")
    head = _parse_head(soup)
    assert head == _EXPECTED_HEAD
    body = _parse_body(soup)
    df = pd.DataFrame(body, columns=head)
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x.str.replace(",", ".")).apply(pd.to_numeric, errors="raise")
    return df


def _parse_head(html: bs4.BeautifulSoup) -> list[str]:
    row = html.select_one("#tabData>thead>tr")
    assert row is not None
    cols = row.select("th>span")
    head = [col.text for col in cols]
    return head


def _parse_body(html: bs4.BeautifulSoup) -> list[list[str]]:
    rows = html.select("#tabData>tbody>tr")
    return [_parse_body_row(row) for row in rows]


def _parse_body_row(row: bs4.Tag) -> list[str]:
    cols = row.select("td>span")
    return [col.text for col in cols]
