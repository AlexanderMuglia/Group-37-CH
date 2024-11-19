import pytest
import sqlite3
from app import app

@pytest.fixture
def client():
    # set up test client
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_navigation_between_pages(client):
    # 1. Test navigation to the main page
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome!' in response.data

    # 2. Test navigation to the flight search page
    response = client.get('/read-table')
    assert response.status_code == 200
    assert b'Flight Search' in response.data

    # 3. Test navigation to the flight viewingh page
    response = client.get('/view/0201')
    assert response.status_code == 200
    assert b'My Flights' in response.data
