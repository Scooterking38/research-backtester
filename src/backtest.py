import pandas as pd


def run_long_only_backtest(
    prices: pd.Series, signal: pd.Series, initial_capital: float = 1.0
) -> pd.DataFrame:
    """
    Vectorized long-only backtest.

    Note: The signal is shifted by one day so today's return uses yesterday's signal. This avoids look-ahead bias.
    """
    if not prices.index.equals(signal.index):
        raise ValueError("prices and signal must have the same index")

    returns = prices.pct_change().fillna(0.0)

    """
    Without .shift(1), we would be trading using information from the same close that generated the signal. 
    That is look-ahead bias.
    """
    position = signal.shift(1).fillna(0.0)

    strategy_returns = position * returns

    result = pd.DataFrame(index=prices.index)
    result["price"] = prices
    result["asset_return"] = returns
    result["signal"] = signal
    result["position"] = position
    result["strategy_return"] = strategy_returns
    result["equity"] = initial_capital * (1.0 + strategy_returns).cumprod()
    result["buy_hold_equity"] = initial_capital * (1.0 + returns).cumprod()

    return result
