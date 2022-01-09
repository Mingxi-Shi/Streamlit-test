import streamlit as st

import pandas as pd
import numpy as np
from io import BytesIO


def page1():
    data = st.file_uploader("上传数据", type=["csv", 'txt', 'xlsx', 'xls'])
    if data is not None:
        if data.name[-3:] == "csv" or data.name[-3:] == "txt":
            df = pd.read_csv(data)
            st.dataframe(df.head(20))
        elif data.name[-3:] == "xls" or data.name[-4:] == "xlsx":
            df = pd.read_excel(data)
            st.dataframe(df.head(20))

        st.download_button(label="Download data as CSV",
                           data=convert2csv_df(df),
                           file_name='test.csv',
                           mime='text/csv',
                           help='click to download the above data as CSV')

        st.download_button(label="Download data as XLSX",
                           data=convert2excel_df(df),
                           file_name='test.xlsx',
                           mime='text/xlsx',
                           help='click to download the above data as XLSX(one sheet)'
                           # https://discuss.streamlit.io/t/download-xlsx-file-with-multiple-sheets-in-streamlit/11509/2
                           )
        st.write("每个功能模块都在container内")
        # 功能0：修改列数据类型
        with st.expander(label="功能0：修改数据类型", expanded=False):
            with st.container():
                df_columns_name = df.columns.to_list()
                modified_datatype = [' ' for _ in range(len(df.columns))]
                p1, p2 = st.columns([1, 5])
                with p1:
                    for i in range(len(df_columns_name)):
                        modified_datatype[i] = st.selectbox(label='选择列 [ ' + df_columns_name[i] + ' ]的数据类型',
                                                            options=['string', 'int64', 'float64', 'bool'], key=i,
                                                            index=judge_original_datatype(df, i))
                    temp = convert_df_columns_datatype(df, df_columns_name, modified_datatype)
                    if st.button("确认修改", key='modify_datatype'):
                        st.write('success')
                        df = temp

                with p2:
                    st.text('')
                    st.text('')
                    st.write(df.head(20))
        # 功能1：数据去空（不同条件）
        with st.expander(label="功能1：数据去空（不同条件）", expanded=False):
            with st.container():
                drop_na_row = st.radio(label="选择你要去空的方式", options=('去空(by row & any)', '去空(by row & all)'))
                if drop_na_row == '去空(by row & any)':
                    temp_na = drop_na_any(df)
                    st.write(temp_na)
                elif drop_na_row == '去空(by row & all)':
                    temp_na = drop_na_all(df)
                    st.write(temp_na)

                if st.button("确认去空"):
                    df = temp_na
                    st.write(df)


def page2():
    st.write("This is page2")


def page3():
    st.write("This is page3")


def page4():
    st.write("This is page4")


def page5():
    st.write("This is page5")


def page6():
    st.write("This is page6")


def page7():
    st.write("This is page7")


def page8():
    st.write("This is page8")


def page9():
    st.write("This is page9")


def page10():
    st.write("This is page10")


def pageExample():
    st.write(1)


# 转换格式函数csv
def convert2csv_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('GB2312')


# 转换格式函数xlsx
def convert2excel_df(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def judge_original_datatype(df, i):
    index = 0
    df_columns_name = df.columns.to_list()
    if df[df_columns_name[i]].dtype == 'string':
        index = 0
    elif df[df_columns_name[i]].dtype == 'int64':
        index = 1
    elif df[df_columns_name[i]].dtype == 'float64':
        index = 2
    elif df[df_columns_name[i]].dtype == 'bool':
        index = 3
    return index


def convert_df_columns_datatype(df, cols, types):
    df_columns_name = df.columns.to_list()
    for i in range(len(cols)):
        if df[cols[i]].dtype == 'object':
            if types[i] == 'int64' or types == 'float64':
                st.write('列 [ ', cols[i], ' ] 不能修改为', types[i], '型')
                df[cols[i]] = df[cols[i]].astype('string')
        else:
            df[cols[i]] = df[cols[i]].astype(types[i])
    return df


def drop_na_any(df):
    st.write('success')
    df = df.dropna(axis=0, how='any', subset=list(df.keys()))
    return df


def drop_na_all(df):
    st.write('success')
    df = df.dropna(axis=0, how='all', subset=list(df.keys()))
    return df
