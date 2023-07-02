import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
import pandas as pd
from ydata_profiling import ProfileReport
import os
from build_hearder import build_header

def build_profile(path, dataframe):
  if not(os.path.exists(path)):
    profile = ProfileReport(dataframe, title=f"HOSPITAL DATASET")
    profile.to_file(path)
  components.html(open(path, 'r').read(), height= 1200, scrolling=True)

def open_profile(path):
  if os.path.exists(path):
    try:
      components.html(open(path, 'r').read(), height= 1200, scrolling=True)
    except:
      print('invalid path.')
  else:
    build_profile(path, pd.read_parquet('venv\project\data\hospital_1k.parquet'))
    
def graph_area(df, x, y, color=None, header=None):
  st.header(header)
  st.table(df)
  if (color == None):
    st.plotly_chart(px.bar(df, x=x, y=y, color='Gender'))
  else:
    st.plotly_chart(px.bar(df, x=x, y=y))

  st.header(f'x={x}')
  st.plotly_chart(px.box(df,  x=x))
  


data = pd.read_parquet('venv\project\data\hospital_100k.parquet')

build_header(
  title="Análise Exploratória",
  header='Análise Exploratória',
  paragraph='''<p>A análise exploratória de dados é uma etapa fundamental para compreender conjuntos de dados. Ela envolve a investigação inicial dos dados, identificando padrões, tendências e anomalias. Através de técnicas estatísticas e visuais, como gráficos e medidas descritivas, a análise exploratória permite entender a estrutura dos dados, identificar relacionamentos entre as variáveis e validar suposições. Além disso, ajuda a gerar hipóteses para análises mais aprofundadas. Essa análise é crucial para orientar o desenvolvimento de modelos e tomar decisões informadas com base nos dados disponíveis.</p>''',
)
open_profile('venv/project/reports/hospital.html')

data_age_group = data.groupby(['Gender', 'Age Group']).size().reset_index(name='Total')
data_age_group = data_age_group.rename(columns={'Age Group': 'Age_Group'})
data_age_group.sort_values('Total', ascending=True, inplace=True)

st.write(data.sort_values('Total Costs', ascending=True)['Total Costs'])

st.plotly_chart(px.box(data, y="Total Costs"))

graph_area(data_age_group, x='Age_Group', y='Total', header='Explorando relação de idade')