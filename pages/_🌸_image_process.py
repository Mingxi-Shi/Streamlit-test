# Done by Muench
# Done by Muench
import base64
import io

import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from aip import AipImageProcess
from streamlit_cropper import st_cropper


def cartonize_image(original_image):
    rgb_array_img = np.array(original_image.convert('RGB'))
    img = cv2.cvtColor(rgb_array_img, 1)
    gray = cv2.cvtColor(rgb_array_img, cv2.COLOR_BGR2GRAY)
    # Edges
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Color
    color = cv2.bilateralFilter(img, 9, 300, 300)
    # Cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


def cannize_image(original_image):
    rgb_array_img = np.array(original_image.convert('RGB'))
    img = cv2.cvtColor(rgb_array_img, 1)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    canny = cv2.Canny(img, 100, 150)
    return canny


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

    img_file = st.sidebar.file_uploader(label='上传图片', type=['png', 'jpg'])

    selected_model = st.sidebar.selectbox(label="选择模块", options=['图像裁剪', '图像特效', '图像增强', '图像水印'], label_visibility="collapsed")

    if selected_model == "图像裁剪":
        realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
        aspect_choice = st.sidebar.radio(label="纵横比", options=["1:1", "16:9", "4:3", "2:3", "自定义"])
        aspect_dict = {
            "1:1": (1, 1),
            "16:9": (16, 9),
            "4:3": (4, 3),
            "2:3": (2, 3),
            "自定义": None
        }
        aspect_ratio = aspect_dict[aspect_choice]

        if img_file:
            img = Image.open(img_file)

            if not realtime_update:
                st.write("Double click to save crop")
            # Get a cropped image from the frontend
            cropped_img = st_cropper(
                img,
                realtime_update=realtime_update,
                aspect_ratio=aspect_ratio,
                return_type='image'
            )

            # Manipulate cropped image at will
            st.write("Preview")
            _ = cropped_img.thumbnail((150, 150))
            st.image(cropped_img)

    elif selected_model == "图像特效":
        func_list_1 = ["黑白图像上色", "图像风格转换", "人像动漫化", "卡通化", "黑白简体化"]
        selected_func_1 = st.sidebar.selectbox(label="选择功能", options=func_list_1, label_visibility="collapsed")

        if img_file:
            if selected_func_1 == "黑白图像上色":
                res_image = client.colourize(image=img_file.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_1 == "图像风格转换":
                options_1 = {}
                style_list = ["cartoon", "pencil", "color_pencil", "warm", "wave", "lavender", "mononoke", "scream",
                              "gothic"]
                selected_option = st.sidebar.selectbox(label="选择风格", options=style_list, label_visibility="collapsed")
                options_1['option'] = selected_option
                res_image = client.styleTrans(image=img_file.getvalue(), options=options_1)
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_1 == "人像动漫化":
                options_2 = {}
                whether_mask = st.sidebar.checkbox(label="添加口罩")
                if whether_mask:
                    options_2['type'] = "anime_mask"
                    options_2['mask_id'] = st.sidebar.slider(label='口罩类型', min_value=1, max_value=8)
                res_image = client.selfieAnime(image=img_file.getvalue(), options=options_2)
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_1 == "卡通化":
                original_image = Image.open(img_file)
                res_image = cartonize_image(original_image)
                st.image(res_image)

            elif selected_func_1 == "黑白简体化":
                original_image = Image.open(img_file)
                res_image = cannize_image(original_image)
                st.image(res_image)

    elif selected_model == "图像增强":
        func_list_2 = ["灰度", "对比度", "亮度", "模糊度", "图像去雾", "图像对比度增强", "图像无损放大", "拉伸图像恢复", "图像修复", "图像清晰度增强", "天空分割"]
        selected_func_2 = st.sidebar.selectbox(label="选择功能", options=func_list_2, label_visibility="collapsed")

        if img_file:
            if selected_func_2 == "灰度":
                original_image = Image.open(img_file)
                rgb_array_img = np.array(original_image.convert('RGB'))
                img = cv2.cvtColor(rgb_array_img, 1)
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                st.text("处理灰度后:")
                st.image(gray_img)

            elif selected_func_2 == "对比度":
                original_image = Image.open(img_file)
                c_rate = st.sidebar.slider("Contrast", 0.5, 3.5)
                enhancer = ImageEnhance.Contrast(original_image)
                contrast_img = enhancer.enhance(c_rate)
                st.text("处理对比度后:")
                st.image(contrast_img)

            elif selected_func_2 == "亮度":
                original_image = Image.open(img_file)
                c_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                enhancer = ImageEnhance.Brightness(original_image)
                brightness_img = enhancer.enhance(c_rate)
                st.text("处理亮度后:")
                st.image(brightness_img)

            elif selected_func_2 == "模糊度":
                original_image = Image.open(img_file)
                rgb_array_img = np.array(original_image.convert('RGB'))
                blur_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                img = cv2.cvtColor(rgb_array_img, 1)
                blur_img = cv2.GaussianBlur(img, (11, 11), blur_rate)
                st.text("处理模糊度后:")
                st.image(blur_img)

            elif selected_func_2 == "图像去雾":
                res_image = client.dehaze(image=img_file.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "图像对比度增强":
                res_image = client.contrastEnhance(image=img_file.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "图像无损放大":
                res_image = client.imageQualityEnhance(image=img_file.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "拉伸图像恢复":
                res_image = client.stretchRestore(image=img_file.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "图像修复":
                # rectangle = [{'width': 92, 'top': 25, 'height': 36, 'left': 543}]
                # res_image = client.inpaintingByMask(image=img.getvalue(), rectangle=rectangle,options=None)
                #
                # st.image(base64.b64decode(res_image['image']))
                st.write("working...")

            elif selected_func_2 == "图像清晰度增强":
                res_image = client.imageDefinitionEnhance(image=img_file.getvalue())
                st.image(base64.b64decode(res_image['image']))

            elif selected_func_2 == "天空分割":
                st.write("working...")
                # res_image = client.skySeg(image=img_file.getvalue())
                # st.image(base64.b64decode(res_image['image']))

    if selected_model == "图像水印":
        marker_type = st.sidebar.radio(label="水印类型", options=['文字水印', '图片logo'], label_visibility="collapsed")
        if marker_type == "文字水印":
            if img_file:
                img = Image.open(img_file)
                col1, col2 = st.sidebar.columns([1, 1])
                with col1:
                    b = st.slider(label="x", min_value=1, max_value=img.size[0], value=img.size[0]-200, label_visibility="collapsed")
                with col2:
                    c = st.slider(label="y", min_value=1, max_value=img.size[1], value=img.size[1]-100, label_visibility="collapsed")
                col3, col4 = st.sidebar.columns([6, 1])
                with col3:
                    a = st.text_input(label="添加文字")
                with col4:
                    d = st.color_picker(label="颜色", value="#1687E2")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(font="./data/宋体.ttc", size=50)
                draw.text((b, c), text=a, fill=d, font=font)
                st.image(img)

        elif marker_type == "图片logo":
            if img_file:
                img = Image.open(img_file)
                col1, col2 = st.sidebar.columns([1, 1])
                with col1:
                    logo_file = st.file_uploader(label="上传logo", type=(['png']))
                with col2:
                    if logo_file:
                        logo = Image.open(logo_file)
                        logo_size_x = st.slider(label="size_x", min_value=1, max_value=logo.size[0], value=50, label_visibility="collapsed")
                        logo_size_y = st.slider(label="size_y", min_value=1, max_value=logo.size[1], value=50, label_visibility="collapsed")
                        logo_pos_x = st.slider(label="pos_x", min_value=1, max_value=img.size[0], value=img.size[0]-100, label_visibility="collapsed")
                        logo_pos_y = st.slider(label="pos_y", min_value=1, max_value=img.size[1], value=img.size[1]-100, label_visibility="collapsed")

                if logo_file:
                    logo = logo.resize((logo_size_x, logo_size_y))
                    t = Image.new(mode='RGBA', size=img.size, color=0)
                    t.paste(img)
                    lg_pos = (logo_pos_x, logo_pos_y)
                    t.paste(im=logo, box=lg_pos, mask=logo)
                    st.image(t)





if __name__ == '__main__':
    main()