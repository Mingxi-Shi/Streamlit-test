# Done by Muench
import streamlit as st
from cryptography.fernet import Fernet


def main():
    st.set_page_config(page_title="文件加密解密", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    selected_model = st.sidebar.radio(label="选择操作", options=["加密", "解密"])

    if selected_model == "加密":

        yet_encrypt_file = st.file_uploader(label="上传未加密的文件", type=['txt', 'png', 'jpg'], key="yet_encrypt_file")

        if yet_encrypt_file:

            sslist = ['key', 'encrypt_file', 'download_name']
            for ss in sslist:
                if ss not in st.session_state:
                    st.session_state[ss] = ""

            if st.button("1.生成密钥并开始加密"):
                st.session_state.key = Fernet.generate_key()
                en_fernet = Fernet(st.session_state.key)
                st.session_state.encrypt_file = en_fernet.encrypt(yet_encrypt_file.getvalue())

                if yet_encrypt_file.name[-3:] == "jpg":
                    st.session_state.download_name = "encrypted_file.jpg"
                elif yet_encrypt_file.name[-3:] == "png":
                    st.session_state.download_name = "encrypted_file.png"
                elif yet_encrypt_file.name[-3:] == "txt":
                    st.session_state.download_name = "encrypted_file.txt"
                    st.success("成功")
            st.download_button(label='2.下载加密后的文件', data=st.session_state.encrypt_file,
                               file_name=st.session_state.download_name)
            # st.write(st.session_state.key)
            if st.download_button(label='3.下载密钥', data=st.session_state.key, file_name='encrypt_key.txt'):
                del st.session_state.key

    elif selected_model == "解密":

        yet_decrypt_file = st.file_uploader(label="上传已加密的文件", type=['txt', 'png', 'jpg'])
        decrypt_key = st.file_uploader(label="上传密钥", type=['txt'])
        if yet_decrypt_file and decrypt_key:

            decrypt_button = st.button(label="开始解密")
            if decrypt_button:
                de_fernet = Fernet(decrypt_key.getvalue())
                decrypted_file = de_fernet.decrypt(yet_decrypt_file.getvalue())

                st.success("成功")

                if yet_decrypt_file.name[-3:] == "jpg":
                    download_name = "decrypted_file.jpg"
                elif yet_decrypt_file.name[-3:] == "png":
                    download_name = "decrypted_file.png"
                elif yet_decrypt_file.name[-3:] == "txt":
                    download_name = "decrypted_file.txt"
                st.download_button(label='下载解密后的文件', data=decrypted_file, file_name=download_name)


if __name__ == '__main__':
    main()