# import necessary libraries
import numpy as np
import pandas as pd
import os

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import keras
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.utils import to_categorical
from sklearn.externals import joblib
from keras import backend as K


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
model = None
graph = None
model_scaler = None


def load_mortgage_model():
    global model
    global graph
    global model_scaler
    model = keras.models.load_model('mortgage_model_trained.h5')
    graph = K.get_session().graph
    model_scaler = joblib.load('model_scaler.pkl')



load_mortgage_model()


def format_and_scale_input(input_data):
    print(f' input_data - {input_data}')
    forminput = pd.DataFrame([input_data])
    forminput_scaled = model_scaler.transform(forminput)
    return forminput_scaled


def make_prediction(input_data):
    forminput_scaled = format_and_scale_input(input_data)
    prediction_binary = model.predict_classes(forminput_scaled)
    return prediction_binary[0]


def generate_response_dict(prediction_binary):
    if int(prediction_binary) == 1:
        prediction = 'approved'
    else:
        prediction = 'denied'
    response_dict = {'prediction_type': str(prediction_binary), 'prediction': prediction}
    return response_dict


'''
POST endpoint that receives applicant data and returns a classification result
'''
@app.route('/submit', methods = ['POST'])
def submit():
    data = request.json
    print(f' json post - {data}')
    correct_keys = ['ApplicantIncome', 'CoapplicantIncome', 'Credit_History',
                    'Dependents', 'Education', 'LoanAmount', 'Loan_Amount_Term',
                    'Married', 'Property_Area', 'Self_Employed']
    if correct_keys == sorted(data.keys()):
        prediction_binary = make_prediction(data)
        response_dict = generate_response_dict(prediction_binary)
        return jsonify(response_dict)
    else:
        error_json = {'error': 'Invalid/incomplete input'}
        return jsonify(error_json)


'''
GET endpoint that serves up the index page
'''
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    load_mortgage_model()
    app.run()
