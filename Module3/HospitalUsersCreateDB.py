import sqlite3
conn = sqlite3.connect(".\sql.dp")
cur = conn.cursor()

# drop and create a new table
print("HospitalUser table dropped.")
cur.execute('''DROP TABLE HospitalUser''')

print("HospitalUser table created.")
cur.execute('''CREATE TABLE HospitalUser(
    UserId INTEGER PRIMARY KEY NOT NULL,
    UserName TEXT NOT NULL,
    UserAge INTEGER NOT NULL,
    UserPhNum TEXT NOT NULL,
    UserHasCOVID BOOL NOT NULL,
    SecurityLevel INTEGER NOT NULL,
    LoginPassword TEXT NOT NULL);
''')

# data in a list format to be Insert into table
data = [
    (1, 'PDiana', 34, '123-675-7645', 0, 1, 'test123'),
    (2, 'TJones', 68, '895-345-6523', 1, 2, 'test123'),
    (3, 'AMath', 29, '428-197-3967', 0, 3, 'test123'),
    (4, 'BSmith', 37, '239-567-3498', 1, 2, 'test123')
]

cur.executemany('Insert Into HOSPITALUSER Values (?,?,?,?,?,?,?);', data)

# commit changes to file
conn.commit()

# print all values in the tables
import pandas as pd

df = pd.read_sql_query("Select * from HOSPITALUSER;", conn)
for d in df.itertuples():
    print(d)

# close connection
conn.close()
print("Connection closed.")
