import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSVファイルの読み込み
file_name = 'production.csv'
try:
    # CSVのデータをデータフレームに読み込む
    df = pd.read_csv(file_name, header=None)

    # 1列目のデータを取得し、0を除外し、欠損値を削除
    column_data = pd.to_numeric(df.iloc[:, 1], errors='coerce').dropna()
    column_data = column_data[column_data != 0]

    # 頻度分布を計算し、降順にソート
    frequency_distribution = column_data.value_counts().sort_values(ascending=False)

    # 順位を計算
    ranks = np.arange(1, len(frequency_distribution) + 1)

    # 両対数グラフを作成
    plt.figure(figsize=(8, 6))
    plt.loglog(ranks, frequency_distribution.values, marker='o', linestyle='-', color='b', label='Data')

    # 回帰直線の計算（対数変換後）
    log_ranks = np.log10(ranks)
    log_freq = np.log10(frequency_distribution.values)
    slope, intercept = np.polyfit(log_ranks, log_freq, 1)

    # 回帰直線のプロット
    log_fit = slope * log_ranks + intercept
    plt.loglog(ranks, 10**log_fit, linestyle='--', color='r', label=f'Fit Line: slope={slope:.2f}')

    # グラフのタイトルとラベル設定
    plt.title('Log-Log Plot of Rank vs Frequency with Regression Line')
    plt.xlabel('Rank (Log Scale)')
    plt.ylabel('Frequency (Log Scale)')
    plt.grid(True, which="both", linestyle='--', alpha=0.6)
    plt.legend()

    # グラフを保存
    output_file = 'rank_vs_frequency_loglog_with_fit.png'
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    print(f"Log-log graph with regression line saved as '{output_file}'.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
