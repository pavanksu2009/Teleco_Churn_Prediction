import numpy as np
import pandas as pd
import streamlit as st
from flask import Flask, json, jsonify, request
import joblib

load_model = joblib.load("models/challa_logistic_regression.sav")


def predict_single(customer, model):
    X = pd.DataFrame([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]



app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    prediction = predict_single(customer, load_model)
    churn = prediction >= 0.5
    
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)    