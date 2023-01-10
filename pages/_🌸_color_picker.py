import random

import streamlit as st


def toggle_show():
    st.session_state.show = not st.session_state.show


def rgb_to_hex(rgb_color):
    r = hex(int(rgb_color[0]))[2:].zfill(2)
    g = hex(int(rgb_color[1]))[2:].zfill(2)
    b = hex(int(rgb_color[2]))[2:].zfill(2)
    hex_color = list([r, g, b])
    return hex_color


def hex_to_rgb(hex_color):
    r = int('0x' + hex_color[1:3], 16)
    g = int('0x' + hex_color[3:5], 16)
    b = int('0x' + hex_color[5:7], 16)
    rgb_color = list([r, g, b])
    return rgb_color


def rgb_to_hsl(rgb):
    sort_rgb = sorted(rgb)

    if sort_rgb[2] == sort_rgb[0]:
        h = 0
    elif sort_rgb[2] == rgb[0] and rgb[1] >= rgb[2]:
        h = round(60 * ((rgb[1] - rgb[2]) / (sort_rgb[2] - sort_rgb[0])) + 0)
    elif sort_rgb[2] == rgb[0] and rgb[1] < rgb[2]:
        h = round(60 * ((rgb[1] - rgb[2]) / (sort_rgb[2] - sort_rgb[0])) + 360)
    elif sort_rgb[2] == rgb[1]:
        h = round(60 * ((rgb[2] - rgb[0]) / (sort_rgb[2] - sort_rgb[0])) + 120)
    elif sort_rgb[2] == rgb[2]:
        h = round(60 * ((rgb[0] - rgb[1]) / (sort_rgb[2] - sort_rgb[0])) + 240)

    l = round((sort_rgb[2] + sort_rgb[0]) / 510, 3)

    if l == 0 or sort_rgb[2] == sort_rgb[0]:
        s = 0
    elif 0 < l <= 0.5:
        s = round((sort_rgb[2] - sort_rgb[0]) / (sort_rgb[2] + sort_rgb[0]), 3)
    elif l > 0.5:
        s = round((sort_rgb[2] - sort_rgb[0]) / (510 - (sort_rgb[2] + sort_rgb[0])), 3)

    hsl = list([h, s, l])
    return hsl


def main():
    st.set_page_config(page_title="取色器", page_icon="🌸", layout="wide")

    sysmenu = '''
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    # color_picked = st.color_picker('选取一种颜色', '#000000')
    #
    # st.write('当前的hex颜色是 ', color_picked)
    #
    # rgb = hex_to_rgb(color_picked)
    # st.write("当前的rgb颜色是 ({}, {}, {})".format(rgb[0], rgb[1], rgb[2]))
    #
    # hsl = rgb_to_hsl(rgb)
    # st.write("当前的hsl颜色是 ({}°, {}%, {}%)".format(hsl[0], round(hsl[1] * 100, 3), round(hsl[2] * 100), 3))

    c1, c2, c3 = st.columns([1, 1, 1], gap="large")
    with c1:
        test_red_1 = st.slider(label="red1", min_value=0, max_value=255)
        test_green_1 = st.slider(label="green1", min_value=0, max_value=255)
        test_blue_1 = st.slider(label="blue1", min_value=0, max_value=255)
        t1 = '#' + str(hex(int(test_red_1))[2:].zfill(2)) + str(hex(int(test_green_1))[2:].zfill(2)) + str(
            hex(int(test_blue_1))[2:].zfill(2))
        tt1 = st.color_picker('测试1', t1)
        st.write('当前的hex颜色是 ', tt1)
        tt1_rgb = hex_to_rgb(tt1)
        st.write("当前的rgb颜色是 ({}, {}, {})".format(tt1_rgb[0], tt1_rgb[1], tt1_rgb[2]))
        tt1_hsl = rgb_to_hsl(tt1_rgb)
        st.write("当前的hsl颜色是 ({}°, {}%, {}%)".format(tt1_hsl[0], round(tt1_hsl[1] * 100, 3), round(tt1_hsl[2] * 100), 3))

    with c2:
        test_red_2 = st.slider(label="red2", min_value=0, max_value=255)
        test_green_2 = st.slider(label="green2", min_value=0, max_value=255)
        test_blue_2 = st.slider(label="blue2", min_value=0, max_value=255)
        t2 = '#' + str(hex(int(test_red_2))[2:].zfill(2)) + str(hex(int(test_green_2))[2:].zfill(2)) + str(
            hex(int(test_blue_2))[2:].zfill(2))
        # st.write(t2)
        tt2 = st.color_picker('测试2', t2)
        st.write('当前的hex颜色是 ', tt2)
        tt2_rgb = hex_to_rgb(tt2)
        st.write("当前的rgb颜色是 ({}, {}, {})".format(tt2_rgb[0], tt2_rgb[1], tt2_rgb[2]))
        tt2_hsl = rgb_to_hsl(tt2_rgb)
        st.write("当前的hsl颜色是 ({}°, {}%, {}%)".format(tt2_hsl[0], round(tt2_hsl[1] * 100, 3), round(tt2_hsl[2] * 100), 3))

    with c3:
        test_red_3 = st.slider(label="red3", min_value=0, max_value=255)
        test_green_3 = st.slider(label="green3", min_value=0, max_value=255)
        test_blue_3 = st.slider(label="blue3", min_value=0, max_value=255)
        t3 = '#' + str(hex(int(test_red_3))[2:].zfill(2)) + str(hex(int(test_green_3))[2:].zfill(2)) + str(
            hex(int(test_blue_3))[2:].zfill(2))
        # st.write(t3)
        tt3 = st.color_picker('测试3', t3)
        st.write('当前的hex颜色是 ', tt3)
        tt3_rgb = hex_to_rgb(tt3)
        st.write("当前的rgb颜色是 ({}, {}, {})".format(tt3_rgb[0], tt3_rgb[1], tt3_rgb[2]))
        tt3_hsl = rgb_to_hsl(tt3_rgb)
        st.write("当前的hsl颜色是 ({}°, {}%, {}%)".format(tt3_hsl[0], round(tt3_hsl[1] * 100, 3), round(tt3_hsl[2] * 100), 3))

    if 'show' not in st.session_state:
        st.session_state.show = False

    st.button('Show', on_click=toggle_show)

    if st.session_state.show:
        ramdom_rgb_color = list([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        ramdom_hex_color = rgb_to_hex(ramdom_rgb_color)
        ramdom_color = '#' + ramdom_hex_color[0] + ramdom_hex_color[1] + ramdom_hex_color[2]
        st.write(ramdom_color)
        test = st.color_picker("a", ramdom_color, label_visibility="collapsed")





if __name__ == '__main__':
    main()
