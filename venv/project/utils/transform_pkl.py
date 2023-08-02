import pandas as pd
from typing import Tuple, List
import numpy as np
import pickle

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def equal_target(data, n):
  new_data = data.groupby('Total Costs Category').apply(
  lambda x: x.sample(n=min(len(x), n), random_state=2)
  ).reset_index(drop=True)
  new_data.drop(['APR DRG Description', 'APR MDC Description', 'APR Severity of Illness Description'], axis=1, inplace=True)
  return new_data

def label_json(x_data):
  le = LabelEncoder()
  le.fit(x_data)
  classes = le.classes_
  numbers = le.transform(classes)
  return dict(zip(classes, numbers))

def label_encoder(data: pd.DataFrame)-> Tuple[np.ndarray, np.ndarray, List[int]]:
  '''(x_data, y_data, colunas que sofreram label)'''
  x_data = data.iloc[:, 0:(len(data.columns)-1)].values
  y_data = data.iloc[:, (len(data.columns)-1)].values
  
  label = LabelEncoder()
  """
  json = {}
  for column in data.columns:
      json[column] = label_json(data[column])
  df_json = pd.DataFrame(json)
  df_json.to_csv('venv/project/data/classes.csv') 
  """
  columns_process = []
  x_data_standard = StandardScaler()
  for key, value in enumerate(x_data[0].tolist()):
    if(not((type(value) == int) or (type(value) == float))):
      x_data[:, key] = label.fit_transform(x_data[:, key])
      columns_process.append(key)
      
  return x_data_standard.fit_transform(x_data), y_data, columns_process



def onehot_encoder(x_data: np.ndarray, columns_process, ) -> np.ndarray:
  onehot = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), columns_process)], remainder='passthrough')
  return onehot.fit_transform(x_data).toarray()

def save_pkl(
  x_data: np.ndarray, y_data: np.ndarray, path: str = 'data.pkl', per: int =0.1, random: int=0
  )-> None:
  '''save(x_training, y_training, x_teste, y_teste)'''
  x_training, x_teste, y_training, y_teste = train_test_split(
    x_data, y_data, test_size=per, random_state=random
    )
  with open(path, mode='wb') as f:
    pickle.dump([x_training, y_training, x_teste, y_teste], f)
  
  
  
data = equal_target(pd.read_parquet('venv/project/data/hospital.parquet'), 2500)
x_data, y_data, columns = label_encoder(data)
save_pkl(x_data, y_data, 'venv/project/data/hospital_standard.pkl')
