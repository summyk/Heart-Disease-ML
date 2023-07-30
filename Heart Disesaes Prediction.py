# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 23:11:42 2023

@author: KIIT
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model

#loaded_model =pickle.load(open('C:\Users\KIIT\Desktop\heart_project/heart_trained_model.sav','rb'))

loaded_model = pickle.load(open(r'C:\Users\KIIT\Desktop\heart_project\heart_trained_model.sav', 'rb'))


# creating function for prediction

def diabetes_prediction(input_data):
    
    
     #Changing the input data to numpy array
     input_data_as_numpy_array = np.asarray(input_data)

     #reshape the array as we predicting  for one instance
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

     prediction =loaded_model.predict(input_data_reshaped)
     print(prediction)
     
     
     if (prediction[0]==0):
         
         return 'The person is not diabatic'
         
     else:
          return 'The person is diabatic'

    
  


    

def main():
    
    
    # giving a title
    st.title('Heart disease prediction Web App')
    
    
    # getting the input data from user
   
    
    
    age = st.text_input('age')
    sex = st.text_input('sex')
    cp = st.text_input('cp')
    trestbps = st.text_input('trestbps')
    chol = st.text_input('choll')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabaties test result'):
        diagnosis = diabetes_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()
    