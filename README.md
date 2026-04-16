# 📈 AI Stock Expert System

A real-time financial dashboard that combines **Technical Analysis (TA)** with **Machine Learning** to provide actionable stock market insights. The system pulls live data, calculates momentum indicators, and uses a Linear Regression model to predict price movements.

## 🚀 Features
*   **Real-time Data Fetching:** Integrates with `yfinance` to pull daily stock and crypto data (default: BTC-USD).
*   **Technical Indicators:** Automatically calculates **RSI (Relative Strength Index)** and **MACD (Moving Average Convergence Divergence)** using the `ta` library.
*   **Hybrid Decision Engine:** 
    *   **Rule-Based:** Uses aggressive RSI/MACD crossovers (40/60 thresholds) to generate BUY/SELL signals.
    *   **AI-Driven:** Uses a Scikit-Learn Linear Regression model to predict the next price point based on current technical features.
*   **Interactive UI:** Clean, responsive Streamlit dashboard with price charts and a technical breakdown tab.

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io)
- **Data:** [yfinance](https://github.com)
- **Indicators:** [Technical Analysis Library (ta)](https://github.com)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org)
- **Data Manipulation:** Pandas & NumPy

## 📁 Project Structure
```bash
├── app.py           # Streamlit UI and dashboard layout
├── data.py          # Data fetching and MultiIndex cleaning
├── indicators.py    # RSI and MACD calculation logic
├── rules.py         # Custom trading logic thresholds
├── model.py         # ML model training and price prediction
└── requirements.txt # Project dependencies
```

## ⚙️ Setup & Installation
```bash
1. Clone the repository
   git clone https://github.com
   cd ai-stock-expert

2. Install dependencies
   pip install -r requirements.txt

3. Run the application
   python -m streamlit run app.py

```
## 📊 How it Works
```bash
Data Processing: Handles yfinance MultiIndex headers automatically.
Expert Rules: Uses 40/60 RSI thresholds for aggressive signal detection.
Decision Logic: "Strong Buy/Sell" triggers only when AI predictions and Technical signals align.
Disclaimer: Educational purposes only. Trading involves risk.

```

