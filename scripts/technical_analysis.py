import pandas as pd
import talib
import matplotlib.pyplot as plt
import os

# Create directories
os.makedirs('C:/Users/Skyline/financial-news-analysis/data/processed', exist_ok=True)
os.makedirs('C:/Users/Skyline/financial-news-analysis/plots', exist_ok=True)

# Data path
data_path = 'C:/Users/Skyline/financial-news-analysis/data/yfinance_data'
stock_files = os.listdir(data_path)
print(f"Found {len(stock_files)} stock files: {stock_files}")

for stock_file in stock_files:
    if stock_file.endswith('.csv'):
        # Extract ticker (remove '_historical_data')
        stock_symbol = stock_file.replace('_historical_data.csv', '').upper()
        print(f"Processing {stock_symbol}")
        stock_df = pd.read_csv(os.path.join(data_path, stock_file))
        stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
        if stock_df['Date'].isna().any():
            print(f"Warning: {stock_df['Date'].isna().sum()} invalid dates in {stock_symbol}")
            stock_df = stock_df.dropna(subset=['Date'])

        # Technical indicators
        stock_df['SMA_20'] = talib.SMA(stock_df['Close'], timeperiod=20)
        stock_df['RSI'] = talib.RSI(stock_df['Close'], timeperiod=14)
        stock_df['MACD'], stock_df['MACD_Signal'], _ = talib.MACD(stock_df['Close'])
        stock_df['Returns'] = stock_df['Close'].pct_change()

        # Visualize
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.plot(stock_df['Date'], stock_df['Close'], label='Close Price')
        plt.plot(stock_df['Date'], stock_df['SMA_20'], label='20-day SMA')
        plt.title(f'{stock_symbol} Stock Price and SMA')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(stock_df['Date'], stock_df['RSI'], label='RSI', color='purple')
        plt.title(f'{stock_symbol} RSI')
        plt.legend()

        plt.tight_layout()
        plt.savefig(f'C:/Users/Skyline/financial-news-analysis/plots/{stock_symbol}_technical_indicators.png')
        plt.close()

        # Save with standard ticker name
        stock_df.to_csv(f'C:/Users/Skyline/financial-news-analysis/data/processed/{stock_symbol}.csv', index=False)
        print(f"Saved processed data for {stock_symbol}")