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
        higher_bool = request.args.get('higher') 
        failures = int(request.args.get('failures'))
        schoolsup_bool = request.args.get('schoolsup')
        if higher_bool == "yes":
            higher_bool = 1
        else:
            higher_bool = 0
        if schoolsup_bool == "yes":
            schoolsup_bool = 1
        else:
            schoolsup_bool = 0

        data = [[higher_bool], [failures], [schoolsup_bool]]
        print(data)
        query_df = pd.DataFrame({
            'higher_bool': pd.Series(higher_bool),
            'failures': pd.Series(failures),
            'schoolsup_bool': pd.Series(schoolsup_bool)
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction))
