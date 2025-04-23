import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf

# 商品參數與對應代碼
assets = {
    "Gold": {"ticker": "GC=F", "base_price": 3480, "geo_w": 200, "usd_w": -150, "infl_w": 180},
    "Silver": {"ticker": "SI=F", "base_price": 25, "geo_w": 1.5, "usd_w": -1.0, "infl_w": 1.2},
    "Oil": {"ticker": "CL=F", "base_price": 82, "geo_w": 15, "usd_w": -12, "infl_w": 10},
    "BTC": {"ticker": "BTC-USD", "base_price": 65000, "geo_w": 3000, "usd_w": -2500, "infl_w": 2200},
}

# UI：標題與選項
st.title("Live Asset Price Prediction Tool")
st.markdown("Estimate future prices and compare with real-time market data.")

# 選擇商品
selected_asset = st.selectbox("Select Asset", list(assets.keys()))
params = assets[selected_asset]

# 即時價格（使用 yfinance）
try:
    ticker_data = yf.Ticker(params["ticker"])
    live_price = ticker_data.history(period="1d")["Close"].iloc[-1]
except:
    live_price = None

# 參數滑桿
st.sidebar.header("Adjust Prediction Parameters")
geo = st.sidebar.slider("Geopolitical Risk", 0.0, 1.0, 0.5, step=0.05)
usd = st.sidebar.slider("USD Strength (negative = weaker)", -1.0, 1.0, -0.3, step=0.05)
inflation = st.sidebar.slider("Inflation Expectation", 0.0, 1.0, 0.5, step=0.05)

# 預測模型計算
delta = geo * params["geo_w"] + usd * params["usd_w"] + inflation * params["infl_w"]
predicted_price = params["base_price"] + delta

# 顯示結果
st.metric(f"Predicted {selected_asset} Price", f"${predicted_price:,.2f}")
if live_price:
    st.metric(f"Live {selected_asset} Price", f"${live_price:,.2f}")
else:
    st.warning("⚠ Unable to fetch live data. Please check internet or ticker code.")

# 圖表顯示
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(['Predicted'], [predicted_price], color='gold', label="Predicted")
if live_price:
    ax.bar(['Live'], [live_price], color='gray', label="Live")

ax.axhline(params["base_price"], color='red', linestyle='--', linewidth=2,
           label=f"Baseline ${params['base_price']}")

# 數字標註與外觀微調
ax.text(0, predicted_price + 0.05 * predicted_price, f"${predicted_price:,.0f}", ha='center', fontsize=14)
if live_price:
    ax.text(1, live_price + 0.05 * live_price, f"${live_price:,.0f}", ha='center', fontsize=14)

ax.set_title(f"{selected_asset} Price Forecast", fontsize=16, pad=30)
ax.set_ylabel("USD", fontsize=14)
ax.legend()

# 補充說明
fig.text(0.5, 0.96, "Forecast based on geopolitical risk, USD strength, and inflation", ha='center', fontsize=10)
fig.text(0.95, 0.1, f"Red dashed line = baseline ${params['base_price']}", ha='right', fontsize=9)

st.pyplot(fig)
