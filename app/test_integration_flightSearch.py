import pytest
import sqlite3
from flightSearch import get_codes
from app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_get_codes_integration():
    # test fetching departure and arrival codes
    con = sqlite3.connect("db/main.db", check_same_thread=False)
    cur = con.cursor()

    # get expected results from db
    cur.execute("SELECT DISTINCT departure_code FROM flight")
    expectedDepartureCodes = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT DISTINCT arrival_code FROM flight")
    expectedArrivalCodes = [row[0] for row in cur.fetchall()]

    departureCodes, arrivalCodes = get_codes()
    assert departureCodes == expectedDepartureCodes
    assert arrivalCodes == expectedArrivalCodes


def test_read_table_integration(client):
    # test the /read-table route
    response = client.get('/read-table')
    assert response.status_code == 200

    # connect to db to fetch expected data
    con = sqlite3.connect("db/main.db", check_same_thread=False)
    cur = con.cursor()
    cur.execute("SELECT DISTINCT departure_code FROM flight")
    departureCodes = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT DISTINCT arrival_code FROM flight")
    arrivalCodes = [row[0] for row in cur.fetchall()]

    # check that  response contains departure and arrival codes
    for code in departureCodes:
        assert str.encode(code) in response.data
    for code in arrivalCodes:
        assert str.encode(code) in response.data


def test_search_integration(client):
    # test the /search route
    testData = [
        {"departure": "YYZ", "arrival": "LAX", "expectedFlightID": "f0001"},
        {"departure": "YYC", "arrival": "YYZ", "expectedFlightID": "f0002"},
        {"departure": "YYZ", "arrival": "SYD", "expectedFlightID": "f1243"},
        {"departure": "XYZ", "arrival": "ABC", "expectedMessage": "No flight found from your selected departure and arrival airports"},
    ]

    for data in testData:
        response = client.post('/search', data={"departure": data["departure"], "arrival": data["arrival"]})
        assert response.status_code == 200

        # check for expected flight ID and message
        if "expectedFlightID" in data:
            assert str.encode(data["expectedFlightID"]) in response.data
        elif "expectedMessage" in data:
            assert str.encode(data["expectedMessage"]) in response.data
