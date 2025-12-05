Heart Disease Risk Assessment

🎯 Project Overview

This project is a Streamlit web application designed to predict the likelihood of a patient having heart disease based on various clinical inputs (like age, gender, chest pain type, and cholesterol levels). It uses a machine learning model (Random Forest Classifier) trained on the UCI Heart Disease Dataset.

💻 Deployment

This application is deployed on Hugging Face Spaces for easy access and demonstration.

App Status: Deployed and Live!
Link: https://huggingface.co/spaces/athidhiveda/heart_app

⚙️ How to Run Locally

To run this application on your local machine, follow these steps:

Clone the repository:
git clone https://github.com/bhargavi-92/heart.app.py

Install the dependencies:
pip install -r requirements.txt

Run the app:
streamlit run heart_app.py

📂 Repository Contents

heart_app.py: The main Streamlit application script containing the UI and prediction logic.

requirements.txt: Python dependencies (Streamlit, scikit-learn, joblib, etc.) required to run the app.

heart_model.joblib: The trained machine learning model file.

scaler.joblib: The pre-trained data scaler object used to normalize input data before prediction.


 final
