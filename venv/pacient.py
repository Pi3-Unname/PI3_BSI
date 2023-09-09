from datetime import date
import numpy as np
import pickle

class Pacient:
  def __init__(self):
    self._area= ''
    self._hospital_county= ''
    self._hospital_name= ''
    self._age = 0
    self._age_group= ''
    self._gender = ''
    self._race = ''
    self._ethnicity = ''
    self._stay = ''
    self._admission = ''
    self._patient_disposition = ''
    self._APR_DRG_code = 0
    self._APR_MDC_code = 0
    self._disease_severity_code = ''
    self._risck_mortality = ''
    self._type_pay = ''
    self._Attending_license_number = 0
    self._Operating_license_number = 0
    self._Abortion_Indicator= ''
    self._Emergency_Indicator= ''
    self._medical_description= ''

  def set_gender(self, value):
    match value:
      case 'Male':
        self._gender = 'M'
      case 'Female':
        self._gender = 'F'
      case _:
        self._gender = 'U'    
  def get_gender(self):
    return self._gender
  
  def set_age(self, value):
    self._age = (date.today() - value).days // 365
    
    if (0 <= self._age and self._age < 18):
      self._age_group = 0
    elif (18 <= self._age and self._age < 30):
      self._age_group = 1
    elif (30 <= self._age and self._age < 50):
      self._age_group = 2
    elif (50 <= self._age and self._age < 70):
      self._age_group = 3
    else:
      self._age_group = 4
  def get_age(self):
    return self._age_group

  def set_area(self, value):
    self._area= value
  def set_hospital_county(self, value):
    self._hospital_county= value
  def set_hospital_name(self, value):
    self._hospital_name= value
  def set_race(self, value):
    self._race = value
  def set_ethnicity(self, value):
    self._ethnicity = value
  def set_stay(self, value):
    self._stay = value
  def set_admission(self, value):
    self._admission = value
  def set_patient_disposition(self, value):
    self._patient_disposition = value
  def set_APR_DRG_code(self, value):
    self._APR_DRG_code = int(value)
  def set_APR_MDC_code(self, value):
    self._APR_MDC_code = int(value)
    
  def set_disease_severity_code(self, value):
    match value:
      case 'Minor':
        self._disease_severity_code = 1
      case 'Moderate':
        self._disease_severity_code = 2
      case 'Major':
        self._disease_severity_code = 3
      case 'Extreme':
        self._disease_severity_code = 4
    
  def set_risck_mortality(self, value):
    self._risck_mortality = value
  def set_type_pay(self, value):
    self._type_pay = value
  def set_Attending_license_number(self, value):
    self._Attending_license_number = value
  def set_Operating_license_number(self, value):
    self._Operating_license_number = value
  def set_Abortion_Indicator(self, value):
    self._Abortion_Indicator= 1 if value else 0
  def set_Emergency_Indicator(self, value):
    self._Emergency_Indicator= 1 if value else 0
  def set_medical_description(self, value):
    self._medical_description = value
  
  def getValues(self):
    return{
      'Health Service Area': self._area,
      'Hospital County': self._hospital_county,
      'Facility Name': self._hospital_name,
      'Age Group': self._age_group,
      'Gender': self._gender,
      'Race': self._race,
      'Ethnicity': self._ethnicity,
      'Length of Stay': self._stay,
      'Type of Admission': self._admission,
      'Patient Disposition': self._patient_disposition,
      'APR DRG Code': self._APR_DRG_code,
      'APR MDC Code': self._APR_MDC_code,
      'APR Severity of Illness Code': self._disease_severity_code,
      'APR Risk of Mortality': self._risck_mortality,
      'APR Medical Surgical Description': self._medical_description,
      'Source of Payment 1': self._type_pay,
      'Attending Provider License Number': self._Attending_license_number,
      'Operating Provider License Number': self._Operating_license_number,
      'Abortion Edit Indicator': self._Abortion_Indicator,
      'Emergency Department Indicator': self._Emergency_Indicator,
    }

  def getvec(self):
    return np.array(
      [
        [self._area, self._hospital_county, self._hospital_name, self._age_group,
        self._gender, self._race, self._ethnicity, self._stay, self._admission,
        self._patient_disposition, self._APR_DRG_code, self._APR_MDC_code,
        self._disease_severity_code, self._risck_mortality, self._medical_description,
        self._type_pay, self._Attending_license_number, self._Operating_license_number,
        self._Abortion_Indicator, self._Emergency_Indicator,],
        ])
  def predict(self):
    x_data = self.getvec()
    with open('venv/project/data/label_standard.pkl', 'rb') as f:
      standard, _, label_service_Area, label_hospital_county, label_facility_name, label_gender, label_race, label_ethnicity, label_type_dmission, label_disposition, label_risk_mortality, label_medical_surgical, label_payment, _, _, _ = pickle.load(f)
 
    x_data[:, 0] = int(label_service_Area.transform(x_data[:, 0]))
    x_data[:, 1] = label_hospital_county.transform(x_data[:, 1])
    x_data[:, 2] = label_facility_name.transform(x_data[:, 2])
    x_data[:, 4] = label_gender.transform(x_data[:, 4])
    x_data[:, 5] = label_race.transform(x_data[:, 5])
    x_data[:, 6] = label_ethnicity.transform(x_data[:, 6])
    x_data[:, 8] = label_type_dmission.transform(x_data[:, 8])
    x_data[:, 9] = label_disposition.transform(x_data[:, 9])
    x_data[:, 13] = label_risk_mortality.transform(x_data[:, 13])
    x_data[:, 14] = label_medical_surgical.transform(x_data[:, 14])
    x_data[:, 15] = label_payment.transform(x_data[:, 15])
    x_data = standard.transform(x_data)
    with open('venv/project/data/random_forest.pkl', 'rb') as f:
      random_forest= pickle.load(f)
    return random_forest.predict(x_data)
