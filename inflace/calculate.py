import typing
import pandas as pd


def calculate_inflation_pct(data: pd.DataFrame, start: str, end: str) -> float:
    start_cpi = _get_value(data, "Úhrn", start)
    end_cpi = _get_value(data, "Úhrn", end)
    assert isinstance(start_cpi, float) and isinstance(end_cpi, float)
    return end_cpi - start_cpi


def _get_value(data: pd.DataFrame, col_name: str, at: str) -> typing.Any:
    selection = data[data["Oddíl ECOICOP"] == at]
    assert len(selection) == 1
    return selection[col_name].iloc[0]


def get_available_months(data: pd.DataFrame) -> list[str]:
    return data["Oddíl ECOICOP"].tolist()
