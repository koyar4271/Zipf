import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSVファイルを読み込む
df = pd.read_csv('temp.csv')

# 2列目と4列目のデータを抽出
temperature_data = df.iloc[:, 1].dropna()  # 2列目 (気温) から欠損値を除外
solar_data = df.iloc[:, 3].dropna()  # 4列目 (全天日射量) から欠損値を除外

# 気温データの頻度分布
temp_freq = temperature_data.value_counts().sort_values(ascending=False)

# 全天日射量データの頻度分布
solar_freq = solar_data.value_counts().sort_values(ascending=False)

# 順位の作成
temp_rank = np.arange(1, len(temp_freq) + 1)
solar_rank = np.arange(1, len(solar_freq) + 1)

# 気温データのグラフ
plt.figure(figsize=(10, 6))
plt.plot(temp_rank, temp_freq.values, marker='o', linestyle='-', color='blue', label='Temperature Data')
plt.title('Temperature Data (Rank vs Frequency)', fontsize=14)
plt.xlabel('Rank', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('temperature_rank_vs_frequency.png', dpi=300)
print("Temperature rank vs frequency graph saved as 'temperature_rank_vs_frequency.png'.")

# 全天日射量データのグラフ
plt.figure(figsize=(10, 6))
plt.plot(solar_rank, solar_freq.values, marker='o', linestyle='-', color='red', label='Solar Radiation Data')
plt.title('Solar Radiation Data (Rank vs Frequency)', fontsize=14)
plt.xlabel('Rank', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('solar_radiation_rank_vs_frequency.png', dpi=300)
print("Solar radiation rank vs frequency graph saved as 'solar_radiation_rank_vs_frequency.png'.")
