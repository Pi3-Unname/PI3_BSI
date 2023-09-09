import pandas as pd
import streamlit as st
dados = pd.read_parquet('alg/hospital.parquet')

st.write(dados)
""" columns_drop = [
  'CCS Diagnosis Code',
  'CCS Diagnosis Description',
  'CCS Procedure Code',
  'CCS Procedure Description',
  'Attending Provider License Number',
  'Operating Provider License Number',
  'Other Provider License Number',
  'Birth Weight',
  'Abortion Edit Indicator',
  'Discharge Year',
  'Source of Payment 2',
  'Source of Payment 3',
  'Zip Code - 3 digits',
]

dados.drop(columns_drop, axis=1, inplace=True)
dados.drop(24036, inplace=True)

#dados['Length of Stay'].astype(str)
#dados['Length of Stay'].astype(int, errors='ignore')

dados['Length of Stay'] = dados['Length of Stay'].apply(lambda x: f'{x} days')

#st.write(dados.loc[dados['Length of Stay'] == '120 +'])

print(dados['Length of Stay'].unique())
#print(dados['Length of Stay'].value_counts())
dados.to_parquet('alg/hospital.parquet') """