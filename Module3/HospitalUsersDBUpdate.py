import pandas as pd
import sqlite3

# function prints contents of HOSPITALUSER with pandas lib
def print_df(conn):
    df = pd.read_sql_query("Select * from HOSPITALUSER;", conn)
    for d in df.itertuples():
        print(d)


conn = sqlite3.connect(".\sql.dp")
cur = conn.cursor()

# test Delete
print("Delete BSmith")
cur.execute('''Delete From HOSPITALUSER
    Where UserName='BSmith'; ''')
print_df(conn)
print()

# test Update
print("Update UserHasCOVID = 1 for \'AMath")
cur.execute('''UPDATE HospitalUser
    Set UserHasCOVID=1
    Where UserName = "AMath";''')
print_df(conn)
print()

# test Select of a single table
print("A select statement that selects data from a single table")
for row in cur.execute("SELECT * FROM HospitalUser"):
    print(row)
print()

# test Select of a single table limiting the columns returned
print("A select statement that selects data from a single table that limits the columns returned;")
for row in cur.execute('SELECT UserName, UserHasCOVID FROM HospitalUser;'):
    print(row)
print()

# test Select of a single table limiting rows returned
print("A select statement that selects data from a single table that limits the rows returned;")
for row in cur.execute('Select * FROM HospitalUser WHERE UserHasCOVID=1;'):
    print(row)
print()

# test Select of a single table limiting rows and columns returned
print("A select statement that selects data from a single table that limits the columns and rows returned;")
for row in cur.execute('Select Username, UserHasCOVID FROM HospitalUser WHERE UserHasCOVID=1;'):
    print(row)
print()

# not commiting changes

# close connection
conn.close()
print("Connection closed.")

''' SAMPLE OUTPUT:
Delete BSmith
Pandas(Index=0, UserId=1, UserName='PDiana', UserAge=34, UserPhNum='123-675-7645', UserHasCOVID=0, SecurityLevel=1, LoginPassword='test123')
Pandas(Index=1, UserId=2, UserName='TJones', UserAge=68, UserPhNum='895-345-6523', UserHasCOVID=1, SecurityLevel=2, LoginPassword='test123')
Pandas(Index=2, UserId=3, UserName='AMath', UserAge=29, UserPhNum='428-197-3967', UserHasCOVID=0, SecurityLevel=3, LoginPassword='test123')

Update UserHasCOVID = 1 for 'AMath
Pandas(Index=0, UserId=1, UserName='PDiana', UserAge=34, UserPhNum='123-675-7645', UserHasCOVID=0, SecurityLevel=1, LoginPassword='test123')
Pandas(Index=1, UserId=2, UserName='TJones', UserAge=68, UserPhNum='895-345-6523', UserHasCOVID=1, SecurityLevel=2, LoginPassword='test123')
Pandas(Index=2, UserId=3, UserName='AMath', UserAge=29, UserPhNum='428-197-3967', UserHasCOVID=1, SecurityLevel=3, LoginPassword='test123')

A select statement that selects data from a single table
(1, 'PDiana', 34, '123-675-7645', 0, 1, 'test123')
(2, 'TJones', 68, '895-345-6523', 1, 2, 'test123')
(3, 'AMath', 29, '428-197-3967', 1, 3, 'test123')

A select statement that selects data from a single table that limits the columns returned;
('PDiana', 0)
('TJones', 1)
('AMath', 1)

A select statement that selects data from a single table that limits the rows returned;
(2, 'TJones', 68, '895-345-6523', 1, 2, 'test123')
(3, 'AMath', 29, '428-197-3967', 1, 3, 'test123')

A select statement that selects data from a single table that limits the columns and rows returned;
('TJones', 1)
('AMath', 1)

Connection closed.

'''