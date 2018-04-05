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
import numpy as np
import pandas as pd
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


sample_input_dict = {'Married': 1,
                    'Dependents': 0,
                    'Education': 1,
                    'Self_Employed': 0,
                    'ApplicantIncome': 9000,
                    'CoapplicantIncome': 2000,
                    'LoanAmount': 275,
                    'Loan_Amount_Term': 360,
                    'Credit_History': 1,
                    'Property_Area': 2}


def load_mortgage_model():
    global model
    global graph
    global model_scaler
    model = keras.models.load_model('static/models/mortgage_model_trained.h5')
    graph = K.get_session().graph
    model_scaler = joblib.load('static/models/model_scaler.pkl')


def format_and_scale_input(input_data):
    forminput = pd.DataFrame([input_data])
    forminput_scaled = model_scaler.transform(forminput)
    return forminput_scaled


def make_prediction(input_data):
    forminput_scaled = format_and_scale_input(input_data)
    prediction_binary = model.predict_classes(forminput_scaled)
    return str(prediction_binary[0])


def generate_response_dict(prediction_binary):
    if int(prediction_binary) == 1:
        prediction = 'approved'
    else:
        prediction = 'denied'
    response_dict = {'prediction_type': prediction_binary, 'prediction': prediction}
    return response_dict


'''
POST endpoint that receives applicant data and returns a classification result
'''
@app.route('/submit', methods = ['POST'])
def submit():
    data = request.json
    print(data)
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


'''
GET endpoint that serves up the index page
'''
@app.route('/test')
def test():
    test_dict = {'test': 'yes'}
    return jsonify(test_dict)







if __name__ == "__main__":
    load_mortgage_model()
    app.run()
