from typing import List
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

#Transformando os valores em Array list
def label_encoder_all_coloumns(data: pd.DataFrame):
  x_datas = data.iloc[:, 0:23].values #Colocando campos que prelecionados
  y_datas = data.iloc[:, 23].values #Definindo campo de previsão

  label = LabelEncoder()
  columns = []

  for x in range(len(data.columns)-1):
    if not((type(x_datas[0, x]) == float) or (type(x_datas[0, x]) == int)):
      x_datas[:, x] = label.fit_transform(x_datas[:, x])
      columns.append(x)
  return x_datas, y_datas, columns

# Transformando as colunas em One Hot Encoder
def onehot_encoder(x_label: np.ndarray, columns: List[int]) -> np.ndarray:
  onehot = ColumnTransformer(transformers=[(
    'OneHot', 
    OneHotEncoder(), 
    columns,
    )], remainder='passthrough')
  x = onehot.fit_transform(x_label).toarray()
  return x
   
# Escalonamento dos valores das colunas depois que estiverem convertido, e transformando em pkl
def scaler_columns(data):
  x, y, columns = label_encoder_all_coloumns(data)
  x = onehot_encoder(x, columns)
  x = StandardScaler().fit_transform(x)

  return train_test_split(x, y, test_size=0.1, random_state=0)

import pickle
def save_pkl(x_training, x_test, y_training, y_test, path):
  with open(path, mode='wb') as f:
    pickle.dump([x_training, y_training, x_test, y_test], f)


#Carregando base excluindo o index
""" data = pd.read_parquet('alg/data/hospital_100k.parquet')
print(data['APR Risk of Mortality'].unique()) """
#x_training, x_test, y_training, y_test = scaler_columns(data)

""" naive = GaussianNB()
naive.fit(x_training, y_training)
previsa
 """
#save_pkl(x_training, x_test, y_training, y_test, 'alg/data/hospital.pkl')