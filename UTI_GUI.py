import streamlit as st
import joblib
import pandas as pd

st.write("# Urinary tract infection Disease Prediction")


#--------------------------------------------
col1, col2, col3 = st.columns(3)
#-------create input variables--------------
Nitrite = col1.selectbox("Urine nitrite",["Positive", "Negative"])
WBC = col1.selectbox("Urine white blood cells(WBC)",["large", "Moderate","small","negative", "Unknown"])
Bili = col1.selectbox("Urine bilirubin",["large", "Moderate","small","negative", "Unknown"])
Leuk = col1.selectbox("Urine leukocyte",["large", "Moderate","small","negative", "Unknown"])
Urobili = col1.selectbox("Urine urobilinogen",["Positive", "Negative"])
Clarity = col1.selectbox("Urine clarity",["Clear", "Not clear"])


#col2
Blood = col2.selectbox("Urine blood", ["large", "Moderate","small","negative", "Unknown"])
Color = col2.selectbox("Urine color",['Amber','Colorless','Orange','Red', 'yellow','other','Unknown'])
Gender = col2.selectbox("gender",["Male", "Female"])
Age = col2.number_input("age (year)")
abxUTI = col2.selectbox("Usage of UTI antibiotics",["Yes", "No"])
abx = col2.selectbox("Usage of antibiotics",["Yes", "No"])


#col3
chief_complaint = col3.selectbox("chief complaint",['ABDOMINAL PAIN', 'ALTERED MENTAL STATUS', 'BACK PAIN',
       'CHEST PAIN', 'DIZZINESS', 'DYSURIA', 'EMESIS', 'FALL', 'FATIGUE',
       'FEMALE GU PROBLEM', 'FEVER', 'FEVER-9 WEEKS TO 74 YEARS',
       'FLANK PAIN', 'HEMATURIA', 'MALE GU PROBLEM', 'NEUROLOGIC PROBLEM',
       'SHORTNESS OF BREATH', 'URINARY TRACT INFECTION',
       'VAGINAL BLEEDING', 'WEAKNESS', 'not_reported', 'other'])
RDW_val = col3.number_input("Red Cell Distribution Width (RDW) %")
Potassium_value = col3.number_input("Blood Potassium (mgr/L)")
Glucose_val = col3.number_input("Blood glucose (mmol/dL)")
Lymph_val = col3.number_input("Blood lymphocytes (Cells/micro Lit)")
MPV_val = col3.number_input("Mean platelet value(MPV) (femtoLitter)")

PREDICT_KEY=st.button('Predict')
#------------------------------------------------------------------
#----------------coding values to categories-----------------------
#------------------------------------------------------------------ 
#glucose
if Glucose_val<=40:
 Glucose='critically low'
elif (Glucose_val>40 and Glucose_val<70):
 Glucose='normal'
elif (Glucose_val>=70 and Glucose_val<=100):
 Glucose='normal'
elif (Glucose_val>100 and Glucose_val<180):
 Glucose='high'  
elif Glucose_val>=180: 
 Glucose='critically high' 
print('')

#-----------------------------------------------
#potassium
if Potassium_value<=2.5:
 Potassium='critically low'
elif (Potassium_value>2.5 and Potassium_value<3.5):
 Potassium='low'
elif (Potassium_value>=3.5 and Potassium_value<=5.1):
 Potassium='normal'
elif (Potassium_value>5.1 and Potassium_value<=6):
 Potassium='high'  
elif Potassium_value>6: 
 Potassium='critically high'
print('')

#----------------------------------------------- 
 #Lymphocytes
 #potassium
if Lymph_val<=800:
  Lymphocyte='critically low'
elif (Lymph_val>800 and Lymph_val<=1000):
  Lymphocyte='low'
elif (Lymph_val>1000 and Lymph_val<=4000):
  Lymphocyte='normal'
elif (Lymph_val>4000 and Lymph_val<=5000):
  Lymphocyte='high'  
