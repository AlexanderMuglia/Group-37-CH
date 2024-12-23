# Group-37-CH
## Flight Booking System

For assignment-related readme content and any other files that were specifically requested in a particular assignment, please see the respective Assignment-X directories. This readme file contains general information about running and testing the app.

### Creating the Database
If the database hasn't been created locally yet or has somehow gotten corrupted, run the following in the project root directory to clear and recreate the database
```
rm db/*
python3 app/bootstrap_db.py
```

### Running the app
In the root directory of the project, after starting your venv, make sure to install the requirements with
```
pip install -r requirements.txt
```

Then, run the app with
```
python3 app/app.py
```

### Testing the app
In the root directory of the project, after starting your venv, make sure to install the requirements with
```
pip install -r requirements.txt
```

Then, run all test files with
```
pytest -v
```
