from flask import Flask, render_template, request, Blueprint
import sqlite3

bp = Blueprint('flightSearch', __name__)

con = sqlite3.connect("db/main.db", check_same_thread=False)
cur = con.cursor()

@bp.route('/read-csv')
def read_csv():
    departureCodes = []
    arrivalCodes = []

    # Query distinct departure and arrival codes from the database
    cur.execute("SELECT DISTINCT departure_code FROM flight")
    departureCodes = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT DISTINCT arrival_code FROM flight")
    arrivalCodes = [row[0] for row in cur.fetchall()]

    # Pass lists to HTML template
    return render_template('flightSearch.html', departureCodes=departureCodes, arrivalCodes=arrivalCodes)

# Route to handle form submission
@bp.route('/search', methods=['POST'])
def search():
    # Get selected departure and arrival codes from the form
    departure = request.form.get('departure')
    arrival = request.form.get('arrival')

    flightId = None
    departureDate = None
    departureTime = None
    price = None
    flightAvailable = False

    # Query the database for a flight matching the selected departure and arrival codes
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

    # Return appropriate message/variables
    if flightAvailable:
        return render_template('flightSearch.html', flightId=flightId, departureDate=departureDate, departureTime=departureTime, price=price)
    else:
        return render_template('flightSearch.html', message="No flight found from your selected departure and arrival airports")

