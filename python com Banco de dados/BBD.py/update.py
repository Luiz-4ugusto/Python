import sqlite3
banco = sqlite3.connect ('banco1.sqlite')
cursor = banco.cursor()

cursor.execute("UPDATE pessoas SET nome = 'H2' WHERE nome = 'luiz'")

banco.commit()