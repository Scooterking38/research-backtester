import pandas as pd


def moving_average_crossover_signal(
    prices: pd.Series, short_window: int, long_window: int
) -> pd.DataFrame:
    """
    Create moving-average crossover signals.

    Signal convention:
    - 1 means long the asset.
    - 0 means out of the market.

    The raw signal is based on information available at the close.
    The tradeable position is shifted by one day in the backtest
    """

    if short_window <= 0 or long_window <= 0:
        raise ValueError("Window must be positive integers.")

    if short_window >= long_window:
        raise ValueError("short_window must be smaller than long_window.")

    result = pd.DataFrame(index=prices.index)
    result["price"] = prices
    result["short_ma"] = prices.rolling(short_window).mean()
    result["long_ma"] = prices.rolling(long_window).mean()

    result["signal"] = 0
    result.loc[result["short_ma"] > result["long_ma"], "signal"] = 1

    return result
