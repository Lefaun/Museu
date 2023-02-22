

import streamlit as st

import streamlit.components.v1 as components
import base64
import streamlit as st


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('Screenshot 2023-02-22 at 17.40.37.png')

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


video_file = open('video2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
col1, col2 = st.columns(2)

with col1:
   components.iframe("https://v3d.net/fbi", width=1800, height=600)
   st.markdown(components.iframe, unsafe_allow_html=True)
