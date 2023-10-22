from TestResult import enc, dec
import sqlite3 as sql

DEFAULT_ADMIN_USERNAME = 'admin'
DEFAULT_ADMIN_PASSWORD = 'admin'

con = sql.connect('HospitalDB.db')
con.execute('DROP TABLE IF EXISTS hospital')
con.execute('''CREATE TABLE IF NOT EXISTS hospital(
            UserID INTEGER NOT NULL PRIMARY KEY,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Phone TEXT NOT NULL,
            COVID INTEGER NOT NULL,
            Security INTEGER NOT NULL,
            Password TEXT NOT NULL);
            ''')
cur = con.cursor()
cur.execute(
    'INSERT INTO hospital(UserID,Name,Age,Phone,Covid,Security,Password) VALUES (?,?,?,?,?,?,?)',
    (-1, enc('Test'), 42, enc('1234567890'), 0, 1, enc('password')))
cur.execute(
    'INSERT INTO hospital(UserID,Name,Age,Phone,Covid,Security,Password) VALUES (?,?,?,?,?,?,?)',
    (0, enc(DEFAULT_ADMIN_USERNAME), 123, enc('9999999999'), 0, 3, enc(DEFAULT_ADMIN_PASSWORD)))
cur.execute(
    'INSERT INTO hospital(UserID,Name,Age,Phone,Covid,Security,Password) VALUES (?,?,?,?,?,?,?)',
    (1, enc("user1"), 11, enc('1111111111'), 0, 1, enc("password1")))
cur.execute(
    'INSERT INTO hospital(UserID,Name,Age,Phone,Covid,Security,Password) VALUES (?,?,?,?,?,?,?)',
    (2, enc("user2"), 22, enc("2222222222"), 1, 1, enc("password2")))

cur.execute(
    'INSERT INTO hospital(UserID,Name,Age,Phone,Covid,Security,Password) VALUES (?,?,?,?,?,?,?)',
    (3, enc("user3"), 33, enc('3333333333'), 0, 1, enc("password3")))
cur.execute(
    'INSERT INTO hospital(UserID,Name,Age,Phone,Covid,Security,Password) VALUES (?,?,?,?,?,?,?)',
    (4, enc("user4"), 44, enc('4444444444'), 0, 1, enc("password4")))

# print table as is
cur.execute('SELECT * FROM hospital')
print(cur.fetchall())

# print encrypted values and its decrypted value for debugging
cur.execute('SELECT Name, Phone, Password FROM hospital')
for row in cur.fetchall():
    for element in row:
        print(element + "\t== ", dec(element))

con.commit()
con.close()

"""
Encryption to Decryption chart:

IurP/g==	==  Test
R+Jn1neszFurfw==	==  1234567890
BniKhwy2PmA=	==  password
FxPaQiM=	==  admin
T9azu3cYMXTSyw==	==  9999999999
FxPaQiM=	==  admin
A0gRmcw=	==  user1
R+FiTkVp88n7mw==	==  1111111111
BniKhwy2PmA7	==  password1
A0gRmc8=	==  user2
RAvnh7pcY0nllw==	==  2222222222
BniKhwy2PmA4	==  password2
A0gRmc4=	==  user3
RWtRgCe6IVrbLQ==	==  3333333333
BniKhwy2PmA5	==  password3
A0gRmck=	==  user4
QsFPIryny6mw6A==	==  4444444444
BniKhwy2PmA+	==  password4

"""