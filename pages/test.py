from io import BytesIO

import streamlit as st
import base64
from aip import AipFace
from PIL import Image


def main():
    APP_ID = '24862934'
    API_KEY = 'k8BDvtNTjXGicgGXxDVH8GzX'
    SECRET_KEY = '3UzbuAMR0z3PcQw8GnNqcanKoVkp7TTI'

    client = AipFace(APP_ID, API_KEY, SECRET_KEY)

    c1r1, c2r1 = st.columns([1, 1])
    with c1r1:
        user_camera_input_image = st.camera_input("Take a picture")
        # if user_camera_input_image is not None:
        #     st.image(user_camera_input_image)
    with c2r1:
        # test_image_bytes = BytesIO()
        # test_image = Image.open('resources/images/facematch/test.jpg', mode='r')
        # test_image.save(test_image_bytes, format="JPEG")
        # st.image(test_image)

        user_file_uploader_image = st.file_uploader(label="上传图片", type=['jpg', 'png'])
        if user_file_uploader_image is not None:
            st.image(user_file_uploader_image)

    # if user_camera_input_image and test_image:
    if user_camera_input_image and user_file_uploader_image:
        image1_bytes = str(base64.b64encode(user_camera_input_image.getvalue()), encoding='utf-8')
        # image2_bytes = str(base64.b64encode(test_image_bytes.getvalue()), encoding='utf-8')
        image2_bytes = str(base64.b64encode(user_file_uploader_image.getvalue()), encoding='utf-8')
        result = client.match(
            [{'image': image1_bytes, 'image_type': 'BASE64'}, {'image': image2_bytes, 'image_type': 'BASE64'}])
        if result["error_msg"] == "SUCCESS" and result["result"]["score"] > 50:
            st.success("人脸比对分数:" + str(result["result"]["score"]))
        else:
            st.error("人脸比对分数:" + str(result["result"]["score"]))


    # 摄像头 抓取用户人脸
    # 比对每一张图片
    # 当分数>50，取图片名，登录帐号




if __name__ == '__main__':
    main()