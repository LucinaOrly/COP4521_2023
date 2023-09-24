import sqlite3

#create new db
conn = sqlite3.connect('CrapsDB.db')

# create Cursor to execute queries
cur = conn.cursor()


# drop table from database
try:
    conn.execute('''Drop table Player''')
    # save changes
    conn.commit()
    print('Player table dropped.')
except:
    print('Player table did not exist')



# create table in database
cur.execute('''CREATE TABLE PLAYER(
Player_ID INTEGER PRIMARY KEY NOT NULL,
Name TEXT NOT NULL,
Age INTEGER NOT NULL,
Money REAL NOT NULL,
Password TEXT NOT NULL);
''')

# save changes
conn.commit()
print('Player Table created.')


cur.execute('''Insert Into PLAYER ('Name','Age','Money','Password') 
Values ('Princess Diana', 28, 1999999888,'test123');''')

conn.commit()

cur.execute('''Insert Into PLAYER ('Name','Age','Money','Password') 
Values ('Henry Thorgood', 56, 39888,'test123');''')

conn.commit()

cur.execute('''Insert Into PLAYER ('Name','Age','Money','Password') 
Values ('Tina Fairchild', 38, 79888,'test123');''')

conn.commit()

# iterate over the rows
for row in cur.execute('SELECT * FROM Player;'):
    print(row)


# close database connection
conn.close()
print('Connection closed.')
