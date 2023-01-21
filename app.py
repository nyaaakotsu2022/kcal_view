import streamlit as st, webbrowser, result
from PIL import Image
from model.Italian.Italian import check_photo_Italian
from model.yousyoku.yousyoku import check_photo_yousyoku
from model.dezato_main import dezato_judge
from model.tyuka_main import tyuka_judge
from model.wasyoku_main import wasyoku_judge


# 定数
MENU = ["メイン", "使い方"]
TYPECHECK = ["image/jpeg", "image/png", "image/heic"]
GENRE = ["和食", "洋食", "中華", "イタリアン", "スイーツ"]
FLAGBOX = [False] * 2   # 画像、表示フラグ

def upload() -> None: return st.file_uploader("画像を選択してください。")

def app_display(foodpicture) -> None: st.image(foodpicture, use_column_width=True)

# 正しい画像ファイルかの確認
def EXTENSIONCHECK(extension) -> bool:
    for i in TYPECHECK:
        if i in extension:
            return True
    return False

def main() -> None:
    select = st.sidebar.selectbox("main", MENU)
    
    # ハンバーガーメニュー削除
    css = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    
    if select == "使い方":
        webbrowser.open("http://kcalhelp.html.xdomain.jp/")
    else:
        st.image("kcal_view_logo.png", width=300)
        col1, col2 = st.columns([3, 1])
        with col1:
            foodpicture = upload()
            option = st.selectbox("料理のジャンルを選択してください。", ("和食", "洋食", "中華", "イタリアン", "スイーツ"))

        # 画像がアップロードされたら、正しいファイルか確認。
        if foodpicture is not None:
            if EXTENSIONCHECK(str(foodpicture)):
                FLAGBOX[0] = True
            else:
                st.error("このファイルは使用できません。", icon="🚨")
        
        with col2:
            number = st.radio("何人前？", ["1人前", "2人前", "3人前", "4人前"])
        
        with st.container():
            try:
                if st.button("表示"):
                    if option == "和食":
                        ansname, anscal, anspro = wasyoku_judge(foodpicture, number)
                    elif option == "洋食":
                        ansname, anscal, anspro = check_photo_yousyoku(foodpicture, number)
                    elif option == "中華":
                        ansname, anscal, anspro = tyuka_judge(foodpicture, number)
                    elif option == "イタリアン":
                        ansname, anscal, anspro = check_photo_Italian(foodpicture, number)
                    elif option == "スイーツ":
                        ansname, anscal, anspro = dezato_judge(foodpicture, number)
                    FLAGBOX[1] = True
            except AttributeError:
                st.error("画像をアップロードしてください。", icon="🚨")
            except option not in set(GENRE):
                st.error("料理のジャンルを選択してください。", icon="🚨")
        
        if FLAGBOX[0]: app_display(Image.open(foodpicture))
        
        if FLAGBOX[0] and FLAGBOX[1]: result.show_result(ansname, anscal, anspro); result.show_chart(ansname)

if __name__ == '__main__': main()