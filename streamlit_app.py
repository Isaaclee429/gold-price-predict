import streamlit as st
import matplotlib.pyplot as plt

# Streamlit 標題
st.title("黃金價格預測小工具")
st.markdown("根據地緣風險、美元走勢與通膨預期，自動模擬金價")

# 模型參數輸入
st.sidebar.header("參數調整")
geo = st.sidebar.slider("地緣政治風險", 0.0, 1.0, 0.6, step=0.05)
usd = st.sidebar.slider("美元強度（負值代表走弱）", -1.0, 1.0, -0.4, step=0.05)
inflation = st.sidebar.slider("通膨預期", 0.0, 1.0, 0.5, step=0.05)

# 模型計算
base_price = 3480
delta = geo * 200 + usd * -150 + inflation * 180
predicted_price = base_price + delta

# 顯示預測結果
st.metric("預測金價（美元/盎司）", f"${predicted_price:.2f}")

# 畫圖
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(['預測值'], [predicted_price], color='gold')
ax.axhline(base_price, color='red', linestyle='--', linewidth=2, label=f"基準價 ${base_price}")
ax.text(0, predicted_price + 100, f"${predicted_price:.0f}", ha='center', fontsize=14)
ax.set_title('黃金價格預測', fontsize=16)
ax.set_ylabel('美元/盎司')
ax.legend()

# 嵌入說明文字
fig.text(0.5, 0.96, "地緣風險、美元走勢與通膨預期綜合影響下的價格預測", ha='center', fontsize=10)
fig.text(0.95, 0.1, "紅色虛線表示基準價格 $3480", ha='right', fontsize=9)
fig.text(0.5, 0.02, "黃色長條代表預測價格 $3750", ha='center', fontsize=9)

st.pyplot(fig)
