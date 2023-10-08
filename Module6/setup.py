import Encryption
import sqlite3 as sql

DEFAULT_ADMIN_USERNAME = 'admin'
DEFAULT_ADMIN_PASSWORD = 'admin'


# encrypt using the Encryption script
def enc(raw):
    return Encryption.cipher.encrypt(bytes(raw, 'utf-8')).decode('utf-8')


# decrypt using the Encryption script
def dec(raw):
    return Encryption.cipher.decrypt(raw)


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

IurP/g==            == Test
R+Jn1neszFurfw==    == 1234567890
BniKhwy2PmA=        == password

FxPaQiM=            == admin
T9azu3cYMXTSyw==    == 9999999999
FxPaQiM=            == admin
"""