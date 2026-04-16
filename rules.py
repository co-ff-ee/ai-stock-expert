def generate_signal(row):
    rsi = float(row['rsi'])
    macd = float(row['macd'])
    signal = float(row['macd_signal'])

    # Aggressive Thresholds: 40/60 instead of 30/70
    if rsi < 40 and macd > signal:
        return "BUY"
    elif rsi > 60 and macd < signal:
        return "SELL"
    else:
        return "NEUTRAL"

def apply_rules(data):
    data['signal'] = data.apply(generate_signal, axis=1)
    return data
