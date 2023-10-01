"""
Name:John Valencia-Londono
Date:Module 5: Role Based Access Control
Assignment:Module 4: Basic Flask Website
Due Date:10/01/2023
About this project:
Develop code that encrypts data stored in a database for a small scale using third-party Python libraries discussed in the course.
Solve a simple programming problem based on various approaches to computer security and information management.
Build a small scale real-world application that incorporates the principles of secure computing including cryptography, network security, and data protection.
Using Python and the flask.session, flask.flash, and os libraries ....

Starting from the website you created in Module 4: Basic Flask Website

The Log In page
Should have two input boxes and one link

textboxes - username and password
Button - Log In - (validates username and password. If valid opens - Home page, Otherwise notifies user "invalid username and/or password!" and stays on login page.)
Develop code that encrypts data stored in a database for a small scale using third-party Python libraries discussed in the course.
Solve a simple programming problem based on various approaches to computer security and information management.
Build a small scale real-world application that incorporates the principles of secure computing including cryptography, network security, and data protection.
Using Python and the flask.session, flask.flash, and os libraries ....

Starting from the website you created in Module 4: Basic Flask Website

The Log In page
Should have two input boxes and one link

textboxes - username and password
Button - Log In - (validates username and password. If valid opens - Home page, Otherwise notifies user "invalid username and/or password!" and stays on login page.)

Assumptions: N/A
All work below was performed by John Valencia-Londono """
from sqlite3 import Connection
from flask import Flask, render_template, request, flash, session
import sqlite3 as sql
import os

app = Flask(__name__)
nm = ''

con = sql.connect('HospitalDB.db')
con.execute('''CREATE TABLE IF NOT EXISTS hospital(
            Name TEXT NOT NULL PRIMARY KEY,
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
    return render_template('home.html',name=session['name'])

@app.route('/enternew')
def new_patient():
    if session.get('logged_in') and session.get('admin'):
        return render_template('input.html')
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

                cur.execute("INSERT INTO hospital (name,age,phone,covid,security,password) VALUES (?,?,?,?,?,?)",
                            (nm, ag, ph, co, sc, pw))

                con.commit()
                msgs.append("record successfully added")
            except:
                print("excepted")
                con.rollback()
            finally:
                print(msgs)
                con.close()
                msg = "<br>"
                return render_template("result.html", msg='<br>' + msg.join(msgs))
    else:
        return render_template("notfound.html")


@app.route('/list')
def list():
    if session.get('logged_in') and session.get('staff'):
        con = sql.connect("HospitalDB.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from hospital")

        rows = cur.fetchall()
        return render_template("list.html", rows=rows)
    else:
        return render_template("notfound.html")

@app.route('/info')
def info():
    if session.get('logged_in'):
        con = sql.connect("HospitalDB.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        print(nm)
        cur.execute("""SELECT * FROM hospital WHERE name = ?""", (session["name"],))
        row = cur.fetchone()
        return render_template("info.html", row=row)
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

            cur.execute("""SELECT * FROM hospital WHERE name = ? AND password = ?""", (nm,pw))

            row = cur.fetchone()
            if (row != None):
                session['name'] = nm
                session['logged_in'] = True
                if row[4] >= 2:
                    session['staff'] = True
                if row[4] == 3:
                    session['admin'] = True
            else:
                session['logged_in'] = False
                flash('invalid username and/or password invalid!')
    except:
        con.rollback()
        flash("error in insert operation")
    finally:
        con.close()
    return home()

@app.route('/logout')
def logout():
    session['name'] = ""
    session['logged_in'] = False
    session['staff'] = False
    session['admin'] = False
    return home()

if __name__ == '__main__':
    app.secret_key = os.urandom(12)

    app.run(debug=False)

""" example output: Console View32G
 * Serving Flask app 'HospitalApp'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
"""