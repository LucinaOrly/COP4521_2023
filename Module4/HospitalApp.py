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
            nm = request.form['name']
            if nm == '':
                msgs.append("You can not enter in an empty name")

            ag = request.form['age']
            if not str.isdigit(ag) or int(ag) < 0 or int(ag) > 121:
                print( str.isdigit(ag))
                msgs.append("The Age must be a whole number greater than 0 and less than 121.")

            ph = request.form['phone']
            if ph == '':
                msgs.append("You can not enter in an empty phone number")

            co = request.form.get('covid')
            if co == 'on':
                co = 1
            else:
                co = 0

            sc = request.form['security']
            if not str.isdigit(sc) or int(sc) < 1 or int(sc) > 3:
                msgs.append("The SecurityRoleLevel must be a numeric between 1 and 3.")

            pw = request.form['password']
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

            # print all messages
            msg = "<br>"
            msg.join(msgs)
        finally:
            print(msgs)
            con.close()
            msg = "\n"
            return render_template("result.html", msg=msg.join(msgs))


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
