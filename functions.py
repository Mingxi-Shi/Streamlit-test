from io import BytesIO
import streamlit as st
import pandas as pd


def page1():
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
