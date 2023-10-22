"""
Name:John Valencia-Londono
Date:10/20/2023
Assignment:Module 7: Send Encrypted Message
Due Date:10/15/2023
About this project:
Use TCP to send encrypted data across servers to send records to the UserTestResults table
Assumptions: pycryptodome package installed CORRECTLY, no duplicate records with the same username and password
All work below was performed by John Valencia-Londono """

from sqlite3 import Connection
from flask import Flask, render_template, request, flash, session
import sqlite3 as sql
import os
import socket
from TestResult import enc, dec  # helper functions

app = Flask(__name__)
nm = ''
strseparator = "^%$"

con = sql.connect('HospitalDB.db')
con.execute('''CREATE TABLE IF NOT EXISTS hospital(
            USERID INTEGER NOT NULL PRIMARY KEY,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Phone TEXT NOT NULL,
            COVID INTEGER NOT NULL,
            Security INTEGER NOT NULL,
            Password TEXT NOT NULL);
            ''')
con.commit()
con.close()


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('home.html', name=session['name'])


@app.route('/enternew')
def new_patient():
    if session.get('logged_in') and session.get('admin'):
        return render_template('input.html', allowed_action=True)
    else:
        return render_template("notfound.html")


@app.route('/input', methods=['post', 'get'])
def addrec():
    if session.get('logged_in') and session.get('admin'):
        if request.method == 'POST':
            con: Connection = sql.connect("HospitalDB.db")
            msgs = []

            try:
                # not empty
                # remove trailing and leading whitespace from input
                nm = request.form['name']
                if nm == '':
                    msgs.append("You can not enter in an empty name")

                # must be from 0 to 121
                ag = request.form['age']
                if not str.isdigit(ag) or int(ag) < 0 or int(ag) > 121:
                    print(str.isdigit(ag))
                    msgs.append("The Age must be a whole number greater than 0 and less than 121.")

                # not empty
                # remove trailing and leading whitespace from input
                ph = request.form['phone']
                if ph == '':
                    msgs.append("You can not enter in an empty phone number")

                # a checkbox that returns 'on' or 'off'
                co = request.form.get('covid')
                if co == 'on':
                    co = 1
                else:
                    co = 0

                # must be from 1 to 3
                sc = request.form['security']
                if not str.isdigit(sc) or int(sc) < 1 or int(sc) > 3:
                    msgs.append("The SecurityRoleLevel must be a numeric between 1 and 3.")


                # remove trailing and leading whitespace from input
                pw = request.form['password'].strip()
                if pw == '':
                    msgs.append("You can not enter in an empty pwd")

                # If any errors in the input, raise exception and write messages to user
                if len(msgs) > 0:
                    raise Exception("Error messages present")

                # write requests to database
                cur = con.cursor()
                cur.execute("SELECT COUNT(*) FROM hospital")
                num_of_rows = cur.fetchone()
                cur.execute("INSERT INTO hospital (userid,name,age,phone,covid,security,password) VALUES (?,?,?,?,?,?,?)",
                            (num_of_rows[0], enc(nm), ag, enc(ph), co, sc, enc(pw)))

                con.commit()
                msgs.append("record successfully added")
            except Exception as e:
                print("excepted:", e)
                con.rollback()
            finally:
                print(msgs)
                con.close()
                msg = "<br>"
                return render_template("result.html", msg='<br>' + msg.join(msgs))
    else:
        return render_template("notfound.html")


