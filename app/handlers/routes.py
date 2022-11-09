import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"


    @app.route('/predict')
    def predict():
        #use entries from the query string here but could also use json
        studytime = int(request.args.get('studytime'))
        failures = int(request.args.get('failures'))
        absences = int(request.args.get('absences'))
        if absences>=10:
            absences=10
        else:
            absences = absences
        

        data = [[absences], [failures], [studytime]]
        print(data)
        query_df = pd.DataFrame({
            'absences': pd.Series(absences),
            'failures': pd.Series(failures),
            'studytime': pd.Series(studytime)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))
