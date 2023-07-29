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
data_stay = data.groupby(['Type of Admission','Hospital County','Operating Certificate Number','Facility ID','Age Group', 'APR Risk of Mortality','Health Service Area', 'Length of Stay',]).size().reset_index(name='Total')
#data_stay = data_stay.rename(columns={'Age Group': 'Age_Group'})
data_stay.sort_values('Total', ascending=True, inplace=True)

st.write(data.columns)

graph(data,x = 'Length of Stay', options = data.columns, type_graph=px.bar, type_txt='...')