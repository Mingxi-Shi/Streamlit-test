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
            Faker.seed(random.randint(1, 1000))

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

            elif fake_data_type == "颜色":
                st.write("颜色名称：", index_fake.color_name())
                st.write("颜色十六进制值：", index_fake.hex_color())
                st.write("颜色RGB值：", index_fake.rgb_color())
                st.write("CSS颜色值：", index_fake.rgb_css_color())
                st.write("安全色：", index_fake.safe_color_name())
                st.write("安全色十六进制值：", index_fake.safe_hex_color())

            elif fake_data_type == "公司":
                st.write("商业用词：", index_fake.bs())
                st.write("妙句(口号)：", index_fake.catch_phrase())
                st.write("公司名称：", index_fake.company())
                st.write("公司名称前缀：", index_fake.company_prefix())
                st.write("公司名称后缀：", index_fake.company_suffix())

            elif fake_data_type == "信用卡":
                st.write("过期年月：", index_fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"))
                st.write("完整信用卡信息：", index_fake.credit_card_full(card_type=None))
                st.write("信用卡卡号：", index_fake.credit_card_number(card_type=None))
                st.write("信用卡提供商：", index_fake.credit_card_provider(card_type=None))
                st.write("信用卡安全码：", index_fake.credit_card_security_code(card_type=None))

            elif fake_data_type == "货币":
                st.write("加密货币代码+名称：", index_fake.cryptocurrency())
                st.write("加密货币代码：", index_fake.cryptocurrency_code())
                st.write("加密货币名称：", index_fake.cryptocurrency_name())
                st.write("货币代码+名称：", index_fake.currency())
                st.write("货币代码：", index_fake.currency_code())
                st.write("货币名称：", index_fake.currency_name())

            elif fake_data_type == "时间":
                st.write("AM或PM：", index_fake.am_pm())
                st.write("世纪：", index_fake.century())
                st.write("日期字符串(可设置格式和最大日期)：", index_fake.date(pattern="%Y-%m-%d", end_datetime=None))
                st.write("日期(可设置限定范围)：", index_fake.date_between(start_date="-30y", end_date="today"))
                st.write("日期(可设置最大日期)：", index_fake.date_object(end_datetime=None))
                st.write("出生日期：", index_fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=115))
                st.write("本世纪日期：", index_fake.date_this_century(before_today=True, after_today=False))
                st.write("本年代中的日期：", index_fake.date_this_decade(before_today=True, after_today=False))
                st.write("本月中的日期：", index_fake.date_this_month(before_today=True, after_today=False))
                st.write("本年中的日期：", index_fake.date_this_year(before_today=True, after_today=False))
                st.write("日期和时间：", index_fake.date_time(tzinfo=None, end_datetime=None))
                st.write("日期和时间(从001年1月1日到现在)：", index_fake.date_time_ad(tzinfo=None, end_datetime=None, start_datetime=None))
                st.write("日期时间(可设置限定范围)：", index_fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None))
                st.write("日期时间(可设置限定范围)：", index_fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None))
                st.write("本世纪中的日期和时间：", index_fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None))
                st.write("本年代中的日期和时间：", index_fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None))
                st.write("本年中的日期和时间：", index_fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
                st.write("本月中的日期和时间：", index_fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None))
                st.write("几号：", index_fake.day_of_month())
                st.write("星期几：", index_fake.day_of_week())
                st.write("未来日期：", index_fake.future_date(end_date="+30d", tzinfo=None))
                st.write("未来日期和时间：", index_fake.future_datetime(end_date="+30d", tzinfo=None))
                st.write("iso8601格式日期和时间：", index_fake.iso8601(tzinfo=None, end_datetime=None))
                st.write("第几月：", index_fake.month())
                st.write("月份名称：", index_fake.month_name())
                st.write("过去日期：", index_fake.past_date(start_date="-30d", tzinfo=None))
                st.write("过去日期和时间：", index_fake.past_datetime(start_date="-30d", tzinfo=None))
                st.write("时间(可设置格式和最大日期时间)：", index_fake.time(pattern="%H:%M:%S", end_datetime=None))
                st.write("时间间隔：", index_fake.time_delta(end_datetime=None))
                st.write("时间(可设置最大日期时间)：", index_fake.time_object(end_datetime=None))
                st.write("时间序列：", index_fake.time_series(start_date="-30d", end_date="now", precision=None, distrib=None, tzinfo=None))
                st.write("时区：", index_fake.timezone())
                st.write("UNIX时间戳：", index_fake.unix_time(end_datetime=None, start_datetime=None))
                st.write("某年：", index_fake.year())

            elif fake_data_type == "文件":
                st.write("文件扩展名：", index_fake.file_extension(category=None))
                st.write("文件名：", index_fake.file_name(category=None, extension=None))
                st.write("文件路径：", index_fake.file_path(depth=1, category=None, extension=None))
                st.write("MIME类型：", index_fake.mime_type(category=None))
                st.write("UNIX设备：", index_fake.unix_device(prefix=None))
                st.write("UNIX分区：", index_fake.unix_partition(prefix=None))

            elif fake_data_type == "坐标":
                st.write("坐标：", index_fake.coordinate(center=None, radius=0.001))
                st.write("纬度：", index_fake.latitude())
                st.write("经纬度：", index_fake.latlng())
                st.write("返回某个国家某地的经纬度：", index_fake.local_latlng(country_code="CN", coords_only=False))
                st.write("返回地球上某个位置的经纬度：", index_fake.location_on_land(coords_only=False))
                st.write("经度：", index_fake.longitude())

            elif fake_data_type == "网络":
                st.write("企业邮箱(ascii编码)：", index_fake.ascii_company_email())
                st.write("企业邮箱+免费邮箱(ascii编码)：", index_fake.ascii_email())
                st.write("免费邮箱(ascii编码)：", index_fake.ascii_free_email())
                st.write("安全邮箱(ascii编码)：", index_fake.ascii_safe_email())
                st.write("企业邮箱：", index_fake.company_email())
                st.write("域名：", index_fake.domain_name(levels=1))
                st.write("二级域名：", index_fake.domain_word())
                st.write("企业邮箱+免费邮箱：", index_fake.email())
                st.write("免费邮箱：", index_fake.free_email())
                st.write("免费邮箱域名：", index_fake.free_email_domain())
                st.write("主机名：", index_fake.hostname())
                st.write("图片URL：", index_fake.image_url(width=None, height=None))
                st.write("ipv4：", index_fake.ipv4(network=False, address_class=None, private=None))
                st.write("ipv4网络等级：", index_fake.ipv4_network_class())
                st.write("私有ipv4：", index_fake.ipv4_private(network=False, address_class=None))
                st.write("公共ipv4：", index_fake.ipv4_public(network=False, address_class=None))
                st.write("ipv6：", index_fake.ipv6(network=False))
                st.write("MAC地址：", index_fake.mac_address())
                st.write("安全邮箱：", index_fake.safe_email())
                st.write("URL中的slug：", index_fake.slug())
                st.write("顶级域名：", index_fake.tld())
                st.write("URI：", index_fake.uri())
                st.write("URI扩展：", index_fake.uri_extension())
                st.write("URI页：", index_fake.uri_page())
                st.write("URI路径：", index_fake.uri_path(deep=None))
                st.write("URL：", index_fake.url(schemes=None))
                st.write("用户名：", index_fake.user_name())

            elif fake_data_type == "图书":
                st.write("ISBN-10图书编号：", index_fake.isbn10(separator="-"))
                st.write("ISBN-13图书编号：", index_fake.isbn13(separator="-"))

            elif fake_data_type == "职位":
                st.write("职位：", index_fake.job())

            elif fake_data_type == "文本":
                st.write("单个段落：", index_fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))
                st.write("多个段落：", index_fake.paragraphs(nb=3, ext_word_list=None))
                st.write("单个句子：", index_fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
                st.write("多个句子：", index_fake.sentences(nb=3, ext_word_list=None))
                st.write("单个文本：", index_fake.text(max_nb_chars=200, ext_word_list=None))
                st.write("多个文本：", index_fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None))
                st.write("单个词语：", index_fake.word(ext_word_list=None))
                st.write("多个词语：", index_fake.words(nb=3, ext_word_list=None, unique=False))

            elif fake_data_type == "编码":
                st.write("二进制：", index_fake.binary(length=1024))
                st.write("布尔值：", index_fake.boolean(chance_of_getting_true=50))
                st.write("Md5：", index_fake.md5(raw_output=False))
                st.write("NULL+布尔值：", index_fake.null_boolean())
                st.write("密码：", index_fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
                st.write("SHA1：", index_fake.sha1(raw_output=False))
                st.write("SHA256：", index_fake.sha256(raw_output=False))
                st.write("UUID4：", index_fake.uuid4())

            elif fake_data_type == "人物":
                st.write("名字：", index_fake.first_name())
                st.write("名字(女)：", index_fake.first_name_female())
                st.write("名字(男)：", index_fake.first_name_male())
                st.write("名字(罗马文)：", index_fake.first_romanized_name())
                st.write("姓：", index_fake.last_name())
                st.write("姓(女)：", index_fake.last_name_female())
                st.write("姓(男)：", index_fake.last_name_male())
                st.write("姓(罗马文)：", index_fake.last_romanized_name())
                st.write("姓名：", index_fake.name())
                st.write("姓名(女)：", index_fake.name_female())
                st.write("姓名(男)：", index_fake.name_male())
                st.write("称谓：", index_fake.prefix())
                st.write("称谓(女)：", index_fake.prefix_female())
                st.write("称谓(男)：", index_fake.prefix_male())
                st.write("称谓(罗马文)：", index_fake.romanized_name())
                st.write("姓名后缀(中文不适用)：", index_fake.suffix())
                st.write("姓名后缀(中文不适用)(女)：", index_fake.suffix_female())
                st.write("姓名后缀(中文不适用)(男)：", index_fake.suffix_male())

            elif fake_data_type == "电话":
                st.write("完整手机号码(加了国家和国内区号)：", index_fake.msisdn())
                st.write("手机号：", index_fake.phone_number())
                st.write("区号：", index_fake.phonenumber_prefix())

            elif fake_data_type == "档案":
                st.write("档案(完整)：", index_fake.profile(fields=None, sex=None))
                st.write("档案(简单)：", index_fake.simple_profile(sex=None))

            elif fake_data_type == "身份证":
                st.write("身份证：", index_fake.ssn(min_age=18, max_age=90))

            elif fake_data_type == "用户代理":
                st.write("安卓：", index_fake.android_platform_token())
                st.write("Chrome：", index_fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899))
                st.write("FireFox：", index_fake.firefox())
                st.write("Ie：", index_fake.internet_explorer())
                st.write("ios：", index_fake.ios_platform_token())
                st.write("Linux：", index_fake.linux_platform_token())
                st.write("Linux处理器：", index_fake.linux_processor())
                st.write("Mac：", index_fake.mac_platform_token())
                st.write("Mac处理器：", index_fake.mac_processor())
                st.write("Opera：", index_fake.opera())
                st.write("Safari：", index_fake.safari())
                st.write("随机用户代理：", index_fake.user_agent())
                st.write("Windows：", index_fake.windows_platform_token())

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