import sqlite3
banco = sqlite3.connect ('banco1.sqlite')
cursor = banco.cursor()

cursor.execute("DELETE FROM pessoas WHERE nome = 'jao'")
banco.commit()