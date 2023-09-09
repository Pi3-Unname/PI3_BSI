import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def graph_treemap(data, options, default=[]):
  col1, col2 = st.columns((3, 1))
  
  data = data
  options = options
  with col1:
    select = st.multiselect(
      'Selecione dois elementos', 
      options=options, 
      default=default, 
      max_selections=3
    )

 
  button = col2.empty()
  if button.button(label='Análisar', use_container_width=25):
    button.button("Analisando...", use_container_width=25, disabled=True)
    st.plotly_chart(px.treemap(data, path=select))

def graph(
  data: pd.DataFrame, x: str, options: np.ndarray, type_graph, type_txt: str,
  ):

  st.markdown(f'## {type_txt.title()}')
  col1, col2 = st.columns((3, 2))
  options = options.tolist()
  options.remove(x)
  options.insert(-1, 'Total')
  options.insert(0, '')
  with col1:
    st.write(f"Selecione um campo para interagir com o campo")
    select = st.selectbox(
      f"{x}{type_graph}",
      options=options,
      index=0,
      label_visibility='hidden'
    )
  with col2:
    st.write('Escolha o campo para separar as cores ')
    color = st.selectbox(
      f"{x}{type_txt}",
      options=options,
      label_visibility='hidden'
    )
  if select != '':
    if select != 'Total':
      new_data = data.groupby([x, select]).size().reset_index(name='Total')
    else:
      new_data = data.groupby([x]).size().reset_index(name='Total')
    if color == '':
      st.plotly_chart(type_graph(new_data, x=x, y=select,))
    elif color == 'Total':
      st.plotly_chart(type_graph(new_data, x=x, y=select, color=color))
    else:
      if select != 'Total':
        new_data = data.groupby([x, select, color]).size().reset_index(name='Total')
      else:
        new_data = data.groupby([x, color]).size().reset_index(name='Total')
      st.plotly_chart(type_graph(new_data, x=x, y=select, color=color))