from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/read-csv')
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
    print(departureCodes)
    print(arrivalCodes)
    
    #pass the lists to html file
    return render_template('flightSearch.html', departureCodes=departureCodes, arrivalCodes=arrivalCodes)

if __name__ == '__main__':
    app.run(debug=True)

