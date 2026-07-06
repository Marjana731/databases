import sqlite3

login = input('')
password = input('')
name = input('')
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute(f"INSERT INTO contacts (login, password, name) VALUES (?, ?, ?)",[login,password,name])

conn.commit()
conn.close()