import pandas as pd
import talib
import matplotlib.pyplot as plt
import os

# Create directories
os.makedirs('C:/Users/Skyline/financial-news-analysis/data/processed', exist_ok=True)
os.makedirs('C:/Users/Skyline/financial-news-analysis/plots', exist_ok=True)

# Define data path
data_path = 'C:/Users/Skyline/financial-news-analysis/data/yfinance_data'

# Process all stock files
stock_files = os.listdir(data_path)
for stock_file in stock_files:
    if stock_file.endswith('.csv'):
        stock_symbol = stock_file.split('.')[0]
        stock_df = pd.read_csv(os.path.join(data_path, stock_file))
        stock_df['Date'] = pd.to_datetime(stock_df['Date'])

        # Calculate technical indicators with TA-Lib
        stock_df['SMA_20'] = talib.SMA(stock_df['Close'], timeperiod=20)
        stock_df['RSI'] = talib.RSI(stock_df['Close'], timeperiod=14)
        stock_df['MACD'], stock_df['MACD_Signal'], _ = talib.MACD(stock_df['Close'])

        # Calculate daily returns
        stock_df['Returns'] = stock_df['Close'].pct_change()

        # Visualize for all stocks
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

        # Save processed data
        stock_df.to_csv(f'C:/Users/Skyline/financial-news-analysis/data/processed/{stock_file}', index=False)