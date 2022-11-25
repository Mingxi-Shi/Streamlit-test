# Done by Muench
import base64

import numpy as np
from bs4 import BeautifulSoup
import requests
import streamlit as st
from rembg import remove
from PIL import  Image


def main():
    print(1)
    # url = "https://www.unicode.org/emoji/charts/full-emoji-list.html"
    # data = requests.get(url)
    # html = data.text
    # file = open(r"C:\Users\muench\Desktop\Full Emoji List, v15.0.html", "rb")
    # html = file.read()
    # bf = BeautifulSoup(html, "html.parser")
    # texts = bf.find_all('td', class_="chars")
    # a = bf.select("[class='chars']")

    # for item in a:
    #     item = str(item)
    #     print(item[18:19], end=' ')

    file = st.file_uploader(label="aaa",type=['png', 'jpg', 'bmp'])
    if file:
        a = Image.open(file)
        b = remove(a)
        st.image(b)


if __name__ == '__main__':
    main()