import requests
from bs4 import BeautifulSoup
import csv

def get_market_cap(stock_code):
    url = f"https://finance.yahoo.co.jp/quote/{stock_code}.T"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error fetching data for {stock_code}")
        return None

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # 時価総額が含まれる場所を指定
        market_cap_tag = soup.find('span', class_='StyledNumber__value__3rXW DataListItem__value__11kV')
        market_cap_suffix_tag = soup.find('span', class_='StyledNumber__suffix__2SD5 DataListItem__suffix__3uht')
        
        if market_cap_tag and market_cap_suffix_tag:
            market_cap = market_cap_tag.get_text(strip=True)
            market_cap_suffix = market_cap_suffix_tag.get_text(strip=True)
            full_market_cap = market_cap + market_cap_suffix
            return full_market_cap
        else:
            print(f"時価総額の情報が見つかりませんでした: 銘柄コード {stock_code}")
            return None
    except Exception as e:
        print(f"Error parsing data for {stock_code}: {e}")
        return None

# 銘柄コードのリスト
stock_codes = ["7203", "9984", "8306"]

# CSVファイルに保存するデータ
market_caps = []

for stock_code in stock_codes:
    print(f"Processing: {stock_code}")
    market_cap = get_market_cap(stock_code)
    if market_cap:
        market_caps.append([stock_code, market_cap])
        print(f"取得成功: 銘柄コード {stock_code}, 時価総額: {market_cap}")
    else:
        print(f"時価総額の取得に失敗しました: 銘柄コード {stock_code}")

# データをCSVに保存
with open('japan_market_cap.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['銘柄コード', '時価総額'])
    writer.writerows(market_caps)

print("データをCSVに保存しました: japan_market_cap.csv")
