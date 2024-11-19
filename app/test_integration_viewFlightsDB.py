import pytest
import sqlite3
from app import app
from viewFlights import get_flight_info

@pytest.fixture
def client():
    # set up test client
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_view_flights_integration(client):
    uid = '0001'
    # test view/0001 route to ensure it loads user 0001's data
    response = client.get(f'/view/{uid}')


    # initiate db instance
    con = sqlite3.connect("db/main.db", check_same_thread=False)
    cur = con.cursor()
    # Make the DB call to compare to view flight data
    flights = []
    res = cur.execute(f"SELECT * FROM user WHERE uid='{uid}'")
    user_info = res.fetchone()

    if user_info:
        for flight in user_info[3].split("|"):
            flightMap = get_flight_info(flight)
            if flightMap:
                flights.append(flightMap)

    assert response.status_code == 200
    # compare direct db call to data from ViewFlights
    for flight in flights:
        for key in flight.keys():
            assert str.encode(flight[key]) in response.data
