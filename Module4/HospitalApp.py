from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

con = sql.connect('HospitalDB.db')
con.execute('''CREATE TABLE IF NOT EXISTS hospital(
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
    return render_template('home.html')

@app.route('/enternew')
def new_patient():
    return render_template('input.html')

@app.route('/input',methods = ['post', 'get'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['name']
            print(nm)
            ag = request.form['age']
            print(ag)
            ph = request.form['phone']
            print(ph)
            co = request.form.get('covid')
            print(co)
            sc = request.form['security']
            print(sc)
            pw = request.form['password']
            print(pw)

            print("load success")
            with sql.connect("hospitaldb.db") as con:
                cur = con.cursor()

                cur.execute("insert into hospital (name,age,phone,covid,security,password) values (?,?,?,?,?,?)",
                                                nm,ag,ph,co,sc,pw)

                con.commit()
                msg = "record successfully added"
        except:
            print("excepted")
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("HospitalDB.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from hospital")

    rows = cur.fetchall()
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug = True)