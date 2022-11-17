from pythonping import ping
import streamlit as st

def main():
    st.set_page_config(page_title="测试1", page_icon="🌏", layout="wide")

    sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
    st.markdown(sysmenu, unsafe_allow_html=True)
    
    ip_str = st.text_area(label='输入ping的IP:', height=400)
    ip_list = [i for i in ip_str.split()]
    if st.button("开始ping"):
        for i in range(len(ip_list)):
            result = str(ping(ip_list[i], verbose=True))
            if result.count('Reply') == 4:
                st.write(ip_list[i], "  通")
            elif result.count('timed out') == 4:
                st.write(ip_list[i], "  不通")


if __name__ == '__main__':
    main()
