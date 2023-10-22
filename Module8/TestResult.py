import Encryption
import sqlite3 as sql

P = "positive"
U = "undermined"
N = "negative"
def enc(raw):
    return Encryption.cipher.encrypt(bytes(raw, 'utf-8')).decode('utf-8')


# decrypt using the Encryption script
def dec(raw):
    return Encryption.cipher.decrypt(raw)


if __name__ == '__main__':
    con = sql.connect("HospitalDB.db")
    con.execute("DROP TABLE IF EXISTS UserTestResults")
    con.execute("""CREATE TABLE UserTestResults(
                 TestResultId INTEGER NOT NULL PRIMARY KEY,
                 UserId INTEGER NOT NULL,
                 TestName STRING NOT NULL,
                 TestResult STRING NOT NULL); 
               """)
    con.execute('INSERT INTO UserTestResults(testresultid,userid,testname,testresult) VALUES (?,?,?,?)',
                (1,1,enc("user1"),enc(N)))
    con.execute('INSERT INTO UserTestResults(testresultid,userid,testname,testresult) VALUES (?,?,?,?)',
                (2,2,enc("user2"),enc(P)))
    con.execute('INSERT INTO UserTestResults(testresultid,userid,testname,testresult) VALUES (?,?,?,?)',
                (3,3,enc("user3"),enc(N)))
    con.execute('INSERT INTO UserTestResults(testresultid,userid,testname,testresult) VALUES (?,?,?,?)',
                (4,4,enc("user4"),enc(N)))

    con.execute('INSERT INTO UserTestResults(testresultid,userid,testname,testresult) VALUES (?,?,?,?)',
                (5,0,enc("admin"),enc(U)))
    con.execute('INSERT INTO UserTestResults(testresultid,userid,testname,testresult) VALUES (?,?,?,?)',
                (6,-1,enc("test"),enc(U)))

    con.commit()

    # print UserTestResults Table
    cur = con.cursor()
    cur.execute("SELECT * from UserTestResults")
    print(cur.fetchall())

    con.commit()
    con.close()