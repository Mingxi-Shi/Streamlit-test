import streamlit as st


def main():
    st.set_page_config(page_title="Muench\'s Tools Page",
                       page_icon="🐯",
                       layout="wide",
                       initial_sidebar_state="auto",
                       menu_items={'About': None}
                       )
    st.set_option('deprecation.showPyplotGlobalUse', False)

    hide_menu_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_menu_style, unsafe_allow_html=True)  # 隐藏网页右上角的菜单


if __name__ == '__main__':
    main()
