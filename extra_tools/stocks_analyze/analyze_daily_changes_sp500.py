import pandas as pd

# Load the CSV file
sp500_data = pd.read_csv('sp500_daily_changes.csv', header=0, parse_dates=[0], index_col=0)

# Ensure the 'Date' column is parsed properly
sp500_data.index = pd.to_datetime(sp500_data.index)

# Group by year and month and calculate the max and min daily changes for each month
monthly_changes = sp500_data['Daily Change %'].resample('M').agg(['max', 'min'])

# Save the results to a new CSV file
monthly_changes.to_csv('sp500_monthly_max_min_changes.csv')

strong_months = monthly_changes[monthly_changes['min'] > -1]

strong_months.to_csv('sp500_strong_months.csv')

# Display the first few rows of the result
print(monthly_changes.head())
