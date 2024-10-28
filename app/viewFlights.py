from flask import Flask, render_template, request, Blueprint
import sqlite3

bp = Blueprint('viewFlights', __name__)

con = sqlite3.connect("db/main.db", check_same_thread=False)
cur = con.cursor()

@bp.route('/view/<uid>')
def view_flights(uid):
    flights = []

    # get current user info from db
    res = cur.execute(f"SELECT * FROM user WHERE uid='{uid}'")
    user_info = res.fetchone()

    if user_info:
        for flight in user_info[3].split("|"):
            flightMap = get_flight_info(flight)
            if flightMap:
                flights.append(flightMap)

    return render_template('viewFlights.html', flights=flights)

def get_flight_info(flight):
    ret = {}

    # get flight info from db
    res = cur.execute(f"SELECT * FROM flight WHERE fid='{flight[:5]}'")
    flight_info = res.fetchone()

    if flight_info:
        ret["id"] = flight_info[0]
        ret["departureDate"] = flight_info[1][:10]
        ret["departureTime"] = flight_info[1][11:]
        ret["departureAirport"] = flight_info[2]
        ret["arrivalAirport"] = flight_info[3]
        ret["price"] = "$" + flight_info[4]
        ret["seatNum"] = flight[-2:]
        return ret
    else:
        return None

