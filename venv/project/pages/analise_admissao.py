import streamlit as st
import pandas as pd
import plotly.express as px

from replace_value import replace_values
from build_hearder import build_header
from graph_treemap import graph_treemap, graph
from create_boxplot import create_box

build_header(
  title='Análise de Admissão',
  header='Análise de Admissão',
  layout='centered',
)

data = pd.read_parquet('venv/project/data/hospital_100k.parquet')

st.write(data['Type of Admission'].unique())

graph_treemap(
  data=data, 
  options=data.columns.to_list(),
  default=data.columns.to_list()[:2],
)

# Boxplot de risco de mortalidade com tempo de estadia
create_box(
  data, 
  y='Type of Admission',
  x='Length of Stay',
  title='Boxplot do Tipo de Admissão por Tempo de Estadia',
  p='''<p style='text-align:justify;'>Com base no boxplot que relaciona o tipo de admissão com o tempo de estadia, podemos observar que os registros com risco "Trauma" apresentam um tempo de internação mais frequente entre 2 e 12 dias. Por outro lado, os registros classificados como "Newborn" têm uma faixa de tempo de estadia media bem menor. podemos visualizar também a quantidade de outliers.</p>'''
)

def category_stay(list_classes, old_values):
  list_classes.sort()
  new_list = [None] * len(old_values)
  for i, old in enumerate(old_values):
    for index, value in enumerate(list_classes):
      if(len(list_classes)-1 == index):
        new_list[i] = f'mais de {value} dias'
      else:
        if(value <= old < list_classes[index+1]):
          new_list[i] = f'{value} a {list_classes[index+1]} dias'
          break
  return new_list
def group_stay(data):
  test_lista= [x*10 for x in range(13)]
  lista_stay_category = category_stay(test_lista, data['Length of Stay'].tolist())
  data['Length of Stay'] = lista_stay_category
  return data
data_modify = group_stay(data)

graph(
  data_modify,
  x = 'Type of Admission',
  options = data_modify.columns,
  type_graph=px.bar,
  type_txt='Gráfico de Barras'
)
graph(
  data_modify,
  x = 'Type of Admission',
  options = data_modify.columns,
  type_graph=px.histogram,
  type_txt='gráfico de histograma'
)
graph(
  data_modify,
  x = 'Type of Admission',
  options = data_modify.columns,
  type_graph=px.area,
  type_txt='Gráfico de area'
)
graph(
  data_modify,
  x = 'Length of Stay',
  options = data_modify.columns,
  type_graph=px.line,
  type_txt='Gráfico de Linha'
)
