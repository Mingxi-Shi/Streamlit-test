import streamlit as st
import pandas as pd

data = st.file_uploader("上传数据", type=["csv", 'txt', 'xlsx', 'xls'])
if data is not None:
    st.write(data.name)
    st.write(data.type)
    if data.name[-3:] == "csv" or data.name[-3:] == "txt":
        df = pd.read_csv(data)
        st.dataframe(df)

    elif data.name[-3:] == "xls" or data.name[-4:] == "xlsx":
        df = pd.read_excel(data)
        st.dataframe(df)

