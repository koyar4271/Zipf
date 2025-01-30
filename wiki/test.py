import MeCab

mecab = MeCab.Tagger("-d /var/lib/mecab/dic/debian")
text = "私はPythonが大好きです。"
parsed_text = mecab.parse(text)

print(parsed_text)
