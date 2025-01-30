import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSVファイルの読み込み
file_name = 'production.csv'
try:
    # CSVのデータをデータフレームに読み込む
    df = pd.read_csv(file_name, header=None)

    # 1列目のデータを取得し、0を除外し、欠損値を削除
    column_data = pd.to_numeric(df.iloc[:, 0], errors='coerce').dropna()
    column_data = column_data[column_data != 0]

    # 降順に並べる
    sorted_data = column_data.sort_values(ascending=False)

    # 順位を計算
    ranks = np.arange(1, len(sorted_data) + 1)

    # 両対数軸のグラフ作成
    plt.figure(figsize=(8, 6))
    plt.loglog(ranks, sorted_data.values, marker='o', linestyle='-', color='b')
    plt.title('Log-Log Plot of Rank vs Value')
    plt.xlabel('Rank (Log Scale)')
    plt.ylabel('Value (Log Scale)')
    plt.grid(True, which="both", linestyle='--', alpha=0.6)
    plt.tight_layout()

    # グラフを保存
    output_file = 'rank_vs_value_loglog.png'
    plt.savefig(output_file, dpi=300)
    print(f"Log-log graph saved as '{output_file}'.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
