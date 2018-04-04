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


from keras.models import load_model
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.utils import to_categorical

# load the trained ML model
model = load_model('static/models/mortgage_model_trained.h5')


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

def scale_input(input_data):
    #scale the input
    forminput = pd.DataFrame([input_data])
    forminput_scaler = StandardScaler().fit(forminput)
    forminput_scaled = forminput_scaler.transform(forminput)
    return forminput_scaled


def make_prediction(input_data):
    forminput_scaled = scale_input(input_data)
    prediction = model.predict_classes(forminput_scaled)
    return prediction[0]



@app.route('/submit', methods = ['POST'])
def submit():
    data = request.form
    correct_keys = ['ApplicantIncome', 'CoapplicantIncome', 'Credit_History',
                    'Dependents', 'Education', 'LoanAmount', 'Loan_Amount_Term',
                    'Married', 'Property_Area', 'Self_Employed']
    '''
    if correct_keys == sorted(data.keys()):
        prediction = make_prediction(data)
        return prediction
    else:
        return 'Invalid or incomplete input'
    '''
    prediction = make_prediction(data)
    return prediction



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




if __name__ == "__main__":
    app.run(debug=True)
