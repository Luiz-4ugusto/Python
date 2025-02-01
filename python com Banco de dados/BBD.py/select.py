import sqlite3
banco = sqlite3.connect ('banco1.sqlite')
cursor = banco.cursor()
cursor.execute("SELECT * FROM pessoas WHERE idade >= ?", (16,))
rows = cursor.fetchall()

for row in rows:
    print(row)
