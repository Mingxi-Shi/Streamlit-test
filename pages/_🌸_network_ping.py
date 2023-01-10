# Done by Muench
import streamlit as st

def main():
    st.set_page_config(page_title="ping命令", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    st.text(r'for /f %d in (ip.txt) do (ping %d -n 4 && echo %d>>tong.txt || echo %d>>butong.txt)')

if __name__ == '__main__':
    main()