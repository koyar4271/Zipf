import csv
from collections import Counter

# 入力CSVファイル
input_file = 'temp.csv'

# 出力CSVファイル
output_file = 'sorted_frequency.csv'

# データを格納するリスト
data = []

# CSVファイルの読み込み
with open(input_file, 'r', newline='', encoding='utf-8-sig') as csvfile:  # BOM対応
    reader = csv.reader(csvfile)
    # 1行目だけを読み取る
    for row in reader:
        if len(row) > 0:  # 空行を無視
            data = [float(value) for value in row]  # 1行目の値をリストに格納
            break

# 出現頻度の計算
frequency = Counter(data)

# 出現頻度順にソート
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# 結果を別のCSVファイルに書き込む
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # ヘッダーを書き込む
    writer.writerow(['Value', 'Frequency'])
    # ソートされたデータを書き込む
    writer.writerows(sorted_frequency)

print(f"出現頻度をソートした結果が '{output_file}' に出力されました。")
