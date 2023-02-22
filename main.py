

import streamlit as st

import streamlit.components.v1 as components

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('backg.png')    

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
   components.iframe("https://v3d.net/fej", width=1800, height=600)
   st.markdown(components.iframe, unsafe_allow_html=True)
