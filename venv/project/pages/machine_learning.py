import pandas as pd
import streamlit as st
from datetime import date
#from pacient import Pacient
from transform_pkl import main, label_json


fields = {
  "Health Service Area": [
    "Capital/Adiron",
    "Western NY",
    "Southern Tier",
    "Central NY",
    "Finger Lakes",
    "Hudson Valley",
    "Long Island",
    "New York City"
  ],
  
  "Gender": [
    "F",
    "M",
    "U"
  ],
  "Facility Name": ['Crouse Hospital', 'St Peters Hospital',
       'University Hospital SUNY Health Science Center',
       'Millard Fillmore Suburban Hospital', 'Brooks Memorial Hospital',
       'St Catherine of Siena Hospital', 'Albany Medical Center Hospital',
       'Huntington Hospital', 'Nassau University Medical Center',
       'Westchester Medical Center',
       'TLC Health Network Lake Shore Hospital',
       'Metropolitan Hospital Center',
       'Montefiore Medical Center - Henry & Lucy Moses Div',
       'New York Methodist Hospital', 'Mount Sinai Hospital',
       'North Shore University Hospital', 'Southside Hospital',
       'Jacobi Medical Center',
       'Eastern Niagara Hospital - Lockport Division',
       'United Health Services Hospitals Inc. - Wilson Medical Center',
       'Strong Memorial Hospital', 'Lutheran Medical Center',
       "St Luke's Cornwall Hospital/Newburgh",
       'St Lukes Roosevelt Hospital - St Lukes Hospital Division',
       'Peconic Bay Medical Center', 'Maimonides Medical Center',
       'Lincoln Medical & Mental Health Center',
       'NYU Hospital for Joint Diseases',
       'Woodhull Medical & Mental Health Center', 'Lenox Hill Hospital',
       'Rochester General Hospital', "Woman's Christian Association",
       'Hospital for Special Surgery', 'Flushing Hospital Medical Center',
       'Orange Regional Medical Center-Middletown Campus',
       'Richmond University Medical Center',
       'Bronx-Lebanon Hospital Center - Concourse Division',
       'UPSTATE University Hospital at Community General',
       'Kingsbrook Jewish Medical Center',
       "Ellis Hospital - Bellevue Woman's Care Center Division",
       'St Charles Hospital',
       'Mount Sinai Hospital - Mount Sinai Hospital of Queens',
       'Massena Memorial Hospital', 'Columbia Memorial Hospital',
       'Faxton-St Lukes Healthcare St Lukes Division',
       'Beth Israel Medical Center/Petrie Campus',
       'New York Presbyterian Hospital - New York Weill Cornell Center',
       'Niagara Falls Memorial Medical Center',
       'Mount St Marys Hospital and Health Center',
       'NYU Hospitals Center', 'Arnot Ogden Medical Center',
       'St Lukes Roosevelt Hospital Center - Roosevelt Hospital Division',
       'Jamaica Hospital Medical Center', 'Putnam Hospital Center',
       'New York Presbyterian Hospital - Columbia Presbyterian Center',
       'St Elizabeth Medical Center', 'Interfaith Medical Center',
       'Good Samaritan Hospital Medical Center', 'Glens Falls Hospital',
       'Benedictine Hospital', 'Samaritan Hospital',
       'Coney Island Hospital', 'Bon Secours Community Hospital',
       'Long Island Jewish Medical Center',
       'Beth Israel Med Center-Kings Hwy Div',
       'White Plains Hospital Center', 'St. Joseph Hospital',
       'Kings County Hospital Center',
       'New York Hospital Medical Center   of Queens',
       'Harlem Hospital Center', 'Kingston Hospital',
       'The Unity Hospital of Rochester', 'Glen Cove Hospital',
       'Memorial Hospital for Cancer and Allied Diseases',
       'Montefiore Med Center - Jack D Weiler Hosp of A Einstein College Div',
       'Mercy Hospital', 'Staten Island University Hosp-North',
       'Kenmore Mercy Hospital', 'Vassar Brothers Medical Center',
       'Highland Hospital', 'Albany Memorial Hospital',
       'Cortland Regional Medical Center Inc', 'Saratoga Hospital',
       "St. Mary's Healthcare", 'SUNY Downstate Medical Center at LICH',
       'North Central Bronx Hospital', 'University Hospital of Brooklyn',
       'Buffalo General Hospital', 'Ellis Hospital',
       'Helen Hayes Hospital', 'Claxton-Hepburn Medical Center',
       'Nyack Hospital', 'Millard Fillmore Hospital',
       'Wyckoff Heights Medical Center',
       "Women And Children's Hospital Of Buffalo",
       'Staten Island University Hosp-South', 'Bellevue Hospital Center',
       'SJRH - St Johns Division', 'Carthage Area Hospital Inc',
       'South Nassau Communities Hospital',
       'Good Samaritan Hospital of Suffern', 'Lawrence Hospital Center',
       'St Francis Hospital', 'Elmhurst Hospital Center',
       'Brooklyn Hospital Center - Downtown Campus',
       'Winthrop-University Hospital',
       'Wyoming County Community Hospital', 'St Barnabas Hospital',
       'Alice Hyde Medical Center', 'Franklin Hospital',
       'Bronx-Lebanon Hospital Center - Fulton Division',
       "St Joseph's Medical Center",
       'Sisters of Charity Hospital - St Joseph Campus',
       'Geneva General Hospital', 'Oswego Hospital',
       "Long Island Jewish Schneiders Children's Hospital Division",
       'SJRH - Dobbs Ferry Pavillion',
       "Seton Health System-St Mary's Campus",
       'Eastern Long Island Hospital', 'Newark-Wayne Community Hospital',
       'Erie County Medical Center',
       "St Joseph's MC-St Vincents Westchester Division",
       'Brookhaven Memorial Hospital Medical Center Inc',
       'Phelps Memorial Hospital Assn',
       'St Johns Episcopal Hospital So Shore',
       'Montefiore Medical Center - North Division',
       'New York Westchester Square Medical Center',
       'Long Beach Medical Center', 'Roswell Park Cancer Institute',
       'St Josephs Hospital Health Center',
       'Nicholas H Noyes Memorial Hospital', 'Lakeside Memorial Hospital',
       'Brookdale Hospital Medical Center',
       'Our Lady of Lourdes Memorial Hospital Inc', 'St Josephs Hospital',
       'New York Community Hospital of Brooklyn, Inc',
       'University Hospital', 'Forest Hills Hospital',
       'Queens Hospital Center', 'Auburn Memorial Hospital',
       'SJRH - Park Care Pavilion', 'Hudson Valley Hospital Center',
       'Institute of Rehab Medicine NYU Medical Center',
       'United Memorial Medical Center North Street Campus',
       'Calvary Hospital Inc',
       'Champlain Valley Physicians Hospital Medical Center',
       'Aurelia Osborn Fox Memorial Hospital', 'Canton-Potsdam Hospital',
       'Mary Imogene Bassett Hospital', 'Mercy Medical Center',
       'Northern Dutchess Hospital', 'Delaware Valley Hospital Inc',
       'Memorial Hosp of Wm F & Gertrude F Jones A/K/A Jones Memorial Hosp',
       'Olean General Hospital', 'Nathan Littauer Hospital',
       'SVCMC-St Vincents Manhattan', 'Cayuga Medical Center at Ithaca',
       'New York Downtown Hospital', 'Peninsula Hospital Center',
       'Mount Vernon Hospital', 'Chenango Memorial Hospital Inc',
       'Oneida Healthcare Center',
       'New York Presbyterian Hospital - Allen Hospital',
       'Syosset Hospital', 'Corning Hospital',
       'Abortion Record - Facility Name Redacted',
       'Little Falls Hospital',
       'Adirondack Medical Center-Saranac Lake Site',
       'Lewis County General Hospital',
       'Summit Park Hospital-Rockland County Infirmary',
       'Catskill Regional Medical Center',
       'Northern Westchester Hospital',
       'St Francis Hospital - St Francis Hospital Beacon Div',
       'Plainview Hospital',
       'New York Presbyterian Hospital - Westchester Division',
       'John T Mather Memorial Hospital of Port Jefferson New York Inc',
       'Winifred Masterson Burke Rehabilitation Hospital',
       'Eastern Niagara Hospital - Newfane Division',
       'Rome Memorial Hospital, Inc',
       'Sound Shore Medical Center of Westchester',
       'Samaritan Medical Center', 'Community Memorial Hospital Inc',
       'F F Thompson Hospital',
       'Orange Regional Medical Center-Goshen Campus',
       'Degraff Memorial Hospital', 'St Anthony Community Hospital',
       'Sisters of Charity Hospital', 'RUMC-Bayley Seton',
       'St James Mercy Hospital', 'Sheehan Memorial Hospital',
       'Bertrand Chaffee Hospital', 'Medina Memorial Hospital',
       'United Memorial Medical Center Bank Street Campus',
       'Blythedale Childrens Hospital', 'Southampton Hospital',
       'St James Mercy Hospital - Mercycare', 'Schuyler Hospital',
       'Soldiers and Sailors Memorial Hospital of Yates County Inc',
       'United Health Services Hospitals Inc. - Binghamton General Hospital',
       "St. Luke's Cornwall Hospital/Cornwall",
       'Ira Davenport Memorial Hospital Inc', 'Clifton-Fine Hospital',
       'Clifton Springs Hospital and Clinic',
       'Edward John Noble Hospital of Gouverneur',
       "St. Mary's Healthcare - Amsterdam Memorial Campus",
       "O'Connor Hospital",
       'Sunnyview Hospital and Rehabilitation Center',
       'Crouse Hospital - Commonwealth Division',
       'Margaretville Hospital', 'Elizabethtown Community Hospital',
       'Coler-Goldwater Spec Hosp&Nurs Fac - Goldwater Hospital Site',
       'NY Eye and Ear Infirmary',
       'Coler-Goldwater Specialty Hospital & Nursing Facility - Coler Hospital',
       'The Unity Hospital of Rochester-St Marys Campus',
       'Cobleskill Regional Hospital', 'Rockefeller University Hospital',
       'Faxton-St Lukes Healthcare Faxton Division',
       'Ellenville Regional Hospital', 'Westfield Memorial Hospital Inc',
       'Albany Medical Center - South Clinical Campus',
       'Cuba Memorial Hospital Inc', 'Moses-Ludington Hospital',
       'River Hospital, Inc.',
       'Catskill Regional Medical Center - G. Hermann Site'],
  "Hospital County": ['Onondaga', 'Albany', 'Erie', 'Chautauqua', 'Suffolk', 'Nassau',
       'Westchester', 'Manhattan', 'Bronx', 'Kings', 'Niagara', 'Broome',
       'Monroe', 'Orange', 'Queens', 'Richmond', 'Schenectady',
       'St Lawrence', 'Columbia', 'Oneida', 'Chemung', 'Putnam', 'Warren',
       'Ulster', 'Rensselaer', 'Dutchess', 'Cortland', 'Saratoga',
       'Montgomery', 'Rockland', 'Jefferson', 'Wyoming', 'Franklin',
       'Ontario', 'Oswego', 'Wayne', 'Livingston', 'Cayuga', 'Genesee',
       'Clinton', 'Otsego', 'Delaware', 'Allegany', 'Cattaraugus',
       'Fulton', 'Tompkins', 'Chenango', 'Madison', 'Steuben', 'Herkimer',
       'Lewis', 'Sullivan', 'Orleans', 'Schuyler', 'Yates', 'Essex',
       'Schoharie'],
  "Race": [
    "White",
    "Black/African American",
    "Other Race",
    "Unknown"
  ],
  "Ethnicity": [
    "Not Span/Hispanic",
    "Spanish/Hispanic",
    "Unknown"
  ],
  "Type of Admission": [
    "Emergency",
    "Elective",
    "Urgent",
    "Newborn",
    "Not Available",
    "Trauma"
  ],
  "Patient Disposition": [
    "Home or Self Care",
    "Home w/ Home Health Services",
    "Inpatient Rehabilitation Facility",
    "Expired",
    "Hospice - Medical Facility",
    "Left Against Medical Advice",
    "Skilled Nursing Home",
    "Court/Law Enforcement",
    "Hospice - Home",
    "Short-term Hospital",
    "Psychiatric Hospital or Unit of Hosp",
    "Facility w/ Custodial/Supportive Care",
    "Medicare Cert Long Term Care Hospital",
    "Another Type Not Listed",
    "Federal Health Care Facility",
    "Cancer Center or Children's Hospital",
    "Critical Access Hospital",
    "Hosp Basd Medicare Approved Swing Bed",
    "Medicaid Cert Nursing Facility"
  ],
  "APR DRG Description": [
    "NON-BACTERIAL GASTROENTERITIS, NAUSEA & VOMITING",
    "MUSCULOSKELETAL & OTHER PROCEDURES FOR MULTIPLE SIGNIFICANT TRAUMA",
    "DIGESTIVE MALIGNANCY",
    "REHABILITATION",
    "HIP JOINT REPLACEMENT",
    "MULTIPLE SIGNIFICANT TRAUMA W/O O.R. PROCEDURE",
    "POISONING OF MEDICINAL AGENTS",
    "FRACTURES & DISLOCATIONS EXCEPT FEMUR, PELVIS & BACK",
    "HERNIA PROCEDURES EXCEPT INGUINAL, FEMORAL & UMBILICAL",
    "DEPRESSION EXCEPT MAJOR DEPRESSIVE DISORDER",
    "BRAIN CONTUSION/LACERATION & COMPLICATED SKULL FX, COMA < 1 HR OR NO COMA",
    "BIPOLAR DISORDERS",
    "TRACHEOSTOMY W MV 96+ HOURS W/O EXTENSIVE PROCEDURE",
    "MAJOR RESPIRATORY & CHEST PROCEDURES",
    "TRACHEOSTOMY W MV 96+ HOURS W EXTENSIVE PROCEDURE OR ECMO",
    "OTHER DIGESTIVE SYSTEM DIAGNOSES",
    "INTRACRANIAL HEMORRHAGE",
    "OTHER VASCULAR PROCEDURES",
    "POST-OP, POST-TRAUMA, OTHER DEVICE INFECTIONS W O.R. PROCEDURE",
    "RESPIRATORY MALIGNANCY",
    "MAJOR RESPIRATORY INFECTIONS & INFLAMMATIONS",
    "PERM CARDIAC PACEMAKER IMPLANT W/O AMI, HEART FAILURE OR SHOCK",
    "PERCUTANEOUS CARDIOVASCULAR PROCEDURES W AMI",
    "MUSCULOSKELETAL MALIGNANCY & PATHOL FRACTURE D/T MUSCSKEL MALIG",
    "OTHER ANEMIA & DISORDERS OF BLOOD & BLOOD-FORMING ORGANS",
    "HEAD TRAUMA W COMA >1 HR OR HEMORRHAGE",
    "SIGNS, SYMPTOMS & OTHER FACTORS INFLUENCING HEALTH STATUS",
    "MODERATELY EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS",
    "NEONATE BWT <500G",
    "HIP & FEMUR PROCEDURES FOR TRAUMA EXCEPT JOINT REPLACEMENT",
    "CONTUSION, OPEN WOUND & OTHER TRAUMA TO SKIN & SUBCUTANEOUS TISSUE",
    "SICKLE CELL ANEMIA CRISIS",
    "POST-OPERATIVE, POST-TRAUMATIC, OTHER DEVICE INFECTIONS",
    "DRUG & ALCOHOL ABUSE OR DEPENDENCE, LEFT AGAINST MEDICAL ADVICE",
    "INTERSTITIAL LUNG DISEASE",
    "URINARY STONES & ACQUIRED UPPER URINARY TRACT OBSTRUCTION",
    "OTHER COMPLICATIONS OF TREATMENT",
    "CARDIAC ARRHYTHMIA & CONDUCTION DISORDERS",
    "SHOULDER, UPPER ARM & FOREARM PROCEDURES",
    "MAJOR SMALL & LARGE BOWEL PROCEDURES",
    "LAPAROSCOPIC CHOLECYSTECTOMY",
    "ELECTROLYTE DISORDERS EXCEPT HYPOVOLEMIA RELATED",
    "CHEST PAIN",
    "SKIN GRAFT FOR SKIN & SUBCUTANEOUS TISSUE DIAGNOSES",
    "CARDIAC DEFIBRILLATOR & HEART ASSIST IMPLANT",
    "OTHER BACK & NECK DISORDERS, FRACTURES & INJURIES",
    "CARDIAC CATHETERIZATION W CIRC DISORD EXC ISCHEMIC HEART DISEASE",
    "CORONARY BYPASS W CARDIAC CATH OR PERCUTANEOUS CARDIAC PROCEDURE",
    "OTHER PNEUMONIA",
    "ANGINA PECTORIS & CORONARY ATHEROSCLEROSIS",
    "OTHER CIRCULATORY SYSTEM DIAGNOSES",
    "OTHER SMALL & LARGE BOWEL PROCEDURES",
    "CONCUSSION, CLOSED SKULL FX NOS,UNCOMPLICATED INTRACRANIAL INJURY, COMA < 1 HR OR NO COMA",
    "INFLAMMATORY BOWEL DISEASE",
    "MIGRAINE & OTHER HEADACHES",
    "DIABETES",
    "HYPERTENSION",
    "RENAL FAILURE",
    "SYNCOPE & COLLAPSE",
    "LYMPHATIC & OTHER MALIGNANCIES & NEOPLASMS OF UNCERTAIN BEHAVIOR",
    "COAGULATION & PLATELET DISORDERS",
    "CARDIOMYOPATHY",
    "PULMONARY EDEMA & RESPIRATORY FAILURE",
    "APPENDECTOMY",
    "NONSPECIFIC CVA & PRECEREBRAL OCCLUSION W/O INFARCT",
    "OTHER RESPIRATORY DIAGNOSES EXCEPT SIGNS, SYMPTOMS & MINOR DIAGNOSES",
    "NEPHRITIS & NEPHROSIS",
    "RESPIRATORY SIGNS, SYMPTOMS & MINOR DIAGNOSES",
    "NEONATE BIRTHWT 1000-1249G W OR W/O OTHER SIGNIFICANT CONDITION",
    "MAJOR DEPRESSIVE DISORDERS & OTHER/UNSPECIFIED PSYCHOSES",
    "SEPTICEMIA & DISSEMINATED INFECTIONS",
    "OTHER SKIN, SUBCUTANEOUS TISSUE & RELATED PROCEDURES",
    "EYE PROCEDURES EXCEPT ORBIT",
    "TOXIC EFFECTS OF NON-MEDICINAL SUBSTANCES",
    "OTHER DISORDERS OF NERVOUS SYSTEM",
    "MAJOR THORACIC & ABDOMINAL VASCULAR PROCEDURES",
    "CELLULITIS & OTHER BACTERIAL SKIN INFECTIONS",
    "CRANIOTOMY EXCEPT FOR TRAUMA",
    "CERVICAL SPINAL FUSION & OTHER BACK/NECK PROC EXC DISC EXCIS/DECOMP",
    "OTHER BLADDER PROCEDURES",
    "VIRAL MENINGITIS",
    "UTERINE & ADNEXA PROCEDURES FOR NON-MALIGNANCY EXCEPT LEIOMYOMA",
    "OTHER RESPIRATORY & CHEST PROCEDURES",
    "INTERVERTEBRAL DISC EXCISION & DECOMPRESSION",
    "NONEXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS",
    "OTHER ENDOCRINE DISORDERS",
    "OTHER ESOPHAGEAL DISORDERS",
    "CARDIAC CATHETERIZATION FOR ISCHEMIC HEART DISEASE",
    "INFECTIONS OF UPPER RESPIRATORY TRACT",
    "INTESTINAL OBSTRUCTION",
    "MAJOR ESOPHAGEAL DISORDERS",
    "NEONATE BIRTHWT >2499G, NORMAL NEWBORN OR NEONATE W OTHER PROBLEM",
    "RESPIRATORY SYSTEM DIAGNOSIS W VENTILATOR SUPPORT 96+ HOURS",
    "OTHER INJURY, POISONING & TOXIC EFFECT DIAGNOSES",
    "OTHER MENTAL HEALTH DISORDERS",
    "EYE DISORDERS EXCEPT MAJOR INFECTIONS",
    "DORSAL & LUMBAR FUSION PROC EXCEPT FOR CURVATURE OF BACK",
    "KNEE & LOWER LEG PROCEDURES EXCEPT FOOT",
    "HIV W ONE SIGNIF HIV COND OR W/O SIGNIF RELATED COND",
    "VAGINAL DELIVERY",
    "MAJOR MALE PELVIC PROCEDURES",
    "FEVER",
    "O.R. PROCEDURE FOR OTHER COMPLICATIONS OF TREATMENT",
    "EXTENSIVE ABDOMINAL/THORACIC PROCEDURES FOR MULT SIGNIFICANT TRAUMA",
    "OTHER KIDNEY & URINARY TRACT DIAGNOSES, SIGNS & SYMPTOMS",
    "SCHIZOPHRENIA",
    "ECTOPIC PREGNANCY PROCEDURE",
    "NON-BACTERIAL INFECTIONS OF NERVOUS SYSTEM EXC VIRAL MENINGITIS",
    "MAJOR CHEST & RESPIRATORY TRAUMA",
    "DEGENERATIVE NERVOUS SYSTEM DISORDERS EXC MULT SCLEROSIS",
    "VERTIGO & OTHER LABYRINTH DISORDERS",
    "MENSTRUAL & OTHER FEMALE REPRODUCTIVE SYSTEM DISORDERS",
    "FACIAL BONE PROCEDURES EXCEPT MAJOR CRANIAL/FACIAL BONE PROCEDURES",
    "PULMONARY EMBOLISM",
    "CVA & PRECEREBRAL OCCLUSION W INFARCT",
    "BRONCHIOLITIS & RSV PNEUMONIA",
    "ABDOMINAL PAIN",
    "OTHER EAR, NOSE, MOUTH & THROAT PROCEDURES",
    "TONSIL & ADENOID PROCEDURES",
    "PEPTIC ULCER & GASTRITIS",
    "PROCEDURES FOR OBESITY",
    "HYPOVOLEMIA & RELATED ELECTROLYTE DISORDERS",
    "EXTRACRANIAL VASCULAR PROCEDURES",
    "MALFUNCTION, REACTION & COMPLICATION OF GI DEVICE OR PROCEDURE",
    "NERVOUS SYSTEM MALIGNANCY",
    "OTHER SKIN, SUBCUTANEOUS TISSUE & BREAST DISORDERS",
    "FEMALE REPRODUCTIVE SYSTEM INFECTIONS",
    "DISORDERS OF GALLBLADDER & BILIARY TRACT",
    "URETHRAL & TRANSURETHRAL PROCEDURES",
    "TRANSIENT ISCHEMIA",
    "ASTHMA",
    "OTHER DISORDERS OF THE LIVER",
    "CRANIOTOMY FOR MULTIPLE SIGNIFICANT TRAUMA",
    "NEONATE BWT 1500-1999G W OR W/O OTHER SIGNIFICANT CONDITION",
    "SEIZURE",
    "NEONATE BIRTHWT >2499G W OTHER MAJOR PROCEDURE",
    "DORSAL & LUMBAR FUSION PROC FOR CURVATURE OF BACK",
    "CHEMOTHERAPY",
    "HEPATIC COMA & OTHER MAJOR ACUTE LIVER DISORDERS",
    "NEONATE BIRTHWT >2499G W OTHER SIGNIFICANT CONDITION",
    "MAJOR HEMATOLOGIC/IMMUNOLOGIC DIAG EXC SICKLE CELL CRISIS & COAGUL",
    "NEONATE BWT <1500G W MAJOR PROCEDURE",
    "NEONATE BIRTHWT 1500-1999G W CONGENITAL/PERINATAL INFECTION",
    "NEONATE BIRTHWT 500-749G W/O MAJOR PROCEDURE",
    "CARDIAC VALVE PROCEDURES W CARDIAC CATHETERIZATION",
    "LYMPHOMA, MYELOMA & NON-ACUTE LEUKEMIA",
    "OTHER CARDIOTHORACIC PROCEDURES",
    "MALFUNCTION,REACTION,COMPLICATION OF CARDIAC/VASC DEVICE OR PROCEDURE",
    "NEONATE BWT 2000-2499G, NORMAL NEWBORN OR NEONATE W OTHER PROBLEM",
    "VENTRICULAR SHUNT PROCEDURES",
    "TESTES & SCROTAL PROCEDURES",
    "NEONATE BWT 2000-2499G W OTHER SIGNIFICANT CONDITION",
    "NEONATE BWT 1250-1499G W RESP DIST SYND/OTH MAJ RESP OR MAJ ANOM",
    "NEONATE BWT 1000-1249G W RESP DIST SYND/OTH MAJ RESP OR MAJ ANOM",
    "NEONATE BWT 2000-2499G W MAJOR ANOMALY",
    "INGUINAL, FEMORAL & UMBILICAL HERNIA PROCEDURES",
    "NEONATE BIRTHWT >2499G W MAJOR CARDIOVASCULAR PROCEDURE",
    "KIDNEY & URINARY TRACT PROCEDURES FOR NONMALIGNANCY",
    "NEONATE BIRTHWT >2499G W MAJOR ANOMALY",
    "MAJOR CARDIOTHORACIC REPAIR OF HEART ANOMALY",
    "OTHER STOMACH, ESOPHAGEAL & DUODENAL PROCEDURES",
    "NEONATE BIRTHWT 750-999G W/O MAJOR PROCEDURE",
    "VIRAL ILLNESS",
    "NONTRAUMATIC STUPOR & COMA",
    "NEONATE BWT 1500-2499G W MAJOR PROCEDURE",
    "SINUS & MASTOID PROCEDURES",
    "NEONATE BWT 2000-2499G W CONGENITAL/PERINATAL INFECTION",
    "OTHER MUSCULOSKELETAL SYSTEM & CONNECTIVE TISSUE PROCEDURES",
    "NEONATE, BIRTHWT >2499G W RESP DIST SYND/OTH MAJ RESP COND",
    "NEONATE BWT 1500-1999G W RESP DIST SYND/OTH MAJ RESP COND",
    "PERCUTANEOUS CARDIOVASCULAR PROCEDURES W/O AMI",
    "SPINAL DISORDERS & INJURIES",
    "INFECTIOUS & PARASITIC DISEASES INCLUDING HIV W O.R. PROCEDURE",
    "KIDNEY & URINARY TRACT INFECTIONS",
    "OTHER INFECTIOUS & PARASITIC DISEASES",
    "OTHER MUSCULOSKELETAL SYSTEM & CONNECTIVE TISSUE DIAGNOSES",
    "MALE REPRODUCTIVE SYSTEM DIAGNOSES EXCEPT MALIGNANCY",
    "DISORDERS OF PANCREAS EXCEPT MALIGNANCY",
    "FRACTURE OF PELVIS OR DISLOCATION OF HIP",
    "CONNECTIVE TISSUE DISORDERS",
    "PARTIAL THICKNESS BURNS W OR W/O SKIN GRAFT",
    "PERITONEAL ADHESIOLYSIS",
    "PERIPHERAL & OTHER VASCULAR DISORDERS",
    "OTHER DIGESTIVE SYSTEM & ABDOMINAL PROCEDURES",
    "MALNUTRITION, FAILURE TO THRIVE & OTHER NUTRITIONAL DISORDERS",
    "DENTAL & ORAL DISEASES & INJURIES",
    "OTHER EAR, NOSE, MOUTH,THROAT & CRANIAL/FACIAL DIAGNOSES",
    "ALLERGIC REACTIONS",
    "CRANIOTOMY FOR TRAUMA",
    "SPINAL PROCEDURES",
    "BPD & OTH CHRONIC RESPIRATORY DISEASES ARISING IN PERINATAL PERIOD",
    "OSTEOMYELITIS, SEPTIC ARTHRITIS & OTHER MUSCULOSKELETAL INFECTIONS",
    "MAJOR CRANIAL/FACIAL BONE PROCEDURES",
    "ALCOHOL ABUSE & DEPENDENCE",
    "TENDON, MUSCLE & OTHER SOFT TISSUE PROCEDURES",
    "SPLENECTOMY",
    "THYROID, PARATHYROID & THYROGLOSSAL PROCEDURES",
    "ANAL PROCEDURES",
    "ACUTE MAJOR EYE INFECTIONS",
    "NEONATE BWT 2000-2499G W RESP DIST SYND/OTH MAJ RESP COND",
    "OTHER HEPATOBILIARY, PANCREAS & ABDOMINAL PROCEDURES",
    "FRACTURE OF FEMUR",
    "NEONATE BIRTHWT >2499G W CONGENITAL/PERINATAL INFECTION",
    "CARDIAC VALVE PROCEDURES W/O CARDIAC CATHETERIZATION",
    "FOOT & TOE PROCEDURES",
    "ACUTE LEUKEMIA",
    "EATING DISORDERS",
    "MAJOR STOMACH, ESOPHAGEAL & DUODENAL PROCEDURES",
    "CYSTIC FIBROSIS - PULMONARY DISEASE",
    "NEONATE BWT 1250-1499G W OR W/O OTHER SIGNIFICANT CONDITION",
    "OTHER CIRCULATORY SYSTEM PROCEDURES",
    "OTHER ANTEPARTUM DIAGNOSES",
    "ORBITAL PROCEDURES",
    "ACUTE ANXIETY & DELIRIUM STATES",
    "ADJUSTMENT DISORDERS & NEUROSES EXCEPT DEPRESSIVE DIAGNOSES",
    "MAJOR GASTROINTESTINAL & PERITONEAL INFECTIONS",
    "INBORN ERRORS OF METABOLISM",
    "PRETERM LABOR",
    "MAJOR O.R. PROCEDURES FOR LYMPHATIC/HEMATOPOIETIC/OTHER NEOPLASMS",
    "CHRONIC OBSTRUCTIVE PULMONARY DISEASE",
    "SKIN GRAFT, EXCEPT HAND, FOR MUSCULOSKELETAL & CONNECTIVE TISSUE DIAGNOSES",
    "OTHER KIDNEY, URINARY TRACT & RELATED PROCEDURES",
    "OTHER DRUG ABUSE & DEPENDENCE",
    "BACTERIAL & TUBERCULOUS INFECTIONS OF NERVOUS SYSTEM",
    "OPIOID ABUSE & DEPENDENCE",
    "MALFUNCTION, REACTION, COMPLIC OF GENITOURINARY DEVICE OR PROC",
    "HIP & FEMUR PROCEDURES FOR NON-TRAUMA EXCEPT JOINT REPLACEMENT",
    "HIV W MAJOR HIV RELATED CONDITION",
    "OTHER O.R. PROCEDURES FOR LYMPHATIC/HEMATOPOIETIC/OTHER NEOPLASMS",
    "CESAREAN DELIVERY",
    "VAGINAL DELIVERY W COMPLICATING PROCEDURES EXC STERILIZATION &/OR D&C",
    "POSTPARTUM & POST ABORTION DIAGNOSES W/O PROCEDURE",
    "PITUITARY & ADRENAL PROCEDURES",
    "OTHER O.R. PROC FOR OBSTETRIC DIAGNOSES EXCEPT DELIVERY DIAGNOSES",
    "VAGINAL DELIVERY W STERILIZATION &/OR D&C",
    "OTHER NERVOUS SYSTEM & RELATED PROCEDURES",
    "EXTENSIVE PROCEDURE UNRELATED TO PRINCIPAL DIAGNOSIS",
    "OTHER FEMALE REPRODUCTIVE SYSTEM & RELATED PROCEDURES",
    "MULTIPLE SCLEROSIS & OTHER DEMYELINATING DISEASES",
    "PERIPHERAL, CRANIAL & AUTONOMIC NERVE DISORDERS",
    "COCAINE ABUSE & DEPENDENCE",
    "RENAL DIALYSIS ACCESS DEVICE PROCEDURE ONLY",
    "MAJOR BLADDER PROCEDURES",
    "FALSE LABOR",
    "CLEFT LIP & PALATE REPAIR",
    "PANCREAS TRANSPLANT",
    "SKIN ULCERS",
    "KNEE JOINT REPLACEMENT",
    "CARDIAC PACEMAKER & DEFIBRILLATOR DEVICE REPLACEMENT",
    "KIDNEY TRANSPLANT",
    "HIV W MULTIPLE MAJOR HIV RELATED CONDITIONS",
    "CARDIAC PACEMAKER & DEFIBRILLATOR REVISION EXCEPT DEVICE REPLACEMENT",
    "PROCEDURE W DIAG OF REHAB, AFTERCARE OR OTH CONTACT W HEALTH SERVICE",
    "CARDIAC STRUCTURAL & VALVULAR DISORDERS",
    "CORONARY BYPASS W/O CARDIAC CATH OR PERCUTANEOUS CARDIAC PROCEDURE",
    "CHOLECYSTECTOMY EXCEPT LAPAROSCOPIC",
    "PENIS PROCEDURES",
    "HAND & WRIST PROCEDURES",
    "HEART FAILURE",
    "DIVERTICULITIS & DIVERTICULOSIS",
    "OTHER MALE REPRODUCTIVE SYSTEM & RELATED PROCEDURES",
    "OTHER & UNSPECIFIED GASTROINTESTINAL HEMORRHAGE",
    "AMPUTATION OF LOWER LIMB EXCEPT TOES",
    "MALIGNANCY OF HEPATOBILIARY SYSTEM & PANCREAS",
    "RADIOTHERAPY",
    "MASTECTOMY PROCEDURES",
    "PELVIC EVISCERATION, RADICAL HYSTERECTOMY & OTHER RADICAL GYN PROCS",
    "UTERINE & ADNEXA PROCEDURES FOR LEIOMYOMA",
    "MAJOR PANCREAS, LIVER & SHUNT PROCEDURES",
    "FEMALE REPRODUCTIVE SYSTEM RECONSTRUCTIVE PROCEDURES",
    "KIDNEY & URINARY TRACT PROCEDURES FOR MALIGNANCY",
    "BREAST PROCEDURES EXCEPT MASTECTOMY",
    "ALCOHOLIC LIVER DISEASE",
    "EXTENSIVE 3RD DEGREE OR FULL THICKNESS BURNS W/O SKIN GRAFT",
    "KIDNEY & URINARY TRACT MALIGNANCY",
    "MAJOR BILIARY TRACT PROCEDURES",
    "EAR, NOSE, MOUTH, THROAT, CRANIAL/FACIAL MALIGNANCIES",
    "TRANSURETHRAL PROSTATECTOMY",
    "ACUTE & SUBACUTE ENDOCARDITIS",
    "HIV W MULTIPLE SIGNIFICANT HIV RELATED CONDITIONS",
    "MAJOR SKIN DISORDERS",
    "MAJOR LARYNX & TRACHEA PROCEDURES",
    "ACUTE MYOCARDIAL INFARCTION",
    "GASTROINTESTINAL VASCULAR INSUFFICIENCY",
    "MALFUNCTION, REACTION, COMPLIC OF ORTHOPEDIC DEVICE OR PROCEDURE",
    "MENTAL ILLNESS DIAGNOSIS W O.R. PROCEDURE",
    "PERMANENT CARDIAC PACEMAKER IMPLANT W AMI, HEART FAILURE OR SHOCK",
    "CARDIAC ARREST",
    "OTHER PROCEDURES OF BLOOD & BLOOD-FORMING ORGANS",
    "OTHER MAJOR HEAD & NECK PROCEDURES",
    "ORGANIC MENTAL HEALTH DISTURBANCES",
    "NEONATE BIRTHWT 1500-1999G W MAJOR ANOMALY",
    "DILATION & CURETTAGE FOR NON-OBSTETRIC DIAGNOSES",
    "MALIGNANCY, MALE REPRODUCTIVE SYSTEM",
    "OTHER PROCEDURES FOR ENDOCRINE, NUTRITIONAL & METABOLIC DISORDERS",
    "MALIGNANT BREAST DISORDERS",
    "FEMALE REPRODUCTIVE SYSTEM MALIGNANCY",
    "FULL THICKNESS BURNS W SKIN GRAFT",
    "UNGROUPABLE",
    "NEONATE, TRANSFERRED <5 DAYS OLD, NOT BORN HERE",
    "NEONATE, TRANSFERRED < 5 DAYS OLD, BORN HERE",
    "DISORDERS OF PERSONALITY & IMPULSE CONTROL",
    "D&C, ASPIRATION CURETTAGE OR HYSTEROTOMY FOR OBSTETRIC DIAGNOSES",
    "CHILDHOOD BEHAVIORAL DISORDERS",
    "OTHER AFTERCARE & CONVALESCENCE",
    "UTERINE & ADNEXA PROCEDURES FOR NON-OVARIAN & NON-ADNEXAL MALIG",
    "NEONATE W ECMO",
    "UTERINE & ADNEXA PROCEDURES FOR OVARIAN & ADNEXAL MALIGNANCY",
    "ALCOHOL & DRUG DEPENDENCE W REHAB OR REHAB/DETOX THERAPY",
    "NEONATAL AFTERCARE",
    "BONE MARROW TRANSPLANT",
    "EXTENSIVE 3RD DEGREE BURNS W SKIN GRAFT",
    "PRINCIPAL DIAGNOSIS INVALID AS DISCHARGE DIAGNOSIS",
    "LIVER TRANSPLANT &/OR INTESTINAL TRANSPLANT",
    "HEART &/OR LUNG TRANSPLANT",
    "ABORTION W/O D&C, ASPIRATION CURETTAGE OR HYSTEROTOMY"
  ],
  "APR MDC Description": [
    "Diseases and Disorders of the Digestive System",
    "Multiple Significant Trauma",
    "Rehabilitation, Aftercare, Other Factors Influencing Health Status and Other Health Service Contacts",
    "Diseases and Disorders of the Musculoskeletal System and Conn Tissue",
    "Poisonings, Toxic Effects, Other Injuries and Other Complications of Treatment",
    "Mental Diseases and Disorders",
    "Diseases and Disorders of the Nervous System",
    "Diseases and Disorders of the Respiratory System",
    "Diseases and Disorders of the Circulatory System",
    "Infectious and Parasitic Diseases, Systemic or Unspecified Sites",
    "Diseases and Disorders of Blood, Blood Forming Organs and Immunological Disorders",
    "Newborns and Other Neonates with Conditions Originating in the Perinatal Period",
    "Diseases and Disorders of the Skin, Subcutaneous Tissue and Breast",
    "Alcohol/Drug Use and Alcohol/Drug Induced Organic Mental Disorders",
    "Diseases and Disorders of the Kidney and Urinary Tract",
    "Diseases and Disorders of the Hepatobiliary System and Pancreas",
    "Endocrine, Nutritional and Metabolic Diseases and Disorders",
    "Lymphatic, Hematopoietic, Other Malignancies, Chemotherapy and Radiotherapy",
    "Diseases and Disorders of the Eye",
    "Diseases and Disorders of the Female Reproductive System",
    "Ear, Nose, Mouth, Throat and Craniofacial Diseases and Disorders",
    "Human Immunodeficiency Virus Infections",
    "Pregnancy, Childbirth and the Puerperium",
    "Diseases and Disorders of the Male Reproductive System",
    "Burns",
    "Pre-MDC or Ungroupable"
  ],
  "APR Severity of Illness Code": [
    "1",
    "3",
    "2",
    "4",
  ],
  "APR Severity of Illness Description": [
    "Minor",
    "Major",
    "Moderate",
    "Extreme"
  ],
  "APR Risk of Mortality": [
    "Minor",
    "Extreme",
    "Major",
    "Moderate"
  ],
  "APR Medical Surgical Description": [
    "Medical",
    "Surgical",
    "Not Applicable"
  ],
  "Source of Payment 1": [
    "Blue Cross",
    "Insurance Company",
    "Medicare",
    "Medicaid",
    "Other Federal Program",
    "Self-Pay",
    "Other Non-Federal Program",
    "Workers Compensation",
    "CHAMPUS",
    "Unknown"
  ],
  "Abortion Edit Indicator": [
    "N",
    "Y"
  ],
  "Emergency Department Indicator": [
    "Y",
    "N"
  ],
  "Total Costs Category": [
    "0k a 5k",
    "50k a 100k",
    "10k a 30k",
    "5k a 10k",
    "200k a 300k",
    "30k a 50k",
    "100k a 200k",
    "mais de 300k"
  ]
}


