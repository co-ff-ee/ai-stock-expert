import yfinance as yf
import pandas as pd

def get_stock_data(symbol="BTC-USD"):
    df = yf.download(symbol, period="1y", interval="1d")
    
    # Ensure columns are flat strings (fixes the empty data issue)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]
    
    return df
