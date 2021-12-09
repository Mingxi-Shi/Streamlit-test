import streamlit as st

st.write("asdsada")

vid_file1 = open("./vedio/7.mp4", "rb").read()
st.video(vid_file1)

vid_file2 = open("./vedio/star.mp4", "rb").read()
st.video(vid_file2)