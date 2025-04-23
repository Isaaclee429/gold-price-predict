# gold-price-predict

# 黃金價格預測互動小工具（使用參數模擬）

import matplotlib.pyplot as plt
import numpy as np

def simulate_gold_price(
    base_price=3480,
    geopolitical_risk=0.0,     # 地緣政治風險因子（0~1）
    usd_strength=0.0,          # 美元強度因子（-1~1，負值表示美元走弱）
    inflation_expectation=0.0  # 通膨預期（0~1）
):
    """
    模擬黃金價格變化。
    每個因子將對最終價格產生線性影響。
    """
    # 因子權重（可以自行調整）
    weights = {
        'geopolitical_risk': 200,
        'usd_strength': -150,
        'inflation_expectation': 180
    }

    # 預測價格計算
    delta = (
        weights['geopolitical_risk'] * geopolitical_risk +
        weights['usd_strength'] * usd_strength +
        weights['inflation_expectation'] * inflation_expectation
    )
    predicted_price = base_price + delta

    # 畫圖
    plt.figure(figsize=(6, 4))
    bars = plt.bar(['預測金價'], [predicted_price], color='gold')
    plt.axhline(base_price, color='red', linestyle='--', label=f'目前金價 ${base_price}')
    plt.title('黃金價格模擬工具')
    plt.ylabel('美元/盎司')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 範例：預設參數模擬
simulate_gold_price(
    base_price=3480,
    geopolitical_risk=0.6,
    usd_strength=-0.4,
    inflation_expectation=0.5
) # 你可根據需要調整這三個參數
