import pandas as pd
import pytest
from src.signals import moving_average_crossover_signal


def test_moving_average_crossover_signal_has_expected_columns():
    prices = pd.Series(
        [100, 101, 102, 103, 104], index=pd.date_range("2020-01-01", periods=5)
    )

    result = moving_average_crossover_signal(
        prices=prices, short_window=2, long_window=3
    )

    assert list(result.columns) == ["price", "short_ma", "long_ma", "signal"]


def test_short_window_must_be_less_than_long_window():
    prices = pd.Series([100, 101, 102], index=pd.date_range("2020-01-01", periods=3))

    with pytest.raises(ValueError):
        moving_average_crossover_signal(prices=prices, short_window=3, long_window=3)
