import streamlit as st
import pandas as pd
import plotly.express as px

from build_hearder import build_header
from graph_treemap import graph_treemap, graph
from create_boxplot import create_box
from graph_dispersion import graph_dispersion

build_header(
  title="Análise Financeira",
  header='Análise Financeira',
  layout='centered',
)
data = pd.read_parquet('venv/project/data/hospital_1k.parquet')


data_costs = data[[
    "Total Costs",
    "Total Charges",
    'Length of Stay', 
    'Type of Admission',
    ]]
#data_costs.sort_values('Total Costs Category', ascending=True, inplace=True)


# Tabela apenas com os dados usados nessa seção
# _, c2, _ = st.columns((1,7,1))
# c2.write(data_costs)

graph_treemap(data_costs, data_costs.columns)

create_box(
  data_costs,
  x='Total Charges', 
  title='Boxplot Total Charges',
  p="""
    <p style='text-indent: 20px; text-align: justify;'>Com base no boxplot dos encargos totais, é possível observar uma quantidade significativa de outliers acima do limite superior definido. Isso indica a presença de valores extremamente altos, que estão fora da faixa normal dos dados, a maioria dos valores dos encargos totais está concentrada entre o primeiro quartil (Q1) de 7396.2 e o terceiro quartil (Q3) de 30.7k. Essa faixa intermediária indica que a maior parte dos encargos totais está distribuída dentro desse intervalo. No entanto, a mediana, que representa o valor central dos dados, é bastante baixa em relação ao limite superior do boxplot. Essa diferença entre a mediana e o limite superior justifica a presença de uma quantidade considerável de outliers acima do upper fence do mesmo.</p>
    - <p style='text-indent: 20px; text-align: justify;'>Essa análise sugere que existem alguns casos com encargos totais muito elevados, que estão além da faixa normal de variação. Esses outliers podem indicar situações especiais ou excepcionais que resultam em encargos financeiros substancialmente mais altos.</p>
  """
)

create_box(
  data_costs, 
  x='Total Costs', 
  title='Boxplot Total Costs',
  p="""
    <p style='text-indent: 20px; text-align: justify;'>A maioria dos valores dos custos totais está concentrada entre o primeiro quartil (Q1) de 3k e o terceiro quartil (Q3) de 11.49k. Essa faixa intermediária indica que a maior parte dos custos totais está distribuída dentro desse intervalo, no entanto, a mediana, que representa o valor central dos dados, é relativamente baixa em relação ao limite superior do boxplot. Essa diferença entre a mediana e o limite superior justifica a presença de um número significativo de outliers acima desse limite, isso sugere que existem alguns casos com custos totais excepcionalmente altos, que estão além da variação normal observada. Esses outliers podem indicar situações especiais ou eventos incomuns que resultaram em custos financeiros substancialmente mais altos.</p>
    - <p style='text-indent: 20px; text-align: justify;'>Essa análise sugere que existem alguns casos com encargos totais muito elevados, que estão além da faixa normal de variação. Esses outliers podem indicar situações especiais ou excepcionais que resultam em encargos financeiros substancialmente mais altos.</p>
  """
)

st.markdown('### Correlação entre os boxplots de Encargos Totais e Custos Totais')
st.markdown(''' 
            <p style='text-indent: 20px; text-align: justify;'>Podemos observar uma correlação entre os outliers dos dois boxplots. Casos com encargos totais mais altos também tendem a apresentar custos totais elevados, e vice-versa. Isso sugere que há uma relação entre os encargos totais e os custos totais, em que os valores mais altos em uma variável geralmente correspondem a valores mais altos na outra variável. No entanto, é importante ressaltar que essa correlação não indica necessariamente uma relação causal direta entre as variáveis. Outros fatores, como a complexidade do tratamento, a duração da internação ou o tipo de cuidado necessário, podem influenciar tanto os encargos totais quanto os custos totais.</p>
            - <p style='text-indent: 20px; text-align: justify;'>A análise conjunta dos boxplots de custos totais e encargos totais nos fornece uma visão abrangente da relação entre essas variáveis e ajuda a identificar padrões e casos atípicos que merecem investigação adicional.</p>'''
            , unsafe_allow_html=True)


graph_dispersion(
  data_costs,
  x='Total Costs', 
  y='Total Charges',
  title='Graph dispersion'
)
st.plotly_chart(px.line(data_costs, x='Total Costs', y='Total Charges', title='Graph Line', color='Type of Admission'))

st.plotly_chart(px.funnel(data_costs, x='Total Costs', y='Total Charges', title='Graph Funnel'))

st.plotly_chart(px.sunburst(data_costs, path=['Type of Admission'], values='Total Costs'))

st.plotly_chart(px.histogram(data_costs, x='Total Costs', color='Type of Admission'))

fig = px.bar(
  data_costs, 
  x='Total Costs', 
  y='Total Charges', 
  color='Type of Admission',
  color_discrete_map={
    'Elective': '#B6E880',
    'Emergency': '#3366CC',
    'Urgent': '#D62728',
    'Not Available': 'rgb(251, 180, 174)',
    'Newborn': 'rgb(136, 204, 238)',
  }
)
fig.update_traces(width=10000)
st.plotly_chart(fig)

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