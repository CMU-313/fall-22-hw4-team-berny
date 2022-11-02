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
        "activities": True,
        "failures": True,
        "school": False
    })
    assert response1.status_code == 200
    assert isinstance(response1.data['G3'],int)
    assert response1.data['G3'] >= 0
    assert response1.data['G3']<=20
    response2 = client.get(url, data={
        "activities": "1",
        "failures": 1,
        "school": "False"
    })
    assert response2.status_code == 400
