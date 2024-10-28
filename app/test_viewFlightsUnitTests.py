import pytest
from app import app

@pytest.fixture
def client():
    # set up test client
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_view_route(client):
    # test view/uid route to ensure it loads correctly
    response = client.get('/view/anyid')
    assert response.status_code == 200

def test_view_id_doesnt_exist(client):
    # test view/uid route for empty flight list
    response = client.get('/view/4343')
    assert response.status_code == 200
    assert b"Looks like you have no flights booked." in response.data

def test_view_0001(client):
    # test view/0001 route to ensure it loads user 0001's data
    response = client.get('/view/0001')
    assert response.status_code == 200
    assert b"Looks like you have no flights booked." not in response.data
    assert b"Departure Airport" in response.data
    assert b"$829.00" in response.data
    assert b"01" in response.data
