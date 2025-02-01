import sqlite3

banco = sqlite3.connect("system.sqlite")

cursor= banco.cursor()

cursor.execute("SELECT * FROM pessoas WHERE idade >=?", (43,) )

rows=cursor.fetchall()
for row in rows:
    print(row[0])