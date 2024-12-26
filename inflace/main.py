import argparse

from inflace.parse import parse_table
from inflace.client import get_ecoicop_html
from inflace.calculate import calculate_inflation_pct, get_available_months


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate inflation between two months.")
    parser.add_argument("start", type=str, help="Start month in format MM/YYYY.")
    parser.add_argument("end", type=str, help="End (exclusive) month in format MM/YYYY.")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()

    html = get_ecoicop_html()
    data = parse_table(html)

    available_months = get_available_months(data)
    if args.start not in available_months or args.end not in available_months:
        print(f"'{args.start}' or '{args.end}' is not in available months: {available_months}")
        exit(1)

    result = calculate_inflation_pct(data, args.start, args.end)
    print(f"Inflation between {args.start} and {args.end} was {result:.2f}%.")
