import ta
import pandas as pd

def add_indicators(data):
    # Ensure we are working with a Series, not a 1-column DataFrame
    close_prices = data['Close'].iloc[:, 0] if len(data['Close'].shape) > 1 else data['Close']

    data['rsi'] = ta.momentum.RSIIndicator(close_prices).rsi()
    
    macd_indicator = ta.trend.MACD(close_prices)
    data['macd'] = macd_indicator.macd()
    data['macd_signal'] = macd_indicator.macd_signal()
    
    return data
