# Financial News & Stock Analyzer 📈

![Financial Analysis](https://img.shields.io/badge/Financial-News%20%26%20Stocks-blueviolet?style=flat-square&logo=python)
[![Python](https://img.shields.io/badge/Python-3.11.9-brightgreen)](https://www.python.org/downloads/release/python-3119/)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/yankee998/financial-news-analysis)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Explore how news shapes stock prices! This project analyzes financial news sentiment and stock trends for seven major companies: Apple (AAPL), Amazon (AMZN), Google (GOOG), Meta (META), Microsoft (MSFT), NVIDIA (NVDA), and Tesla (TSLA). Built with Python, it’s perfect for anyone curious about markets. 🚀

## 🌟 What It Does

- 📢 **News Insights**: Checks the mood of financial news headlines.
- 📈 **Stock Trends**: Tracks price movements and key indicators.
- 🔗 **News-Stock Link**: Shows how news vibes affect stock prices.
- 📊 **Cool Charts**: Visualizes trends and correlations.

**Data**:
- News headlines (`raw_analyst_ratings.csv`).
- Stock prices (`yfinance_data/*.csv`).
- Get data from [Google Drive](https://drive.google.com/drive/folders/1rsispvTGPjC8pbKS-yYb-6dcJiXTKSAv).

## 🛠️ Main Features

- 📊 Eye-catching charts for news and stock trends.
- 🧠 News sentiment analysis with TextBlob.
- 📈 Technical indicators like moving averages and RSI.
- 🔗 Correlation between news and stock price changes.
- 💻 Easy to run on any system.

## 🚀 Get Started

### What You Need

- Python 3.11.9 ([Download](https://www.python.org/downloads/release/python-3119/))
- Git ([Download](https://git-scm.com/download/win))
- A code editor (like VS Code)
- Project data files

### Setup

<details>
<summary>📋 Quick Steps</summary>

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/yankee998/financial-news-analysis.git
   cd financial-news-analysis
   ```

2. **Set Up Python**:
   - Install Python 3.11.9.
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install Libraries**:
   - Use `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Get Data**:
   - Place `raw_analyst_ratings.csv` and `yfinance_data/` in the `data/` folder.
   - Download from [Google Drive](https://drive.google.com/drive/folders/1rsispvTGPjC8pbKS-yYb-6dcJiXTKSAv).

</details>

### How to Run

<details>
<summary>🏃 Quick Guide</summary>

1. **Explore News**:
   - Open `notebooks/eda.ipynb` in your editor.
   - Run it to see charts in the `plots/` folder.

2. **Analyze Stocks**:
   ```bash
   python scripts/technical_analysis.py
   ```
   - Creates stock data files and charts in `data/processed/` and `plots/`.

3. **Check News-Stock Links**:
   ```bash
   python scripts/sentiment_correlation.py
   ```
   - Generates correlation results and charts.

4. **Read Summary**:
   - See `notebooks/final_report.md` for key findings.

</details>

## 📁 What's in the Repo

```plaintext
financial-news-analysis/
├── data/                   # News and stock data
├── notebooks/              # Analysis notebooks
│   ├── eda.ipynb           # News analysis
│   └── final_report.md     # Project summary
├── plots/                  # Charts
├── scripts/                # Python scripts
│   ├── technical_analysis.py
│   └── sentiment_correlation.py
├── README.md               # This file
└── requirements.txt        # Python libraries
```

## 📊 Sample Outputs

- **Charts**: News trends, stock price graphs, sentiment correlations.
- **Data**: Processed stock files with indicators.
- **Report**: Summary of findings in `final_report.md`.

## ❓ Need Help?

- **No Charts?** Ensure data files are in `data/`.
- **Errors?** Check Python version (`python --version`) and library installs.
- **Questions?** Open an issue on [GitHub](https://github.com/yankee998/financial-news-analysis/issues).

## 🤝 Join In

Want to add features? 🌟
1. Fork the repo.
2. Create a branch: `git checkout -b my-feature`.
3. Commit: `git commit -m "Added cool stuff"`.
4. Push: `git push origin my-feature`.
5. Open a pull request.

## 📜 License

MIT License. See [LICENSE](LICENSE).

## 🙌 Thanks

- Data from [Google Drive](https://drive.google.com/drive/folders/1rsispvTGPjC8pbKS-yYb-6dcJiXTKSAv).
- Powered by Python, pandas, TextBlob, and more!

---

⭐ **Star this repo** to support the project!  
📧 Reach out via [GitHub](https://github.com/yankee998) for feedback.
