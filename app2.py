import streamlit as st
from PIL import Image
import help2
import result2

# 定数
CALORIE = {"オムライス" : 850, "カレーライス" : 859, "タラコパスタ": 742}
MENU = ["メイン", "使い方"]
TYPECHECK = ["image/jpeg", "image/png", "image/heic"]

def upload() -> None: return st.file_uploader("画像を選択してください。")   #, type='jpg'

def app_display(foodpicture) -> None: st.image(foodpicture, caption='元画像',use_column_width=True)
# def changeto_jpg(foodpicture): pass

# 正しい画像ファイルかの確認
def EXTENSIONCHECK(extension):
    for i in TYPECHECK:
        if i in extension:
            return True
    return False

def main() -> None:
    select = st.sidebar.selectbox("main", MENU)
    if select == "使い方":
        help2.main()
    else:
        st.title("カロビュー")
        foodpicture = upload()

        # 画像がアップロードされたら元画像を出力。
        if foodpicture is not None:
            if EXTENSIONCHECK(str(foodpicture)):
                #foodpicture = Image.open(foodpicture)
                #app_display(foodpicture)
                foodpicture2 = Image.open(foodpicture)
                app_display(foodpicture2)
            else:
                st.error('このファイルは使用できません。', icon="🚨")
        number = st.radio("何人前？", ["1人前", "2人前", "3人前", "4人前"])
        
        # 表示ボタンが押されたら結果を表示する。
        if st.button("表示"):
            #result2.result_display(foodpicture)
            result2.check_photo_str(foodpicture, number)
            #result2.result_kcal(result2.result_serving(number))

if __name__ == '__main__': main()