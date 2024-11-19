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
    # ensure that the link to search flights is there.
    assert b'Search for flights' in response.data
    assert b'/read-table' in response.data

    # 2. Test navigation to the flight search page. This simulates
    # a user clicking the link that we confirmed exists above.
    response = client.get('/read-table')
    assert response.status_code == 200
    assert b'Flight Search' in response.data
    # ensure that the link to home is there.
    assert b'Home' in response.data
    assert b'/' in response.data

    # 3. Test navigation back to the home page. This simulates
    # a user clicking the link that we confirmed exists above.
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome!' in response.data
    # ensure that the link to search flights is there.
    assert b'View my flights' in response.data
    assert b'/view' in response.data

    # 4. Test navigation to the flight viewing page. This simulates
    # a user clicking the link that we confirmed exists above.
    response = client.get('/view/0201')
    assert response.status_code == 200
    assert b'My Flights' in response.data
    # ensure that the link to home is there.
    assert b'Home' in response.data
    assert b'/' in response.data

    # 5. Finally, test going back home from the view flights page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome!' in response.data
