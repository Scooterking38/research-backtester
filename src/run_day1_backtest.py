from src.backtest import run_long_only_backtest
from src.config import RAW_DATA_DIR, REPORTS_DIR
from src.data import download_price_data, load_price_data
from src.metrics import summarize_backtest
from src.plotting import plot_equity_curve
from src.signals import moving_average_crossover_signal


def main() -> None:
    ticker = "SPY"
    start = "2015-01-01"
    end = "2025-01-01"

    data_path = RAW_DATA_DIR / f"{ticker}_{start}_{end}.csv"
    if data_path.exists():
        data = load_price_data(data_path)
    else:
        data = download_price_data(
            ticker=ticker, start=start, end=end, output_path=data_path
        )

    signals = moving_average_crossover_signal(
        prices=data["close"], short_window=50, long_window=200
    )

    result = run_long_only_backtest(prices=signals["price"], signal=signals["signal"])

    metrics = summarize_backtest(result)

    print("\nSPY Moving-Average Crossover: 2015-2024")
    print("----------------------------------------")
    for key, value in metrics.items():
        print(f"{key:25s}: {value: .4f}")

    output_path = REPORTS_DIR / "day1_spy_ma_crossover_equity.png"
    plot_equity_curve(result, output_path)

    print(f"\nSaved equity curve to: {output_path}")

if __name__ == "__main__":
    main()
