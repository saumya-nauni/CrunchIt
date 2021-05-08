#app.py
import app1
import app2
import streamlit as st

st. set_page_config(layout="centered")

PAGES = {
    "About the app": app1,
    "Start Summarizing!": app2
}
st.sidebar.image('Logo.png', width = 250)
st.markdown("""
    <style>
    .big-font1 {
    font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.markdown('<p class="big-font1"; style="font-family:verdana"><b>CrunchIt</b></p>', unsafe_allow_html=True)
selection = st.sidebar.radio(" ", list(PAGES.keys()))
page = PAGES[selection]
page.app()