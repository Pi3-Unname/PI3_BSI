import streamlit as st
import pandas as pd
import plotly.express as px

from replace_value import replace_values
from build_hearder import build_header
from graph_treemap import graph_treemap, graph
from create_boxplot import create_box

build_header(
  title="Análise de tempo de estadia",
  header='Análise de tempo de estadia',
  layout='centered',
)

data = pd.read_parquet('venv/project/data/hospital_100k.parquet')
data_stay = data.groupby(['Type of Admission', 'APR Risk of Mortality', 'Length of Stay',]).size().reset_index(name='Total')
#data_stay = data_stay.rename(columns={'Age Group': 'Age_Group'})
data_stay.sort_values('Total', ascending=True, inplace=True)

# Tabela apenas com os dados usados nessa seção
_, c2, _ = st.columns((1,7,1))
c2.write(data_stay)


graph_treemap(
  data=data_stay, 
  options=data_stay.columns.to_list(),
  default=data_stay.columns.to_list()[:2],
)
label_mapping = {0: 'Unknown', 1: 'Minor', 2: 'Moderate', 3: 'Major', 4: 'Extreme',}

st.write(data_stay['APR Risk of Mortality'].unique())
    
replace_values(data_stay, 'APR Risk of Mortality', {
  'Minor': 0,
  'Moderate': 1,
  'Major': 2,
  'Extreme': 3,
})

# Boxplot de tempo de estadia
create_box(
  data_stay, 
  x='Length of Stay',
  title='Boxplot of Length of Stay',
  p='''<p style='text-align:justify;'>Com base nesses dados, podemos inferir que a maioria dos registros possui uma estadia de 14.5 a 58 dias, com uma mediana de 33 dias. Não há valores atípicos perceptíveis além dos limites do boxplot, indicando uma distribuição relativamente concentrada dos comprimentos de estadia.</p>'''
)
# Boxplot de risco de mortalidade com tempo de estadia
create_box(
  data_stay, 
  y='APR Risk of Mortality',
  x='Length of Stay',
  title='Boxplot of APR Risk of Mortality for Length of Stay',
  label_mapY=label_mapping,
  p='''<p style='text-align:justify;'>Com base no boxplot que relaciona o risco de mortalidade e o tempo de estadia, podemos observar que os registros com risco "Extreme" apresentam um tempo de internação mais frequente entre 18 e 65 dias. Por outro lado, os registros classificados como "Unknown" têm uma faixa de tempo de estadia entre 1.75 e 7.25 dias. Essa análise sugere uma relação entre o aumento do risco de mortalidade e o aumento do tempo de estadia dos pacientes. Quanto maior o risco, tende a ser maior o tempo necessário para o tratamento e cuidado adequados.</p>'''
)
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
  data['Length of Stay'] = lista_costs_category
  return data
data_modify = group_stay(data)
graph(
  data_modify,
  x = 'Length of Stay',
  options = data_modify.columns,
  type_graph=px.bar,
  type_txt='Gráfico de Barras'
)
graph(
  data_modify,
  x = 'Length of Stay',
  options = data_modify.columns,
  type_graph=px.histogram,
  type_txt='gráfico de histograma'
)
graph(
  data_modify,
  x = 'Length of Stay',
  options = data_modify.columns,
  type_graph=px.area,
  type_txt='Gráfico de area'
)
graph(
  data_modify,
  x = 'Length of Stay',
  options = data_modify.columns,
  type_graph=px.line,
  type_txt='Gráfico de Linhas'
)
