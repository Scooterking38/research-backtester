from pathlib import Path

import pandas as pd
import yfinance as yf


def download_price_data(
    ticker: str, start: str, end: str, output_path: Path | None = None
) -> pd.DataFrame:
    """
    Download daily OHLCV data from Yahoo Finance.

    Parameters
    ------------
    ticker:
        Market ticker, for example "SPY"
    start:
        Start date, inclusive, in YYYY-MM-DD format
    end:
        End date, exclusive, in YYYY-MM-DD format
    output_path:
        Optional CSV path for saving the data.

    Returns
    --------------
    pd.DataFrame
        DataFrame indexed by date
    """

    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No data downloaded for {ticker}.")

    data.index = pd.to_datetime(data.index)
    data.index.name = "date"

    # yfinance can sometimes return multi-level columns.
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.rename(columns=str.lower)

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        data.to_csv(output_path)

    return data


def load_price_data(path: Path) -> pd.DataFrame:
    """
    Load save OHLCV data from CSV
    """
    data = pd.read_csv(path, parse_dates=["date"], index_col="date")
    return data.sort_index()
