import streamlit as st

def main():
    st.title("オンラインヘルプ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**良い例**")
        st.image("image\Ok.png")
        st.markdown("- 単体の写真")
        st.markdown("- 料理が分かりやすく映っている")
    
    with col2:
        st.markdown("**悪い例**")
        st.image(r"image\NG.png", use_column_width=True)
        st.markdown("- 複数の料理が映っている写真")
        st.markdown("- 料理が分かりにくい")
    
    with col3:
        st.markdown("lll")
        st.image(r"image\No.png", use_column_width=True)