data=pd.read_parquet('venv\project\data\hospital_100k.parquet')
data_hospitais = data.groupby(
  ['Health Service Area', 'Hospital County', 'Facility Name',]
).size().reset_index(name='Total')


def code_describe(label: str, data: pd.DataFrame, code: str, description: str,) -> str:
  data_test = data.groupby([code, description,]).size().reset_index(name='total')
  input_select = st.selectbox(label= label, options= ['']+fields[description])
  if input_select != '':
    return data_test[data_test[description]==input_select].iloc[0][code]

def after_select_next(
  label: str, data: pd.DataFrame, first, afterEl: str, nextEl: str, selection: st.selectbox= st.selectbox
  ) -> str:
  option_list = []
  if first != '':
    option_list = list(data[data[afterEl] == first][nextEl].unique())
  input_next = selection(label, ['']+option_list, disabled=(first==''))
  return input_next

def hospital_info():
  c1, c2 = st.columns((2, 2))
  area = c1.selectbox('Área de serviço de saúde', options=['']+list(data['Health Service Area'].unique()))
  hospital_county = after_select_next(
    'Condado Hospitalar', 
    data=data_hospitais, 
    first=area, 
    afterEl='Health Service Area', 
    nextEl='Hospital County',
    selection= c2.selectbox
  )
  hospital_name= after_select_next(
    'Nome do hospital', 
    data=data_hospitais, 
    first=hospital_county, 
    nextEl='Facility Name', 
    afterEl='Hospital County'
  )
  return area, hospital_county, hospital_name

