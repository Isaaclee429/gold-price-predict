import streamlit as st
import matplotlib.pyplot as plt

# 標題
st.title("黃金價格預測小工具")
st.markdown("根據地緣風險、美元強度與通膨預期模擬金價")

# 參數輸入
base_price = 3480
geo = st.slider("地緣政治風險", 0.0, 1.0, 0.6, step=0.05)
usd = st.slider("美元強度（負值為走弱）", -1.0, 1.0, -0.4, step=0.05)
inflation = st.slider("通膨預期", 0.0, 1.0, 0.5, step=0.05)

# 計算
delta = geo * 200 + usd * -150 + inflation * 180
predicted_price = base_price + delta

# 顯示結果
st.metric("預測金價（美元/盎司）", f"${predicted_price:.2f}")

# 畫圖
fig, ax = plt.subplots()
ax.bar(['預測金價'], [predicted_price], color='gold')
ax.axhline(base_price, color='red', linestyle='--', label=f'目前金價 ${base_price}')
ax.set_ylabel("美元/盎司")
ax.set_title("模擬黃金價格")
ax.legend()
st.pyplot(fig)
