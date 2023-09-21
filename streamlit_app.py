# Streamlitライブラリをインポート
import streamlit as st

# 西側諸国の国名をリストに格納
western_countries = ["アメリカ", "イギリス", "フランス", "ドイツ", "トルコ", "日本", "韓国", "イスラエル", "サウジアラビア"]

# ランダムな国名を取得
random_country = western_countries[random.randint(0, len(western_countries) - 1)]

# アプリのUIを作成
st.title("ランダムな西側諸国の国")
st.write("ランダムに選択された国は、" + random_country + "です。")
    

    



