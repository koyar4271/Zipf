import pandas as pd
import numpy as np
from scipy.stats import linregress
import csv

# 入力CSVファイル名
input_file = "science_each.csv"
# 出力CSVファイル名
output_file = "zipf_slopes_science.csv"

# CSVファイルの読み込み
data = pd.read_csv(input_file, header=0)

# 作品ごとの処理
results = []
for column_index in range(0, len(data.columns), 3):
    file_name = data.columns[column_index]
    if pd.isna(file_name):
        continue
    # 単語と頻度を取得
    frequencies = data.iloc[:, column_index + 2].dropna().tolist()
    frequencies = [int(freq) for freq in frequencies if freq != '']
    # 順位と頻度を計算
    ranks = range(1, len(frequencies) + 1)
    # 両対数変換
    log_ranks = np.log10(ranks)
    log_frequencies = np.log10(frequencies)
    # 回帰直線を計算
    slope, intercept, _, _, _ = linregress(log_ranks, log_frequencies)
    # 総単語数を計算
    total_words = sum(frequencies)
    # 結果を保存
    results.append([file_name, total_words, slope])

# 結果をCSVに出力
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ファイル名", "総単語数", "Zipf則の傾き"])
    writer.writerows(results)

print(f"Zipf則の傾きと総単語数が {output_file} に出力されました。")
