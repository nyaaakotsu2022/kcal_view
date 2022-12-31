import streamlit as st
import app2

def main():
    st.title("（仮）オンラインヘルプ")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**良い例**")
        st.image("Ok.png")
        st.markdown("- 単体の写真")
        st.markdown("- 料理が分かりやすく映っている")
    
    with col2:
        st.markdown("**悪い例**")
        st.image("NG.png", use_column_width=True)
        st.markdown("- 複数の料理が映っている写真")
        st.markdown("- 料理が分かりにくい")
    
    with col3:
        st.markdown("\n  ")
        st.image("No.jpg", use_column_width=True)