# Assignment 3

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

## Testing code coverage
Install coverage.py if you haven't already with: pip install coverage
Then run: coverage report -m to see a full report on the code coverage