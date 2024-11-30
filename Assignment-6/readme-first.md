# Assignment 6

### Creating the Database
If the database hasn't been created locally yet or has somehow gotten corrupted, run the following in the project root directory to clear and recreate the database
```
rm db/*
python3 app/bootstrap_db.py
```

## Running the app
In the root directory of the project, after starting your venv, make sure to install the requirements with
```
pip install -r requirements.txt
```

Then, run the app with
```
python3 app/app.py
```

## Testing the app
In the root directory of the project, after starting your venv, make sure to install the requirements with
```
pip install -r requirements.txt
```

Then, run all test files with
```
pytest -v
```
Integration tests run alongside the unit tests.

## Testing code coverage
Install coverage.py if you haven't already with
```
pip install coverage
```

Then in the root project directory, run the test scripts through coverage with
```
coverage run -m pytest -v
```

Finally, view the coverage report with
```
coverage report -m 
```
to see a full report on the code coverage

# Running E2E Tests

Please install Google Chrome if you don't have it yet.

Run your test of choice with:
```
python3 app/<test-name>
```

For example, to run the e2e_test_view_flights test, use the command:
```
python3 app/e2e_test_view_flights.py
```

