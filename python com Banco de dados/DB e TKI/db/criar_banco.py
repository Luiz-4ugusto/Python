import sqlite3

banco= sqlite3.connect('system.sqlite')

cursor= banco.cursor()
#objeto do sqlite para executar operações do qlite


cursor.execute('CREATE TABLE pessoas(nome text, idade integer, email text)')
#cria table


banco.commit()
#fechar transação