import pandas as pd

database = pd.read_csv('alg/hospital.csv')
database

database.isnull().sum()

# Tratando os valores nulos do 'Zip Code - 3 digits'

database['Zip Code - 3 digits'].fillna(0, inplace=True)
database.loc[database['Zip Code - 3 digits'] == 'OOS', 'Zip Code - 3 digits'] = 0
database.isnull().sum()

# Excluindo colunas que não fazem sentido para o processamento

columns_drop = [
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

data_modify = database.drop(columns_drop, axis=1)
data_modify.isnull().sum()

data_modify.loc[pd.isnull(data_modify['Race'])]

# Excluindo registro com todas as células vazias

data_modify.drop(24036, inplace=True)

data_modify.isnull().sum()

data_modify.loc[pd.isnull(data_modify['APR Severity of Illness Description'])]

data_modify['APR Risk of Mortality'].value_counts()

data_modify['APR Severity of Illness Description'].value_counts()

# Tratei transformando o valor dos camos 'APR Severity of Illness Description' e 'APR Risk of Mortality' de nulo para a classe 'minor' por não termos informações necessarias para classificar de forma correta.

data_modify['APR Risk of Mortality'].fillna('minor', inplace=True)
data_modify['APR Severity of Illness Description'].fillna('minor', inplace=True)

data_modify.isnull().sum()

hospital_1000 = data_modify.sample(1000, replace=False)
hospital_2000 = data_modify.sample(2000, replace=False)
hospital_5000 = data_modify.sample(5000, replace=False)
hospital_10000 = data_modify.sample(10000, replace=False)
hospital_50000 = data_modify.sample(50000, replace=False)
hospital_100000 = data_modify.sample(100000, replace=False)

hospital_1000.to_csv('alg/hospital_1K.csv')
hospital_2000.to_csv('alg/hospital_2K.csv')
hospital_5000.to_csv('alg/hospital_5K.csv')
hospital_10000.to_csv('alg/hospital_10K.csv')
hospital_50000.to_csv('alg/hospital_50K.csv')
hospital_100000.to_csv('alg/hospital_100K.csv')