def race_ethnicity():
  c1, c2, c3 = st.columns((1, 1, 1))
  gender= c3.radio('Gênero', fields['Gender'])
  race= c1.radio('Raça', fields['Race'])
  ethnicity= c2.radio('etinia', fields['Ethnicity'])
  return gender, race, ethnicity


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
  def getValuesVec(self):
    return{
      'Health Service Area': fields['Health Service Area']+[self._area],
      'Hospital County': fields['Hospital County']+[self._hospital_county],
      'Facility Name': fields['Facility Name']+[self._hospital_name],
      'Age Group': self._age_group,
      'Gender': fields['Gender']+[self._gender],
      'Race': fields['Race']+[self._race],
      'Ethnicity': fields['Ethnicity']+[self._ethnicity],
      'Length of Stay': self._stay,
      'Type of Admission': fields['Type of Admission']+[self._admission],
      'Patient Disposition': fields['Patient Disposition']+[self._patient_disposition],
      'APR DRG Code': self._APR_DRG_code,
      'APR MDC Code': self._APR_MDC_code,
      'APR Severity of Illness Code': self._disease_severity_code,
      'APR Risk of Mortality': fields['APR Risk of Mortality']+[self._risck_mortality],
      'APR Medical Surgical Description': fields['APR Medical Surgical Description']+[self._medical_description],
      'Source of Payment 1': fields['Source of Payment 1']+[self._type_pay],
      'Attending Provider License Number': self._Attending_license_number,
      'Operating Provider License Number': self._Operating_license_number,
      'Abortion Edit Indicator': fields['Abortion Edit Indicator']+[self._Abortion_Indicator],
      'Emergency Department Indicator': fields['Emergency Department Indicator']+[self._Emergency_Indicator],
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


with st.container():
  area, hospital_county, hospital_name = hospital_info()
  
  birth_day= st.date_input('Data de nascimento', min_value=date(1800, 1, 1), max_value=date.today())
  
  gender, race, ethnicity=race_ethnicity()
  stay= st.slider('Tempo de estadia', 0, 120)
  admission= st.radio('Tipo da admissão', fields['Type of Admission'], horizontal=True)
  patient_disposition= st.selectbox('Local de tratamento', ['']+fields['Patient Disposition'])
  
  APR_DRG_code= code_describe('Descrição por APR DRG', data, 'APR DRG Code', 'APR DRG Description')
  APR_MDC_code= code_describe('Descrição por APR MDC', data, 'APR MDC Code', 'APR MDC Description')
  
  disease_severity = st.radio('Gravidade da doença', fields['APR Severity of Illness Description'], horizontal=True)
  
  risck_mortality= st.radio('Risco de mortalidade', fields['APR Risk of Mortality'], horizontal=True)
  medical_description = st.selectbox("Descrição cirúrgica", ['']+fields['APR Medical Surgical Description'])
  
  type_pay= st.selectbox('Planos de saúde', ['']+fields['Source of Payment 1'])
  Attending_license_number= st.number_input(
    label = 'Número da licença do provedor de atendimento', value=0., min_value=0., step=.1, format='%.1f'
    )
  Operating_license_number= st.number_input(
    label='Número de licença do provedor operacional', value=0., min_value=0., step=.1, format='%.1f'
    )
  _, c1, c2, _ = st.columns((.3, 1, 1, .3))
  Abortion_Indicator= c1.checkbox('Indicador de aborto')
  Emergency_Indicator= c2.checkbox('Indicador de Emergência')
  
  _, meio, _ = st.columns((1, .5, 1))
  if meio.button('Submit', ):
    flag = [
      area == '',
      hospital_county == '',
      hospital_name == '',
      race == '',
      patient_disposition == '',
      APR_DRG_code == '',
      APR_MDC_code == '',
      type_pay == '',            
    ]

    if sum(flag) != 0:
      st.markdown(
        """<p style='text-align: center; color: red;'>
            Você deixou campos vazios!
          </p>""", 
        unsafe_allow_html=True
      )
    else:
      pacient = Pacient()
      
      pacient.set_area(area)
      pacient.set_hospital_county(hospital_county)
      pacient.set_hospital_name(hospital_name)
      pacient.set_age(birth_day)
      pacient.set_gender(gender)
      pacient.set_race(race)
      pacient.set_ethnicity(ethnicity)
      pacient.set_stay(stay)
      pacient.set_admission(admission)
      pacient.set_patient_disposition(patient_disposition)
      pacient.set_APR_DRG_code(APR_DRG_code)
      pacient.set_APR_MDC_code(APR_MDC_code)
      pacient.set_disease_severity_code(disease_severity)
      pacient.set_risck_mortality(risck_mortality)
      pacient.set_type_pay(type_pay)
      pacient.set_Attending_license_number(Attending_license_number)
      pacient.set_Operating_license_number(Operating_license_number)
      pacient.set_Abortion_Indicator(Abortion_Indicator)
      pacient.set_Emergency_Indicator(Emergency_Indicator)
      pacient.set_medical_description(medical_description)
      
      #st.write(pacient.getValuesVec())

      x_data = pacient.getvec()
      with open('venv/project/data/test.pkl', 'rb') as f:
        standard, label_service_Area, label_hospital_county, label_facility_name, label_gender, label_race, label_ethnicity, label_type_dmission, label_disposition, label_risk_mortality, label_medical_surgical, label_payment, _, _, _ = pickle.load(f)
      
      t = []
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
      st.write(random_forest.predict(x_data))