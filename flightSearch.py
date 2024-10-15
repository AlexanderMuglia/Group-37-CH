from flask import Flask
import csv

app = Flask(__name__)

@app.route('/read-csv')
def read_csv():
    departureCodes = []
    arrivalCodes = []
    csv_file_path = 'db/flights.csv'

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2] not in departureCodes:
                departureCodes.append(row[2])
            if row[3] not in arrivalCodes:
                arrivalCodes.append(row[3])
        print(departureCodes)
        print(arrivalCodes)

    return "CSV file content printed in the terminal!"

if __name__ == '__main__':
    app.run(debug=True)
