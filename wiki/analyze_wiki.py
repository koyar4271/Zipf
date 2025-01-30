import MeCab
import collections
import csv

# MeCabのタグ付け器を初期化
m = MeCab.Tagger('-Ochasen')

# 出現頻度をカウントするためのCounter
c = collections.Counter()

# ファイルを順次処理
for i in range(1, 101):  # 1から1731までのファイルに分割されている
    file_name = f'jawiki-latest-pages-articles.xml-{i}.txt'
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            print(f"prosessing : {file_name}")
            text = f.read()  # ファイル終端まで全て読み込む
        # MeCabで解析
        node = m.parseToNode(text)
        while node:
            hinshi = node.feature.split(",")[0]  # 品詞を取得
            if hinshi in ["名詞", "動詞", "形容詞"]:  # 対象品詞を確認
                origin = node.feature.split(",")[6]  # 原形を取得
                if origin != '*':  # 原形が有効な場合のみ追加
                    c[origin] += 1
            node = node.next

    except FileNotFoundError:
        print(f"ファイル {file_name} が見つかりませんでした。")

# 結果をCSVファイルに出力
output_file = 'word_frequencies_100files.csv'
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['単語', '出現回数'])  # ヘッダー行を追加
    writer.writerows(c.most_common())  # 全ての単語を出力

print(f"単語出現頻度は {output_file} に出力されました。")
