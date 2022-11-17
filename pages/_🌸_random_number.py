import streamlit as st
import random


def gen_random_number(amount, min_num, max_num, whether_unique):
    if whether_unique == '唯一':
        result = set()
        while len(result) != amount:
            result.add(random.randint(min_num, max_num))
        result = list(result)
    else:
        result = []
        for i in range(amount):
            result.append(random.randint(min_num, max_num))

    random.shuffle(result)
    return result


def main():
    st.set_page_config(page_title="随机数生成", page_icon="🌸", layout="wide")

    sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    amount = st.number_input(label='数目', value=10)
    min_num = st.number_input(label='最小数', value=0)
    max_num = st.number_input(label='最大数', value=100)
    whether_unique = st.selectbox(label='选择是否为唯一随机数：', options=('唯一', '随便'))
    generate = st.button(label='点击生成')

    result = gen_random_number(amount, min_num, max_num, whether_unique)
    st.text(result)


if __name__ == '__main__':
    main()
