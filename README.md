# Financial Data Analysis Project

## Overview
Welcome to the **Financial Data Analysis Project**, a Python-based initiative designed to perform quantitative analysis on historical stock data using technical indicators and financial metrics. This project leverages the TA-Lib library for technical analysis (e.g., Simple Moving Average, Relative Strength Index, MACD) and pandas/numpy for financial calculations (e.g., daily returns, annualized volatility, cumulative returns). The analysis is conducted for seven major stocks: AAPL (Apple), AMZN (Amazon), GOOG (Alphabet), META (Meta), MSFT (Microsoft), NVDA (NVIDIA), and TSLA (Tesla). Results are visualized using Matplotlib and Seaborn, with plots saved in an organized folder structure.

This repository was created and is maintained using **Visual Studio Code (VS Code)** on a **Windows** environment with **Python 3.13.3**. It includes Jupyter notebooks for each stock, providing a step-by-step analysis process and key results summary.

## Project Goals
- Perform technical analysis using TA-Lib to calculate indicators like SMA, RSI, and MACD.
- Compute financial metrics including daily returns, annualized volatility, and cumulative returns.
- Visualize data trends with plots for close price with SMA, RSI, MACD, and cumulative returns.
- Organize outputs in a structured manner for easy access and scalability.
- Provide a reproducible workflow for analyzing multiple stocks.

## Prerequisites
Before running the project, ensure you have the following installed:

- **Python 3.13.3**: Download from [python.org](https://www.python.org/downloads/) or use your preferred package manager.
- **Git**: For version control and repository management (download from [git-scm.com](https://git-scm.com/)).
- **Visual Studio Code**: IDE for development (download from [code.visualstudio.com](https://code.visualstudio.com/)).
- **Required Python Packages**:
  - `pandas`
  - `numpy`
  - `ta-lib`
  - `matplotlib`
  - `seaborn`

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yankee998/financial-news-analysis.git
   cd FinancialDataAnalysis


Set Up a Virtual Environment (recommended):
python -m venv venv
venv\Scripts\activate


Install Dependencies:

Install standard packages via pip:pip install pandas numpy matplotlib seaborn


Install TA-Lib (note: TA-Lib requires a precompiled wheel for Windows due to its C dependencies):
Download the appropriate wheel for Python 3.13 from Unofficial Windows Binaries.
Example command (adjust path and version as needed):pip install TA_Lib‑0.4.24‑cp313‑cp313‑win_amd64.whl






Verify Installation:

Run python -c "import talib; print(talib.__version__)" to confirm TA-Lib is installed.


Key Files and Folders

data/yfinance_data/: Contains historical stock data CSV files downloaded from yfinance or another source, along with raw_analyst_ratings.csv for potential future analysis.
notebooks/: Houses Jupyter notebooks for each stock's analysis and a visualizations/ subfolder for plots.
notebooks/visualizations/STOCK/: Stores stock-specific plots (e.g., AAPL/aapl_close_sma.png).
.gitignore: Excludes virtual environment files and other unnecessary items.
README.md: This file, providing project documentation.
requirements.txt: List of Python dependencies (to be created with pip freeze > requirements.txt after installation).

Usage
Running the Analysis

Open VS Code:

Launch VS Code and open the FinancialDataAnalysis folder (File > Open Folder).
Select the Python 3.13.3 interpreter (Ctrl + Shift + P, "Python: Select Interpreter").


Run a Notebook:

Open a notebook (e.g., AAPL_quantitative_analysis.ipynb).
Run all cells (Ctrl + Enter or click "Run Cell") to:
Calculate TA-Lib indicators (20-day SMA, 14-day RSI, MACD).
Compute financial metrics (daily returns, annualized volatility, cumulative returns).
Display a Key Results Summary table with the latest values.
Generate and display four plots, saved to notebooks/visualizations/STOCK/.



Guidelines

Follow the existing code structure and naming conventions.
Ensure plots are saved in the appropriate visualizations/STOCK/ folder.
Update this README if adding significant features.

License
This project is licensed under the MIT License. See the LICENSE file for details. (Note: Create a LICENSE file with MIT License text if not already present.)
Acknowledgments

TA-Lib: For technical analysis capabilities (https://ta-lib.github.io/).
Pandas/Numpy: For data manipulation and financial calculations (https://pandas.pydata.org/, https://numpy.org/).
Matplotlib/Seaborn: For data visualization (https://matplotlib.org/, https://seaborn.pydata.org/).
yfinance: For providing historical stock data (assumed as the data source).

Contact
For questions or suggestions, please open an issue on the GitHub repository or contact the maintainer at [yaredgenanaw99@gmail.com]. 