# Done by Muench
import streamlit as st
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np


def get_stopwords():
    with open('./data/cn_stopwords.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        text_list = text.split(';\n')
        s = set(text_list)
    return s


def remove_stopwords(words):
    return [word for word in words if words not in get_stopwords()]


def main():
    st.set_page_config(page_title="词云图", page_icon="🌸", layout="wide")

    sysmenu = '''
                      <style>
                      #MainMenu {visibility:hidden;}
                      footer {visibility:hidden;}
                      '''
    st.markdown(sysmenu, unsafe_allow_html=True)


    colormap_list = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu',
                     'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r',
                     'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired',
                     'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn',
                     'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu',
                     'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
                     'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r',
                     'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd',
                     'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r',
                     'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r',
                     'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare',
                     'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r',
                     'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r',
                     'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r',
                     'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r',
                     'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r',
                     'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket',
                     'rocket_r',
                     'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20',
                     'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r',
                     'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag',
                     'vlag_r', 'winter', 'winter_r']

    # 载入文本 1.文本框 2.文本文件txt
    load_text_way = st.radio(label="选择载入文本方式", options=('文本框', '上传文本文件'))
    if load_text_way == '文本框':
        text = st.text_area(label="输入文本", placeholder="Type Here")
    elif load_text_way == '上传文本文件':
        text_file = st.file_uploader("上传文本文件", type=['txt'])
        text = ""
        if text_file is not None:
            text = text_file.getvalue().decode('utf-8')

    if text:
        txt = jieba.cut(text)  # 使用jieba分词
        txt = remove_stopwords(txt)
        txt = "/".join(txt)

        font_names = []
        for files in os.listdir('resources/fonts'):  # 用os库获取文件夹下所有文件名
            font_names.append(files)
        default_font_color = st.sidebar.checkbox(label="统一字体颜色")
        col1, col2, col3 = st.sidebar.columns([4, 2, 6])
        with col1:
            if default_font_color:
                font_color = st.color_picker(label='字体颜色', value='#FFFFFF')
            else:
                font_color = st.selectbox(label="颜色图", options=colormap_list)
        with col2:
            background_color = st.color_picker(label='背景颜色', value='#000000')
        with col3:
            font_type = st.selectbox(label="字体类型", options=font_names)

        col4, col5 = st.sidebar.columns([2, 1])
        with col4:
            font_max_size = st.slider(label='字体大小', min_value=1, max_value=100, value=50)
        with col5:
            word_margin = st.slider(label='单词间隔', min_value=1, max_value=30, value=2)

        generate_way = st.sidebar.radio(label="选择你要生成的方式", options=('默认', '选择或上传图片作为背景'))
        if generate_way == '默认':
            col6, col7 = st.sidebar.columns([1, 1])
            with col6:
                image_width = st.slider(label='画布宽度', min_value=1, max_value=400, value=400)
            with col7:
                image_height = st.slider(label='画布高度', min_value=1, max_value=400, value=200)
            if default_font_color:
                wc = WordCloud(font_path='resources/fonts/' + font_type, width=image_width, height=image_height,
                               margin=word_margin,
                               background_color=background_color, max_font_size=font_max_size,
                               color_func=lambda *args, **kwargs: font_color)
            else:
                wc = WordCloud(font_path='resources/fonts/' + font_type, width=image_width, height=image_height,
                               margin=word_margin,
                               background_color=background_color, max_font_size=font_max_size, colormap=font_color)
            # wc.generate(txt)  # 导入字体
            wc.generate_from_text(txt)

            fig, ax = plt.subplots()

            plt.imshow(wc)  # 以图片的形式显示词云
            # plt.imshow(wc, interpolation='bilinear')  # 以图片的形式显示词云
            plt.axis("off")  # 关闭图像坐标系
            st.pyplot(fig)  # 显示图片

        elif generate_way == '选择或上传图片作为背景':
            selected_way = st.sidebar.radio(label="选择方式", options=('内置图片', '上传图片'))
            if selected_way == "内置图片":
                bg_img = []
                for files in os.listdir('resources/images/wordcloud'):
                    bg_img.append(files)
                background_image = st.selectbox(label="选择图片", options=bg_img)
                image = Image.open('resources/images/wordcloud/' + background_image)

            elif selected_way == "上传图片":
                background_image = st.sidebar.file_uploader(label="上传词云图背景", type=['jpg', 'png', 'jpeg'],
                                                            key='page8_file_upload_2')
                if background_image:
                    image = Image.open(background_image)  # 初始化自定义背景图

            if background_image is not None:

                graph = np.array(image)  # 图像数据化
                if default_font_color:
                    wc = WordCloud(font_path='resources/fonts/' + font_type, margin=word_margin,
                                   background_color=background_color,
                                   max_font_size=80, mask=graph, color_func=lambda *args, **kwargs: font_color)
                else:
                    wc = WordCloud(font_path='resources/fonts/' + font_type, margin=word_margin,
                                   background_color=background_color,
                                   max_font_size=80, mask=graph, colormap=font_color)
                image_color = ImageColorGenerator(graph)  # 获得背景图的颜色值
                wc.generate(txt)  # 导入字体

                fig, ax = plt.subplots()
                plt.imshow(wc)  # 以图片的形式显示词云
                # plt.imshow(wc, interpolation='bilinear')  # 以图片的形式显示词云
                plt.axis("off")  # 关闭图像坐标系
                st.pyplot(fig)  # 显示图片


if __name__ == '__main__':
    main()