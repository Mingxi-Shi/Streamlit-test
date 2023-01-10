# Done by Muench

import streamlit as st

# sslist = ['a', 'b', 'c', 'd']
# for ss in sslist:
#     if ss not in st.session_state:
#         st.session_state[ss] = ""


def power_update(last):
    sliders = ['GongZhiMaLi', 'YingZhiMaLi', 'QianWa', 'Wa']
    last = sliders.index(last)
    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 0.9860294
        st.session_state[sliders[2]] = st.session_state[sliders[0]] * 0.7352941
        st.session_state[sliders[3]] = st.session_state[sliders[0]] * 735.2941
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] * 1.0141686
        st.session_state[sliders[2]] = st.session_state[sliders[1]] * 0.7457122
        st.session_state[sliders[3]] = st.session_state[sliders[1]] * 745.712172
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] * 1.3600000
        st.session_state[sliders[1]] = st.session_state[sliders[2]] * 1.341
        st.session_state[sliders[3]] = st.session_state[sliders[2]] * 1000
    elif last == 3:
        st.session_state[sliders[0]] = st.session_state[sliders[3]] * 0.0013600
        st.session_state[sliders[1]] = st.session_state[sliders[3]] * 0.001341
        st.session_state[sliders[2]] = st.session_state[sliders[3]] / 1000


def power_conversion():
    st.number_input(label="公制马力(PS)", key="GongZhiMaLi", format="%.f", on_change=power_update, args=('GongZhiMaLi',))
    st.number_input(label="英制马力(HP)", key="YingZhiMaLi", format="%.f", on_change=power_update, args=('YingZhiMaLi',))
    st.number_input(label="千瓦(kW)", key="QianWa", format="%.f", on_change=power_update, args=('QianWa',))
    st.number_input(label="瓦(W)", key="Wa", format="%.f", on_change=power_update, args=('Wa',))


def pressure_update(last):
    sliders = ['BiaoZhunDaQiYa', 'QianPa']
    last = sliders.index(last)
    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 101.325
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] / 101.325


def pressure_conversion():
    st.number_input(label="标准大气压(atm)", key="BiaoZhunDaQiYa", format="%.f", on_change=pressure_update, args=('BiaoZhunDaQiYa',))
    st.number_input(label="千帕(kPa)", key="QianPa", format="%.f", on_change=pressure_update, args=('QianPa',))


def area_update(last):
    sliders = ['GongQing', 'ShiMu', 'PingFangMi']
    last = sliders.index(last)
    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 15
        st.session_state[sliders[2]] = st.session_state[sliders[0]] * 10000
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] / 15
        st.session_state[sliders[2]] = st.session_state[sliders[1]] * 2000 / 3
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] / 10000
        st.session_state[sliders[1]] = st.session_state[sliders[2]] * 3 / 2000


def area_conversion():
    st.number_input(label="公顷", key="GongQing", format="%.f", on_change=area_update, args=('GongQing',))
    st.number_input(label="市亩", key="ShiMu", format="%.f", on_change=area_update, args=('ShiMu',))
    st.number_input(label="平方米(㎡)", key="PingFangMi", format="%.f", on_change=area_update, args=('PingFangMi',))


def weight_update(last):
    sliders = ['D', 'GJ', 'K']
    last = sliders.index(last)

    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 1000
        st.session_state[sliders[2]] = st.session_state[sliders[0]] * 1000000
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] / 1000
        st.session_state[sliders[2]] = st.session_state[sliders[1]] * 1000
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] / 1000000
        st.session_state[sliders[1]] = st.session_state[sliders[2]] / 1000


def weight_conversion():
    st.number_input(label="吨(t)", key="D", format="%.6f", on_change=weight_update, args=('D',))
    st.number_input(label="公斤(kg)", key="GJ", format="%.3f", on_change=weight_update, args=('GJ',))
    st.number_input(label="克(g)", key="K", format="%f", on_change=weight_update, args=('K',))


def volume_update(last):
    sliders = ['LFM', 'GS', 'SS']
    last = sliders.index(last)

    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 10
        st.session_state[sliders[2]] = st.session_state[sliders[0]] * 100
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] / 10
        st.session_state[sliders[2]] = st.session_state[sliders[1]] * 10
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] / 100
        st.session_state[sliders[1]] = st.session_state[sliders[2]] / 10


def volume_conversion():
    st.number_input(label="立方米(m³)", key="LFM", format="%.2f", on_change=volume_update, args=('LFM',))
    st.number_input(label="公石(hl)", key="GS", format="%.2f", on_change=volume_update, args=('GS',))
    st.number_input(label="十升(dal)", key="SS", format="%.2f", on_change=volume_update, args=('SS',))


def angle_update(last):
    sliders = ['Yuan', 'ZhiJiao', 'Du']
    last = sliders.index(last)

    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 4
        st.session_state[sliders[2]] = st.session_state[sliders[0]] * 360
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] / 4
        st.session_state[sliders[2]] = st.session_state[sliders[1]] * 90
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] / 360
        st.session_state[sliders[1]] = st.session_state[sliders[2]] / 90


