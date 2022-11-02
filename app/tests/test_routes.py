from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'
    response1 = client.get(url, data={
        "G3": 1,
        "activities": True,
        "failures": True,
        "school": False
    })
    assert response1.status_code == 200
    response2 = client.get(url, data={
        "G3": "No",
        "activities": "1",
        "failures": 1,
        "school": "False"
    })
    assert response2.status_code != 200