elif Lymph_val>5000: 
  Lymphocyte='critically high' 
print('')
#-------------------------------------------------------

if RDW_val<=8:
  RDW='critically low'
elif (RDW_val>8 and RDW_val<11.5):
  RDW='low'
elif (RDW_val>=11.5 and RDW_val<15.4):
  RDW='normal'
elif (RDW_val>=15.4 and RDW_val<=30.6):
  RDW='high'  
elif RDW_val>30.6: 
  RDW='critically high' 
print('')
  
  #MPV
if MPV_val<7:
  MPV='critically low'
elif (MPV_val>=7 and MPV_val<=7.4):
  MPV='low'
elif (MPV_val>7.4 and MPV_val<10.4):
  MPV='normal'
elif (MPV_val>=10.4 and MPV_val<=11.5):
  MPV='high'  
elif MPV_val>11.5: 
  MPV='critically high'
print('')
#-------------------------------------------transform data------------------
#---------------------------------------------------------------------------
#--------------------------------------------------------------------------- 
if Nitrite=='Negative':
 NITRITE=0
else: 
 NITRITE=1
print('')
 #-----------------------------
if WBC=='Moderate':
    wbc=1
elif WBC=='small':
    wbc=5
elif WBC=='large':
    wbc=0
elif WBC=='Unknown':
   wbc=3
elif WBC=='negative':
   wbc=2
print('')
#--------------------------------
if Bili=='Moderate':
  BILI=1
elif Bili=='small':
  BILI=5
elif Bili=='large':
  BILI=0
elif Bili=='Unknown':
  BILI=3
elif Bili=='negative':
  BILI=2
print('')
#---------------------------

if Leuk=='Moderate':
  LEUK=1
elif Leuk=='small':
  LEUK=5
elif Leuk=='large':
  LEUK=0
elif Leuk=='Unknown':
  LEUK=3
elif Leuk=='negative':
  LEUK=2
print('')
  
#---------------------------------
if Urobili=='Negative':
    UROBILI=0
else: 
    UROBILI=1
print('')

#------------------------------------
CLARITY=0
if Clarity=='clear':
    CLARITY=0
elif Clarity=='not_clear':
    CLARITY=1
elif Clarity=='not_reported':
    CLARITY=2
print('')  
#----------------------------------
if Blood=='Moderate':
   BLOOD=1
elif Blood=='small':
   BLOOD=5
elif Blood=='large':
    BLOOD=0
elif Blood=='Unknown':
   BLOOD=3
elif Blood=='negative':
  BLOOD=2
print('')
  
#-----------------------------------
Color='yellow'
if Color=='Orange':
    COLOR=3 
elif Color=='Unknown':
   COLOR=2
elif Color=='Red':
   COLOR=5  
elif Color=='Amber':
   Color=0
elif Color=='Colorless':
   COLOR=1
elif Color== 'yellow':
   COLOR=6
elif Color== 'other':
   COLOR=4 
print('')
#-------------------------------------  
if Gender=='male':
 GENDER=1
else: 
 GENDER=0
print('')
#-----------------------------------
if abxUTI=='yes':
 ABXUTI=1
else: 
 ABXUTI=0
print('')
#-------------------------------------
if abx=='yes':
 ABX=1
else: 
 ABX=0
print('')

#---------------------------------------
if RDW=='critically low':
  rdw=1 
elif RDW=='low':
  rdw=2
elif RDW=='normal':
  rdw=3  
elif RDW=='high':
  rdw=4
elif RDW=='critically high':
  rdw=5
elif RDW== 'Unknown':
  rdw=6
print('')

#-------------------------------------
if Potassium=='critically low':
 POTASSIUM=1 
elif Potassium=='low':
 POTASSIUM=2
elif Potassium=='normal':
 POTASSIUM=3  
elif Potassium=='high':
 POTASSIUM=4
elif Potassium=='critically high':
 POTASSIUM=5
