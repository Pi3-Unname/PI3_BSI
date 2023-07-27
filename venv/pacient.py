from datetime import date

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
    self._APR_DRG_description = ''
    self._APR_MDC_description = ''
    self._disease_severity = ''
    self._risck_mortality = ''
    self._type_pay = ''
    self._Attending_license_number = 0
    self._Operating_license_number = 0
    self._Abortion_Indicator= ''
    self._Emergency_Indicator= ''

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
      self._age_group = '0 to 17'
    elif (18 <= self._age and self._age < 30):
      self._age_group = '18 to 29'
    elif (30 <= self._age and self._age < 50):
      self._age_group = '30 to 49'
    elif (50 <= self._age and self._age < 70):
      self._age_group = '50 to 69'
    else:
      self._age_group = '70 or Older'
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
  def set_APR_DRG_description(self, value):
    self._APR_DRG_description = value
  def set_APR_MDC_description(self, value):
    self._APR_MDC_description = value
  def set_disease_severity(self, value):
    self._disease_severity = value
  def set_risck_mortality(self, value):
    self._risck_mortality = value
  def set_type_pay(self, value):
    self._type_pay = value
  def set_Attending_license_number(self, value):
    self._Attending_license_number = value
  def set_Operating_license_number(self, value):
    self._Operating_license_number = value
  def set_Abortion_Indicator(self, value):
    self._Abortion_Indicator= 'Y' if value else 'N'
  def set_Emergency_Indicator(self, value):
    self._Emergency_Indicator= 'Y' if value else 'N'

  def getValues(self):
    return{
      'area': self._area,
      'hospital_county': self._hospital_county,
      'hospital_name': self._hospital_name,
      'age': self._age,
      'age_group': self._age_group,
      'gender': self._gender,
      'race': self._race,
      'ethnicity': self._ethnicity,
      'stay': self._stay,
      'admission': self._admission,
      'patient_disposition': self._patient_disposition,
      'APR_DRG_description': self._APR_DRG_description,
      'APR_MDC_description': self._APR_MDC_description,
      'disease_severity': self._disease_severity,
      'risck_mortality': self._risck_mortality,
      'type_pay': self._type_pay,
      'Attending_license_number': self._Attending_license_number,
      'Operating_license_number': self._Operating_license_number,
      'Abortion_Indicator': self._Abortion_Indicator,
      'Emergency_Indicator': self._Emergency_Indicator,
    }