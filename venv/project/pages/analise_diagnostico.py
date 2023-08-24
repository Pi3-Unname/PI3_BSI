import streamlit as st
import pandas as pd
import plotly.express as px

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
label_mapping = {0: 'Unknown', 1: 'Minor', 2: 'Moderate', 3: 'Major', 4: 'Extreme',}

st.write(data_stay['APR DRG Description'].unique())
    
replace_values(data_stay, 'APR Risk of Mortality', {
  'Minor': 0,
  'Moderate': 1,
  'Major': 2,
  'Extreme': 3,
})


def category_costs(list_classes, old_values):
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
  lista_costs_category = category_costs(test_lista, data['Length of Stay'].tolist())
  data['Type of Admission'] = lista_costs_category
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
  type_txt='Gráfico de test'
)
