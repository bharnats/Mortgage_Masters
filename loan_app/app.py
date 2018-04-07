# import necessary libraries
import numpy as np
import pandas as pd
import os
import time


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
    relative_model_directory = get_relative_model_directory()
    model = keras.models.load_model(f'{relative_model_directory}/mortgage_model_trained.h5')
    graph = K.get_session().graph
    model_scaler = joblib.load(f'{relative_model_directory}/model_scaler.pkl')


def get_relative_model_directory():
    current_directory_path = os.getcwd()
    loan_app_position = current_directory_path.find('loan_app')
    if loan_app_position < 0:
        path_to_model = 'loan_app/static/model'
    else:
        path_to_model = 'static/model'
    return path_to_model


load_mortgage_model()


def format_and_scale_input(input_data):
    forminput = pd.DataFrame([input_data])
    column_order_list = ['Married', 'Dependents', 'Education', 'Self_Employed',
                         'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                         'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    forminput = forminput[column_order_list]
    forminput_scaled = model_scaler.transform(forminput)
    return forminput_scaled


def make_prediction(input_data):
    forminput_scaled = format_and_scale_input(input_data)
    prediction_binary = model.predict_classes(forminput_scaled)
    return prediction_binary[0]


def generate_response_dict(prediction_binary):
    if prediction_binary == 1:
        prediction = 'approved'
        prediction_text = 'Congratulations, Your Loan Has Been Approved!'
    else:
        prediction = 'denied'
        prediction_text = 'Sorry, Your Loan Has Been Denied'
    response_dict = {'prediction_type': int(prediction_binary),
                     'prediction': prediction,
                     'prediction_text': prediction_text}
    return response_dict


'''
POST endpoint that receives applicant data and returns a classification result
'''
@app.route('/submit', methods = ['POST'])
def submit():
    data = request.json
    correct_keys = ['ApplicantIncome', 'CoapplicantIncome', 'Credit_History',
                    'Dependents', 'Education', 'LoanAmount', 'Loan_Amount_Term',
                    'Married', 'Property_Area', 'Self_Employed']
    if correct_keys == sorted(data.keys()):
        prediction_binary = make_prediction(data)
        response_dict = generate_response_dict(prediction_binary)
        time.sleep(3)
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
GET endpoint that serves up the data page
'''
@app.route('/data')
def data():
    return render_template('data.html')



if __name__ == "__main__":
    load_mortgage_model()
    app.run()
