# 学習ノート

このファイルは、SignalCheckを開発しながら学んだ用語、考え方、コマンドの意味を整理するためのノートです。

目的は、コードをただ貼るのではなく、自分で再現できる理解を残すことです。

## app.py

`app.py` は、Streamlitアプリの入口になるPythonファイルです。

Streamlitでアプリを起動するときは、次のように実行します。

```powershell
py -m streamlit run app.py

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