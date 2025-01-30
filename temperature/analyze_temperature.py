import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# CSVファイルの読み込み
file_name = 'temp.csv'
try:
    # データフレームを作成
    df = pd.read_csv(file_name, header=None)  # ヘッダーなしで読み込み

    # 必要な列を抽出 (2列目: index=1, 4列目: index=3)
    temperature_data = pd.to_numeric(df[1], errors='coerce').dropna()
    radiation_data = pd.to_numeric(df[3], errors='coerce').dropna()

    # 温度データの正規化 (最小値を基準に平行移動)
    temperature_min = temperature_data.min()
    print(f'Minimum temperature is {temperature_min}')
    temperature_data_normalized = temperature_data - temperature_min + 1

    # 日射量データの正規化 (同様に平行移動)
    radiation_min = radiation_data.min()
    print(f'Minimum solar radiation is {radiation_min}')
    radiation_data_normalized = radiation_data - radiation_min + 1

    # 頻度分布の計算とソート
    temperature_sorted = sorted(temperature_data_normalized, reverse=True)
    radiation_sorted = sorted(radiation_data_normalized, reverse=True)

    # 順位の作成 (1から始まる)
    temp_ranks = range(1, len(temperature_sorted) + 1)
    radiation_ranks = range(1, len(radiation_sorted) + 1)

    # 両対数データ
    temp_log_ranks = (temp_ranks)
    temp_log_values = (temperature_sorted)
    radiation_log_ranks = (radiation_ranks)
    radiation_log_values = (radiation_sorted)

    slope_temp, intercept_temp, _, _, _ = linregress(temp_log_ranks, temp_log_values)
    slope_rad, intercept_rad, _, _, _ = linregress(radiation_log_ranks, radiation_log_values)

    fitted_line_temp = slope_temp * temp_log_ranks + intercept_temp
    print(slope_temp)
    fitted_line_rad = slope_rad * radiation_log_ranks + intercept_rad

    # グラフの作成 (両データを1つの図にまとめる)
    plt.figure(figsize=(10, 8))

    # 温度データをプロット
    plt.plot(temp_log_ranks, temp_log_values, marker='o', linestyle='-', markersize=3,
             label='Temperature Data', color='blue')
    plt.plot(temp_log_ranks, fitted_line_temp, linestyle='--', label=f'Temperature Regression (slope={slope_temp:.10f})')

    # 日射量データをプロット
    plt.plot(radiation_log_ranks, radiation_log_values, marker='o', linestyle='-', markersize=3,
             label='Radiation Data', color='orange')
    plt.plot(radiation_log_ranks, fitted_line_rad, linestyle='--', label=f'Radiation Regression (slope={slope_rad:.10f})')

    # グラフ設定
    plt.grid(True, which="both", linestyle='--', alpha=0.6)
    plt.title("Temperature and Radiation Data", fontsize=14)
    plt.xlabel("Rank", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    plt.legend()
    plt.tight_layout()

    # グラフの保存
    plt.savefig('combined_log_graph_normalized.png', dpi=300)
    print("Combined graph saved as 'combined_log_graph_normalized.png'.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