def angle_conversion():
    st.number_input(label="圆(Circles)", key="Yuan", format="%.4f", on_change=angle_update, args=('Yuan',))
    st.number_input(label="直角(RightAngles)", key="ZhiJiao", format="%.2f", on_change=angle_update, args=('ZhiJiao',))
    st.number_input(label="度(Degrees)", key="Du", format="%.2f", on_change=angle_update, args=('Du',))


def temperature_update(last):
    sliders = ['SSD', 'HSD', 'KSD', 'LSDRa', 'LSDRe']
    last = sliders.index(last)

    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 1.8 + 32
        st.session_state[sliders[2]] = st.session_state[sliders[0]] + 273.15
        st.session_state[sliders[3]] = st.session_state[sliders[0]] * 1.8 + 491.67
        st.session_state[sliders[4]] = st.session_state[sliders[0]] * 0.8

    elif last == 1:
        st.session_state[sliders[0]] = (st.session_state[sliders[1]] - 32) * 5 / 9
        st.session_state[sliders[2]] = (st.session_state[sliders[1]] + 459.67) * 5 / 9
        st.session_state[sliders[3]] = st.session_state[sliders[1]] + 459.67
        st.session_state[sliders[4]] = (st.session_state[sliders[1]] - 32) / 2.25
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] - 273.15
        st.session_state[sliders[1]] = (st.session_state[sliders[2]] / 1.8) - 459.67
        st.session_state[sliders[3]] = st.session_state[sliders[2]] * 1.8
        st.session_state[sliders[4]] = (st.session_state[sliders[2]] * 0.8) - 218.52
    elif last == 3:
        st.session_state[sliders[0]] = (st.session_state[sliders[3]] - 491.67) * 5 / 9
        st.session_state[sliders[1]] = st.session_state[sliders[3]] - 459.67
        st.session_state[sliders[2]] = st.session_state[sliders[3]] / 1.8
        st.session_state[sliders[4]] = (st.session_state[sliders[3]] * 4 / 9) - 218.52
    elif last == 4:
        st.session_state[sliders[0]] = st.session_state[sliders[4]] / 0.8
        st.session_state[sliders[1]] = (st.session_state[sliders[4]] * 2.25) + 32
        st.session_state[sliders[2]] = (st.session_state[sliders[4]] + 218.52) / 0.8
        st.session_state[sliders[3]] = (st.session_state[sliders[4]] * 2.25) + 491.67


def temperature_conversion():
    st.number_input(label="摄氏度(C)", key="SSD", format="%.2f", on_change=temperature_update, args=('SSD',))
    st.number_input(label="华氏度(F)", key="HSD", format="%.2f", on_change=temperature_update, args=('HSD',))
    st.number_input(label="开氏度(K)", key="KSD", format="%.2f", on_change=temperature_update, args=('KSD',))
    st.number_input(label="兰氏度(Ra)", key="LSDRa", format="%.2f", on_change=temperature_update, args=('LSDRa',))
    st.number_input(label="列氏度(Re)", key="LSDRe", format="%.2f", on_change=temperature_update, args=('LSDRe',))


def length_update(last):
    sliders = ['GL', 'M', 'FM', 'LM', 'HM', 'S', 'WM']
    last = sliders.index(last)

    if last == 0:
        st.session_state[sliders[1]] = st.session_state[sliders[0]] * 1000
        st.session_state[sliders[2]] = st.session_state[sliders[0]] * 10000
        st.session_state[sliders[3]] = st.session_state[sliders[0]] * 100000
        st.session_state[sliders[4]] = st.session_state[sliders[0]] * 1000000
        st.session_state[sliders[5]] = st.session_state[sliders[0]] * 100000000
        st.session_state[sliders[6]] = st.session_state[sliders[0]] * 1000000000
    elif last == 1:
        st.session_state[sliders[0]] = st.session_state[sliders[1]] / 1000
        st.session_state[sliders[2]] = st.session_state[sliders[1]] * 10
        st.session_state[sliders[3]] = st.session_state[sliders[1]] * 100
        st.session_state[sliders[4]] = st.session_state[sliders[1]] * 1000
        st.session_state[sliders[5]] = st.session_state[sliders[1]] * 100000
        st.session_state[sliders[6]] = st.session_state[sliders[1]] * 1000000
    elif last == 2:
        st.session_state[sliders[0]] = st.session_state[sliders[2]] / 10000
        st.session_state[sliders[1]] = st.session_state[sliders[2]] / 10
        st.session_state[sliders[3]] = st.session_state[sliders[2]] * 10
        st.session_state[sliders[4]] = st.session_state[sliders[2]] * 100
        st.session_state[sliders[5]] = st.session_state[sliders[2]] * 10000
        st.session_state[sliders[6]] = st.session_state[sliders[2]] * 100000
    elif last == 3:
        st.session_state[sliders[0]] = st.session_state[sliders[3]] / 100000
        st.session_state[sliders[1]] = st.session_state[sliders[3]] / 100
        st.session_state[sliders[2]] = st.session_state[sliders[3]] / 10
        st.session_state[sliders[4]] = st.session_state[sliders[3]] * 10
        st.session_state[sliders[5]] = st.session_state[sliders[3]] * 10000
        st.session_state[sliders[6]] = st.session_state[sliders[3]] * 100000
    elif last == 4:
        st.session_state[sliders[0]] = st.session_state[sliders[4]] / 1000000
        st.session_state[sliders[1]] = st.session_state[sliders[4]] / 1000
        st.session_state[sliders[2]] = st.session_state[sliders[4]] / 100
        st.session_state[sliders[3]] = st.session_state[sliders[4]] / 10
        st.session_state[sliders[5]] = st.session_state[sliders[4]] * 100
        st.session_state[sliders[6]] = st.session_state[sliders[4]] * 1000
    elif last == 5:
        st.session_state[sliders[0]] = st.session_state[sliders[5]] / 100000000
        st.session_state[sliders[1]] = st.session_state[sliders[5]] / 100000
        st.session_state[sliders[2]] = st.session_state[sliders[5]] / 10000
        st.session_state[sliders[3]] = st.session_state[sliders[5]] / 1000
        st.session_state[sliders[4]] = st.session_state[sliders[5]] / 100
        st.session_state[sliders[6]] = st.session_state[sliders[5]] * 10
    elif last == 6:
        st.session_state[sliders[0]] = st.session_state[sliders[6]] / 1000000000
        st.session_state[sliders[1]] = st.session_state[sliders[6]] / 1000000
        st.session_state[sliders[2]] = st.session_state[sliders[6]] / 100000
        st.session_state[sliders[3]] = st.session_state[sliders[6]] / 10000
        st.session_state[sliders[4]] = st.session_state[sliders[6]] / 1000
        st.session_state[sliders[5]] = st.session_state[sliders[6]] / 10
    # https://c.runoob.com/front-end/5575/


