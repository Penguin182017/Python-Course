import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Binance AI Dashboard", layout="wide")

# =========================
# 🪙 COINS
# =========================
symbols = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "BNBUSDT",
    "XMRUSDT",
    "YFIUSDT",
    "LINKUSDT",
    "AVAXUSDT"
]

st.title("🚀 Binance AI Trading Dashboard")

# =========================
# 🔴 LIVE PRICES
# =========================
st.subheader("Live Prices")

cols = st.columns(len(symbols))

for i, sym in enumerate(symbols):
    try:
        price = requests.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": sym}
        ).json()["price"]

        cols[i].metric(sym, f"${float(price):,.2f}")

    except:
        cols[i].metric(sym, "Error")

st.divider()

# =========================
# 🪙 SELECT COIN
# =========================
symbol = st.selectbox("Select Coin", symbols)

# =========================
# 📊 GET CANDLE DATA
# =========================
url = "https://api.binance.com/api/v3/klines"
params = {"symbol": symbol, "interval": "1d", "limit": 200}

data = requests.get(url, params=params).json()

df = pd.DataFrame(data, columns=[
    "Date","Open","High","Low","Close","Volume",
    "Close Time","Quote Asset Volume","Trades",
    "Taker Buy Base","Taker Buy Quote","Ignore"
])

df["Date"] = pd.to_datetime(df["Date"], unit="ms")

for col in ["Open","High","Low","Close","Volume"]:
    df[col] = df[col].astype(float)

# =========================
# 🤖 INDICATORS (AI STYLE)
# =========================
df["EMA20"] = df["Close"].ewm(span=20).mean()
df["EMA50"] = df["Close"].ewm(span=50).mean()

# RSI
delta = df["Close"].diff()
gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
rs = gain / loss
df["RSI"] = 100 - (100 / (1 + rs))

# =========================
# 📈 CANDLE CHART
# =========================
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=df["Date"],
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"],
    name="Price"
))

fig.add_trace(go.Scatter(x=df["Date"], y=df["EMA20"], name="EMA20"))
fig.add_trace(go.Scatter(x=df["Date"], y=df["EMA50"], name="EMA50"))

fig.update_layout(
    title=f"{symbol} AI Trading Chart",
    xaxis_rangeslider_visible=False,
    template="plotly_dark",
    height=650
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# 🤖 AI SIGNAL
# =========================
latest_rsi = df["RSI"].iloc[-1]
ema20 = df["EMA20"].iloc[-1]
ema50 = df["EMA50"].iloc[-1]
price = df["Close"].iloc[-1]

st.subheader("AI Signal Engine")

if latest_rsi < 30 and ema20 > ema50:
    st.success("🟢 BUY SIGNAL")
elif latest_rsi > 70 and ema20 < ema50:
    st.error("🔴 SELL SIGNAL")
else:
    st.warning("🟡 HOLD")

st.write(f"""
- Price: ${price:,.2f}  
- RSI: {latest_rsi:.2f}  
- EMA20: {ema20:.2f}  
- EMA50: {ema50:.2f}  
""")

# =========================
# 📊 MARKET OVERVIEW
# =========================
st.subheader("Market Overview")

overview = []

for sym in symbols:
    try:
        p = requests.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": sym}
        ).json()["price"]

        overview.append({"Coin": sym, "Price": float(p)})

    except:
        overview.append({"Coin": sym, "Price": None})

st.dataframe(pd.DataFrame(overview))