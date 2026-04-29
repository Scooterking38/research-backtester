import numpy as np
import pandas as pd

from src.config import TRADING_DAYS_PER_YEAR


def total_return(equity: pd.Series) -> float:
    return equity.iloc[-1] / equity.iloc[0] - 1.0


def annualized_volatility(returns: pd.Series) -> float:
    return returns.std() * np.sqrt(TRADING_DAYS_PER_YEAR)


def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    Annualized Sharpe ratio. For Day 1, we assume a zero risk-free rate.
    """
    excess_returns = returns - risk_free_rate / TRADING_DAYS_PER_YEAR

    if excess_returns.std() == 0:
        return np.nan

    return excess_returns.mean() / (
        excess_returns.std() * np.sqrt(TRADING_DAYS_PER_YEAR)
    )


def max_drawdown(equity: pd.Series) -> float:
    running_max = equity.cummax()
    drawdown = equity / (running_max - 1.0)
    return drawdown.min()


def summarize_backtest(result: pd.DataFrame) -> dict[str, float]:
    return {
        "total_return": total_return(result["equity"]),
        "annualized_volatility": annualized_volatility(result["strategy_return"]),
        "sharpe_ratio": sharpe_ratio(result["strategy_return"]),
        "max_drawdown": max_drawdown(result["equity"]),
        "buy_hold_total_return": total_return(result["buy_hold_equity"]),
    }
