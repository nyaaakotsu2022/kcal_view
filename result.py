import streamlit as st

# 定数
CALORIE = {"オムライス" : 850, "カレーライス" : 859, "タラコパスタ": 742}
VALUE = {"1人前" : 1, "2人前" : 2, "3人前" : 3, "4人前" : 4}

# N人前のカロリーを返す。
@st.cache
def result_serving(X: int) -> None:
    return CALORIE["オムライス"] * VALUE[X]

# カロリーを出力。
def result_kcal(number: int) -> None:
    return st.text('{}{}'.format(number, "kcalです。"))

# 処理した画像を出力。
def result_display(foodpicture) -> None:
    # 画像処理するコード入れて、処理した画像を出力
    return st.image(foodpicture, caption='オムライスの出力結果です。',use_column_width=True)