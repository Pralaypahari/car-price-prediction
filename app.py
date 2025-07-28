import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('car_p_pred.pkl', 'rb'))
st.title("car_price_prediction web")

name = st.text_input("Car name:")
company = st.text_input("company name:")
year = st.number_input("year of purchase:", min_value=1985, max_value=2025)
Kms_driven = st.number_input("Kilometers driven", min_value=0, max_value=1000000)
fuel_type = st.selectbox("fuel:", ['Petrol', 'Diesel', 'CNG'])

if st.button("Predict value:"):
    input_df = pd.DataFrame([[name, company, year, Kms_driven, fuel_type]], columns=['name', 'company', 'year', 'Kms_driven', 'fuel_type'])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated car price: {int(prediction)} Rs")
    
