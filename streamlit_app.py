import streamlit as st
import pandas as pd
import base64
import openpyxl

data = st.file_uploader("上传数据", type=["csv", 'txt', 'xlsx', 'xls'])
if data is not None:
    st.write(data.name)
    st.write(data.type)
    if data.name[-3:] == "csv" or data.name[-3:] == "txt":
        df = pd.read_csv(data)
        st.dataframe(df)

    elif data.name[-3:] == "xls" or data.name[-4:] == "xlsx":
        df = pd.read_excel(data)
        data = base64.b64encode(data).decode('UTF-8')
        st.dataframe(df)

