import yfinance as yf
import pandas as pd

# Download S&P 500 data for the past year
sp500_data = yf.download('^GSPC', start='1928-01-01', end='2024-10-19', interval='1d')

# Calculate daily percentage changes
sp500_data['Daily Change %'] = sp500_data['Adj Close'].pct_change() * 100

# Drop rows with NaN values (the first row will have NaN because there's no previous day to compare)
sp500_data.dropna(inplace=True)

# Save to CSV (optional)
sp500_data.to_csv('sp500_daily_changes.csv')

# Display the first few rows of the daily changes
# print(sp500_data[['Adj Close', 'Daily Change %']].head())
