import pandas as pd
import streamlit as st
import plotly.express as px

from build_hearder import build_header
from graph_treemap import graph_treemap, graph
from create_boxplot import create_box
build_header(
    title='Análise de admissões',
    layout='centered',
    header='Análise de admissões'
)

data=pd.read_parquet('venv\project\data\hospital_1k.parquet')
data_stay = data.groupby(['Facility Name','Facility ID','Type of Admission','Health Service Area','Hospital County','Operating Certificate Number','Age Group','Gender', 'Race', 'Ethnicity','Patient Disposition', 'APR Risk of Mortality','APR Medical Surgical Description']).size().reset_index(name='Total')
data_stay.sort_values('Total', ascending=True, inplace=True)

st.write(data_stay)
st.write('''<p style='Nas analises de admissões contém informações podem ajudar a identificar os principais impulsionadores na demanda dos diferentes tipos de admissão. </p> O campo de seleção a baixo é responsavel por gera infograficos, que relacionam as informações desejadas visualmente. </p>''',unsafe_allow_html=True)

st.write(data.columns)

graph_treemap(
    data_stay,
    options=data_stay.columns,
)

#Health ServiceCounty Area
fig_area = px.bar(
  data_stay, 
  x='Health Service Area', 
  y='Total', 
  color='Type of Admission',
)
st.plotly_chart(fig_area)

#Hospital County
bar_county_admission = px.area(
    data_stay,
    y='Total',
    line_group='Type of Admission',
    x='Hospital County',
    color='Type of Admission',
)
st.plotly_chart(bar_county_admission)

#Operating Certificate Number
fig_operating = px.bar(
  data_stay, 
  x='Type of Admission', 
  y='Operating Certificate Number', 
  color='Total',
)
st.plotly_chart(fig_operating)

#Facility ID
graphic_id_admission = px.scatter(
  data_stay, 
  x='Type of Admission', 
  y='Facility ID', 
  color='Total', 
)
st.plotly_chart(graphic_id_admission)

#Facility Name = Facility ID
data_facility_id_name = data.groupby(['Facility ID','Facility Name']).size().reset_index(name='Total')
st.write(data_facility_id_name)

#Age group
fig_age = px.bar(
  data_stay, 
  x='Age Group', 
  y='Total', 
  color='Type of Admission',
)
st.plotly_chart(fig_age)

#Gender
bar_gender_admission = px.bar(
  data_stay, 
  x='Type of Admission', 
  y='Total', 
  color='Gender',
)
st.plotly_chart(bar_gender_admission)

#Race
bar_race_admission = px.bar(
  data_stay, 
  x='Race', 
  y='Total', 
  color='Type of Admission',
)
st.plotly_chart(bar_race_admission)

#Ethnicity
fig_ethnicity = px.bar(
  data_stay, 
  x='Type of Admission', 
  y='Total', 
  color='Ethnicity',
)
st.plotly_chart(fig_ethnicity)

bar_mortality_admission = px.area(
    data_stay,
    y='Total',
    line_group='APR Risk of Mortality',
    x='Type of Admission',
    color='APR Risk of Mortality',
)
st.plotly_chart(bar_mortality_admission)




bar_disposition_admission = px.area(
    data_stay,
    y='Total',
    line_group='Patient Disposition',
    x='Type of Admission',
    color='Patient Disposition',
)
st.plotly_chart(bar_disposition_admission)

