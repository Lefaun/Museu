
import streamlit as st

import streamlit.components.v1 as components
st.title("Museu Virtual da Arte Urbana - AMadora")
components.iframe("https://v3d.net/fbi", width=1024, height=640)

st.markdown(components.iframe, unsafe_allow_html=True)
