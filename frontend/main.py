import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with open('style.css') as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html=True)



content = st.container()

topbar = st.container()
col1, col2 = topbar.columns([1, 1])
with col1:
    st.image('revolt-united-logo.png', width=80)
with col2:
    st.title('Re-Volt United')

