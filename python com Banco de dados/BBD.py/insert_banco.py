import sqlite3
banco = sqlite3.connect ('banco1.sqlite')
cursor = banco.cursor()

nome = input ('digite o nome:')
email = input ('digite o email:')
idade = int(input('digite a idade:'))

cursor.execute (f"INSERT INTO pessoas VALUES ('{nome}', '{idade}', '{email}' )")
banco.commit()
