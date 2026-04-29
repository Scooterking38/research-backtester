from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_equity_curve(result: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(result.index, result["equity"], label="MA crossover")
    plt.plot(result.index, result["buy_hold_equity"], label="Buy and hold")
    plt.title("SPY Moving-Average Crossover Backtest")
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
