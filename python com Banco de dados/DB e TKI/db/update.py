import sqlite3
banco=sqlite3.connect('system.sqlite')
cursor= banco.cursor()

cursor.execute("UPDATe pessoas SET nome= 'luiz' Wh")