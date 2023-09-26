"""
Name:John Valencia-Londono
Date:09/25/2023
Assignment:Module 4: Basic Flask Website
Due Date:09/24/2023
About this project:
    Develop a frontend application that interacts with a database for a small scale real-world applications using third-party Python libraries discussed in the course.
    Solve a simple programming problem based on various approaches to computer security and information management.
    Directions:
    Using Python and the Flask library, create a Flask website with the following pages

    Home
    Add a new Hospital App User
    List Hospital App Users
    Results
    The Home page
    Should have

    Link - Add a new Hospital App User - (opens the add a new Hospital App User page)
    Link - List Hospital App Users - (opens the list Hospital App Users page)
    The Add new Hospital App User page
    Should have

    a label and input text field for each possible attribute other than the id and Has COVID
    a label and input checkbox field for Has COVID
    Submit button -
    When the Submit button is clicked:

    Validates the values entered by the user.

    If the values are valid then a record is added to the HospitalUser table with the values entered by the user and a record added message is sent to the result page to display to the user.

    Otherwise, an error message is created indicating all the input errors. This message is sent to the result page to display to the user.)

    Input Validation Rules:

    the Name is not empty and does not only contain spaces
    the Age is a whole number greater than 0 and less than 121 (Hint: Python - How to validate that a variable stores a numeric valueLinks to an external site.)
    the PhoneNumber is not empty and does not only contain spaces
    The SecurityRoleLevel must be a numeric between 1 and 3. (Hint: Python - How to validate that a variable stores a numeric valueLinks to an external site.)
    the LoginPassword is not empty and does not only contain spaces
    The List Hospital App Users page
    Should have

    a table that displays the following information for every record in the HospitalUser table:
    UserName, UserAge, UserPhNum, UserHasCOVID, UserSecurityLevel, and LoginPassword

    Link - Go back to home page - (opens the Home page)
    The Results page
    Should have

    display the value of the variable msg (Note this message could be a recorded added message or an input validation error record not added message)
    Link - Go back to home page - (opens the Home page)
Assumptions: N/A
All work below was performed by John Valencia-Londono """
from sqlite3 import Connection

from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

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
    return render_template('home.html')


@app.route('/enternew')
def new_patient():
    return render_template('input.html')


@app.route('/input', methods=['post', 'get'])
def addrec():
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


@app.route('/list')
def list():
    con = sql.connect("HospitalDB.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from hospital")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=False)

""" example output: Console View
 * Serving Flask app 'HospitalApp'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
"""