import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load trained model and scaler
model = joblib.load("ensemble.pkl")        
scaler = joblib.load("scaler.pkl")         

# Defining the 23 feature names (from x.columns)
feature_names = [
    'day_of_week', 'hour_of_day', 'is_holiday', 'special_event', 'pressure_sensor', 'ir_sensor',
    'ultrasonic_sensor', 'magnetic_sensor', 'camera_detection', 'rfid_sensor', 'temperature_sensor', 'humidity_sensor',
    'vibration_sensor', 'light_sensor', 'gas_sensor', 'motion_sensor', 'weight_sensor', 'proximity_sensor',
    'nearby_traffic', 'air_quality_index', 'noise_level_db', 'prev_hour_occupied', 'weather'
]

st.set_page_config(page_title="Parking Space Predictor", layout="wide")

st.title("🚗 Parking Space Occupancy Predictor")
st.markdown("Enter the input values below to predict whether the parking space is **occupied or not**.")

# columns to make UI responsive
cols = st.columns(3)
user_input = []

for i, feature in enumerate(feature_names):
    val = cols[i % 3].number_input(f"{feature}", value=0.0, step=0.01, format="%.5f")
    user_input.append(val)

if st.button("Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    st.subheader("🧾 Prediction Result:")
    st.success(f"The parking space is: **{'Occupied' if prediction == 1 else 'Not Occupied'}**")

