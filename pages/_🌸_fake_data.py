# Done by Muench
import streamlit as st
import time
from faker import Faker
import pandas as pd
from io import BytesIO
import random



timestr = time.strftime("%Y%m%d-%H%M%S")


def download_df(df):
    df = df
    col1, col2 = st.columns([1, 2])
    with col1:
        st.download_button(label="Download data as CSV",
                           data=make_downloadable_df_format(df, "csv"),
                           file_name="fake_dataset_{}.csv".format(timestr),
                           mime='text/csv',
                           key='download_as_csv',
                           help='click to download the above data as CSV'
                           )
    with col2:
        st.download_button(label="Download data as XLSX",
                           data=make_downloadable_df_format(df, "xlsx"),
                           file_name="fake_dataset_{}.xlsx".format(timestr),
                           mime='text/xlsx',
                           key='download_as_xlsx',
                           help='click to download the above data as XLSX(one sheet)'
                           )


# Fxn to Download Into A Format
def make_downloadable_df_format(df, format_type):
    if format_type == "csv":
        datafile = df.to_csv(index=False).encode('GB2312')
    elif format_type == "xlsx":
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format1 = workbook.add_format({'num_format': '0.00'})
        worksheet.set_column('A:A', None, format1)
        writer.save()
        datafile = output.getvalue()
    return datafile


@st.cache
# Generate A Customized Profile Per Locality
def generate_customized_profile(number, locale, fields, random_seed=200):
    custom_fake = Faker(locale)
    Faker.seed(random_seed)
    data = [custom_fake.profile(fields=fields) for i in range(number)]
    df = pd.DataFrame(data)
    return df





def main():
    st.set_page_config(page_title="假数据生成", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    st.title("假数据生成器")

    menu = st.sidebar.selectbox("菜单", ["主页", "客制化档案"])
    if menu == "主页":
        st.subheader("主页")

        locale = st.sidebar.multiselect("选择语言环境", options=["en_US", "zh_CN"], default="zh_CN")
        fake_data_type = st.sidebar.selectbox(label="选择假数据类型", options=['地址', '汽车', '银行', '条形码', '颜色', '公司', '信用卡'
                                                                        , '货币', '时间', '文件', '坐标', '网络', '图书', '职位', '文本'
                                                                        , '编码', '人物', '电话', '档案', '身份证', '用户代理'])
        index_fake = Faker(locale)

        generate_data_index_button = st.sidebar.button(label="生成")
        if generate_data_index_button:
            Faker.seed(random.randint(1,1000))

            if fake_data_type == "地址":
                st.write("地址：", index_fake.address())
                st.write("楼名：", index_fake.building_number())
                st.write("完整城市名：", index_fake.city())
                st.write("城市名字(不带市县)：", index_fake.city_name())
                st.write("城市后缀名：", index_fake.city_suffix())
                st.write("国家名称：", index_fake.country())
                st.write("国家编号：", index_fake.country_code(representation="alpha-2"))
                st.write("地区：", index_fake.district())
                st.write("邮编：", index_fake.postcode())
                st.write("省：", index_fake.province())
                st.write("街道地址：", index_fake.street_address())
                st.write("街道名称：", index_fake.street_name())
                st.write("街道后缀名：", index_fake.street_suffix())

            elif fake_data_type == "汽车":
                st.write("牌照：", index_fake.license_plate())

            elif fake_data_type == "银行":
                st.write("银行所属国家：", index_fake.bank_country())
                st.write("基本银行账号：", index_fake.bban())
                st.write("国际银行代码：", index_fake.iban())

            elif fake_data_type == "条形码":
                st.write("EAN条形码：", index_fake.ean(length=13))
                st.write("EAN13条形码：", index_fake.ean13())
                st.write("EAN8条形码：", index_fake.ean8())

            # https://zhuanlan.zhihu.com/p/422182497


    elif menu == "客制化档案":
        st.subheader("客制化档案假数据")
        locale = st.sidebar.multiselect("选择语言环境", options=["en_US", "zh_CN"], default="zh_CN")

        row_number = st.sidebar.number_input("数据行数", 10, 10000)
        profile_options_list = ['username', 'name', 'sex', 'address', 'mail', 'birthdate', 'job', 'company', 'ssn',
                                'residence', 'current_location', 'blood_group', 'website']
        profile_fields = st.sidebar.multiselect(label="可选字段", options=profile_options_list,
                                                default=['username', 'name'])

        df = generate_customized_profile(row_number, locale, profile_fields)
        st.dataframe(df)
        download_df(df)




if __name__ == '__main__':
    main()