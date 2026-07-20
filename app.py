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
    
#投資前に見るべき観点を確認させるチェック項目
st.subheader("確認した項目")

understands_business = st.checkbox("企業の主な事業内容を理解している")
checked_financials = st.checkbox("直近の業績や決算を確認した")
checked_risks = st.checkbox("リスク要因を確認した")
compared_competitors = st.checkbox("競合企業と比較した")

missing_checks = []

if not understands_business:
    missing_checks.append("企業の主な事業内容")

if not checked_financials:
    missing_checks.append("直近の業績や決算")

if not checked_risks:
    missing_checks.append("リスク要因")

if not compared_competitors:
    missing_checks.append("競合企業との違い")

if missing_checks:
    st.subheader("追加で確認すべきこと")

    for item in missing_checks:
        st.write(f"- {item}")
else:
    st.success("基本的な確認項目は一通り確認できています。")

#確認済みの数を表示
check_results = [
    understands_business,
    checked_financials,
    checked_risks,
    compared_competitors,
]

checked_count = 0

for check in check_results:
    if check:
        checked_count = checked_count + 1

total_checks = len(check_results)  #len() は、Pythonで 中身の数を数える関数

st.write(f"{total_checks}項目中{checked_count}項目を確認済みです。")


if checked_count <= 1:
    st.warning(
        "確認できている項目が少ないため、投資判断の前に基本情報をもう少し確認する必要があります。"
    )
elif checked_count < total_checks:
    st.info(
        "いくつかの基本項目は確認できていますが、未確認の項目も残っています。追加確認項目を見直してみてください。"
    )
else:
    st.success(
        "基本的な確認項目は一通り確認できています。情報源の偏りもあわせて確認しましょう。"
    )