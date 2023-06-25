import streamlit as st
import plotly.express as px
import pandas as pd

def create_box(
  df: pd.DataFrame, x: str, y: str='', title: str='',p: str='', label_mapX=None, label_mapY=None
  ) -> None:
  if (y != ''): 
    fig_box = px.box(df, x=x, y=y)
  else: 
    fig_box = px.box(df, x=x)
  
  # Atualizar os rótulos do eixo x
  if (label_mapX != None):
    fig_box.update_xaxes(
      ticktext=[label_mapX[label] for label in df[x]],
      tickvals=df[x]
  )
  if (label_mapY != None):
    fig_box.update_yaxes(
      ticktext=[label_mapY[label] if label in label_mapY else label for label in df[y]],
      tickvals=df[y]
    )
  field = st.container()
  field.markdown(f'### {title}')
  field.plotly_chart(fig_box)
  field.markdown(p, unsafe_allow_html=True)

