import streamlit as st
from data import get_stock_data
from indicators import add_indicators
from rules import apply_rules
from model import train_model, predict_price

st.set_page_config(page_title="AI Stock Expert", layout="wide")
st.title("📈 AI Stock Expert System")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Configuration")
symbol = st.sidebar.text_input("Enter Stock Symbol", "BTC-USD").upper()
predict_days = st.sidebar.slider("Prediction Sensitivity", 1, 10, 5)

# --- DATA PROCESSING ---
data = get_stock_data(symbol)
data = add_indicators(data)
data = apply_rules(data)
model = train_model(data)

latest = data.iloc[-1]
prev_close = data.iloc[-2]['Close']
prediction = predict_price(model, [latest['rsi'], latest['macd']])

# --- DECISION LOGIC ---
def final_decision(signal, prediction, price):
    if signal == "BUY" and prediction > price:
        return "🔥 STRONG BUY", "inverse"
    elif signal == "SELL" and prediction < price:
        return "⚠️ STRONG SELL", "error"
    else:
        return "⏳ HOLD / NEUTRAL", "off"

decision_text, color = final_decision(latest['signal'], prediction, latest['Close'])

# --- DASHBOARD LAYOUT ---
col1, col2, col3 = st.columns(3)

with col1:
    delta = float(latest['Close'] - prev_close)
    st.metric("Current Price", f"${latest['Close']:,.2f}", delta=f"{delta:,.2f}")

with col2:
    pred_delta = float(prediction - latest['Close'])
    st.metric("AI Predicted Price", f"${prediction:,.2f}", delta=f"{pred_delta:,.2f}")

with col3:
    st.subheader(decision_text)

# --- CHARTS ---
st.divider()
tab1, tab2 = st.tabs(["Price Chart", "Technical Indicators"])

with tab1:
    st.line_chart(data['Close'], use_container_width=True)

with tab2:
    st.write("MACD & RSI Comparison")
    st.line_chart(data[['rsi', 'macd']], use_container_width=True)

st.subheader("Recent Data Breakdown")
st.dataframe(data.tail(10), use_container_width=True)