@app.route('/recordslist')
def listtests():
    if session.get('logged_in'):
        con = sql.connect("HospitalDB.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        print(session.get('userid'))
        cur.execute('SELECT * from UserTestResults WHERE UserId=?', (str(session.get('userid')),))
        rows = cur.fetchall()

        # decode information for use in display list
        for row in rows:
            enc_id = row[0]
            enc_nm = row[2]
            enc_res = row[3]
            cur.execute('UPDATE UserTestResults SET TestName=?,TestResult=? WHERE UserId=? AND TestResultID=?', (
                dec(enc_nm), dec(enc_res), session.get('userid'), enc_id))
            print(row)

        rows = cur.execute('SELECT * from UserTestResults WHERE UserId=?', (session.get('userid'),))
        print(rows)
        return render_template("recordlist.html", rows=rows)
    else:
        return render_template("notfound.html")


@app.route('/record', methods=['GET'])
def recordtestform():
    if session.get('logged_in') and session.get('staff'):
        return render_template("testform.html", allowed_action=True)
    else:
        return render_template("notfound.html")


@app.route('/record', methods=['POST'])
def recordtest():
    if session.get('logged_in') and session.get('staff'):
        if request.method == 'POST':
            sock = socket.socket()
            # sock.sendall(bytes())

            msgs = []

            try:
                # userid > 0
                userid = request.form['userid']
                if not str.isdigit(userid) or int(userid) < 0:
                    msgs.append("UserID Must be a numerical value > 0.")

                # not empty
                testname = request.form['testname']
                if testname.strip == '':
                    msgs.append("TestName cannot be empty.")

                # not empty
                testresult = request.form['testresult']
                if testresult.strip == '':
                    msgs.append("TestResult cannot be empty.")
                    print(userid, testname, testresult)

                print(len(msgs))
                if len(msgs) > 0:
                    print(msgs)
                    raise Exception("Error messages present")

                resultstr = userid + strseparator + testname + strseparator + testresult
                sock.connect(("localhost", 9999))
                sock.sendall(bytes(enc(resultstr), 'utf-8'))
                sock.close()

                msgs.append("Successfully sent results!")
            except sock.error as e:
                msgs.append("Error connecting to sock:" + e)
                print("did not connect")
            except Exception as e:
                print("excepted: " + e)
            finally:
                msg = '<br>'
                return render_template("result.html", msg='<br>' + msg.join(msgs))
    else:
        return render_template("notfound.html")


@app.route('/list')
def list():
    if session.get('logged_in') and session.get('staff'):
        con = sql.connect("HospitalDB.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        # goal: decode encrypted data for display, does not commit to database
        cur.execute("select name, phone, password from hospital")

        row = cur.fetchone()
        while row:
            enc_nm = row[0]
            enc_ph = row[1]
            enc_pw = row[2]
            con.execute("UPDATE hospital SET name=?,phone=?,password=? WHERE name=?",
                        (dec(enc_nm), dec(enc_ph), dec(enc_pw), enc_nm))
            row = cur.fetchone()

        rows = cur.execute("SELECT * FROM hospital")
        return render_template("list.html", rows=rows)
    else:
        return render_template("notfound.html")


@app.route('/info')
def info():
    if session.get('logged_in'):
        con = sql.connect("HospitalDB.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("""SELECT * FROM hospital WHERE name = ?""", (enc(session["name"]),))

        # decode encrypted data, do not commit
        row = cur.fetchone()
        enc_nm = row[1]
        enc_ph = row[3]
        enc_pw = row[6]

        cur.execute("UPDATE hospital SET name=?,phone=?,password=? WHERE UserID=?",
                    (dec(enc_nm), dec(enc_ph), dec(enc_pw), row[0]))

        row = cur.execute("SELECT * FROM hospital WHERE name = ?", (session["name"],))
        return render_template("info.html", row=row.fetchone())
    else:
        return render_template("notfound.html")


@app.route('/login', methods=['POST'])
def login():
    try:
        nm = request.form['username']
        pw = request.form['password']

        with sql.connect("HospitalDB.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()

            cur.execute("""SELECT * FROM hospital WHERE name = ? AND password = ?""", (enc(nm), enc(pw)))

            row = cur.fetchone()

            if (row != None):
                session['userid'] = row['userid']
                session['name'] = nm
                session['logged_in'] = True
                if row[5] >= 2:
                    session['staff'] = True
                if row[5] == 3:
                    session['admin'] = True
            else:
                session['logged_in'] = False
                flash('invalid username and/or password invalid!')
    except Exception as e:
        con.rollback()
        flash("error in insert operation:" + str(e))
    finally:
        con.close()
    return home()


@app.route('/logout')
def logout():
    session['name'] = ""
    session['logged_in'] = False
    session['staff'] = False
    session['admin'] = False
    session['userid'] = None
    return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)

    app.run(debug=False)

""" example output: Console View
 * Serving Flask app 'HospitalApp'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

"""
