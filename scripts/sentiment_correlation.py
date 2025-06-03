import pandas as pd
import numpy as np
from textblob import TextBlob
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create directories
os.makedirs('C:/Users/Skyline/financial-news-analysis/data/processed', exist_ok=True)
os.makedirs('C:/Users/Skyline/financial-news-analysis/plots', exist_ok=True)

# Load news data
print("Loading raw_analyst_ratings.csv...")
news_df = pd.read_csv('C:/Users/Skyline/financial-news-analysis/data/raw_analyst_ratings.csv')
print(f"News data shape: {news_df.shape}")
print(f"News columns: {news_df.columns.tolist()}")
print(f"Unique stocks in news: {news_df['stock'].unique()[:10]}")

# Convert dates
news_df['date'] = pd.to_datetime(news_df['date'], format='mixed', errors='coerce', utc=True)
if news_df['date'].isna().any():
    print(f"Warning: {news_df['date'].isna().sum()} rows with invalid dates dropped.")
    news_df = news_df.dropna(subset=['date'])
news_df['date_only'] = news_df['date'].dt.date

# Sentiment analysis
print("Performing sentiment analysis...")
news_df['sentiment'] = news_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
print(f"Sentiment range: {news_df['sentiment'].min()} to {news_df['sentiment'].max()}")

# Process all stocks
stock_files = os.listdir('C:/Users/Skyline/financial-news-analysis/data/processed')
print(f"Found {len(stock_files)} files in data/processed: {stock_files}")
correlations = []
for stock_file in stock_files:
    if stock_file.endswith('.csv'):
        stock_symbol = stock_file.split('.')[0].upper()  # e.g., AAPL
        print(f"Processing stock: {stock_symbol}")

        # Load stock data
        stock_df = pd.read_csv(f'C:/Users/Skyline/financial-news-analysis/data/processed/{stock_file}')
        stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce').dt.date
        if stock_df['Date'].isna().any():
            print(f"Warning: {stock_df['Date'].isna().sum()} invalid dates in {stock_symbol}")
            stock_df = stock_df.dropna(subset=['Date'])
        stock_df['Daily_Return'] = stock_df['Close'].pct_change()
        print(f"Stock data shape for {stock_symbol}: {stock_df.shape}")

        # Filter news for the stock
        stock_news = news_df[news_df['stock'].str.upper() == stock_symbol]
        print(f"News articles for {stock_symbol}: {len(stock_news)}")
        if stock_news.empty:
            print(f"No news data for {stock_symbol}, skipping.")
            continue

        # Aggregate sentiment by date
        daily_sentiment = stock_news.groupby('date_only')['sentiment'].mean().reset_index()
        daily_sentiment.rename(columns={'date_only': 'date'}, inplace=True)
        print(f"Daily sentiment shape for {stock_symbol}: {daily_sentiment.shape}")

        # Merge datasets
        merged_df = pd.merge(
            daily_sentiment,
            stock_df[['Date', 'Daily_Return']],
            left_on='date',
            right_on='Date',
            how='inner'
        )
        print(f"Merged data shape for {stock_symbol}: {merged_df.shape}")

        # Correlation analysis
        if not merged_df.empty:
            corr, p_val = pearsonr(merged_df['sentiment'], merged_df['Daily_Return'].fillna(0))
            correlations.append({'Stock': stock_symbol, 'Correlation': corr, 'P-value': p_val})
            print(f"Correlation for {stock_symbol}: {corr:.4f}, P-value: {p_val:.4f}")

            # Visualize
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='sentiment', y='Daily_Return', data=merged_df)
            plt.title(f'Sentiment vs. Daily Stock Returns ({stock_symbol})')
            plt.xlabel('Average Daily Sentiment Score')
            plt.ylabel('Daily Stock Return')
            plt.savefig(f'C:/Users/Skyline/financial-news-analysis/plots/{stock_symbol}_sentiment_vs_returns.png')
            plt.close()
        else:
            print(f"No overlapping dates for {stock_symbol}, skipping visualization.")

# Save correlations
corr_df = pd.DataFrame(correlations)
print(f"Correlations found for {len(corr_df)} stocks.")
if not corr_df.empty:
    corr_df.to_csv('C:/Users/Skyline/financial-news-analysis/data/processed/correlations.csv', index=False)
    print("Saved correlations.csv")

    # Plot correlation summary
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Correlation', y='Stock', data=corr_df)
    plt.title('Sentiment-Return Correlations by Stock')
    plt.savefig('C:/Users/Skyline/financial-news-analysis/plots/correlation_summary.png')
    plt.close()
    print("Saved correlation_summary.png")
else:
    print("No correlations to save.")