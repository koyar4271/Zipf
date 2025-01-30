import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# CSVファイルの読み込み
def plot_loglog_from_csv(file_path, column_index):
    # CSVファイルを読み込む (1行目をヘッダーとしてスキップ)
    data = pd.read_csv(file_path, header=0)
    
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
    plt.figure(figsize=(8, 6))
    plt.loglog(ranks, frequencies, marker="o", linestyle="none", markersize=3, label="Frequency Data")

    # 回帰直線を追加
    plt.loglog(ranks, fitted_line, linestyle="-", color="blue", label=f"Fitted Line (slope = {slope:.2f})")

    # 軸ラベルとタイトルの設定
    plt.xlabel("Rank (log scale)")
    plt.ylabel("Frequency (log scale)")
    plt.title(f"Log-Log Plot of Column {column_index + 1} Frequency vs Rank")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()

    # グラフを画像ファイルとして保存
    plt.savefig('wiki.png')
    print("グラフが 'wiki' として保存されました。")  

    # グラフの表示
    plt.show()

    

# ファイルパスを指定してプロット実行
file_path = "word_frequency.csv"  # ファイル名を指定
column_index = 1  # 使用する列のインデックス (0から始まる)
plot_loglog_from_csv(file_path, column_index)
