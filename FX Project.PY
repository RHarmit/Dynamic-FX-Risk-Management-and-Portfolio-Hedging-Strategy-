import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Step 1: Fetch Historical Exchange Rate Data
start_date = "2022-01-01"
end_date = "2023-01-01"
fx_data = yf.download("EURUSD=X", start=start_date, end=end_date, auto_adjust=False)

# Step 2: Calculate Daily Returns
fx_data['Returns'] = fx_data['Adj Close'].pct_change()

# Step 3: Calculate Moving Average and Bollinger Bands
window = 20
fx_data['20_MA'] = fx_data['Adj Close'].rolling(window=window).mean()

# Robust rolling std extraction (handles both Series and DataFrame cases)
rolling_std = fx_data['Adj Close'].rolling(window=window).std()
if isinstance(rolling_std, pd.DataFrame):
    rolling_std = rolling_std.iloc[:, 0]  # Convert to Series if DataFrame

fx_data['Upper_Band'] = fx_data['20_MA'] + 2 * rolling_std
fx_data['Lower_Band'] = fx_data['20_MA'] - 2 * rolling_std

# Step 4: Simulate a Hedged Portfolio
initial_portfolio_value = 100_000  # USD
hedged_ratio = 0.8  # 80% hedged

unhedged_returns = fx_data['Returns'].fillna(0)
hedged_returns = hedged_ratio * (-unhedged_returns) + (1 - hedged_ratio) * unhedged_returns

fx_data['Unhedged Portfolio Value'] = initial_portfolio_value * (1 + unhedged_returns).cumprod()
fx_data['Hedged Portfolio Value'] = initial_portfolio_value * (1 + hedged_returns).cumprod()

# Step 5: Calculate Performance Metrics
def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = returns - risk_free_rate / 252
    return np.sqrt(252) * np.mean(excess_returns) / np.std(excess_returns)

hedged_sharpe = calculate_sharpe_ratio(hedged_returns)
unhedged_sharpe = calculate_sharpe_ratio(unhedged_returns)

# Step 6: Visualization
plt.figure(figsize=(14, 10))

# Exchange Rate and Bollinger Bands
plt.subplot(2, 1, 1)
plt.plot(fx_data.index, fx_data['Adj Close'], label='EUR/USD', color='blue')
plt.plot(fx_data.index, fx_data['20_MA'], label='20-Day MA', color='orange')
plt.fill_between(fx_data.index, fx_data['Upper_Band'], fx_data['Lower_Band'], color='gray', alpha=0.2)
plt.title('EUR/USD Exchange Rate with Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()

# Portfolio Performance
plt.subplot(2, 1, 2)
plt.plot(fx_data.index, fx_data['Hedged Portfolio Value'], label='Hedged Portfolio', color='green')
plt.plot(fx_data.index, fx_data['Unhedged Portfolio Value'], label='Unhedged Portfolio', color='red')
plt.title('Hedged vs Unhedged Portfolio Performance')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (USD)')
plt.legend()

plt.tight_layout()
plt.show()

# Step 7: Print Performance Metrics
print(f"Hedged Portfolio Sharpe Ratio:   {hedged_sharpe:.2f}")
print(f"Unhedged Portfolio Sharpe Ratio: {unhedged_sharpe:.2f}")
