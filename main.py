import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# temp.csv ファイルを読み込む
df = pd.read_csv('temp.csv', header=None)

# 一列目のデータを取得
data = df.iloc[:, 0].values

# データを数値型に変換（NaNがある場合は除外）
data = pd.to_numeric(data, errors='coerce')

# numpyを使用してNaNを除外
data = data[~np.isnan(data)]

# データをソートして順位をつける
sorted_data = sorted(data, reverse=True)

# 順位を生成 (1から始まる)
ranks = range(1, len(sorted_data) + 1)

# グラフを作成
plt.figure(figsize=(10, 6))

# 横軸：順位の対数、縦軸：データの対数
plt.plot(np.log10(ranks), np.log10(sorted_data), marker='o', linestyle='-', markersize=3)

# グラフのタイトルとラベル
plt.title("Log-Log Plot of Rank vs Data", fontsize=14)
plt.xlabel("Log(Rank)", fontsize=12)
plt.ylabel("Log(Data)", fontsize=12)

# グリッド線を追加して見やすくする
plt.grid(True, which="both", linestyle='--', alpha=0.6)

plt.savefig('rank_vs_frequency.png', dpi=300)
print("グラフが 'rank_vs_frequency.png' として保存されました。")
