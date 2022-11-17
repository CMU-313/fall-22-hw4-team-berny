from flask import Flask

from app.handlers.routes import configure_routes

import csv

import numpy as np
import pandas as pd


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'


def test_prediction_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    correct = 0
    total = 0
    df = pd.read_csv('data/student-mat.csv', sep=';')
    for ind in df.index:
        total += 1
        studytime = df['studytime'][ind]
        failure = df['failures'][ind]
        absences = df['absences'][ind]
        G3 = df['G3'][ind]
        qual_student = 1
        if G3 < 15:
            qual_student = 0
        url = '/predict?studytime=' + str(studytime) + '&failures=' + str(failure) + '&absences=' + str(absences)
        response = client.get(url)
        assert response.status_code == 200
        assert (int(response.get_data()) == 1 or int(response.get_data()) == 0)
        if int(response.get_data()) == qual_student:
            correct += 1
    assert 0.5 < (correct / total)
    