def length_conversion():
    c1r1, c2r1, c3r1, c4r1 = st.columns([1, 1, 1, 1], gap='large')
    with c1r1:
        st.number_input(label="公里(km)", key='GL', format="%.9f", on_change=length_update, args=('GL',))
    with c2r1:
        st.number_input(label="米(m)", key='M', format="%.6f", on_change=length_update, args=('M',))
    with c3r1:
        st.number_input(label="分米(dm)", key='FM', format="%.5f", on_change=length_update, args=('FM',))
    with c4r1:
        st.number_input(label="厘米(cm)", key='LM', format="%.4f", on_change=length_update, args=('LM',))

    c1r2, c2r2, c3r2, c4r2 = st.columns([1, 1, 1, 1], gap='large')
    with c1r2:
        st.number_input(label="毫米(mm)", key='HM', format="%.3f", on_change=length_update, args=('HM',))
    with c2r2:
        st.number_input(label="丝(dmm)", key='S', format="%.2f", on_change=length_update, args=('S',))
    with c3r2:
        st.number_input(label="微米(um)", key='WM', format="%f", on_change=length_update, args=('WM',))
    with c4r2:
        st.write(1)
        # st.number_input(label="里", key='H', format="%f", on_change=length_update, args=('H',))


def number_conversion():
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap='large')
    with col1:
        bin_num = st.text_input(label="二进制转换", value=1010)
        st.write("八进制：", oct(eval('0b' + bin_num))[2:])
        # st.write("十进制：", eval('0b' + bin_num))
        st.write("十进制：", int(bin_num, 2))
        st.write("十六进制：", hex(eval('0b' + bin_num))[2:])

    with col2:
        oct_num = st.text_input(label="八进制转换", value=12)
        st.write("二进制：", bin(int(oct_num, 8))[2:])
        st.write("十进制：", int(oct_num, 8))
        st.write("十六进制：", hex(eval('0o' + oct_num))[2:])

    with col3:
        int_num = st.text_input(label='十进制转换', value=10)
        st.write("二进制：", bin(int(int_num))[2:])
        st.write("八进制：", oct(int(int_num))[2:])
        st.write("十六进制：", hex(int(int_num))[2:])

    with col4:
        hex_num = st.text_input(label="十六进制转换", value='a')
        st.write("二进制：", bin(int(hex_num, 16))[2:])
        st.write("八进制：", oct(int(hex_num, 16))[2:])
        st.write("十进制：", int(hex_num, 16))


def main():

    st.set_page_config(page_title="单位转换", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    model_list = ["进制", "长度", "温度", "角度", "重量", "面积", "体积", "压力", "功率", "时间", "速度"]
    model_selected = st.sidebar.selectbox(label="选择", options=model_list)
    if model_selected == "进制":
        number_conversion()
    elif model_selected == "长度":
        length_conversion()
    elif model_selected == "温度":
        temperature_conversion()
    elif model_selected == "角度":
        angle_conversion()
    elif model_selected == "重量":
        weight_conversion()
    elif model_selected == "面积":
        area_conversion()
    elif model_selected == "体积":
        volume_conversion()
    elif model_selected == "压力":
        pressure_conversion()
    elif model_selected == "功率":
        power_conversion()
    elif model_selected == "时间":
        st.write(1)
    elif model_selected == "速度":
        st.write(1)


if __name__ == '__main__':
    main()
