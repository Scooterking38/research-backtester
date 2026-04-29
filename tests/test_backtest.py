import pandas as pd

from src.backtest import run_long_only_backtest


def test_backtest_shifts_signal_to_avoid_lookahead():
    dates = pd.date_range("2020-01-01", periods=3)
    prices = pd.Series([100.0, 110.0, 121.0], index=dates)

    # Signal becomes long on day 2
    signal = pd.Series([0, 1, 1], index=dates)

    result = run_long_only_backtest(prices, signal)

    # Day 2 position should still be yesterday's signal: 0.
    assert result.loc[dates[1], "position"] == 0

    # Day 3 position should now be 1.
    assert result.loc[dates[2], "position"] == 1

    # Therefore startegy only earns the return from day 2 to day 3
    assert round(result.loc[dates[2], "equity"], 6) == 1.1
