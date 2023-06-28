import streamlit as st
import pandas as pd
import plotly.express as px

from replace_value import replace_values
from build_hearder import build_header
from graph_treemap import graph_treemap
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


    
replace_values(data_stay, {
  'unknown': 0,
  'Minor': 1,
  'Moderate': 2,
  'Major': 3,
  'Extreme': 4,
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

# Boxplot de risco de mortalidade
create_box(
  data_stay, 
  'APR Risk of Mortality',
  title='APR Mortality Risk Boxplot', 
  label_mapX=label_mapping,
  p='''<p style='text-align: justify;'>No boxplot de risco de mortalidade, podemos observar que a maioria dos pacientes registrados apresentou um risco classificado como "Minor" a "Major". Isso indica que a maior parte dos pacientes teve um nível de risco relativamente baixo a moderado. Essa informação é relevante para compreender a distribuição e a gravidade dos riscos de mortalidade entre os pacientes analisados.</p>'''
)

replace_values(data_stay, {
  0: 'Unknown',
  1: 'Minor',
  2: 'Moderate',
  3: 'Major',
  4: 'Extreme',
})

# Gráfico
fig = px.scatter(
  data_stay, 
  title='Graph Length of Stay',
  x='Length of Stay', 
  y='Total', 
  color='APR Risk of Mortality', 
  color_discrete_map={
    'unknown':'#FFF', 
    'Minor':'#66AA00', 
    'Moderate':'#FFA14A', 
    'Major':'#D62728', 
    'Extreme':'#9134BD'
  }
)
st.plotly_chart(fig)

st.plotly_chart(
  px.bar(
    data_stay, 
    title='Graph APR Risk of Mortality',
    x='Length of Stay', 
    y='APR Risk of Mortality', 
  )
)