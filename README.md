# research-backtester

A Python-based backtesting framework designed for quantitative finance research. This repository provides a modular architecture to simulate trading strategies, evaluate performance metrics, and visualize results.

## Architecture Overview

The `research-backtester` is structured into several key modules:

- **src/backtest.py**: Contains the main logic for running backtests.
- **src/config.py**: Manages configuration settings such as directory paths and constants.
- **src/data.py**: Handles data retrieval and preprocessing, specifically downloading historical price data from Yahoo Finance.
- **src/metrics.py**: Computes various performance metrics like total return, volatility, Sharpe ratio, and maximum drawdown.
- **src/plotting.py**: Provides functions to visualize backtest results.
- **src/run_day1_backtest.py**: A script to execute a specific backtesting scenario.
- **src/signals.py**: Defines trading signals used in the backtests.

The `tests` directory contains unit tests for the core components, ensuring robustness and reliability of the framework.

## Tech Stack

- **Programming Language**: Python
- **Data Handling**: Pandas, NumPy
- **Financial Data Retrieval**: yfinance
- **Visualization**: Matplotlib
- **Testing**: Pytest
- **Code Formatting & Linting**: Black, Ruff

## Getting Started / Setup Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/research-backtester.git
   cd research-backtester
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed. Then, install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run a Backtest**:
   Execute the Day 1 backtest script:
   ```bash
   python src/run_day1_backtest.py
   ```

4. **Explore and Modify**:
   Feel free to modify the code in `src/` to implement your own trading strategies or adjust parameters.

5. **Testing**:
   Run unit tests to verify the functionality of individual components:
   ```bash
   pytest
   ```

This setup provides a comprehensive environment for conducting quantitative finance research and backtesting trading strategies.