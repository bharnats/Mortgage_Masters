# import necessary libraries
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route('/submit', methods = ['POST'])
def submit():
    data = request.form
    return jsonify(data)


if __name__ == "__main__":
    app.run()
