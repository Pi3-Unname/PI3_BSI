import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

"""
d = pd.read_parquet('alg/hospital3.parquet')
array = [
  'Home or Self Care',
  'Home w/ Home Health Services'
  'Inpatient Rehabilitation Facility',
  'Expired'
  'Hospice - Medical Facility',
  'Left Against Medical Advice'
  'Skilled Nursing Home',
  'Court/Law Enforcement',
  'Hospice - Home'
  'Short-term Hospital',
  'Psychiatric Hospital or Unit of Hosp'
  'Facility w/ Custodial/Supportive Care'
  'Medicare Cert Long Term Care Hospital',
  'Another Type Not Listed'
  'Federal Health Care Facility' "Cancer Center or Children's Hospital"
  'Critical Access Hospital',
  'Hosp Basd Medicare Approved Swing Bed',
  'Medicaid Cert Nursing Facility',
  None]

print(d.isnull().sum())
print(d['Patient Disposition'].unique())
"""


data = pd.read_parquet('venv\project\data\hospital.parquet')

ProfileReport(data, title='test').to_file('venv\project/reports/hospital2.html')

