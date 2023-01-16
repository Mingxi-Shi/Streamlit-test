# done by Muench
# Creation Date: 2022/6/8 16:07
# -*- coding:utf-8 -*-
import base64
from Crypto.Cipher import AES
import streamlit as st


# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密
def encrypt(plaintext, public_key):
    text = base64.b64encode(plaintext.encode('utf-8')).decode('ascii')
    # 初始化加密器
    aes = AES.new(add_to_16(public_key), AES.MODE_ECB)
    # 先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    # 用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes

    return encrypted_text


# 解密
def decrypt(ciphertext, private_key):
    # 初始化加密器
    aes = AES.new(add_to_16(private_key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(ciphertext.encode(encoding='utf-8'))
    #
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8') # 执行解密密并转码返回str
    decrypted_text = base64.b64decode(decrypted_text.encode('utf-8')).decode('utf-8')
    return decrypted_text


def main():
    st.set_page_config(page_title="文本加密解密", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    plaintext = st.text_input(label="输入明文")
    public_key = st.text_input(label="输入公钥")
    if plaintext and public_key:
        st.write(encrypt(plaintext=plaintext, public_key=public_key))

    ciphertext = st.text_input(label="输入密文")
    private_key = st.text_input(label="输入密钥")
    if ciphertext and private_key:
        try:
            st.write(decrypt(ciphertext=ciphertext, private_key=private_key))
        except ValueError as e:
            st.write("错误的密文或密钥")


if __name__ == '__main__':
    main()
