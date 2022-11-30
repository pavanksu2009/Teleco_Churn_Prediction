import numpy as np
import pandas as pd
import streamlit as st
import joblib

load_model = joblib.load("models/challa_logistic_regression.sav")

def  main():
    st.sidebar.info("This app is created to predict churn")
    st.title("Predicting customer churn")
    Gender = st.selectbox('Gender:', [0, 1])
    Senior_Citizen= st.selectbox(' Customer is a senior citizen:', [0, 1])
    Partner= st.selectbox(' Customer has a partner:', ['Yes', 'No'])
    Dependents = st.selectbox(' Customer has  dependents:', ['Yes', 'No'])
    Phone_Service = st.selectbox(' Customer has phoneservice:', ['Yes', 'No'])
    Multiple_Lines = st.selectbox(' Customer has multiplelines:', ['Yes', 'No', 'no_phone_service'])
    Internet_Service= st.selectbox(' Customer has internetservice:', ['DSL', 'No', 'Fiber optic'])
    Online_Security= st.selectbox(' Customer has onlinesecurity:', ['Yes', 'No', 'No_internet_service'])
    Online_Backup = st.selectbox(' Customer has onlinebackup:', ['Yes', 'No', 'No_internet_service'])
    Device_Protection = st.selectbox(' Customer has deviceprotection:', ['Yes', 'No', 'No_internet_service'])
    Tech_Support = st.selectbox(' Customer has techsupport:', ['Yes', 'No', 'No_internet_service'])
    Streaming_TV = st.selectbox(' Customer has streamingtv:', ['Yes', 'No', 'No_internet_service'])
    Streaming_Movies = st.selectbox(' Customer has streamingmovies:', ['Yes', 'No', 'No_internet_service'])
    Contract= st.selectbox(' Customer has a contract:', ['Month-to-month', 'One year', 'Two year'])
    Paperless_Billing = st.selectbox(' Customer has a paperlessbilling:', ['Yes', 'No'])
    Payment_Method= st.selectbox('Payment Option:', ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check' ,'Mailed check'])
    Tenure = st.number_input('Number of months the customer has been with the current telco provider :', min_value=0, max_value=240, value=0)
    Monthly_Charges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
    Total_Charges = Tenure*Monthly_Charges
    output= ""
    input_dict = {
        "Gender":Gender ,
		"Senior_Citizen": Senior_Citizen,
		"Partner": Partner,
		"Dependents": Dependents,
		"Phone_Service": Phone_Service,
		"Multiple_Lines": Multiple_Lines,
		"Internet_Service": Internet_Service,
		"Online_Security": Online_Security,
		"Online_Backup": Online_Backup,
		"Device_Protection": Device_Protection,
		"Tech_Support": Tech_Support,
		"Streaming_TV": Streaming_TV,
		"Streaming_Movies": Streaming_Movies,
		"Contract": Contract,
		"Paperless_Billing": Paperless_Billing,
		"Payment_Method": Payment_Method,
		"Tenure": Tenure,
		"Monthly_Charges": Monthly_Charges,
		"Total_Charges": Total_Charges,
		}
    ok = st.button("Churn Prediction")
    if ok:
        X =  pd.DataFrame([input_dict])
        y_pred = load_model.predict(X)
        output = y_pred[0]
        if output > 0.5:
            st.write("The customer Exited")
        else:
            st.write("The customer Stayed")    
            

if __name__ == '__main__':
	main()