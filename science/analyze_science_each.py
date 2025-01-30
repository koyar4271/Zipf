import MeCab
import collections
import csv
import glob
import os

# MeCabのタグ付け器を初期化
m = MeCab.Tagger('-Ochasen')

# 現在のディレクトリ内のすべてのテキストファイルを取得
text_files = glob.glob("*.txt")

# 出力ファイルの初期化
output_file = 'word_frequencies.csv'

# CSV出力準備
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # ヘッダー行を作成
    header = []
    for file_name in text_files:
        header.extend([file_name, "単語", "頻度"])
    writer.writerow(header)

    # 最大行数を取得するための処理
    file_word_counts = []
    for file_name in text_files:
        try:
            with open(file_name, 'r', encoding='shift_jis') as f:  # Shift_JISで読み込み
                text = f.read()  # ファイル終端まで全て読み込む

            # 出現頻度をカウントするためのCounter
            c = collections.Counter()

            # MeCabで解析
            node = m.parseToNode(text)
            while node:
                hinshi = node.feature.split(",")[0]  # 品詞を取得
                if hinshi in ["名詞", "動詞", "形容詞"]:  # 対象品詞を確認
                    origin = node.feature.split(",")[6]  # 原形を取得
                    if origin != '*':  # 原形が有効な場合のみ追加
                        c[origin] += 1
                node = node.next

            # 単語ごとの頻度を格納
            sorted_words = c.most_common()
            file_word_counts.append(sorted_words)

        except FileNotFoundError:
            print(f"ファイル {file_name} が見つかりませんでした。")
            file_word_counts.append([])
        except UnicodeDecodeError:
            print(f"ファイル {file_name} の文字コードが異なる可能性があります。")
            file_word_counts.append([])
        except Exception as e:
            print(f"ファイル {file_name} の処理中にエラーが発生しました: {e}")
            file_word_counts.append([])

    # 最大行数を取得
    max_rows = max(len(words) for words in file_word_counts)

    # 各ファイルのデータを行単位でCSVに書き込む
    for i in range(max_rows):
        row = []
        for words in file_word_counts:
            if i < len(words):
                word, count = words[i]
                row.extend(["", word, count])
            else:
                row.extend(["", "", ""])
        writer.writerow(row)

print(f"単語出現頻度は {output_file} に出力されました。")