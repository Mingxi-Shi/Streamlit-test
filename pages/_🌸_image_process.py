# Done by Muench
import base64
import io

import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance
from aip import AipImageProcess


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def main():
    st.set_page_config(page_title="图片处理", page_icon="🌸", layout="wide")

    sysmenu = '''
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    st.title("图片处理")

    APP_ID = '28410890'
    API_KEY = 'T1XLiuoYEGKerVoU9yXCl46s'
    SECRET_KEY = 's2uuKO0FiMUIv65kIPG1ElR1k5QxYkn8'

    client = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)

    selected_model = st.sidebar.selectbox(label=" ", options=['图像特效', '图像增强'], label_visibility="collapsed")
    if selected_model == "图像特效":
        selected_func_1 = st.sidebar.selectbox(label=" ", options=["黑白图像上色", "图像风格转换", "人像动漫化"], label_visibility="collapsed")

        img = st.sidebar.file_uploader(label="上传图片", type=['jpg', 'png'], key="txtx")
        if img:
            if selected_func_1 == "黑白图像上色":
                res_image = client.colourize(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_1 == "图像风格转换":
                options_1 = {}
                style_list = ["cartoon", "pencil", "color_pencil", "warm", "wave", "lavender", "mononoke", "scream",
                              "gothic"]
                selected_option = st.sidebar.selectbox(label="", options=style_list, label_visibility="collapsed")
                options_1['option'] = selected_option
                res_image = client.styleTrans(image=img.getvalue(), options=options_1)
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_1 == "人像动漫化":
                options_2 = {}
                whether_mask = st.sidebar.checkbox(label="添加口罩")
                if whether_mask:
                    options_2['type'] = "anime_mask"
                    options_2['mask_id'] = st.sidebar.slider(label='口罩类型', min_value=1, max_value=8)
                res_image = client.selfieAnime(image=img.getvalue(), options=options_2)
                st.image(base64.b64decode(res_image['image']))

    elif selected_model == "图像增强":
        func_list = ["图像去雾", "图像对比度增强", "图像无损放大", "拉伸图像恢复", "图像修复", "图像清晰度增强", "天空分割"]
        selected_func_2 = st.sidebar.selectbox(label=" ", options=func_list, label_visibility="collapsed")

        img = st.sidebar.file_uploader(label="上传图片", type=['jpg', 'png'], key="txzq")
        if img:
            if selected_func_2 == "图像去雾":
                res_image = client.dehaze(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "图像对比度增强":
                res_image = client.contrastEnhance(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "图像无损放大":
                res_image = client.imageQualityEnhance(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "拉伸图像恢复":
                res_image = client.stretchRestore(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "图像修复":
                # rectangle = [{'width': 92, 'top': 25, 'height': 36, 'left': 543}]
                # res_image = client.inpaintingByMask(image=img.getvalue(), rectangle=rectangle,options=None)
                #
                # st.image(base64.b64decode(res_image['image']))
                st.write(1)

            elif selected_func_2 == "图像清晰度增强":
                res_image = client.imageDefinitionEnhance(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "天空分割":
                res_image = client.skySeg(image=img.getvalue())
                st.image(base64.b64decode(res_image['image']))


if __name__ == '__main__':
    main()