elif Potassium== 'Unknown':
 POTASSIUM=6
print('')

#----------------------------------
if Glucose=='critically low':
 GLUCOSE=1 
elif Glucose=='low':
 GLUCOSE=2
elif Glucose=='normal':
 GLUCOSE=3  
elif Glucose=='high':
 GLUCOSE=4
elif Glucose=='critically high':
 GLUCOSE=5
elif Glucose== 'Unknown':
 GLUCOSE=6
print('')
 #---------------------------------
if Lymphocyte=='critically low':
  LYMPH=1 
elif Lymphocyte=='low':
  LYMPH=2
elif Lymphocyte=='normal':
  LYMPH=3  
elif Lymphocyte=='high':
  LYMPH=4
elif Lymphocyte=='critically high':
  LYMPH=5
elif Lymphocyte== 'Unknown':
  LYMPH=6
print('')
#---------------------------------

if MPV=='critically low':
 mpv=1 
elif MPV=='low':
 mpv=2
elif MPV=='normal':
 mpv=3  
elif MPV=='high':
 mpv=4
elif MPV=='critically high':
 mpv=5
elif MPV== 'Unknown':
 mpv=6
print('')
 #-------------------------------------------
if chief_complaint=='ABDOMINAL PAIN':
  CC=0 
elif chief_complaint=='ALTERED MENTAL STATUS':
  CC=1 
elif chief_complaint=='BACK PAIN':
  CC= 2  
elif chief_complaint=='CHEST PAIN':
  CC= 3
elif chief_complaint=='DIZZINESS':
  CC=4 
elif chief_complaint=='DYSURIA':
  CC= 5
elif chief_complaint=='EMESIS':
  CC= 6
elif chief_complaint=='FALL':
  CC= 7  
elif chief_complaint=='FATIGUE':
  CC=8 
elif chief_complaint=='FEMALE GU PROBLEM':
  CC= 9
elif chief_complaint== 'FEVER':
  CC=10 
elif chief_complaint=='FEVER-9 WEEKS TO 74 YEARS':
  CC= 11
elif chief_complaint=='FLANK PAIN':
  CC=12   
elif chief_complaint=='HEMATURIA':
  CC= 12
elif chief_complaint=='MALE GU PROBLEM':
  CC= 14
elif chief_complaint=='NEUROLOGIC PROBLEM':
  CC= 15
elif chief_complaint== 'SHORTNESS OF BREATH':
  CC=16 
elif chief_complaint=='URINARY TRACT INFECTION':
  CC=17   
elif chief_complaint=='VAGINAL BLEEDING':
  CC=18 
elif chief_complaint=='WEAKNESS':
  CC=19 
elif chief_complaint=='not_reported':
  CC=20 
elif chief_complaint=='other':
  CC=21 
print('')
 
  
df_pred = pd.DataFrame([[NITRITE, wbc,BILI,LEUK,UROBILI,ABX,ABXUTI, Age, CC, GENDER
                        ,GLUCOSE ,LYMPH,mpv, POTASSIUM,rdw,BLOOD,    
                         CLARITY ,COLOR]],
                       columns= ['Nitrite','WBC','Bilirubin','Urine leukocyte','Urine Urobilinogen', 'Antibiotic Usage',
                                 'UTI antibiotic usage', 'Age','Cheif Compliant', 'Gender',
                                 'Glucose','Blood lymphocyte', 'MPV','Potassium','RDW','Urine Blood',
                                 'Urine clarity','Urine Color'])
 


# load the model from disk
import pickle
model = pickle.load(open('UTI_prediction_model.sav', 'rb'))
prediction = model.predict_proba(df_pred)[:,1]


if PREDICT_KEY:
    if Age>=18:
        st.write('The probability for UTI is:',format(prediction[0]*100,'.2f'), '%')
    else:
        st.write('This model is valid for adult subjects (Age>=18)') 
        

    
 

    
 
