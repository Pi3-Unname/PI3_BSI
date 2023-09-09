import pandas as pd
import plotly.express as px
import streamlit as st
import pickle
import numpy as np

import os
from transform_dump_stay import main

from build_hearder import build_header
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

build_header(
  title="Compare machine learning sem o atributo Length of Stay",
  header='Compare machine learning sem o atributo Length of Stay',
  layout='centered',
)

def table_report(y_test: np.ndarray, previsao: np.ndarray, method:str =''):
  st.markdown(f'#### Classification report do médoto <span style="color: red">{method}</span>', unsafe_allow_html=True)
  report = classification_report(y_test, previsao, output_dict=True)
  df_classification_report = pd.DataFrame(report).transpose()
  st.table(df_classification_report)

def confusion_graph(y_test, previsao, method:str = ''):
  st.markdown(f'#### Matriz de Confução do médoto <span style="color: red">{method}</span>', unsafe_allow_html=True)
  labels = sorted(list(set(y_test) | set(previsao)))
  cm = pd.DataFrame(0, index=labels, columns=labels)
  for true_label, predicted_label in zip(y_test, previsao):
      cm.loc[true_label, predicted_label] += 1
  st.table(cm)
   
def naive_bayes_no_stay(
  x_training: np.ndarray, y_training: np.ndarray, x_test: np.ndarray, y_test: np.ndarray
  )-> None:
  st.markdown('### Resultado do machine learning usando o método Naive Bayes')
  if not(os.path.isfile('venv/project/data/naive_bayes_no_stay.pkl')):
    naive_bayes_no_stay = GaussianNB()
    naive_bayes_no_stay.fit(x_training, y_training)
    with open('venv/project/data/naive_bayes_no_stay.pkl', mode='wb') as f:
      pickle.dump(naive_bayes_no_stay, f)
  else:
    with open('venv/project/data/naive_bayes_no_stay.pkl', 'rb') as f:
      naive_bayes_no_stay = pickle.load(f)
  previsao_naive = naive_bayes_no_stay.predict(x_test)
  table_report(y_test, previsao_naive, 'Naive Bayes')
  confusion_graph(y_test, previsao_naive, 'Naive Bayes')
  
def tree_decision_no_stay(
  x_training: np.ndarray, y_training: np.ndarray, x_test: np.ndarray, y_test: np.ndarray
  )-> None:
  st.markdown('### Resultado do machine learning usando o método Árvore de decisão')
  if not(os.path.isfile('venv/project/data/tree_decision_no_stay.pkl')):
    tree_decision_no_stay = DecisionTreeClassifier(criterion='entropy')
    tree_decision_no_stay.fit(x_training, y_training)
    with open('venv/project/data/tree_decision_no_stay.pkl', mode='wb') as f:
      pickle.dump(tree_decision_no_stay, f)
  else:
    with open('venv/project/data/tree_decision_no_stay.pkl', 'rb') as f:
      tree_decision_no_stay = pickle.load(f)
  prevision_tree = tree_decision_no_stay.predict(x_test)
  table_report(y_test, prevision_tree,'Árvore de decisão')
  confusion_graph(y_test, prevision_tree, 'Árvore de decisão')
  
def random_forest_no_stay(
  x_training: np.ndarray, y_training: np.ndarray, x_test: np.ndarray, y_test: np.ndarray
  )-> None:
  st.markdown('### Resultado do machine learning usando o método Random Forest')
  
  if not(os.path.isfile('venv/project/data/random_forest_no_stay.pkl')):
    random_forest_no_stay = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
    random_forest_no_stay.fit(x_training, y_training)
    with open('venv/project/data/random_forest_no_stay.pkl', mode='wb') as f:
      pickle.dump(random_forest_no_stay, f)
  else:
    with open('venv/project/data/random_forest_no_stay.pkl', 'rb') as f:
      random_forest_no_stay = pickle.load(f)
      
  prevision_random_forest = random_forest_no_stay.predict(x_test)
  importances = pd.Series(
    data=random_forest_no_stay.feature_importances_, 
    index=[
      'Health Service Area', 'Hospital County', 'Facility Name', 'Age Group',
      'Gender', 'Race', 'Ethnicity', 'Length of Stay', 'Type of Admission',
      'Patient Disposition', 'APR DRG Code', 'APR MDC Code',
      'APR Severity of Illness Code', 'APR Risk of Mortality',
      'APR Medical Surgical Description', 'Source of Payment 1',
      'Attending Provider License Number',
      'Operating Provider License Number', 'Abortion Edit Indicator',
      'Emergency Department Indicator',
    ]
  )
  important = importances.to_frame()
  important.reset_index(inplace=True)
  important.columns = ['Importância','Feature', ]
  st.write('Gráfico de Importância de parametros')
  st.plotly_chart(px.bar(data_frame=important, x='Feature', y='Importância', orientation='h', template='plotly_dark'))
  table_report(y_test, prevision_random_forest, 'Random Forest')
  confusion_graph(y_test, prevision_random_forest, 'Random Forest')
  
if not(os.path.isfile('venv/project/data/hospital_standard.pkl')):
  print('teste')
  main()  

with open('venv/project/data/hospital_standard.pkl', 'rb') as f:
  x_training, y_training, x_test, y_test = pickle.load(f)
  
naive_bayes_no_stay(x_training, y_training, x_test, y_test)
tree_decision_no_stay(x_training, y_training, x_test, y_test)
random_forest_no_stay(x_training, y_training, x_test, y_test)

