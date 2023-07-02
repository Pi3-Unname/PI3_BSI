import streamlit as st
import pandas as pd
import plotly.express as px

from replace_value import replace_values
from build_hearder import build_header
from graph_treemap import graph_treemap
from create_boxplot import create_box

# Diagnostico
# Gênero
# Idade

build_header(
  title="Análise de tempo de estadia",
  header='Análise de tempo de estadia',
  layout='centered',
)

data = pd.read_parquet('venv/project/data/hospital_100k.parquet')

data_diagnostic = data[['Age Group', 'Gender', 'APR DRG Code', 'APR DRG Description']]

# Tabela apenas com os dados usados nessa seção
_, c2, _ = st.columns((1,7,1))
c2.write(data_diagnostic)


graph_treemap(
  data=data_diagnostic, 
  options=data_diagnostic.columns.to_list(),
  default=data_diagnostic.columns.to_list()[:2],
)

replace_values(
  data_diagnostic, 
  'Age Group',
  {
    '0 to 17': 0,
    '18 to 29': 1,
    '30 to 49': 2,
    '50 to 69': 3,
    '70 or Older': 4,
  }
)

# Boxplot de tempo de estadia
create_box(
  data_diagnostic, 
  x='Age Group',
  title='Boxplot of Length of Stay',
  label_mapX={
    0: '0 to 17',
    1: '18 to 29',
    2: '30 to 49',
    3: '50 to 69',
    4: '70 or Older',
  },
  p='''
  <p style='text-align: justify; text-indent: 15px;'>Observando o boxplot, podemos notar que a maioria das idades está concentrada entre os 18 e 29 anos, representando o primeiro quartil (Q1). Isso indica a presença de um grupo significativo de indivíduos mais jovens nos dados. A mediana, que está na faixa dos 50 aos 69 anos, divide o conjunto de dados ao meio. Essa medida central indica que há uma distribuição equilibrada entre idades mais jovens e idades mais avançadas, à medida que avançamos para o terceiro quartil (Q3), observamos que as idades se estendem além dos 70 anos ou mais. Isso sugere a presença de um grupo considerável de indivíduos mais velhos nos dados, além disso, é importante destacar que o boxplot não mostra a presença de valores atípicos ou extremos no conjunto de dados de idades. Essa ausência indica que a maioria das idades está dentro dos limites do boxplot, sem ocorrência de valores excepcionalmente altos ou baixos.</p>
  '''
)

data_Age_Gender = data_diagnostic.groupby(['Age Group', 'Gender']).size().reset_index(name='Total')

fig_line = px.line(data_Age_Gender, x='Age Group', y='Total', color='Gender',)
label_mapX = {
  0: '0 to 17',
  1: '18 to 29',
  2: '30 to 49',
  3: '50 to 69',
  4: '70 or Older',
  }
fig_line.update_xaxes(
  ticktext=[label_mapX[label] for label in data_Age_Gender['Age Group']],
  tickvals=data_Age_Gender['Age Group']
  )
st.plotly_chart(fig_line)
st.markdown('''
            
  <p style='text-align: justify; text-indent: 15px;'>No gráfico de linhas que relaciona os grupos etários (age groups) com o total de registros, podemos obter uma melhor compreensão da relação entre a faixa etária e o número de internações. Analisando os dados separadamente por gênero, podemos observar padrões interessantes.</p>

  <p style='text-align: justify; text-indent: 15px;'>Para os homens, podemos observar que a faixa etária com o maior número de internações é de 50 a 69 anos. Isso indica que os homens nessa faixa etária têm uma maior incidência de necessidade de cuidados médicos e hospitalização, por outro lado, para as mulheres, a faixa etária com o maior número de internações é de 70 anos ou mais. Isso sugere que as mulheres mais idosas tendem a demandar mais serviços de saúde e hospitalização.</p>

  <p style='text-align: justify; text-indent: 15px;'>Por outro lado, os grupos de idade que apresentam o menor número de internações são os homens de 18 a 29 anos e as mulheres de 0 a 17 anos. Isso pode indicar uma baixa procura por serviços de saúde nesses grupos específicos.</p>

  <p style='text-align: justify; text-indent: 15px;'>Essa diferença pode ser atribuída a vários fatores. Para os homens até os 30 anos, é possível que existam fatores sociais, culturais ou comportamentais que influenciem essa baixa busca por serviços de saúde. Esses fatores podem incluir uma percepção de boa saúde, menor preocupação com exames médicos de rotina ou menor conscientização sobre a importância do cuidado preventivo.    </p>    
            
''', unsafe_allow_html=True
)


_, c, _ = st.columns((1, 7, 1))
data_code = data_diagnostic.groupby(['APR DRG Code', 'APR DRG Description', 'Gender']).size().reset_index(name='Total').sort_values('APR DRG Code', ascending=True)
c.write(data_code)

st.plotly_chart(px.line(data_code, x='APR DRG Code', y='Total', labels={'index': 'Quanti' }))