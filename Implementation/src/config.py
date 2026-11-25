
from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CONFIG_PATH = PROJECT_ROOT / "configs" / "data.yaml"


def load_config(path=CONFIG_PATH):

    with open(path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if not isinstance(config, dict):
        raise ValueError("Invalid configuration file")

    return config


def get_tickers(config):

    market = config["data"]["market"]

    if market not in config["markets"]:
        raise ValueError(f"Unknown market: {market}")

    market_data = config["markets"][market]

    selection = config["selection"]

    mode = selection["mode"]

    tickers = []

    if mode == "all":

        for sector_tickers in market_data.values():
            tickers.extend(sector_tickers)

    elif mode == "sectors":

        for sector in selection["sectors"]:

            if sector not in market_data:
                raise ValueError(f"Unknown sector: {sector}")

            tickers.extend(market_data[sector])

    elif mode == "tickers":

        tickers = selection["tickers"]

        available = {
            ticker
            for group in market_data.values()
            for ticker in group
        }

        unknown = set(tickers) - available

        if unknown:
            raise ValueError(f"Unknown tickers: {unknown}")

    else:

        raise ValueError(f"Invalid selection mode: {mode}")

    # Remove duplicate tickers
    tickers = list(dict.fromkeys(tickers))

    if not tickers:
        raise ValueError("No tickers selected")

    return tickers


def get_project_path(relative_path):

    return PROJECT_ROOT / relative_path


if __name__ == "__main__":

    config = load_config()

    tickers = get_tickers(config)

    print("Market:", config["data"]["market"])
    print("Total tickers:", len(tickers))
    print("Tickers:", tickers)
