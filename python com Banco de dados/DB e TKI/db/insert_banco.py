import sqlite3

banco= sqlite3.connect("system.sqlite")
cursor=banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pessoas(name, idade, email)")
banco.commit

nome=input('digite o nome: ')
email=input('digite o email: ')
idade=int(input('digite a idade: '))

cursor.execute(f"INSERT INTO pessoas(name, idade, email) VALUES(?, ?, ?)", (nome, idade, email))
banco.commit()