import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Predictor", layout="centered")

st.title("🩺 Diabetes Prediction App")
st.markdown("Enter your health details below:")

# Input fields
data = {
    "pregnancies": st.number_input("Pregnancies", min_value=0),
    "glucose": st.number_input("Glucose Level", min_value=0),
    "blood_pressure": st.number_input("Blood Pressure", min_value=0),
    "skin_thickness": st.number_input("Skin Thickness", min_value=0),
    "insulin": st.number_input("Insulin", min_value=0),
    "bmi": st.number_input("BMI", min_value=0.0),
    "diabetes_pedigree_function": st.number_input("Diabetes Pedigree Function", min_value=0.0),
    "age": st.number_input("Age", min_value=0)
}

if st.button("Predict"):
    response = requests.post("https://diabetes-predictor-d2jp.onrender.com/predict", json=data)  # Replace localhost with Render/HF URL after deployment
    if response.status_code == 200:
        result = response.json()
        prediction = result["prediction"]
        if prediction == "Diabetic":
            st.error("🛑 You are likely to have diabetes.")
        else:
            st.success("✅ You are not likely to have diabetes.")
    else:
        st.warning("Something went wrong with the prediction request.")
