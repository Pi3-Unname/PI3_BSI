import streamlit as st

def build_header(title: str, header: str, layout='wide', paragraph: str = ''):
  st.set_page_config(
    page_title = title,
    layout = layout,
  )
  st.header(header)
  st.write(paragraph, unsafe_allow_html=True)