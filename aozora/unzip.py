import os
import zipfile

# 現在のディレクトリ
current_directory = os.getcwd()

# 現在のディレクトリ内のすべてのファイルを取得
files = os.listdir(current_directory)

# ZIP ファイルを見つけて展開
for file in files:
    if file.endswith('.zip'):  # ZIP ファイルか確認
        zip_path = os.path.join(current_directory, file)
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(current_directory)  # 現在のディレクトリに展開
                print(f"Extracted: {file}")
        except zipfile.BadZipFile:
            print(f"Failed to extract (Bad ZIP file): {file}")
