import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction")
st.write("Enter Customer Details")

# --- MAPPINGS (based on your LabelEncoder logic) ---
yes_no = {"No": 0, "Yes": 1}

multiple_lines_map = {"No": 0, "Yes": 1, "No phone service": 2}

internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}

service_map = {"No": 0, "Yes": 1, "No internet service": 2}

contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}

payment_map = {
    "Bank transfer (automatic)": 0,
    "Credit card (automatic)": 1,
    "Electronic check": 2,
    "Mailed check": 3
}

gender_map = {"Female": 0, "Male": 1}

# --- USER INPUTS ---
gender = gender_map[st.selectbox("Gender", list(gender_map.keys()))]
SeniorCitizen = {"No": 0, "Yes": 1}[
    st.selectbox("Senior Citizen", ["No", "Yes"])
]

Partner = yes_no[st.selectbox("Partner", list(yes_no.keys()))]
Dependents = yes_no[st.selectbox("Dependents", list(yes_no.keys()))]

tenure = st.number_input("Tenure (months)", min_value=0)

PhoneService = yes_no[st.selectbox("Phone Service", list(yes_no.keys()))]
MultipleLines = multiple_lines_map[st.selectbox("Multiple Lines", list(multiple_lines_map.keys()))]

InternetService = internet_map[st.selectbox("Internet Service", list(internet_map.keys()))]

OnlineSecurity = service_map[st.selectbox("Online Security", list(service_map.keys()))]
OnlineBackup = service_map[st.selectbox("Online Backup", list(service_map.keys()))]
DeviceProtection = service_map[st.selectbox("Device Protection", list(service_map.keys()))]
TechSupport = service_map[st.selectbox("Tech Support", list(service_map.keys()))]

StreamingTV = service_map[st.selectbox("Streaming TV", list(service_map.keys()))]
StreamingMovies = service_map[st.selectbox("Streaming Movies", list(service_map.keys()))]

Contract = contract_map[st.selectbox("Contract", list(contract_map.keys()))]
PaperlessBilling = yes_no[st.selectbox("Paperless Billing", list(yes_no.keys()))]

PaymentMethod = payment_map[st.selectbox("Payment Method", list(payment_map.keys()))]

MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

# --- PREDICTION ---
if st.button("Predict"):

    input_data = np.array([[gender, SeniorCitizen, Partner, Dependents,
                            tenure, PhoneService, MultipleLines,
                            InternetService, OnlineSecurity, OnlineBackup,
                            DeviceProtection, TechSupport,
                            StreamingTV, StreamingMovies,
                            Contract, PaperlessBilling, PaymentMethod,
                            MonthlyCharges, TotalCharges]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer will stay")