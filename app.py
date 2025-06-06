import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle

## loading the trained model
model = tf.keras.models.load_model('model.h5')

## load the encoder and scaler
with open ('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


## streamlit app
st.title("Customer Churn Prediction")
st.write("This app predicts whether a customer will churn or not based on their information.")

## User input
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.number_input('Age', min_value=18, max_value=92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', min_value=0, max_value=10)
num_of_products = st.slider('Number of Products', min_value=1, max_value=4)
has_credit_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

## prepare input data
input_data = {
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_credit_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
}
input_data = pd.DataFrame(input_data)
## One hot encode geography
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoder_df=pd.DataFrame(geo_encoded,columns=onehot_encoder_geo.get_feature_names_out())

# combine oencoded geography with input data
input_data =  pd.concat([input_data.reset_index(drop=True), geo_encoder_df], axis=1)

## scasle the input data
input_data_scaled = scaler.transform(input_data)

## predict churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]
if prediction_proba > 0.5:
    st.write(f"Prediction: Churn (Probability: {prediction_proba:.2f})")
else:
    st.write(f"Prediction: No Churn (Probability: {1 - prediction_proba:.2f})")
