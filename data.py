import yfinance as yf
import pandas as pd
import streamlit as st

def get_stock_data(symbol="BTC-USD"):
    try:
        # Download data with a timeout
        df = yf.download(symbol, period="1y", interval="1d", progress=False)
        
        if df is None or df.empty:
            return None

        # Fix for the MultiIndex column error on Streamlit Cloud
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        return df
    except Exception as e:
        return None

