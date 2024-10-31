from flask import Flask, render_template, request, Blueprint
import sqlite3

bp = Blueprint('flightSearch', __name__)

con = sqlite3.connect("db/main.db", check_same_thread=False)
cur = con.cursor()

@bp.route('/read-table')
def read_table():
    departureCodes = []
    arrivalCodes = []

    cur.execute("SELECT DISTINCT departure_code FROM flight")
    departureCodes = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT DISTINCT arrival_code FROM flight")
    arrivalCodes = [row[0] for row in cur.fetchall()]

    return render_template('flightSearch.html', departureCodes=departureCodes, arrivalCodes=arrivalCodes)

@bp.route('/search', methods=['POST'])
def search():
    departure = request.form.get('departure')
    arrival = request.form.get('arrival')

    flightId = None
    departureDate = None
    departureTime = None
    price = None
    flightAvailable = False

    cur.execute("""
        SELECT fid, departure_datetime, price
        FROM flight
        WHERE departure_code = ? AND arrival_code = ?
    """, (departure, arrival))

    flight = cur.fetchone()

    if flight:
        flightAvailable = True
        flightId = flight[0]
        departureDate = flight[1][:10]
        departureTime = flight[1][11:]
        price = flight[2]

    if flightAvailable:
        return render_template('flightSearch.html', flightId=flightId, departureDate=departureDate, departureTime=departureTime, price=price)
    else:
        return render_template('flightSearch.html', message="No flight found from your selected departure and arrival airports")

