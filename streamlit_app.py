import streamlit as st
import pandas as pd
import base64
import openpyxl
from io import BytesIO
from xlsxwriter import Workbook

# 转换格式函数csv
@st.cache
def convert2csv_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('GB2312')


# 转换格式函数xlsx
@st.cache
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


def main():
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


if __name__ == '__main__':
    main()

