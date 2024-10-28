import pytest
import os
from bootstrap_db import populate_db

def test_create_db():
    # test creation of our database.
    # Simply invoking the function as any error should cause test failure
    populate_db("test")
    # clean up after test
    os.remove("db/test.db")
