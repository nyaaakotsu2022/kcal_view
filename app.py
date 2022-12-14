import streamlit as st
from PIL import Image
import result

image = Image.open('test.png')
st.set_page_config(
    page_title="カロビュ―",
    page_icon=image,
    layout="wide",
    initial_sidebar_state="auto")

# 定数
CALORIE = {"オムライス": 850, "カレーライス": 859, "タラコパスタ": 742}
VALUE = {"1人前": 1, "2人前": 2, "3人前": 3, "4人前": 4}


def upload() -> None: return st.file_uploader("画像を選択してください。")  # , type='jpg'


def app_display(foodpicture) -> None: st.image(foodpicture,
                                               caption='元画像', use_column_width=True)
# def changeto_jpg(foodpicture): pass


def main() -> None:
    container = st.container()
    col1, col2 = st.columns(2)
    with container:
        headerimg = Image.open('kcal_view_logo.png')
        st.image(headerimg, use_column_width=False)

    with col1:
        foodpicture = upload()
        print(str(foodpicture))
        # foodpicture = changeto_jpg(foodpicture)

        # 画像がアップロードされたら元画像を出力。
        if foodpicture is not None:
            foodpicture = Image.open(foodpicture)
            app_display(foodpicture)
    with col2:
        number = st.radio("何人前？", ["1人前", "2人前", "3人前", "4人前"])

        # 表示ボタンが押されたら結果を表示する。
        if st.button("表示"):
            result.result_kcal(result.result_serving(number))
            result.result_display(foodpicture)


if __name__ == '__main__':
    main()
