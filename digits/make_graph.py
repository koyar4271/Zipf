import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def plot_log_log_from_csv_with_column_indices(file_name, column_indices):
    try:
        # CSVファイルの読み込み
        df = pd.read_csv(file_name)

        # グラフの準備
        plt.figure(figsize=(10, 8))
        colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']  # 色リスト
        for idx, column_index in enumerate(column_indices):
            if column_index >= len(df.columns):
                print(f"Error: Column index {column_index} is out of range for the file '{file_name}'.")
                continue

            # 指定された列を読み込む
            column_data = pd.to_numeric(df.iloc[:, column_index], errors='coerce').dropna()
            if column_data.empty:
                print(f"Column at index {column_index} is empty or invalid.")
                continue

            # 順位と値の準備
            ranks = np.arange(1, len(column_data) + 1)
            sorted_values = column_data.sort_values(ascending=False).to_numpy()

            # 両対数変換
            log_ranks = np.log10(ranks)
            log_values = np.log10(sorted_values)

            # 回帰直線の計算
            model = LinearRegression()
            log_ranks_reshaped = log_ranks.reshape(-1, 1)
            model.fit(log_ranks_reshaped, log_values)
            regression_line = model.predict(log_ranks_reshaped)

            # グラフにプロット
            column_name = df.columns[column_index]  # ヘッダー名を取得
            plt.scatter(log_ranks, log_values, label=f'{column_name}', color=colors[idx % len(colors)])
            plt.plot(log_ranks, regression_line, linestyle='--', color=colors[idx % len(colors)],
                     label=f'{column_name} Regression\n$y={model.coef_[0]:.2f}x + {model.intercept_:.2f}$')

        # グラフの設定
        plt.title('Log-Log Plot with Regression Lines', fontsize=14)
        plt.xlabel('Log(Rank)', fontsize=12)
        plt.ylabel('Log(Frequency)', fontsize=12)
        plt.grid(True, which="both", linestyle='--', alpha=0.6)
        plt.legend()
        plt.ylim(bottom=2.0)
        plt.tight_layout()

        # グラフを保存
        output_file = 'log_log_graph_with_regression_indices.png'
        plt.savefig(output_file, dpi=300)
        print(f"Log-log graph saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 使用例
file_name = 'digits.csv'  # 調べるCSVファイル
column_indices = [5,6,7,8]  # 調べる列のインデックスを指定 (0ベース)
plot_log_log_from_csv_with_column_indices(file_name, column_indices)
