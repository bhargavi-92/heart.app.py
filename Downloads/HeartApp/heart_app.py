{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcab78b4-7e04-47fc-a432-c86738faf58f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "from joblib import load\n",
    "\n",
    "# Title\n",
    "st.title(\"❤️ Heart Failure Prediction App - 12 Features\")\n",
    "\n",
    "# Load trained model (NO scaler)\n",
    "model = load(\"heart_model.joblib\")\n",
    "\n",
    "st.sidebar.header(\"Patient Medical Data\")\n",
    "\n",
    "# Taking 12 input features\n",
    "def user_input():\n",
    "    age = st.sidebar.slider(\"Age\", 20, 100, 50)\n",
    "    anaemia = st.sidebar.selectbox(\"Anaemia (0: No, 1: Yes)\", [0, 1])\n",
    "    creatinine_phosphokinase = st.sidebar.slider(\"CPK Level\", 20, 8000, 250)\n",
    "    diabetes = st.sidebar.selectbox(\"Diabetes (0: No, 1: Yes)\", [0, 1])\n",
    "    ejection_fraction = st.sidebar.slider(\"Ejection Fraction (%)\", 10, 80, 40)\n",
    "    high_blood_pressure = st.sidebar.selectbox(\"High Blood Pressure (0: No, 1: Yes)\", [0, 1])\n",
    "    platelets = st.sidebar.slider(\"Platelets (x10^3/mL)\", 20000, 800000, 300000)\n",
    "    serum_creatinine = st.sidebar.slider(\"Serum Creatinine\", 0.0, 9.0, 1.0)\n",
    "    serum_sodium = st.sidebar.slider(\"Serum Sodium\", 110, 160, 135)\n",
    "    sex = st.sidebar.selectbox(\"Sex (0: Female, 1: Male)\", [0, 1])\n",
    "    smoking = st.sidebar.selectbox(\"Smoking (0: No, 1: Yes)\", [0, 1])\n",
    "    time = st.sidebar.slider(\"Follow-up Time (days)\", 0, 300, 150)\n",
    "\n",
    "    features = np.array([[age, anaemia, creatinine_phosphokinase,\n",
    "                          diabetes, ejection_fraction, high_blood_pressure,\n",
    "                          platelets, serum_creatinine, serum_sodium,\n",
    "                          sex, smoking, time]])\n",
    "    return features\n",
    "\n",
    "# Get input values\n",
    "features = user_input()\n",
    "\n",
    "# Predict Button\n",
    "if st.button(\"Predict\"):\n",
    "    prediction = model.predict(features)[0]\n",
    "\n",
    "    if prediction == 1:\n",
    "        st.error(\"⚠️ High Risk of Heart Failure — Consult a Cardiologist Soon!\")\n",
    "    else:\n",
    "        st.success(\"💚 Low Risk of Heart Failure — Stay Healthy!\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
