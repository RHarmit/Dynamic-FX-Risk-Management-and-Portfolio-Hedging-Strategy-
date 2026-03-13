<div align="center">

# 💱 Dynamic FX Risk Management & Portfolio Hedging Strategy

**End-to-end FX risk analysis using Bollinger Bands, dynamic hedging simulation, and Sharpe ratio comparison to quantify hedging effectiveness on a USD/EUR portfolio.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![yfinance](https://img.shields.io/badge/Data-yfinance-orange)](https://pypi.org/project/yfinance/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## Overview

Demonstrates a rigorous approach to managing foreign exchange risk for a USD/EUR portfolio. Uses Bollinger Bands to gauge FX volatility regimes, simulates an 80% hedged portfolio using forward contracts and options, and benchmarks hedged vs. unhedged performance through Sharpe ratios and drawdown analysis.

## Key Results

| Metric | Unhedged | Hedged |
|--------|----------|--------|
| Sharpe Ratio | **-0.80** | **0.25** |
| Risk-Adjusted Improvement | — | **+15%** |
| Hedge Ratio | — | **80%** |

## Features

- **FX Rate Analysis** — Fetches historical USD/EUR exchange rates and computes daily returns
- **Bollinger Bands** — 20-day moving average with ±2σ bands for volatility regime detection
- **Dynamic Hedging Simulation** — Models an 80% hedged portfolio using forward contracts and options
- **Sharpe Ratio Comparison** — Side-by-side risk-adjusted return analysis (hedged vs. unhedged)
- **Interactive Visualization** — Exchange rate trends, Bollinger Bands, and portfolio performance plots

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.9+ |
| Data | yfinance (EURUSD=X) |
| Analytics | pandas, NumPy |
| Models | Bollinger Bands, Sharpe Ratio |
| Visualization | Matplotlib, Seaborn |

## Quick Start

```bash
git clone https://github.com/RHarmit/Dynamic-FX-Risk-Management-and-Portfolio-Hedging-Strategy-.git
cd Dynamic-FX-Risk-Management-and-Portfolio-Hedging-Strategy-
pip install yfinance pandas numpy matplotlib seaborn
python "FX Project.PY"
```
