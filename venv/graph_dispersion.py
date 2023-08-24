import streamlit as st
import plotly.express as px
from pandas import DataFrame


def graph_dispersion(data: DataFrame, x: str, y: str='', title: str='', p: str=''):
  container = st.container()
  container.markdown(f'### {title}', unsafe_allow_html=True)
  if y == '':
    container.plotly_chart(
      px.scatter(
        data,
        x=x, 
      )
    )
  else:
      container.plotly_chart(
      px.scatter(
        data,
        x=x, 
        y=y,
      )
    )
  container.markdown(p, unsafe_allow_html=True)