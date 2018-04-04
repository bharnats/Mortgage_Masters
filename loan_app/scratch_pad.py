from keras.models import load_model
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.utils import to_categorical
from sklearn.externals import joblib
from tensorflow import get_default_graph

model = load_model('static/models/mortgage_model_trained.h5')
model_scaler = joblib.load('static/models/model_scaler.pkl')


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

'''
forminput = pd.DataFrame([sample_input_dict])

print(forminput)


forminput_scaled = model_scaler.transform(forminput)
prediction = model.predict_classes(forminput_scaled)[0]
print(f'prediction - {prediction}')
'''
def format_and_scale_input(input_data):
    '''input_dict = input_data.to_dict(flat=False)
    for key, value in input_dict.items():
        input_dict[key] = value[0]
    forminput = pd.DataFrame([input_dict])
    '''
    forminput = pd.DataFrame([sample_input_dict])
    print(forminput)
    forminput_scaled = model_scaler.transform(forminput)
    return forminput_scaled


def make_prediction(input_data):
    forminput_scaled = format_and_scale_input(input_data)
    prediction = model.predict_classes(forminput_scaled)
    return prediction[0]


prediction = make_prediction(sample_input_dict)
print(prediction)
