# Done by Muench
from aip import AipFace
import streamlit as st
from PIL import Image
import base64


def main():
    st.set_page_config(page_title="人脸对比", page_icon="🌸", layout="wide")

    sysmenu = '''
                    <style>
                    #MainMenu {visibility:hidden;}
                    footer {visibility:hidden;}
                    '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    APP_ID = '24862934'
    API_KEY = 'k8BDvtNTjXGicgGXxDVH8GzX'
    SECRET_KEY = '3UzbuAMR0z3PcQw8GnNqcanKoVkp7TTI'

    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    selected_model = st.sidebar.radio(label="选择操作", options=["图片和图片", "图片和摄像头"])

    if selected_model == "图片和图片":

        c1r1, c2r1 = st.columns([1, 1], gap="large")
        with c1r1:
            image1_data = st.file_uploader(label="上传第一张图片", type=['jpg', 'png'])
            if image1_data:
                st.image(image1_data)
        with c2r1:
            image2_data = st.file_uploader(label="上传第二张图片", type=['jpg', 'png'])
            if image2_data:
                st.image(image2_data)

        if image1_data and image2_data:
            image1_bytes = str(base64.b64encode(image1_data.getvalue()), encoding='utf-8')
            image2_bytes = str(base64.b64encode(image2_data.getvalue()), encoding='utf-8')
            result = client.match(
                [{'image': image1_bytes, 'image_type': 'BASE64'}, {'image': image2_bytes, 'image_type': 'BASE64'}])
            if result["error_msg"] == "SUCCESS" and result["result"]["score"] > 50:
                st.success("人脸比对分数:" + str(result["result"]["score"]))
            elif result["error_msg"] == "SUCCESS" and result["result"]["score"] < 50:
                st.error("人脸比对分数:" + str(result["result"]["score"]))
            else:
                st.info("人脸比对未成功（可能其中一个无人脸信息）")

    elif selected_model == "图片和摄像头":

        c1r1, c2r1 = st.columns([1, 1])
        with c1r1:
            user_camera_input_image = st.camera_input("Take a picture")
            # if user_camera_input_image is not None:
            #     st.image(user_camera_input_image)
        with c2r1:
            user_file_uploader_image = st.file_uploader(label="上传图片", type=['jpg', 'png'])
            if user_file_uploader_image is not None:
                st.image(user_file_uploader_image)

        if user_camera_input_image and user_file_uploader_image:
            image1_bytes = str(base64.b64encode(user_camera_input_image.getvalue()), encoding='utf-8')
            image2_bytes = str(base64.b64encode(user_file_uploader_image.getvalue()), encoding='utf-8')
            result = client.match(
                [{'image': image1_bytes, 'image_type': 'BASE64'}, {'image': image2_bytes, 'image_type': 'BASE64'}])
            if result["error_msg"] == "SUCCESS" and result["result"]["score"] > 50:
                st.success("人脸比对分数:" + str(result["result"]["score"]))
            elif result["error_msg"] == "SUCCESS" and result["result"]["score"] < 50:
                st.error("人脸比对分数:" + str(result["result"]["score"]))
            else:
                st.info("人脸比对未成功（可能其中一个无人脸信息）")


if __name__ == '__main__':
    main()