from typing import List
import pandas as pd

def columns_process(data: pd.DataFrame, del_columns: List[str]) -> pd.DataFrame:
  
  test_lista= [0, 5, 10, 30, 50, 100, 200, 300]
  lista_costs_category = category_costs(test_lista, edit_total_costs(data))
  data.insert(38, 'Total Costs Category', lista_costs_category)
  
  data_modify = data.drop(del_columns, axis=1) 
  data_modify = setting_values_null(data_modify)
  
  data_modify['Length of Stay'] = data_modify['Length of Stay'].apply(format_length_stay)
  
  return data_modify

def format_length_stay(value) -> int:
  if (value == '120 +'):
    return 120
  return int(value)

def setting_values_null(data):
  data['Attending Provider License Number'].fillna(0, inplace=True)
  data['Operating Provider License Number'].fillna(0, inplace=True)
  data["Patient Disposition"].fillna("Home or Self Care", inplace=True)
  data["APR Severity of Illness Description"].fillna("Minor", inplace=True)
  data["APR Risk of Mortality"].fillna("Minor", inplace=True)
  data["Hospital County"].fillna("Manhattan", inplace=True)
  data["Health Service Area"].fillna("New York City", inplace=True)
  return data

def edit_total_costs(data: pd.DataFrame) -> List[float]:
  lista_costs = [None] * len(data)

  for i in data['index']:
    lista_costs[i] = float(data.iloc[i, 37])
    
  return lista_costs

def category_costs(list_classes: List[int], old_values: List[float]):
  list_classes.sort()
  new_list = [None] * len(old_values)
  for i, old in enumerate(old_values):
    for index, value in enumerate(list_classes):
      if(len(list_classes)-1 == index):
        new_list[i] = f'mais de {value}k'
      else:
        if(value*1000 <= old < list_classes[index+1]*1000):
          new_list[i] = f'{value}k a {list_classes[index+1]}k'
          break
  return new_list


def transformat_parquet(data: pd.DataFrame, columns: List[str], path: str) -> None:
  #Transformado dataframe em um arquivo .parquet
  #try:
  data_base = columns_process(data, columns)
  data_base.to_parquet(path) 
  print('OK.')
  #except:
  #  print('Fail.')
    
def parquet_random(path: str, num: int) -> None:
  #Transforma um aquivo .parquet em um menor, com menos registros
  data = pd.read_parquet(path)
  new_data = data.sample(num, replace=False)
  num2 = ''.join(reversed(''.join(reversed(f'{num}')).replace('000', 'k')))
  new_data.to_parquet(path.replace('.', f'_{num2}.'))
  
columns_drop = [
  'index',
  'Other Provider License Number', # Mais de 70% de valores nulos
  'Source of Payment 2',
  'Source of Payment 3',
  'Discharge Year', #Todos os anos são 2010
  'CCS Diagnosis Code',
  'CCS Diagnosis Description',
  'CCS Procedure Code',
  'CCS Procedure Description',
  'Birth Weight', # Não temos informação da unidade de medida dos pesos e mais de 70% dos valores esta zerado
  'Operating Certificate Number',
  'Facility ID',
  'Zip Code - 3 digits',
]

#database = pd.read_csv('venv\project\data\hospital.csv')
#transformat_parquet(database, columns_drop, 'venv\project\data\hospital.parquet')

for i in [500, 1000, 100000]:
  parquet_random('venv\project\data\hospital.parquet', i)

#print(pd.read_parquet('alg/data/hospital.parquet'))

# all_colmuns_data = ['index',                                      
# 'Health Service Area',                       
# 'Hospital County',                           
# 'Operating Certificate Number',              
# 'Facility ID',                               
# 'Facility Name',                              
# 'Age Group',                                  
# 'Zip Code - 3 digits',                       
# 'Gender',                                     
# 'Race',                                       
# 'Ethnicity',                                  
# 'Length of Stay',                             
# 'Type of Admission',                          
# 'Patient Disposition',                        
# 'Discharge Year',                             
# 'CCS Diagnosis Code',                        
# 'CCS Diagnosis Description',                 
# 'CCS Procedure Code',                        
# 'CCS Procedure Description',                 
# 'APR DRG Code',                               
# 'APR DRG Description',                        
# 'APR MDC Code',                               
# 'APR MDC Description',                        
# 'APR Severity of Illness Code',               
# 'APR Severity of Illness Description',        
# 'APR Risk of Mortality',                      
# 'APR Medical Surgical Description',           
# 'Source of Payment 1',                        
# 'Source of Payment 2',                     
# 'Source of Payment 3',                    
# 'Attending Provider License Number',         
# 'Operating Provider License Number',       
# 'Other Provider License Number',          
# 'Birth Weight',                               
# 'Abortion Edit Indicator',                    
# 'Emergency Department Indicator',             
# 'Total Charges',                              
# 'Total Costs']