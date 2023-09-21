# Streamlitライブラリをインポート
import streamlit as st
import random

st.title("おみくじアプリ")
if st.button("おみくじを引く"):
    results=["ロシア","北朝鮮","エリトリア","アフガニスタン","ミャンマー","イエメン"]
    result=random.choice(results)
    st.write(f"結果：{result}")
    

    



