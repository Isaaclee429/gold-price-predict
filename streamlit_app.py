# 加入中文字體（以微軟雅黑為例）
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='msyh.ttc', size=14)  # 你可以換成 SimHei.ttf 或其他中文字體路徑
plt.title('预测金价', fontproperties=font)
plt.ylabel('美元/盎司', fontproperties=font)


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
bars = ax.bar(['預測金價'], [predicted_price], color='gold')
ax.axhline(base_price, color='red', linestyle='--', label=f'目前金價 ${base_price}')
ax.set_ylabel("美元/盎司")
ax.set_title("模擬黃金價格")
ax.legend()

# 加上數值標籤
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 20, f"${yval:.0f}", ha='center', va='bottom', fontsize=12)

st.pyplot(fig)

