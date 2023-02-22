

import streamlit as st

import streamlit.components.v1 as components
st.title("Museu Virtual da Arte Urbana - AMadora")

col1, col2, col3 = st.columns(3)
with col1:
   st.header("Museu - Arte Urbana ")
   st.image("1foto.png")

with col2:
   st.header("Criação de APP Online")
   st.image("2foto.png")

with col3:
   st.header("Modelação Urbana")
   st.image("4foto.png")


video_file = open('/Museu/video.mov', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

components.iframe("https://v3d.net/fbi", width=1800, height=600)
st.markdown(components.iframe, unsafe_allow_html=True)
