import streamlit as st
import numpy as np
from joblib import load

# Title
st.title("❤️ Heart Failure Prediction App - 12 Features")

# Load trained model (NO scaler)
model = load("heart_model.joblib")

st.sidebar.header("Patient Medical Data")

# Taking 12 input features
def user_input():
    age = st.sidebar.slider("Age", 20, 100, 50)
    anaemia = st.sidebar.selectbox("Anaemia (0: No, 1: Yes)", [0, 1])
    creatinine_phosphokinase = st.sidebar.slider("CPK Level", 20, 8000, 250)
    diabetes = st.sidebar.selectbox("Diabetes (0: No, 1: Yes)", [0, 1])
    ejection_fraction = st.sidebar.slider("Ejection Fraction (%)", 10, 80, 40)
    high_blood_pressure = st.sidebar.selectbox("High Blood Pressure (0: No, 1: Yes)", [0, 1])
    platelets = st.sidebar.slider("Platelets (x10^3/mL)", 20000, 800000, 300000)
    serum_creatinine = st.sidebar.slider("Serum Creatinine", 0.0, 9.0, 1.0)
    serum_sodium = st.sidebar.slider("Serum Sodium", 110, 160, 135)
    sex = st.sidebar.selectbox("Sex (0: Female, 1: Male)", [0, 1])
    smoking = st.sidebar.selectbox("Smoking (0: No, 1: Yes)", [0, 1])
    time = st.sidebar.slider("Follow-up Time (days)", 0, 300, 150)

    features = np.array([[age, anaemia, creatinine_phosphokinase,
                          diabetes, ejection_fraction, high_blood_pressure,
                          platelets, serum_creatinine, serum_sodium,
                          sex, smoking, time]])
    return features

# Get input values
features = user_input()

# Predict Button
if st.button("Predict"):
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Failure — Consult a Cardiologist Soon!")
    else:
        st.success("💚 Low Risk of Heart Failure — Stay Healthy!")
