import pandas as pd
import streamlit as st
import plotly.express as px

from build_hearder import build_header
from graph_treemap import graph_treemap
from create_boxplot import create_box
build_header(
    title='Análise de admissões',
    layout='centered',
    header='Análise de admissões'
)

data=pd.read_parquet('venv\project\data\hospital_1k.parquet')
data_stay = data.groupby(['Facility Name', 'Hospital County', 'Type of Admission','Age Group', 'Ethnicity', 'Race', 'APR Risk of Mortality']).size().reset_index(name='Total')
data_stay.sort_values('Total', ascending=True, inplace=True)

st.write(data_stay)
st.write('''<p style='Nas analises de admissões contém informações podem ajudar a identificar os principais impulsionadores na demanda dos diferentes tipos de admissão. </p> O campo de seleção a baixo é responsavel por gera infograficos, que relacionam as informações desejadas visualmente. </p>''',unsafe_allow_html=True
)

graph_treemap(
    data_stay,
    options=data_stay.columns,
)

bar_county_admission = px.area(
    data_stay,
    y='Total',
    line_group='Type of Admission',
    x='Hospital County',
    color='Type of Admission',
)
#bar_county_admission.update_traces(width=10)
st.plotly_chart(bar_county_admission)

bar_age_admission = px.area(
    data_stay,
    y='Total',
    line_group='Age Group',
    x='Type of Admission',
    color='Age Group',
)
#bar_age_admission.update_traces(width=10)
st.plotly_chart(bar_age_admission)

bar_ethnicity_admission = px.area(
    data_stay,
    y='Total',
    line_group='Ethnicity',
    x='Type of Admission',
    color='Ethnicity',
)
#bar_ethnicity_admission.update_traces(width=10)
st.plotly_chart(bar_ethnicity_admission)

bar_mortality_admission = px.area(
    data_stay,
    y='Total',
    line_group='APR Risk of Mortality',
    x='Type of Admission',
    color='APR Risk of Mortality',
)
#bar_ethnicity_admission.update_traces(width=10)
st.plotly_chart(bar_mortality_admission)

bar_race_admission = px.area(
    data_stay,
    y='Total',
    line_group='Race',
    x='Type of Admission',
    color='Race',
)
#bar_ethnicity_admission.update_traces(width=10)
st.plotly_chart(bar_race_admission)
