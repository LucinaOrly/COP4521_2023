"""
Name:John Valencia-Londono
Date:09/17/2023
Assignment:Module 3: SQLite3 Database
Due Date:09/17/2023
About this project:
    This submission requires the following to be submitted in

1) In a single Python script called HospitalUsersCreateDB.py:

    DDL for the table
    DML for the table
    Use Cursor results from a Select statement to display the information from all the rows in the table
    DDL Script Requirements:
    You must have a drop table command at the top of your script to drop the table in your database.
    You must have a create table statement
    Your table must contain the following attributes: UserId, UserName, UserAge, UserPhNum, UserHasCOVID, SecurityLevel, and LoginPassword
    Your table create script must properly define UserId as the primary key.
    Your script must run to completion without errors.
    DML Script Requirements:
    Your script must create at least 4 rows of data in the table created above with relevant data.
    Use Cursor results from a Select statement to display the information from all the rows in the table
2) In a different Python script called HospitalUsersDBUpdate.py:

    This script must contain the following:

    A deletion SQL statement that only deletes at least 1 row but not all rows of data in your table.
    An update SQL statement for the table that only updates attributes for at least 1 row but not all rows of data in your table.
    A select statement that selects data from a single table;
    A select statement that selects data from a single table that limits the columns returned; (Hint: use Select statement that lists the column names)
    A select statement that selects data from a single table that limits the rows returned; (Hint: use a where clause in your Select statement)
    A select statement that selects data from a single table that limits both the columns and the rows returned; (Hint: use Select statement that lists the column names and uses a where clause)
Assumptions:sql.dp exists and has table HOSPITALUSER
All work below was performed by John Valencia-Londono """
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
    UserHasCOVID INTEGER NOT NULL,
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

''' SAMPLE OUTPUT
HospitalUser table dropped.
HospitalUser table created.
Pandas(Index=0, UserId=1, UserName='PDiana', UserAge=34, UserPhNum='123-675-7645', UserHasCOVID=0, SecurityLevel=1, LoginPassword='test123')
Pandas(Index=1, UserId=2, UserName='TJones', UserAge=68, UserPhNum='895-345-6523', UserHasCOVID=1, SecurityLevel=2, LoginPassword='test123')
Pandas(Index=2, UserId=3, UserName='AMath', UserAge=29, UserPhNum='428-197-3967', UserHasCOVID=0, SecurityLevel=3, LoginPassword='test123')
Pandas(Index=3, UserId=4, UserName='BSmith', UserAge=37, UserPhNum='239-567-3498', UserHasCOVID=1, SecurityLevel=2, LoginPassword='test123')
Connection closed.

'''