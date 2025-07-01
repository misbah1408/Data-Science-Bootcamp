import pickle
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application  = Flask(__name__)
app = application

# import ridge and scaler pickle
ridge_model = pickle.load(open('models/model.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_data():
    if request.method == 'POST':
        Temparature = int(request.form.get('TEMPERATURE'))
        RH = int(request.form.get('RH'))
        Ws = int(request.form.get('WS'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = int(request.form.get('Classes'))
        Region = int(request.form.get('Region'))

        new_data = standard_scaler.transform([[Temparature, RH, Ws, Rain, FFMC, DMC, ISI , Classes, Region]])
        result = ridge_model.predict(new_data)
        print(result)
        return render_template('home.html', result="{:.1f}".format(result[0]))
    else:
        return render_template('home.html')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)