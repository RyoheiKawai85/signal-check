# 学習ノート

このファイルは、SignalCheckを開発しながら学んだ用語、考え方、コマンドの意味を整理するためのノートです。

目的は、コードをただ貼るのではなく、自分で再現できる理解を残すことです。

## app.py

`app.py` は、Streamlitアプリの入口になるPythonファイルです。

Streamlitでアプリを起動するときは、次のように実行します。

```powershell
py -m streamlit run app.py
```


## Streamlit

Streamlitは、Pythonだけで簡単なWebアプリを作るためのライブラリです。

通常、Webアプリを作るには、画面の構造を作るHTML、見た目を整えるCSS、画面の動きを作るJavaScriptなどを使う必要があります。

しかしStreamlitを使うと、Pythonのコードだけで、文章、見出し、入力欄、ボタン、表、グラフなどをブラウザ上に表示できます。

たとえば、次のように書きます。

```python
import streamlit as st

st.title("タイトル")
st.write("説明文")
st.button("診断する")
```
## git add

`git add` は、変更したファイルを次のcommitに含める準備をするコマンドです。

Gitには、作業フォルダ、ステージ、commit履歴という考え方があります。

```text
作業フォルダ
VSCodeで実際に編集している場所

ステージ
次のcommitに入れる変更を一時的に置く場所

commit履歴
正式に記録された変更
```

## Streamlitの画面構造整理

SignalCheckでは、入力フォームと診断結果を分けて表示するために、`st.divider()`、`st.header()`、`st.container()`、`st.caption()` を使いました。

目的は、単に見た目を変えることではなく、画面上でもコード上でも「入力する場所」と「結果を見る場所」を分けることです。

## st.divider()

`st.divider()` は、画面に区切り線を表示する命令です。

```python
st.divider()
```