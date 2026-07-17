import streamlit as st
#Streamlitを使えるようにした。st はStreamlitを短く呼ぶための名前

st.set_page_config(
    page_title="SignalCheck",
    page_icon="📊",
)

st.title("SignalCheck")

st.write(
    "SignalCheckは、投資判断の前に情報源の偏りや確認不足に気づくためのリスク可視化ツールです。"
)

st.warning(
    "このアプリは特定の銘柄の売買を推奨するものではありません。金融アドバイスではなく、判断材料を整理するための補助ツールです。"
)