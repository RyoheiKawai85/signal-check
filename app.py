#上から順番に実行される画面設計図

import streamlit as st
#Streamlitを使えるようにした。st はStreamlitを短く呼ぶための名前

st.set_page_config(
    page_title="SignalCheck",
    page_icon="📊",
)
#アプリの中身ではなく、ブラウザ上のページ設定を決める命令
#具体的には、ブラウザのタブに出る名前やアイコンを設定


st.title("SignalCheck")
#タイトルを表示する この画面が何の画面かを示す一番大きな見出し

st.write(
    "SignalCheckは、投資判断の前に情報源の偏りや確認不足に気づくためのリスク可視化ツールです。"
)
#本文・説明・結果表示などに利用する

st.warning(
    "このアプリは特定の銘柄の売買を推奨するものではありません。金融アドバイスではなく、判断材料を整理するための補助ツールです。"
)
#注意書きを目立つ形で表示する命令

#企業名・銘柄名の入力欄
st.header("診断フォーム")

company_name = st.text_input("企業名または銘柄名を入力してください")

if company_name:
    st.write(f"入力された企業名・銘柄名: {company_name}")
    #f は、文字列の中に変数の中身を埋め込むための印

#投資を考えた理由を書く欄
reason = st.text_area("投資を考えた理由を書いてください")

if reason:
    st.write("投資を考えた理由:")
    st.write(reason)


information_sources = st.multiselect(
    "参考にした情報源を選んでください",
    [
        "SNS",
        "YouTube",
        "ニュース記事",
        "友人・知人",
        "企業IR",
        "決算資料",
        "株価チャート",
        "配当利回り",
        "アナリストレポート",
        "その他",
    ],
)

if information_sources:
    st.write("参考にした情報源:")
    st.write(information_sources)

#簡単な 情報源の偏りチェック
'''casual_sources
手軽に得られるが、偏りやすい可能性がある情報源
formal_sources
企業や専門家が出していて、根拠を確認しやすい情報源'''
casual_sources = ["SNS", "YouTube", "友人・知人"]
formal_sources = ["企業IR", "決算資料", "アナリストレポート"]

selected_casual_sources = [
    source for source in information_sources if source in casual_sources
]

selected_formal_sources = [
    source for source in information_sources if source in formal_sources
]

if information_sources:
    st.subheader("情報源の偏りチェック")

    if selected_casual_sources and not selected_formal_sources:
        st.warning(
            "SNS、YouTube、友人・知人など、手軽に得られる情報に偏っている可能性があります。企業IRや決算資料なども確認してみてください。"
        )
    elif selected_formal_sources:
        st.success(
            "企業IR、決算資料、アナリストレポートなど、比較的根拠を確認しやすい情報源も含まれています。"
        )
    else:
        st.info(
            "選択した情報源をもとに、追加で確認すべき情報がないか考えてみましょう。"
        )