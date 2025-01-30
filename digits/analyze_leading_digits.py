import os
from collections import Counter
import re

def count_leading_digits_in_files(file_list):
    # 最上位桁をカウントするための辞書
    leading_digit_counter = Counter()

    for file_name in file_list:
        if not os.path.exists(file_name):
            print(f"File not found: {file_name}")
            continue
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                # 数字列を抽出
                numbers = re.findall(r'\d+', content)
                # 数字列の最上位桁を抽出してカウント
                leading_digits = [num[0] for num in numbers if num]
                leading_digit_counter.update(leading_digits)
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")

    # 出現回数を表示
    print("Leading digit counts across all files:")
    for digit in range(10):
        print(f"{digit}: {leading_digit_counter[str(digit)]}")

# 使用例
file_list = ['word_frequencies.csv']  # 調べるファイル名をリストで指定
count_leading_digits_in_files(file_list)
