from flask import Flask, render_template, request, Blueprint
import csv

bp = Blueprint('viewFlights', __name__)

@bp.route('/view')
def view_flights():
    flights = []
    user_csv_file_path = 'db/users.csv'
    
    # read csv file
    users = open(user_csv_file_path, newline="")
    reader = csv.reader(users)
    # skip headings row
    next(reader)
    for row in reader:
        if row[0] == "0001":
            for flight in row[3].split("|"):
                flightMap = get_flight_info(flight)
                flights.append(flightMap)
    return render_template('viewFlights.html', flights=flights)

def get_flight_info(flight):
    flight_csv_file_path = 'db/flights.csv'
    ret = {}
    # read csv file
    flight_file = open(flight_csv_file_path, newline="")
    reader = csv.reader(flight_file)
    # skip headings row
    next(reader)
    for row in reader:
        if row[0] == flight[:5]:
            ret["id"] = row[0]
            ret["departureDate"] = row[1][:10]
            ret["departureTime"] = row[1][11:]
            ret["departureAirport"] = row[2]
            ret["arrivalAirport"] = row[3]
            ret["price"] = "$"+row[4]
            ret["seatNum"] = flight[-2:]

    return ret
