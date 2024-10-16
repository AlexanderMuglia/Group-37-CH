from flask import Flask, render_template, request, Blueprint
import csv

bp = Blueprint('flightSearch', __name__)
@bp.route('/read-csv')
def read_csv():
    departureCodes = []
    arrivalCodes = []
    csv_file_path = 'db/flights.csv'
    
    # read csv file
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # skip headings row
        next(reader)
        for row in reader:
            if row[2] not in departureCodes:
                departureCodes.append(row[2])
            if row[3] not in arrivalCodes:
                arrivalCodes.append(row[3])
    
    # pass lists to html
    return render_template('flightSearch.html', departureCodes=departureCodes, arrivalCodes=arrivalCodes)

# route to handle form submission
@bp.route('/search', methods=['POST'])
def search():
    # get selected departure and arrival codes from the form
    departure = request.form.get('departure')
    arrival = request.form.get('arrival')
    
    flightId = None
    departureDate = None
    departureTime = None
    price = None
    flightAvailable = False
    csv_file_path = 'db/flights.csv'
    
    # read csv file
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # skip headings row
        next(reader)
        for row in reader:
            if row[2] == departure and row[3] == arrival:
                flightAvailable = True
                flightId = row[0]
                departureDate = row[1][:10]
                departureTime = row[1][11:]
                price = row[4]
                break

    # return appropriate message/variables
    if flightAvailable:
        return render_template('flightSearch.html', flightId=flightId, departureDate=departureDate, departureTime=departureTime, price=price)
    else:
        return render_template('flightSearch.html', message="No flight found from your selected departure and arrival airports")
