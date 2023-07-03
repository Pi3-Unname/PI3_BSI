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

data=pd.read_parquet('venv\project\data\hospital_100k.parquet')
data_stay = data.groupby(['Facility Name', 'Hospital County', 'Type of Admission', 'Ethnicity', 'Race']).size().reset_index(name='Total')
data_stay.sort_values('Total', ascending=True, inplace=True)

st.write(data_stay)

st.write('''<p style='text-align:justify;'> Na tabela a cima estão os dados de altas relevantes para as analises de admissões, entre estão eles, os 50 condados, o tipo de admissão de cada pascinete, sua etinia e raça. Essas informações podem ajudar a identificar os principais impulsionadores da demanda e a prever alterações futuras na demanda com base em tendências e fatores demográficos. </p> O campo de seleção a baixo é responsavel por gera infograficos, que relacionam as informações desejadas visualmente. </p>''',unsafe_allow_html=True
)

graph_treemap(
    data_stay,
    options=data_stay.columns,
)

st.write('''<p style='text-align:justify;'> A Próxima tabela referencia apenas os condados, os tipos de admissões e o total. Tonando os dados mais abragentes. Informações úteis para as organizações de saúde no planejamento da capacidade, alocação de recursos e otimização da prestação de serviços.</p>''',unsafe_allow_html=True
)

data_county_admission = data.groupby(['Hospital County', 'Type of Admission']).size().reset_index(name='Total')
data_county_admission.sort_values('Total', ascending=True, inplace=True )

bar_county = px.bar(
    data_stay, 
    x='Hospital County', 
    y='Total', 
    color='Hospital County',
)

st.write(data_county_admission,)

st.write('''<p style='text-align:justify;'>Com base nos dados foram gerados dois gráficos. O primeiro trata-se de um gráfico de barras, que ilustra a quantidade total de admissões por condato. O segundo, trata-se de um gráfico de área, no qual é possivel visualizar a quatidade de cada tipo de admissão por condado. Essas informações seriam valiosas para aprimorar a tomada de decisão e o planejamento estratégico, permitindo que essas organizações identifiquem áreas de melhoria, desenvolvam políticas mais eficazes e implementem estratégias.</p>''',unsafe_allow_html=True
)

bar_county = px.bar(
    data_county_admission, 
    x='Hospital County', 
    y='Total', 
    color='Hospital County',
)
#bar_county.update_traces(width=10)
st.plotly_chart(bar_county)

#gráfico de área 
bar_county_admission = px.area(
    data_county_admission,
    y='Total',
    line_group='Type of Admission',
    x='Hospital County',
    color='Type of Admission',
    )

#bar_county_admission.update_traces(width=10)
st.plotly_chart(bar_county_admission)

