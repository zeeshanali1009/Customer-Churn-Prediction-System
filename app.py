import streamlit as st
from src.predict import predict_churn

st.set_page_config(page_title="Customer Churn Prediction System")
st.title("📉 Customer Churn Prediction System")
st.markdown("Predict whether a customer is likely to churn or stay.")

# Input fields
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner", ["No", "Yes"])
dependents = st.selectbox("Has Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
phone = st.selectbox("Phone Service", ["No", "Yes"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
payment = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
monthly = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total = st.number_input("Total Charges", min_value=0.0, value=1000.0)

if st.button("Predict Churn"):
    input_data = {
        "gender": 1 if gender=="Male" else 0,
        "SeniorCitizen": senior,
        "Partner": 1 if partner=="Yes" else 0,
        "Dependents": 1 if dependents=="Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone=="Yes" else 0,
        "MultipleLines": 0,  # default
        "InternetService": 2 if internet=="Fiber optic" else 1 if internet=="DSL" else 0,
        "OnlineSecurity": 0,
        "OnlineBackup": 0,
        "DeviceProtection": 0,
        "TechSupport": 0,
        "StreamingTV": 0,
        "StreamingMovies": 0,
        "Contract": 2 if contract=="Two year" else 1 if contract=="One year" else 0,
        "PaperlessBilling": 1 if paperless=="Yes" else 0,
        "PaymentMethod": 0 if payment=="Electronic check" else 1 if payment=="Mailed check" else 2 if payment=="Bank transfer (automatic)" else 3,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    prediction, probability = predict_churn(input_data)
    result = "Churn" if prediction==1 else "Stay"
    st.success(f"Prediction: {result}  |  Probability of churn: {probability*100:.2f}%")
