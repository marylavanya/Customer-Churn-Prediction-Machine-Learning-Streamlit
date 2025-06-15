import streamlit as st
import joblib
import numpy as np

# Load the model

model = joblib.load("churn_gb_model_.pkl")

# Streamlit UI
st.title("Customer Churn Prediction App")
st.write("Please enter the details  below and click **Predict** to know the churn status.")

# Input fields
Age = st.number_input("Enter Age", min_value=12, max_value=85, value=30)
Tenure = st.number_input("Enter Tenure (in months)", min_value=0, max_value=130, value=10)
MonthlyCharges = st.number_input("Enter Monthly Charges ", min_value=30, max_value=130,value=50)
Gender = st.selectbox("Select Gender", ["Male","Female"])

if st.button("Predict"):
    Gender = 1 if Gender == "Female" else 0
    X = np.array([[Age, Gender, Tenure, MonthlyCharges]])
    prediction = model.predict(X)[0]
    result = "Churned" if prediction == 1 else "Not Churned"

    st.success(f"Prediction: **{result}**")