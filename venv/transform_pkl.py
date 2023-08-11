import pandas as pd
from typing import Tuple, List
import numpy as np
import pickle
import os

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def equal_target(data: pd.DataFrame, n):
  data.drop(['APR DRG Description', 'APR MDC Description', 'APR Severity of Illness Description'], axis=1, inplace=True)
  training_label(data)
  new_data = data.groupby('Total Costs Category').apply(
  lambda x: x.sample(n=min(len(x), n), random_state=2)
  ).reset_index(drop=True)
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
  
  with open('venv/project/data/test.pkl', 'rb') as f:
        x_data_standard, label_service_Area, label_hospital_county, label_facility_name, label_gender, label_race, label_ethnicity, label_type_dmission, label_disposition, label_risk_mortality, label_medical_surgical, label_payment, label_age_group, label_abortion, label_emergency= pickle.load(f)

  columns_process = []
  for key, value in enumerate(x_data[0].tolist()):
    if(not((type(value) == int) or (type(value) == float))):
      columns_process.append(key)
  
  x_data[:, 0] = label_service_Area.transform(x_data[:, 0])
  x_data[:, 1] = label_hospital_county.transform(x_data[:, 1])
  x_data[:, 2] = label_facility_name.transform(x_data[:, 2])
  x_data[:, 3] = label_age_group.transform(x_data[:, 3])
  x_data[:, 4] = label_gender.transform(x_data[:, 4])
  x_data[:, 5] = label_race.transform(x_data[:, 5])
  x_data[:, 6] = label_ethnicity.transform(x_data[:, 6])
  x_data[:, 8] = label_type_dmission.transform(x_data[:, 8])
  x_data[:, 9] = label_disposition.transform(x_data[:, 9])
  x_data[:, 13] = label_risk_mortality.transform(x_data[:, 13])
  x_data[:, 14] = label_medical_surgical.transform(x_data[:, 14])
  x_data[:, 15] = label_payment.transform(x_data[:, 15])
  x_data[:, 18] = label_abortion.transform(x_data[:, 18])
  x_data[:, 19] = label_emergency.transform(x_data[:, 19])
  
  x_data = x_data_standard.transform(x_data)
    
  return x_data, y_data, columns_process

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
  
def training_label(data):
  x_data = data.iloc[:, 0:(len(data.columns)-1)].values
  
  if not(os.path.isfile('venv/project/data/encoder_standard.pkl')):
    label_service_Area = LabelEncoder() #0: Health Service Area
    label_hospital_county = LabelEncoder() #1: Hospital County
    label_facility_name = LabelEncoder() #2: Facility Name
    label_age_group = LabelEncoder() #3: Age Group
    label_gender = LabelEncoder() #4: Gender
    label_race = LabelEncoder() #5: Race
    label_ethnicity = LabelEncoder() #6: Ethnicity
    label_type_dmission = LabelEncoder() #8: Type of Admission
    label_disposition = LabelEncoder() #9: Patient Disposition
    label_risk_mortality = LabelEncoder() #13: APR Risk of Mortality
    label_medical_surgical = LabelEncoder() #14: APR Medical Surgical Description
    label_payment = LabelEncoder() #15: Source of Payment 1
    label_abortion = LabelEncoder() #18: Abortion Edit Indicator
    label_emergency= LabelEncoder() #19: Emergency Department Indicator
  
    x_data[:, 0] = label_service_Area.fit_transform(x_data[:, 0])
    x_data[:, 1] = label_hospital_county.fit_transform(x_data[:, 1])
    x_data[:, 2] = label_facility_name.fit_transform(x_data[:, 2])
    x_data[:, 3] = label_age_group.fit_transform(x_data[:, 3])
    x_data[:, 4] = label_gender.fit_transform(x_data[:, 4])
    x_data[:, 5] = label_race.fit_transform(x_data[:, 5])
    x_data[:, 6] = label_ethnicity.fit_transform(x_data[:, 6])
    x_data[:, 8] = label_type_dmission.fit_transform(x_data[:, 8])
    x_data[:, 9] = label_disposition.fit_transform(x_data[:, 9])
    x_data[:, 13] = label_risk_mortality.fit_transform(x_data[:, 13])
    x_data[:, 14] = label_medical_surgical.fit_transform(x_data[:, 14])
    x_data[:, 15] = label_payment.fit_transform(x_data[:, 15])
    x_data[:, 18] = label_abortion.fit_transform(x_data[:, 18])
    x_data[:, 19] = label_emergency.fit_transform(x_data[:, 19])
    standard = StandardScaler()
    standard.fit_transform(x_data, [0, 1, 2, 3, 4, 5, 6, 8, 9, 13, 14, 15, 18, 19] )
    with open('venv/project/data/test.pkl', mode='wb') as f:
      pickle.dump([
        standard, label_service_Area, label_hospital_county, label_facility_name,
        label_gender, label_race, label_ethnicity, label_type_dmission, 
        label_disposition, label_risk_mortality, label_medical_surgical, 
        label_payment, label_age_group, label_abortion, label_emergency
      ], f)
  
def main():
  #if not(os.path.isfile('venv/project/data/hospital_standard.pkl')):
    data = equal_target(pd.read_parquet('venv/project/data/hospital.parquet'), 2500)
    x_data, y_data, columns = label_encoder(data)
    save_pkl(x_data, y_data, 'venv/project/data/hospital_standard.pkl')

main()
