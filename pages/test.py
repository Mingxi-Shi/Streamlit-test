import streamlit as st


def main():
    st.markdown('Streamlit is **_really_ cool**.')
    st.markdown("This text is :red[colored red], and this is **:blue[colored] ** and bold.")
    st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
    st.write(":smile:")
    st.button("click me :shark:")


    a = st.camera_input("Take a picture")
    st.write(a)
    # 摄像头 抓取用户人脸
    # 比对每一张图片
    # 当分数>50，取图片名，登录帐号




if __name__ == '__main__':
    main()