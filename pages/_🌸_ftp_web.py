# Done by Muench
import streamlit as st
import ftplib
from ftplib import error_perm


def ftp_upload():

    file = st.file_uploader("请选择要上传的文件", accept_multiple_files=True)

    if file is not None:
        if len(file) > 0:
            file_name_list = []
            for m in range(len(file)):
                file_name_list.append(file[m].name)
            with st.expander("点击查看待上传的文件列表"):
                st.write(file_name_list)

            c1, c2 = st.columns(2)
            with c1:
                ftp_host = st.text_input("请输入FTP服务器IP")
                ftp_port = st.number_input("请输入服务器端口号", value=21)
            with c2:
                ftp_username = st.text_input("请输入FTP用户名")
                ftp_password = st.text_input("请输入FTP用户密码")

            if len(ftp_host) > 0 and ftp_port > 0 and len(ftp_username) > 0 and len(ftp_password) > 0:
                ftp = ftplib.FTP(timeout=30)
                ftp.encoding = 'GBK'
                ftp.connect(ftp_host, int(ftp_port))
                try:
                    ftp.login(ftp_username, ftp_password)
                    if ftp.getwelcome().startswith("220"):
                        st.success("连接FTP服务器成功！")

                        #ftp.cwd("FTP")
                        #ftp.mkd("新上传的文件")
                        #ftp.cwd("新上传的文件")
                        with st.form("FTP上传"):
                            submitted = st.form_submit_button("点我开始上传文件")
                            if submitted:
                                bar = st.progress(0)
                                if len(file_name_list) > 0:
                                    for x in range(len(file_name_list)):
                                        ftp.storbinary("STOR " + str(file_name_list[x]), file[x], blocksize=8192)
                                    bar.progress(100)
                                    st.success("上传完成！")
                                    with st.expander("点击查看上传成功的文件列表"):
                                        st.write(ftp.nlst())
                        ftp.quit()
                except error_perm:
                    st.error("连接FTP失败，请检查输入信息是否正确！")


def ftp_download():

    c1, c2 = st.columns(2)
    with c1:
        ftp_host = st.text_input("请输入FTP服务器IP")
        ftp_port = st.number_input("请输入服务器端口号", value=21)
    with c2:
        ftp_username = st.text_input("请输入FTP用户名")
        ftp_password = st.text_input("请输入FTP用户密码")

    if len(ftp_host) > 0 and ftp_port > 0 and len(ftp_username) > 0 and len(ftp_password) > 0:
        ftp = ftplib.FTP(timeout=30)
        ftp.connect(ftp_host, int(ftp_port))
        try:
            ftp.login(ftp_username, ftp_password)
            if ftp.getwelcome().startswith("220"):
                st.success("连接FTP服务器成功！")
                #ftp.cwd("FTP")
                with st.expander("查看FTP服务器上文件信息"):
                    ftp.encoding = 'GBK'
                    st.write(ftp.nlst())

                with st.form("FTP下载"):
                    file_wait_download = st.multiselect("请选择要下载的文件", ftp.nlst())
                    local_save_path = st.text_input("请输入本地用来保存下载文件的文件夹路径")
                    submitted = st.form_submit_button("点我开始下载文件")
                    if submitted:
                        bar = st.progress(0)
                        if len(file_wait_download) > 0:
                            if len(local_save_path) > 0:
                                for x in range(len(file_wait_download)):
                                    with open(local_save_path + "\\" + str(file_wait_download[x]), "wb") as fp:
                                        ftp.retrbinary("RETR " + str(file_wait_download[x]), fp.write)
                                bar.progress(100)
                                st.success("下载完成！")

                ftp.quit()
        except error_perm:
            st.error("连接FTP失败，请检查输入信息是否正确！")
    else:
        st.warning("您还有FTP服务器的连接信息没有完整填写！")


def main():

    st.set_page_config(page_title="网页版FTP的上传下载", page_icon="🌸", layout="wide")
    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            .stProgress > div > div > div > div {
            background-image:linear-gradient(to right, #454584, #00ccff);
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    selected_model = st.sidebar.radio(label="选择操作", options=["上传", "下载"])
    if selected_model == "上传":
        ftp_upload()
    elif selected_model == "下载":
        ftp_download()


if __name__ == '__main__':
    main()
