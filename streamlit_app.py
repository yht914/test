# Streamlitライブラリをインポート
# 世界の首都のリスト
capitals = {
    "日本": "東京",
    "アメリカ": "ワシントンD.C.",
    "イギリス": "ロンドン",
    "フランス": "パリ",
    "ドイツ": "ベルリン",
    "中国": "北京",
    "インド": "ニューデリー",
    "ブラジル": "ブラジリア",
    "ロシア": "モスクワ",
}

# ランダムな国名を取得
random_country = list(capitals.keys())[random.randint(0, len(capitals) - 1)]

# ランダムに選択された首都を表示
print("ランダムに選択された首都は、" + capitals[random_country] + "です。")

    



