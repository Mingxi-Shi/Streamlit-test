import streamlit as st

st.write("asdsada")

vid_file1 = open("./vedio/7.mp4", "rb").read()
st.video(vid_file1)

vid_file2 = open("./vedio/star.mp4", "rb").read()
st.video(vid_file2)

audio_file1 = open("./music/稻香-周杰伦.mp3", "rb").read()
st.audio(audio_file1, format='audio/mp3', start_time=0)

audio_file2 = open("./music/七里香-周杰伦.mp3", "rb").read()
st.audio(audio_file2, format='audio/mp3', start_time=0)