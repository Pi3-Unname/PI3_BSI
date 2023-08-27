import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from replace_value import replace_values
from build_hearder import build_header
from graph_treemap import graph_treemap, graph
from create_boxplot import create_box

build_header(
  title='Análise de Diagnóstico',
  header='Análise de Diagnóstico',
  layout='centered',
)

data = pd.read_parquet('venv/project/data/hospital_100k.parquet')
data_stay = data.groupby(['APR DRG Description','Type of Admission', 'APR Risk of Mortality', 'Length of Stay',]).size().reset_index(name='Total')
data_stay.sort_values('Total', ascending=True, inplace=True)
data_diagnostic = data[['Age Group', 'Gender', 'APR DRG Code', 'APR DRG Description']]


# Tabela apenas com os dados usados nessa seção
_, c2, _ = st.columns((1,7,1))
c2.write(data_diagnostic)

graph_treemap(
  data=data_stay, 
  options=data_stay.columns.to_list(),
  default=data_stay.columns.to_list()[:2],
)
    


graph(
  data,
  x = 'APR DRG Description',
  options = data.columns,
  type_graph=px.bar,
  type_txt='Gráfico de Barras'
)
graph(
  data,
  x = 'APR DRG Description',
  options = data.columns,
  type_graph=px.histogram,
  type_txt='gráfico de histograma'
)
graph(
  data,
  x = 'APR DRG Description',
  options = data.columns,
  type_graph=px.area,
  type_txt='Gráfico de area'
)
graph(
  data,
  x = 'APR DRG Description',
  options = data.columns,
  type_graph=px.line,
  type_txt='Gráfico de Linha'
)