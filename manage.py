from crypt import methods
from unicodedata import name
from flask import Flask, request, redirect, url_for, render_template
import sqlite3 as sql
app = Flask(__name__)

@app.route('/home/')
def welcome():
     return render_template("Home.htm")

@app.route('/add/', methods = ["POST", "GET"])
def addItem():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        checkin_date = request.form["checkin_date"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO ")
        con.commit()
        message = "Item added"
    return render_template("ItemAdd.htm", msg = message)

@app.route('/list/')
def List():
    con = sql.connect("")
    con.row_factory = sql.Row

    cur = cur.cursor()
    cur.execute("SELECT * FROM ")

    rows = cur.fetchall()

    return render_template("List.htm", rows = rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

