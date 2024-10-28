import sqlite3

# only need to call once to create db. Left here in case we delete it for any reason
def populate_db(db_name):
    con = sqlite3.connect(f"db/{db_name}.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE user(uid, username, password, flights)")
    cur.execute("CREATE TABLE flight(fid, departure_datetime, departure_code, arrival_code, price, seats_taken)")
    user_data = [
        ('0001','alex', 'hunter2', 'f0001s01|f0002s03|f0003s01'),
        ('0002','user2', 'user2', 'f0001s02|f0002s02')
    ]
    flight_data = [
        ('f0001', '2024-12-24T17:00:00', 'YYZ', 'LAX', '829.00', 's01|s02'),
        ('f0002', '2025-01-14T22:00:00', 'YYC', 'YYZ', '432.00', 's02|s03'),
        ('f0003', '2024-12-29T09:30:00', 'YYZ', 'YYC', '649.00', 's01'),
        ('f1243', '2024-12-29T19:10:00', 'YYZ', 'SYD', '2249.00', '')
    ]
    cur.executemany("INSERT INTO user VALUES(?, ?, ?, ?)", user_data)
    cur.executemany("INSERT INTO flight VALUES(?, ?, ?, ?, ?, ?)", flight_data)
    con.commit()

if __name__ == "__main__":
    populate_db("main")
