import csv
from collections import Counter

# 入力CSVファイル
input_file = 'word_frequency.csv'

# データを格納するリスト
digits = []

# CSVファイルの読み込み
with open(input_file, 'r', newline='', encoding='utf-8-sig') as csvfile:  # BOM対応
    reader = csv.reader(csvfile)
    # 2列目の全データを処理
    for row in reader:
        if len(row) > 1:  # 2列目が存在する場合
            value = row[1]  # 2列目のデータを取得
            for char in value:  # 各値を1文字ずつ取り出す
                if char.isdigit():  # 数字のみを対象とする
                    digits.append(char)

# 出現頻度の計算
frequency = Counter(digits)

# 0から9までの数字の出現回数を表示
print("数字の出現回数:")
for digit in range(10):  # 0～9の順で表示
    print(f"{digit}: {frequency[str(digit)]}")
