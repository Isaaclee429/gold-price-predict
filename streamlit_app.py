import streamlit as st
import matplotlib.pyplot as plt
import yfinance as yf

# 商品參數設定
assets = {
    "Gold": {"ticker": "GC=F", "base_price": 3480, "geo_w": 200, "usd_w": -150, "infl_w": 180},
    "Silver": {"ticker": "SI=F", "base_price": 25, "geo_w": 1.5, "usd_w": -1.0, "infl_w": 1.2},
    "Oil": {"ticker": "CL=F", "base_price": 82, "geo_w": 15, "usd_w": -12, "infl_w": 10},
    "BTC": {"ticker": "BTC-USD", "base_price": 65000, "geo_w": 3000, "usd_w": -2500, "infl_w": 2200},
}

# 頁面 UI
st.title("Live Asset Price Prediction Tool")
st.markdown("Estimate asset prices based on geopolitical risk, USD strength, and inflation. Compare with real-time market data.")

# 選擇商品
selected_asset = st.selectbox("Select Asset", list(assets.keys()))
params = assets[selected_asset]

# 即時價格取得
try:
    ticker_data = yf.Ticker(params["ticker"])
    live_price = ticker_data.history(period="1d")["Close"].iloc[-1]
except:
    live_price = None

# 使用者輸入
st.sidebar.header("Adjust Parameters")
geo = st.sidebar.slider("Geopolitical Risk", 0.0, 1.0, 0.5, step=0.05)
usd = st.sidebar.slider("USD Strength (negative = weaker)", -1.0, 1.0, -0.3, step=0.05)
inflation = st.sidebar.slider("Inflation Expectation", 0.0, 1.0, 0.5, step=0.05)

# 模擬價格預測
delta = geo * params["geo_w"] + usd * params["usd_w"] + inflation * params["infl_w"]
predicted_price = params["base_price"] + delta

# 顯示預測與即時數據
st.metric(f"Predicted {selected_asset} Price", f"${predicted_price:,.2f}")
if live_price:
    st.metric(f"Live {selected_asset} Price", f"${live_price:,.2f}")
else:
    st.warning("⚠ Unable to fetch live data. Please check your internet or ticker code.")

# 繪製圖表
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(['Predicted', 'Live'],
              [predicted_price, live_price if live_price else 0],
              color=['gold', 'gray'],
              label=['Predicted', 'Live'])

# 標註數字
ax.text(0, predicted_price + 0.05 * predicted_price, f"${predicted_price:,.0f}", ha='center', fontsize=14)
if live_price:
    ax.text(1, live_price + 0.05 * live_price, f"${live_price:,.0f}", ha='center', fontsize=14)

# 標題與參考線
ax.axhline(params["base_price"], color='red', linestyle='--', linewidth=2, label=f"Baseline ${params['base_price']}")
ax.set_title(f"{selected_asset} Price Forecast", fontsize=16, pad=30)
ax.set_ylabel("USD", fontsize=14)
ax.legend(loc='lower left')

# 改善：用 figtext 顯示說明，避免與標題重疊
plt.figtext(0.5, 1.02, "Forecast based on geopolitical risk, USD strength, and inflation", ha='center', fontsize=10)

st.pyplot(fig)
