# Done by Muench
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math
import mpl_toolkits.axisartist as axisartist


def add_coordinate(fig, x1, y1, x2, y2):
    ax = axisartist.Subplot(fig, 111)
    fig.add_axes(ax)
    #通过set_visible方法设置绘图区所有坐标轴隐藏
    ax.axis[:].set_visible(False)
    #ax.new_floating_axis代表添加新的坐标轴
    ax.axis["x"] = ax.new_floating_axis(0,0)
    #给x坐标轴加上箭头
    ax.axis["x"].set_axisline_style("->", size = 1.0)
    #添加y坐标轴，且加上箭头
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("->", size = 1.0)
    #设置x、y轴上刻度显示方向
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")
    plt.xlim(x1,y1)
    plt.ylim(x2, y2)


def main():
    st.set_page_config(page_title="三角函数", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    # number_input输入角度
    # 输出 正弦、余弦、正切、余切、正割、余割
    inputted_degree = st.number_input(label='输入度数')

    st.write('正弦sin: ', math.sin(math.radians(inputted_degree)),
             '余弦cos: ', math.cos(math.radians(inputted_degree)),
             '正切tan: ', math.tan(math.radians(inputted_degree)),
             '余切cot: ', np.nan if inputted_degree == 0 else (1 / math.tan(math.radians(inputted_degree))),
             '正割sec: ', 1 / math.cos(math.radians(inputted_degree)),
             '余割csc: ', np.nan if inputted_degree == 0 else (1 / math.sin(math.radians(inputted_degree))))
    st.write(math.sin(math.pi / 6))


    c1r1, c2r1 = st.columns([1, 1])
    with c1r1:
        x = np.linspace(-2 * math.pi, 2 * math.pi, 100)
        fig1 = plt.figure(figsize=(15, 8))
        add_coordinate(fig1, -7, 7, -1, 1)
        y1 = np.sin(x)
        plt.plot(x, y1, '#ff3300', label='sin(x)')
        plt.grid(True, linestyle='solid')
        plt.title('正弦函数sin(x)')
        plt.legend()
        st.pyplot(fig1)

        x = np.linspace(-2 * math.pi, 2 * math.pi, 100)
        fig3 = plt.figure(figsize=(15, 8))
        add_coordinate(fig3, -5, 5, -4, 4)
        y3 = np.tan(x)
        plt.plot(x, y3, '#00e600', label='tan(x)')
        plt.grid(True, linestyle='solid')
        plt.title('正切函数tan(x)')
        plt.legend()
        st.pyplot(fig3)

    with c2r1:
        x = np.linspace(-2 * math.pi, 2 * math.pi, 100)
        fig2 = plt.figure(figsize=(15, 8))
        add_coordinate(fig2, -7, 7, -1, 1)
        y2 = np.cos(x)
        plt.plot(x, y2, '#0066ff', label='cos(x)')
        plt.grid(True, linestyle='solid')
        plt.title('余弦函数cos(x)')
        plt.legend()
        st.pyplot(fig2)

        x = np.linspace(-2 * math.pi, 2 * math.pi, 100)
        fig4 = plt.figure(figsize=(15, 8))
        add_coordinate(fig4, -5, 5, -4, 4)
        y4 = np.cos(x) / np.sin(x)
        plt.plot(x, y4, '#ff1aff', label='cot(x)')
        plt.grid(True, linestyle='solid')
        plt.title('余切函数cot(x)')
        plt.legend()
        st.pyplot(fig4)


    # 另外一个文件 chatgpt
    #


if __name__ == '__main__':
    main()