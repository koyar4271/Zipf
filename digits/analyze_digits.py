import pandas as pd
from collections import Counter

def count_digits_in_csv(file_name, column_indices):
    try:
        # CSVを読み込む
        df = pd.read_csv(file_name, header=None)
        # 数字のカウント用の辞書
        digit_counter = Counter()
        # 指定された複数の列を処理
        for column_index in column_indices:
            if column_index >= len(df.columns):
                print(f"Error: Column index {column_index} is out of range for the file '{file_name}'. Skipping...")
                continue
            # 列データを取得し、欠損値を削除
            column_data = df.iloc[:, column_index].dropna().astype(str)
            # 数字をカウント
            for value in column_data:
                digit_counter.update(char for char in value if char.isdigit())
        # 出現回数を表示
        print(f"Digit counts in columns {column_indices} of '{file_name}':")
        for digit in range(10):
            print(f"{digit_counter[str(digit)]}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
# 使用例
file_name = 'production.csv'  # 調べるCSVファイル名
column_indices = [0,1]  # 調べたい列のインデックス (0始まり)
count_digits_in_csv(file_name, column_indices)
