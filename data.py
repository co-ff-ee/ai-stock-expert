import yfinance as yf
import pandas as pd

def get_stock_data(symbol="AAPL"):
    # Download without the problematic argument
    df = yf.download(symbol, period="1y", interval="1d")
    
    # FIX: If yfinance returned a MultiIndex (2D columns), flatten it to 1D
    # This prevents the 'ValueError: Data must be 1-dimensional' error
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    df.dropna(inplace=True)
    return df
