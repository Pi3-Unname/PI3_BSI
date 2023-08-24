import pandas as pd
import streamlit as st

data = pd.read_csv('alg\hospital_edited_dataset.csv')

hospital_1000 = data.sample(1000, replace=False)
hospital_2000 = data.sample(2000, replace=False)
hospital_5000 = data.sample(5000, replace=False)
hospital_10000 = data.sample(10000, replace=False)
hospital_50000 = data.sample(50000, replace=False)
hospital_100000 = data.sample(100000, replace=False)

#st.write(hospital_1000)
#a = data['Hospital Country'].value_counts()
#st.write(a)
columns = [
  'Unnamed: 0', 
  'index', 
  'Health Service Area', 
  'Hospital County', #Possui 58 valores diferentes
  'Operating Certificate Number', 
  'Facility ID', 
  'Facility Name',       
  'Age Group', 
  'Gender', 
  'Race',
  'Ethnicity',
  'Length of Stay',
  'Type of Admission',
  'Patient Disposition', 
  'APR DRG Code',
  'APR DRG Description', 
  'APR MDC Code', 
  'APR MDC Description',
  'APR Severity of Illness Code', 
  'APR Severity of Illness Description',
  'APR Risk of Mortality', 
  'APR Medical Surgical Description',
  'Source of Payment 1', 
  'Emergency Department Indicator',
  'Total Charges', 
  'Total Costs'
]

hospital_1000.to_csv('alg/hospital_1K.csv')
hospital_2000.to_csv('alg/hospital_2K.csv')
hospital_5000.to_csv('alg/hospital_5K.csv')
hospital_10000.to_csv('alg/hospital_10K.csv')
hospital_50000.to_csv('alg/hospital_50K.csv')
hospital_100000.to_csv('alg/hospital_100K.csv')

""" data1 = pd.read_parquet('alg\hospital_1k.parquet')
data2 = pd.read_parquet('alg\hospital_2k.parquet')
st.header('Dados com 1k')
st.write(data1)
st.header('Dados de 2k')
st.write(data2) """