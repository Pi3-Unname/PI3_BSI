import streamlit as st
import pandas as pd
import plotly.express as px

from build_hearder import build_header
from graph_treemap import graph_treemap, graph
from create_boxplot import create_box
#Análise financeira Silas
#Encargos totais
#Tempo de estadia
#Gravidade da doença
#Fonte de pagamento

build_header(
  title="Análise Financeira",
  header='Análise Financeira',
  layout='centered',
)
data = pd.read_parquet('venv/project/data/hospital_100k.parquet')


data_costs = data[['Total Costs Category', 'Length of Stay', 'Type of Admission',]]
data_costs.sort_values('Total Costs Category', ascending=True, inplace=True)


# Tabela apenas com os dados usados nessa seção
# _, c2, _ = st.columns((1,7,1))
# c2.write(data_costs)

graph_treemap(data_costs, data_costs.columns)

create_box(
  data_costs,
  x='Total Costs Category', 
  title='Boxplot Total Charges',
  p="""
    <p style='text-indent: 20px; text-align: justify;'>Com base no boxplot dos encargos totais, é possível observar uma quantidade significativa de outliers acima do limite superior definido. Isso indica a presença de valores extremamente altos, que estão fora da faixa normal dos dados, a maioria dos valores dos encargos totais está concentrada entre o primeiro quartil (Q1) de 7396.2 e o terceiro quartil (Q3) de 30.7k. Essa faixa intermediária indica que a maior parte dos encargos totais está distribuída dentro desse intervalo. No entanto, a mediana, que representa o valor central dos dados, é bastante baixa em relação ao limite superior do boxplot. Essa diferença entre a mediana e o limite superior justifica a presença de uma quantidade considerável de outliers acima do upper fence do mesmo.</p>

    - <p style='text-indent: 20px; text-align: justify;'>Essa análise sugere que existem alguns casos com encargos totais muito elevados, que estão além da faixa normal de variação. Esses outliers podem indicar situações especiais ou excepcionais que resultam em encargos financeiros substancialmente mais altos.</p>
  """
)

create_box(
  data_costs, 
  x='Total Costs Category', 
  y='Type of Admission', 
  title='Boxplot relating Total Costs and Type Admission',
)

st.write('''
  <p style='text-indent: 20px; text-align: justify;'>No boxplot que relaciona o tipo de admissão com o total dos custos, podemos observar a presença de muitos outliers, que representam valores atípicos em relação aos custos cobrados dos pacientes. Esses outliers indicam a existência de uma quantidade significativa de casos em que os valores cobrados diferem consideravelmente da maioria dos casos.</p>

  <p style='text-indent: 20px; text-align: justify;'>Esses valores atípicos podem surgir por diversos motivos, como procedimentos médicos complexos, tratamentos especializados, despesas adicionais ou situações excepcionais relacionadas à admissão dos pacientes. Esses casos podem influenciar significativamente os custos totais, resultando em valores que se distanciam dos valores típicos observados na maioria dos pacientes.</p>
''',unsafe_allow_html=True
)

graph(
  data=data,
  options=data.columns,
  x='Total Costs Category',
  type_graph=px.histogram,
  type_txt='Gráfico de Histograma'
)
graph(
  data=data,
  options=data.columns,
  x='Total Costs Category',
  type_graph=px.bar,
  type_txt='Gráfico de Barras'
)
graph(
  data=data,
  options=data.columns,
  x='Total Costs Category',
  type_graph=px.line,
  type_txt='Gráfico de Linhas'
)
graph(
  data=data,
  options=data.columns,
  x='Total Costs Category',
  type_graph=px.area,
  type_txt='Gráfico de Areas'
)