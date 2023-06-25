import streamlit as st
import plotly.express as px

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
    col2.plotly_chart(px.treemap(data, path=select))
  
