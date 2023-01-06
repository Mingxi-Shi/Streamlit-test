import streamlit as st
import pandas as pd
import numpy as np


def upload(answer):
    st.write(answer)


def main():
    data = pd.read_excel('data/question.xlsx')

    st.dataframe(data)

    # for index, row in data.iterrows():
    #     st.write("问题：", row[0])
    #     st.button(label="选项A："+row[1], on_click=upload(row[1]))
    #     st.button(label="选项B："+row[2], on_click=upload(row[2]))
    #     st.button(label="选项C："+row[3], on_click=upload(row[3]))
    #     st.button(label="选项D："+row[4], on_click=upload(row[4]))

    # for i in data.index:
    #     st.write(data.loc[i])

    if 'i' not in st.session_state:
        st.session_state.i = 0
    if st.session_state.i < len(data) and st.button("下一题"):
        st.write(data.loc[st.session_state.i])
        st.session_state.i = st.session_state.i + 1

    c1r1, c2r1, c3r1, c4r1 = st.columns([1, 1, 1, 1])
    with c1r1:
        select_A = st.button(label="选项A")
    with c2r1:
        select_B = st.button(label="选项B")
    with c3r1:
        select_C = st.button(label="选项C")
    with c4r1:
        select_D = st.button(label="选项D")

    if st.button("重新开始"):
        st.session_state.i = 0

    # for i in range(len(data)):
    #     st.write(data.loc[i])


if __name__ == '__main__':
    main()