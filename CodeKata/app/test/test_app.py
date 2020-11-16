import pytest, json
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = "Unable to generate fixed width file and Unable to generate delimited file" # Testing a negative scenario
    assert expected == json.loads(res.get_data(as_text=True))
    return app.test_client()


def test_generateFixedWidthFile(app, client):
    # TODO: test the test_generateFixedWidthFile func here
    return app.test_client()


def test_generateDelimitedFile(app, client):
    # TODO: test the test_generateDelimitedFile func here
    return app.test_client()
