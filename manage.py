from flask import Flask, request, redirect, url_for, render_template
import sqlite3 as sql
app = Flask(__name__)

@app.route('/home/')
def welcome():
     return render_template("Home.htm")

@app.route('/add_form/')
def add_form():
    return render_template("ItemAdd.htm")

@app.route('/add/', methods = ["POST", "GET"])
def addItem():
    if request.method == "POST":
        nm = request.form["name"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        checkin_date = request.form["checkin_date"]

        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO products (name, description, Quantity, checkin) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, description, quantity, checkin_date))
            con.commit()
        return redirect(url_for('list'))
    return "Error"

@app.route('/list/')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()

    return render_template("List.htm", rows = rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

