from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# 設定頁面標題與佈局
st.set_page_config(
    page_title="經典復古掌機合輯",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 隱藏 Streamlit 上方工具列、頁尾與減少周圍留白，讓畫面更貼合掌機
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0rem;
            padding-left: 0.2rem;
            padding-right: 0.2rem;
            max-width: 480px;
        }
        #MainMenu, footer, header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# 使用 pathlib 確保在 Streamlit Cloud 執行時正確找到同目錄下的 index.html
html_path = Path(__file__).parent / "index.html"

if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        arcade_html = f.read()
    components.html(arcade_html, height=860, scrolling=False)
else:
    st.error("找不到 index.html，請確認該檔案已上傳至 GitHub 根目錄。")
