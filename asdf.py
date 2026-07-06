import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT,
email TEXT)
''')
cursor.execute("INSERT INTO contacts(name, phone, email) VALUES ('Maria','234567890','asdfgh')",)
cursor.execute("INSERT INTO contacts(name, phone, email) VALUES ('Anna','9876534504','kdfg')",)
cursor.execute("SELECT * FROM contacts WHERE email = 'kdfg' AND id =5")
cursor.execute("UPDATE contacts SET name = 'Olena' WHERE name = 'Maria'")
cursor.execute('SELECT * FROM contacts')
cursor.execute("DELETE FROM contacts WHERE name = 'Olena'")
print(cursor.fetchall())
a= cursor.fetchall()
print(a)
conn.commit()
conn.close()