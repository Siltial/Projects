import sqlite3

con = sqlite3.connect("new.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM Movies")
films = res.fetchall()

print (films)