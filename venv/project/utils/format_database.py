from typing import List
import pandas as pd

def columns_process(data: pd.DataFrame, del_columns: List[str]) -> pd.DataFrame:
  # Processamento de colunas
  data_modify = data.drop(del_columns, axis=1) #Deletando colunas as quais não serão utilizadas
  
  # Tratamento de valores nulos
  data_modify['APR Risk of Mortality'].fillna('minor', inplace=True)
  data_modify['APR Severity of Illness Description'].fillna('minor', inplace=True)
  
  # Tratamento de valores inconsistentes
  data_modify.drop(24036, inplace=True)
  data_modify['Length of Stay'] = data_modify['Length of Stay'].apply(format_length_stay)
  
  return data_modify

def format_length_stay(value) -> int:
  if (value == '120 +'):
    return 120
  return int(value)


def transformat_parquet(data: pd.DataFrame, columns: List[str], path: str) -> None:
  #Transformado dataframe em um arquivo .parquet
  try:
    data_base = columns_process(data, columns)
    data_base.to_parquet(path) 
    print('OK.')
  except:
    print('Fail.')
    
def parquet_random(path: str, num: int) -> None:
  #Transforma um aquivo .parquet em um menor, com menos registros
  data = pd.read_parquet(path)
  new_data = data.sample(num, replace=False)
  num2 = ''.join(reversed(''.join(reversed(f'{num}')).replace('000', 'k')))
  new_data.to_parquet(path.replace('.', f'_{num2}.'))
  
""" columns_drop = [
  'index',
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

database = pd.read_csv('alg\data\hospital.csv')
print(database)
transformat_parquet(database, columns_drop, 'alg/data/hospital.parquet')  """
parquet_random('venv\project\data\hospital.parquet', 500)
#print(pd.read_parquet('alg/data/hospital.parquet'))

