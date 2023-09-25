import sqlite3 as sql

con = sql.connect('HospitalDB.db')
con.execute('DROP TABLE IF EXISTS hospital')
con.execute('''CREATE TABLE IF NOT EXISTS hospital(
            Name TEXT NOT NULL PRIMARY KEY,
            Age INTEGER NOT NULL,
            Phone TEXT NOT NULL,
            COVID INTEGER NOT NULL,
            Security INTEGER NOT NULL,
            Password TEXT NOT NULL);
            ''')
cur = con.cursor()
cur.execute('''INSERT INTO hospital(name,age,phone,covid,security,password) VALUES (?,?,?,?,?,?);''', (
            'Test',42,'1234567890',0,1,'password'))
con.commit()
con.close()
