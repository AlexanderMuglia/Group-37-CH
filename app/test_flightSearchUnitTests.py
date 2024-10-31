import pytest
from app import app

@pytest.fixture
def client():
    # set up test client
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_read_table_route(client):
    # test read-table route to ensure it loads correctly
    response = client.get('/read-table')
    assert response.status_code == 200
    assert b"Flight Search" in response.data  

def test_valid_flight_found(client):
    # simulate form submission with departure and arrival that a flight exists for
    response = client.post('/search', data=dict(departure='YYZ', arrival='LAX'))
    assert response.status_code == 200
    assert b"Flight Details" in response.data  
    assert b"Flight ID" in response.data  

def test_no_flight_found(client):
    # simulate form submission with departure and arrival that doesn't match any flight
    response = client.post('/search', data=dict(departure='YYC', arrival='SYD'))
    assert response.status_code == 200
    assert b"No flight found" in response.data  

def test_same_departure_and_arrival(client):
    # simulate form submission with the same departure and arrival codes 
    response = client.post('/search', data=dict(departure='YYC', arrival='YYC'))
    assert response.status_code == 200
    assert b"No flight found" in response.data  

def test_invalid_departure_and_arrival(client):
    # simulate form submission with completely invalid departure and arrival codes 
    response = client.post('/search', data=dict(departure='AAA', arrival='BBB'))
    assert response.status_code == 200
    assert b"No flight found" in response.data  

