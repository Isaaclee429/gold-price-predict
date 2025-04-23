import streamlit as st
import matplotlib.pyplot as plt

# 商品設定與參數調整
assets = {
    "Gold": {"base_price": 3480, "geo_w": 200, "usd_w": -150, "infl_w": 180},
    "Silver": {"base_price": 25, "geo_w": 1.5, "usd_w": -1.0, "infl_w": 1.2},
    "Oil": {"base_price": 82, "geo_w": 15, "usd_w": -12, "infl_w": 10},
    "BTC": {"base_price": 65000, "geo_w": 3000, "usd_w": -2500, "infl_w": 2200},
}

# UI
st.title("Asset Price Prediction Tool")
st.markdown("Estimate future prices based on geopolitical risk, USD strength, and inflation expectations.")

# 商品選擇
selected_asset = st.selectbox("Select Asset", list(assets.keys()))
params = assets[selected_asset]

# Sidebar sliders
st.sidebar.header("Adjust Parameters")
geo = st.sidebar.slider("Geopolitical Risk", 0.0, 1.0, 0.5, step=0.05)
usd = st.sidebar.slider("USD Strength (negative = weaker)", -1.0, 1.0, -0.3, step=0.05)
inflation = st.sidebar.slider("Inflation Expectation", 0.0, 1.0, 0.5, step=0.05)

# 模型運算
delta = geo * params["geo_w"] + usd * params["usd_w"] + inflation * params["infl_w"]
predicted_price = params["base_price"] + delta

# 顯示結果
st.metric(f"Predicted {selected_asset} Price", f"${predicted_price:,.2f}")

# 畫圖
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(['Predicted'], [predicted_price], color='gold')
ax.axhline(params["base_price"], color='red', linestyle='--', linewidth=2,
           label=f"Baseline ${params['base_price']}")
ax.text(0, predicted_price + 0.05 * predicted_price, f"${predicted_price:,.0f}", ha='center', fontsize=14)
ax.set_title(f'{selected_asset} Price Forecast', fontsize=16)
ax.set_ylabel('USD', fontsize=14)
ax.legend()

# 嵌入說明
fig.text(0.5, 0.96, f"Forecast based on geopolitical risk, USD strength, and inflation", ha='center', fontsize=10)
fig.text(0.95, 0.1, f"Red dashed line: Baseline ${params['base_price']}", ha='right', fontsize=9)
fig.text(0.5, 0.02, f"Yellow bar = predicted {selected_asset.lower()} price", ha='center', fontsize=9)

st.pyplot(fig)
