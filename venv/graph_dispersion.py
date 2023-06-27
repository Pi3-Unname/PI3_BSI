import streamlit as st
import plotly.express as px
from pandas import DataFrame


def graph_dispersion(data: DataFrame, x: str, y: str='', title: str='', p: str=''):
  container = st.container()
  container.markdown(f'### {title}', unsafe_allow_html=True)
  
  container.plotly_chart(
    px.scatter(
      data,
      x='Total Costs', 
      y='Total Charges',
    )
  )
  container.markdown(p, unsafe_allow_html=True)