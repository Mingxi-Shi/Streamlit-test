import streamlit as st
import pandas as pd


def main():
    st.set_page_config(page_title="icons_2", page_icon="🍔", layout="wide")

    sysmenu = '''
                      <style>
                      #MainMenu {visibility:hidden;}
                      footer {visibility:hidden;}
                      '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    df = pd.read_excel('./resources/emoji/emoji.xlsx')

    st.table(df)


if __name__ == '__main__':
    main()