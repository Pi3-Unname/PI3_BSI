import pandas as pd
import streamlit as st
import plotly.express as px

from build_hearder import build_header
from graph_treemap import graph_treemap
from create_boxplot import create_box
build_header(
    title='Análise de estadia',
    layout='centered',
    header='Análise de estadia'
)

data=pd.read_parquet('venv\project\data\hospital_100k.parquet')
data_stay = data.groupby(['Facility Name', 'Hospital County', 'Type of Admission', 'Ethnicity', 'Race']).size().reset_index(name='Total')
data_stay.sort_values('Total', ascending=True, inplace=True)

st.write(data_stay)

graph_treemap(
    data_stay,
    options=data_stay.columns,
)

create_box(
    data_stay,
    x='Hospital County',
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

bar_county = px.bar(
    data_county_admission, 
    x='Hospital County', 
    y='Total', 
    color='Hospital County',
)
#bar_county.update_traces(width=10)
st.plotly_chart(bar_county)


bar_county_admission = px.area(
    data_county_admission,
    y='Total',
    line_group='Type of Admission',
    x='Hospital County',
    color='Type of Admission',
)
#bar_county_admission.update_traces(width=10)
st.plotly_chart(bar_county_admission)
