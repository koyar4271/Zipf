import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# CSVファイルの読み込み
def plot_loglog_from_csv(file_path, column_indices):
    # CSVファイルを読み込む (1行目をヘッダーとしてスキップ)
    data = pd.read_csv(file_path, header=0)
    # ヘッダー名を取得
    headers = data.columns.tolist()
    plt.figure(figsize=(8, 6))
    for column_index in column_indices:
        # 指定列を取得してリストに変換
        frequencies = data.iloc[:, column_index].dropna().tolist()
        # 出現頻度の順位を計算
        ranks = range(1, len(frequencies) + 1)
        # 両対数変換
        log_ranks = np.log10(ranks)
        log_frequencies = np.log10(frequencies)
        # 回帰直線を計算
        slope, intercept, _, _, _ = linregress(log_ranks, log_frequencies)
        fitted_line = 10**(intercept + slope * log_ranks)
        # 両対数グラフを描画
        plt.loglog(ranks, frequencies, marker="o", linestyle="none", markersize=3, label=f"{headers[column_index]} Data")
        # 回帰直線を追加
        plt.loglog(ranks, fitted_line, linestyle="-", label=f"{headers[column_index]} Fit (slope = {slope:.2f})")

    # 軸ラベルとタイトルの設定
    plt.xlabel("Rank (log scale)")
    plt.ylabel("Frequency (log scale)")
    plt.title("Log-Log Plot of Frequency vs Rank")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    # 凡例をプロットの外に配置
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    # グラフを画像ファイルとして保存
    plt.savefig('wiki.png', bbox_inches='tight')
    print("グラフが 'wiki.png' として保存されました。")  

# ファイルパスを指定してプロット実行
file_path = "word_frequency.csv"  # ファイル名を指定
column_indices = [1,2]  # 使用する列のインデックスのリスト (0から始まる)
plot_loglog_from_csv(file_path, column_indices)
