import sqlite3 as sql

conn = sql.connect('database.db')
print("Opened database")
conn. execute("CREATE TABLE products (name TEXT, description TEXT, Quantity INTEGER, checkin TEXT)")
print("Table created")
conn.close()