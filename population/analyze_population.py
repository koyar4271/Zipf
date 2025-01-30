import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import matplotlib.font_manager as fm

# 日本語フォントを設定
#plt.rcParams['font.family'] = 'IPAexGothic'  # 必要に応じて、インストールされている日本語フォント名に変更

# pop.csv ファイルを読み込む
df = pd.read_csv('population_past.csv', header=0)  # ヘッダーを利用

# ヘッダーから列名を取得
#target_columns = df.columns[3,4,5]  # 最初の列を除いた列を対象
# 必要な列を指定（4列目から6列目を選択）
target_columns = df.columns[0: 9]

# グラフを作成
plt.figure(figsize=(12, 8))

for column_name in target_columns:
    try:
        # 人口データを取得し、数値型に変換
        populations = pd.to_numeric(df[column_name], errors='coerce').dropna().values

        # データを降順にソートし、無効な値を除外
        populations_sorted = sorted([p for p in populations if p > 0], reverse=True)

        # 無効データの場合はスキップ
        if not populations_sorted:
            print(f"Column '{column_name}' has no valid data to plot.")
            continue

        # 順位 (1から始まる)
        ranks = range(1, len(populations_sorted) + 1)

        # 両対数スケール用のデータ
        log_ranks = np.log10(ranks)
        log_populations = np.log10(populations_sorted)

        # 回帰直線を計算
        slope, intercept, _, _, _ = linregress(log_ranks, log_populations)

        # 回帰直線の値を計算
        fitted_line = slope * log_ranks + intercept

        # データと回帰直線をプロット
        plt.plot(ranks, log_populations, marker='o', linestyle='-', markersize=3, label=f'{column_name}')
        plt.plot(ranks, fitted_line, linestyle='--', label=f'{column_name} Regression (slope={slope:.2f})')

    except KeyError:
        print(f"Column '{column_name}' does not exist in the data.")
    except Exception as e:
        print(f"An error occurred while processing column '{column_name}': {e}")

# グラフのタイトルとラベル
plt.title("Population vs Rank (Log Scale)", fontsize=14)
plt.xlabel("Rank (Log Scale)", fontsize=12)
plt.ylabel("Population (Log Scale)", fontsize=12)

# 横軸を対数スケールに設定
plt.xscale('log')

# グリッド線を追加して見やすくする
plt.grid(True, which="both", linestyle='--', alpha=0.6)

# 凡例を追加
plt.legend()

plt.tight_layout()
plt.savefig('rank_vs_frequency_with_regression_multiple.png', dpi=300)
print("グラフが 'rank_vs_frequency_with_regression_multiple.png' として保存されました。")
